import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

public class Zadanie1 extends Application {

    Stage window;
    Scene look;
    BorderPane setting;

    @Override
    public void start(Stage primaryStage) {

        window = primaryStage;
        window.setTitle("Zadania JavaFX JPWP");
        window.setResizable(false);

        setting = new BorderPane();

        // Zadanie 1: Dodaj do centralnej części siatki panel do wyboru daty (klasa DatePicker), natomiast do dolnej części
        // siatki przycisk submit. Przycisk ma być nieaktywny (metoda setDisable), dopóki nie wybierzemy daty dzisiejszej (26.05.2020).
        // Aktywny przycisk powinien zamykać okno aplikacji.

        // Uwaga! Data wybierana z panelu jest zmienną typu LocalDate!

        // Tu wpisz rozwiązanie:

        ///////////////////////////////////


        look = new Scene(setting, 200, 100);
        window.setScene(look);
        window.show();

    }

    public static void main(String[] args) {
        launch(args);
    }


}
