import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

class Synchronizer {
    private Set<String> delete;
    private Set<String> copy;
    Synchronizer(String S, String D) throws java.io.IOException {
        this.delete = new TreeSet<>();
        this.copy = new TreeSet<>();
        compareCatalogs(S, D);
    }
    private boolean compareFiles(String S, String D) throws IOException {
        byte[] f1 = Files.readAllBytes(Paths.get(S));
        byte[] f2 = Files.readAllBytes(Paths.get(D));
        return Arrays.equals(f1, f2);
    }
    private void compareCatalogs(String S, String D) throws java.io.IOException {
        Set<String> filesS = new HashSet<>();
        Files.walk(Paths.get(S)).forEach(filePath -> {
            if (Files.isRegularFile(filePath)) {
                filesS.add(filePath.toString().replaceFirst(S,""));
            }
        });
        Set<String> filesD = new HashSet<>();
        Files.walk(Paths.get(D)).forEach(filePath -> {
            if (Files.isRegularFile(filePath)) {
                filesD.add(filePath.toString().replaceFirst(D,""));
            }
        });
        Set<String> toRemove = new HashSet<>(filesD);
        toRemove.removeAll(filesS);
        delete.addAll(toRemove);
        Set<String> toCopy = new HashSet<>(filesS);
        toCopy.removeAll(filesD);
        copy.addAll(toCopy);
        Set<String> intersection = new HashSet<>(filesS);
        intersection.retainAll(filesD);
        for (String file: intersection) {
            if (!compareFiles(S+file, D+file)) {
                delete.add(file);
                copy.add(file);
            }
        }
    }
    public String toString() {
        if (delete.size()==0 && copy.size()==0) return "IDENTICAL";
        else {
            String result="";
            for (String elem: delete) result+="DELETE "+elem+'\n';
            for (String elem: copy) result+="COPY "+elem+'\n';
            return result.substring(0, result.length()-1);
        }
    }
}

public class Sync {
    public static void main(String[] args) throws java.io.IOException {
        Synchronizer sync = new Synchronizer(args[0]+'/', args[1]+'/');
        System.out.print(sync);
    }
}

