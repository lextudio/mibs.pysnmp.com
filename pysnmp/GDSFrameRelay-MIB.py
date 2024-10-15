# SNMP MIB module (GDSFrameRelay-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDSFrameRelay-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:24 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gds_ObjectIdentity = ObjectIdentity
gds = _Gds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955)
)
_Seriesfr_ObjectIdentity = ObjectIdentity
seriesfr = _Seriesfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5)
)
_Is_GDS_frame_relay_device5_ObjectIdentity = ObjectIdentity
is_GDS_frame_relay_device5 = _Is_GDS_frame_relay_device5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5)
)
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1)
)
_UVersion_Strings_ObjectIdentity = ObjectIdentity
uVersion_Strings = _UVersion_Strings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1)
)


class _UMain_HW_Version_Type(DisplayString):
    """Custom type uMain_HW_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UMain_HW_Version_Type.__name__ = "DisplayString"
_UMain_HW_Version_Object = MibScalar
uMain_HW_Version = _UMain_HW_Version_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 1),
    _UMain_HW_Version_Type()
)
uMain_HW_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uMain_HW_Version.setStatus("mandatory")


class _UComm_HW_Version_Type(DisplayString):
    """Custom type uComm_HW_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UComm_HW_Version_Type.__name__ = "DisplayString"
_UComm_HW_Version_Object = MibScalar
uComm_HW_Version = _UComm_HW_Version_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 2),
    _UComm_HW_Version_Type()
)
uComm_HW_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uComm_HW_Version.setStatus("mandatory")


class _UMain_SW_Version_Type(DisplayString):
    """Custom type uMain_SW_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UMain_SW_Version_Type.__name__ = "DisplayString"
_UMain_SW_Version_Object = MibScalar
uMain_SW_Version = _UMain_SW_Version_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 3),
    _UMain_SW_Version_Type()
)
uMain_SW_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uMain_SW_Version.setStatus("mandatory")


class _UComm_SW_Version_Type(DisplayString):
    """Custom type uComm_SW_Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UComm_SW_Version_Type.__name__ = "DisplayString"
_UComm_SW_Version_Object = MibScalar
uComm_SW_Version = _UComm_SW_Version_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 4),
    _UComm_SW_Version_Type()
)
uComm_SW_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uComm_SW_Version.setStatus("mandatory")


class _UAlgorithm_Type(DisplayString):
    """Custom type uAlgorithm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UAlgorithm_Type.__name__ = "DisplayString"
_UAlgorithm_Object = MibScalar
uAlgorithm = _UAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 5),
    _UAlgorithm_Type()
)
uAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uAlgorithm.setStatus("mandatory")


class _UAccess_Table_Type(DisplayString):
    """Custom type uAccess_Table based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UAccess_Table_Type.__name__ = "DisplayString"
_UAccess_Table_Object = MibScalar
uAccess_Table = _UAccess_Table_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 1, 6),
    _UAccess_Table_Type()
)
uAccess_Table.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uAccess_Table.setStatus("mandatory")
_UConfigured_ObjectIdentity = ObjectIdentity
uConfigured = _UConfigured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 2)
)


class _UOwn_SID_Type(Integer32):
    """Custom type uOwn_SID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UOwn_SID_Type.__name__ = "Integer32"
_UOwn_SID_Object = MibScalar
uOwn_SID = _UOwn_SID_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 2, 1),
    _UOwn_SID_Type()
)
uOwn_SID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uOwn_SID.setStatus("mandatory")
_UDynamic_ObjectIdentity = ObjectIdentity
uDynamic = _UDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3)
)


class _UCurrent_Date_Type(DisplayString):
    """Custom type uCurrent_Date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UCurrent_Date_Type.__name__ = "DisplayString"
_UCurrent_Date_Object = MibScalar
uCurrent_Date = _UCurrent_Date_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 1),
    _UCurrent_Date_Type()
)
uCurrent_Date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uCurrent_Date.setStatus("mandatory")


class _UCurrent_Time_Type(DisplayString):
    """Custom type uCurrent_Time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UCurrent_Time_Type.__name__ = "DisplayString"
_UCurrent_Time_Object = MibScalar
uCurrent_Time = _UCurrent_Time_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 2),
    _UCurrent_Time_Type()
)
uCurrent_Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uCurrent_Time.setStatus("mandatory")


class _UDevice_State_Type(Integer32):
    """Custom type uDevice_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail-cipher-chip", 5),
          ("fail-lock-open", 6),
          ("fail-lock-open-and-cipher-chip", 7),
          ("failure", 4),
          ("normal", 1),
          ("test-empty", 2),
          ("test-loaded", 3))
    )


_UDevice_State_Type.__name__ = "Integer32"
_UDevice_State_Object = MibScalar
uDevice_State = _UDevice_State_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 3),
    _UDevice_State_Type()
)
uDevice_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uDevice_State.setStatus("mandatory")


class _UComms_State_Type(Integer32):
    """Custom type uComms_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("booting", 1),
          ("encrypting", 2),
          ("failure", 4),
          ("not-encrypting", 3))
    )


_UComms_State_Type.__name__ = "Integer32"
_UComms_State_Object = MibScalar
uComms_State = _UComms_State_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 4),
    _UComms_State_Type()
)
uComms_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uComms_State.setStatus("mandatory")


class _UNMS_State_Type(Integer32):
    """Custom type uNMS_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("read-only", 2),
          ("read-write", 3))
    )


_UNMS_State_Type.__name__ = "Integer32"
_UNMS_State_Object = MibScalar
uNMS_State = _UNMS_State_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 5),
    _UNMS_State_Type()
)
uNMS_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uNMS_State.setStatus("mandatory")


class _USM_State_Type(Integer32):
    """Custom type uSM_State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("ok", 1),
          ("removed", 2))
    )


_USM_State_Type.__name__ = "Integer32"
_USM_State_Object = MibScalar
uSM_State = _USM_State_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 6),
    _USM_State_Type()
)
uSM_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSM_State.setStatus("mandatory")


class _UReady_Alarm_Led_Type(Integer32):
    """Custom type uReady_Alarm_Led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("flashing-red-alarm", 9),
          ("flashing-yellow-user-logged-in", 11),
          ("green-normal", 2),
          ("red-test-mode", 1),
          ("yellow-self-testing", 3))
    )


_UReady_Alarm_Led_Type.__name__ = "Integer32"
_UReady_Alarm_Led_Object = MibScalar
uReady_Alarm_Led = _UReady_Alarm_Led_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 3, 7),
    _UReady_Alarm_Led_Type()
)
uReady_Alarm_Led.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uReady_Alarm_Led.setStatus("mandatory")
_UBackground_ObjectIdentity = ObjectIdentity
uBackground = _UBackground_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 4)
)
_URAG_tests_Type = Counter32
_URAG_tests_Object = MibScalar
uRAG_tests = _URAG_tests_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 4, 1),
    _URAG_tests_Type()
)
uRAG_tests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uRAG_tests.setStatus("mandatory")
_URAG_fails_Type = Counter32
_URAG_fails_Object = MibScalar
uRAG_fails = _URAG_fails_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 4, 2),
    _URAG_fails_Type()
)
uRAG_fails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uRAG_fails.setStatus("mandatory")
_URAG_threshold_Type = Counter32
_URAG_threshold_Object = MibScalar
uRAG_threshold = _URAG_threshold_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 1, 4, 3),
    _URAG_threshold_Type()
)
uRAG_threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uRAG_threshold.setStatus("mandatory")
_Frame_relay_ObjectIdentity = ObjectIdentity
frame_relay = _Frame_relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2)
)


class _Reset_FR_statistic_counters_Type(Integer32):
    """Custom type reset_FR_statistic_counters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Reset_FR_statistic_counters_Type.__name__ = "Integer32"
_Reset_FR_statistic_counters_Object = MibScalar
reset_FR_statistic_counters = _Reset_FR_statistic_counters_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 1),
    _Reset_FR_statistic_counters_Type()
)
reset_FR_statistic_counters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset_FR_statistic_counters.setStatus("mandatory")
_FR_Traffic_Table_Object = MibTable
fR_Traffic_Table = _FR_Traffic_Table_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2)
)
if mibBuilder.loadTexts:
    fR_Traffic_Table.setStatus("mandatory")
_FR_Traffic_Entry_Object = MibTableRow
fR_Traffic_Entry = _FR_Traffic_Entry_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1)
)
fR_Traffic_Entry.setIndexNames(
    (0, "GDSFrameRelay-MIB", "frPort-Index"),
)
if mibBuilder.loadTexts:
    fR_Traffic_Entry.setStatus("mandatory")
_FrPort_Index_Type = Integer32
_FrPort_Index_Object = MibScalar
frPort_Index = _FrPort_Index_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 1),
    _FrPort_Index_Type()
)
frPort_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPort_Index.setStatus("mandatory")


class _FrPort_Type_Type(Integer32):
    """Custom type frPort_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher-port", 2),
          ("plain-port", 1))
    )


_FrPort_Type_Type.__name__ = "Integer32"
_FrPort_Type_Object = MibScalar
frPort_Type = _FrPort_Type_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 2),
    _FrPort_Type_Type()
)
frPort_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPort_Type.setStatus("mandatory")
_FrGood_Frames_Type = Counter32
_FrGood_Frames_Object = MibScalar
frGood_Frames = _FrGood_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 3),
    _FrGood_Frames_Type()
)
frGood_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frGood_Frames.setStatus("mandatory")
_FrBad_Frames_Type = Counter32
_FrBad_Frames_Object = MibScalar
frBad_Frames = _FrBad_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 4),
    _FrBad_Frames_Type()
)
frBad_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frBad_Frames.setStatus("mandatory")
_FrInactive_DLCI_Type = Counter32
_FrInactive_DLCI_Object = MibScalar
frInactive_DLCI = _FrInactive_DLCI_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 5),
    _FrInactive_DLCI_Type()
)
frInactive_DLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInactive_DLCI.setStatus("mandatory")
_FrReceived_FECN_Type = Counter32
_FrReceived_FECN_Object = MibScalar
frReceived_FECN = _FrReceived_FECN_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 6),
    _FrReceived_FECN_Type()
)
frReceived_FECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frReceived_FECN.setStatus("mandatory")
_FrReceived_BECN_Type = Counter32
_FrReceived_BECN_Object = MibScalar
frReceived_BECN = _FrReceived_BECN_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 7),
    _FrReceived_BECN_Type()
)
frReceived_BECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frReceived_BECN.setStatus("mandatory")
_FrSent_Frames_Type = Counter32
_FrSent_Frames_Object = MibScalar
frSent_Frames = _FrSent_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 8),
    _FrSent_Frames_Type()
)
frSent_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSent_Frames.setStatus("mandatory")
_FrDropped_Frames_Type = Counter32
_FrDropped_Frames_Object = MibScalar
frDropped_Frames = _FrDropped_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 2, 1, 9),
    _FrDropped_Frames_Type()
)
frDropped_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDropped_Frames.setStatus("mandatory")
_FR_RX_Err_Table_Object = MibTable
fR_RX_Err_Table = _FR_RX_Err_Table_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3)
)
if mibBuilder.loadTexts:
    fR_RX_Err_Table.setStatus("mandatory")
_FR_RX_Err_Entry_Object = MibTableRow
fR_RX_Err_Entry = _FR_RX_Err_Entry_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1)
)
fR_RX_Err_Entry.setIndexNames(
    (0, "GDSFrameRelay-MIB", "frRxErrIndex"),
)
if mibBuilder.loadTexts:
    fR_RX_Err_Entry.setStatus("mandatory")
_FrRxErrIndex_Type = Integer32
_FrRxErrIndex_Object = MibTableColumn
frRxErrIndex = _FrRxErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 1),
    _FrRxErrIndex_Type()
)
frRxErrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrIndex.setStatus("mandatory")
_FrRxErrShort_Frames_Type = Counter32
_FrRxErrShort_Frames_Object = MibScalar
frRxErrShort_Frames = _FrRxErrShort_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 2),
    _FrRxErrShort_Frames_Type()
)
frRxErrShort_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrShort_Frames.setStatus("mandatory")
_FrRxErrAborted_Frames_Type = Counter32
_FrRxErrAborted_Frames_Object = MibScalar
frRxErrAborted_Frames = _FrRxErrAborted_Frames_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 3),
    _FrRxErrAborted_Frames_Type()
)
frRxErrAborted_Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrAborted_Frames.setStatus("mandatory")
_FrRxErrResidual_Bits_Type = Counter32
_FrRxErrResidual_Bits_Object = MibScalar
frRxErrResidual_Bits = _FrRxErrResidual_Bits_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 4),
    _FrRxErrResidual_Bits_Type()
)
frRxErrResidual_Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrResidual_Bits.setStatus("mandatory")
_FrRxErrOverruns_Type = Counter32
_FrRxErrOverruns_Object = MibTableColumn
frRxErrOverruns = _FrRxErrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 5),
    _FrRxErrOverruns_Type()
)
frRxErrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrOverruns.setStatus("mandatory")
_FrRxErrCRC_Errors_Type = Counter32
_FrRxErrCRC_Errors_Object = MibScalar
frRxErrCRC_Errors = _FrRxErrCRC_Errors_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 2, 3, 1, 6),
    _FrRxErrCRC_Errors_Type()
)
frRxErrCRC_Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frRxErrCRC_Errors.setStatus("mandatory")
_Configure_ObjectIdentity = ObjectIdentity
configure = _Configure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3)
)
_Pi_FR_Layer1_ObjectIdentity = ObjectIdentity
pi_FR_Layer1 = _Pi_FR_Layer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1)
)


class _PiFRInterface_Installed_Type(Integer32):
    """Custom type piFRInterface_Installed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("is-E1", 4),
          ("is-RS422", 1),
          ("is-T1", 3),
          ("is-V35", 2),
          ("is-X21", 5),
          ("is-undefined", 6))
    )


_PiFRInterface_Installed_Type.__name__ = "Integer32"
_PiFRInterface_Installed_Object = MibScalar
piFRInterface_Installed = _PiFRInterface_Installed_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 1),
    _PiFRInterface_Installed_Type()
)
piFRInterface_Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piFRInterface_Installed.setStatus("mandatory")


class _PiFRTX_Clock_Source_Type(Integer32):
    """Custom type piFRTX_Clock_Source based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is-DCE", 1),
          ("is-DTE", 2))
    )


_PiFRTX_Clock_Source_Type.__name__ = "Integer32"
_PiFRTX_Clock_Source_Object = MibScalar
piFRTX_Clock_Source = _PiFRTX_Clock_Source_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 2),
    _PiFRTX_Clock_Source_Type()
)
piFRTX_Clock_Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRTX_Clock_Source.setStatus("mandatory")


class _PiFRE1_Plain_Port_Impedance_Type(Integer32):
    """Custom type piFRE1_Plain_Port_Impedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is-120-OHMS-D-SUB", 2),
          ("is-75-OHMS-BNC", 1))
    )


_PiFRE1_Plain_Port_Impedance_Type.__name__ = "Integer32"
_PiFRE1_Plain_Port_Impedance_Object = MibScalar
piFRE1_Plain_Port_Impedance = _PiFRE1_Plain_Port_Impedance_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 3),
    _PiFRE1_Plain_Port_Impedance_Type()
)
piFRE1_Plain_Port_Impedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRE1_Plain_Port_Impedance.setStatus("mandatory")


class _PiFRE1_Cipher_Port_Impedance_Type(Integer32):
    """Custom type piFRE1_Cipher_Port_Impedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is-120-OHMS-D-SUB", 2),
          ("is-75-OHMS-BNC", 1))
    )


_PiFRE1_Cipher_Port_Impedance_Type.__name__ = "Integer32"
_PiFRE1_Cipher_Port_Impedance_Object = MibScalar
piFRE1_Cipher_Port_Impedance = _PiFRE1_Cipher_Port_Impedance_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 4),
    _PiFRE1_Cipher_Port_Impedance_Type()
)
piFRE1_Cipher_Port_Impedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRE1_Cipher_Port_Impedance.setStatus("mandatory")


class _PiFRE1_Framing_Mode_Type(Integer32):
    """Custom type piFRE1_Framing_Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is-G704", 2),
          ("is-unframed", 1))
    )


_PiFRE1_Framing_Mode_Type.__name__ = "Integer32"
_PiFRE1_Framing_Mode_Object = MibScalar
piFRE1_Framing_Mode = _PiFRE1_Framing_Mode_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 5),
    _PiFRE1_Framing_Mode_Type()
)
piFRE1_Framing_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRE1_Framing_Mode.setStatus("mandatory")


class _PiFRE1_Time_Slot_Options_Type(Integer32):
    """Custom type piFRE1_Time_Slot_Options based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-slots-except-TS0", 1),
          ("all-slots-except-TS0-and-TS16", 2))
    )


_PiFRE1_Time_Slot_Options_Type.__name__ = "Integer32"
_PiFRE1_Time_Slot_Options_Object = MibScalar
piFRE1_Time_Slot_Options = _PiFRE1_Time_Slot_Options_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 6),
    _PiFRE1_Time_Slot_Options_Type()
)
piFRE1_Time_Slot_Options.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRE1_Time_Slot_Options.setStatus("mandatory")


class _PiFRE1_Time_Slots_Type(OctetString):
    """Custom type piFRE1_Time_Slots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PiFRE1_Time_Slots_Type.__name__ = "OctetString"
_PiFRE1_Time_Slots_Object = MibScalar
piFRE1_Time_Slots = _PiFRE1_Time_Slots_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 7),
    _PiFRE1_Time_Slots_Type()
)
piFRE1_Time_Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piFRE1_Time_Slots.setStatus("mandatory")


class _PiFRT1_Plain_Port_Pulse_Type(Integer32):
    """Custom type piFRT1_Plain_Port_Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("is-CSU", 1),
          ("is-CSU-T1C1", 2),
          ("is-DSX-1-0-40m", 3),
          ("is-DSX-1-120-160m", 6),
          ("is-DSX-1-160-200m", 7),
          ("is-DSX-1-40-80m", 4),
          ("is-DSX-1-80-120m", 5))
    )


_PiFRT1_Plain_Port_Pulse_Type.__name__ = "Integer32"
_PiFRT1_Plain_Port_Pulse_Object = MibScalar
piFRT1_Plain_Port_Pulse = _PiFRT1_Plain_Port_Pulse_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 8),
    _PiFRT1_Plain_Port_Pulse_Type()
)
piFRT1_Plain_Port_Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRT1_Plain_Port_Pulse.setStatus("mandatory")


class _PiFRT1_Cipher_Port_Pulse_Type(Integer32):
    """Custom type piFRT1_Cipher_Port_Pulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("is-CSU", 1),
          ("is-CSU-T1C1", 2),
          ("is-DSX-1-0-40m", 3),
          ("is-DSX-1-120-160m", 6),
          ("is-DSX-1-160-200m", 7),
          ("is-DSX-1-40-80m", 4),
          ("is-DSX-1-80-120m", 5))
    )


_PiFRT1_Cipher_Port_Pulse_Type.__name__ = "Integer32"
_PiFRT1_Cipher_Port_Pulse_Object = MibScalar
piFRT1_Cipher_Port_Pulse = _PiFRT1_Cipher_Port_Pulse_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 9),
    _PiFRT1_Cipher_Port_Pulse_Type()
)
piFRT1_Cipher_Port_Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRT1_Cipher_Port_Pulse.setStatus("mandatory")


class _PiFRT1_Framing_Mode_Type(Integer32):
    """Custom type piFRT1_Framing_Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("is-D4", 4),
          ("is-ESF", 3),
          ("is-unframed", 1))
    )


_PiFRT1_Framing_Mode_Type.__name__ = "Integer32"
_PiFRT1_Framing_Mode_Object = MibScalar
piFRT1_Framing_Mode = _PiFRT1_Framing_Mode_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 10),
    _PiFRT1_Framing_Mode_Type()
)
piFRT1_Framing_Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRT1_Framing_Mode.setStatus("mandatory")


class _PiFRT1_Time_Slot_Options_Type(Integer32):
    """Custom type piFRT1_Time_Slot_Options based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("all-slots", 1)
    )


_PiFRT1_Time_Slot_Options_Type.__name__ = "Integer32"
_PiFRT1_Time_Slot_Options_Object = MibScalar
piFRT1_Time_Slot_Options = _PiFRT1_Time_Slot_Options_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 11),
    _PiFRT1_Time_Slot_Options_Type()
)
piFRT1_Time_Slot_Options.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRT1_Time_Slot_Options.setStatus("mandatory")


class _PiFRT1_Time_Slots_Type(OctetString):
    """Custom type piFRT1_Time_Slots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_PiFRT1_Time_Slots_Type.__name__ = "OctetString"
_PiFRT1_Time_Slots_Object = MibScalar
piFRT1_Time_Slots = _PiFRT1_Time_Slots_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 1, 12),
    _PiFRT1_Time_Slots_Type()
)
piFRT1_Time_Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piFRT1_Time_Slots.setStatus("mandatory")
_Pi_FR_Layer2_ObjectIdentity = ObjectIdentity
pi_FR_Layer2 = _Pi_FR_Layer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 2)
)


class _Pi_FR_Logical_Interface_Type_Type(Integer32):
    """Custom type pi_FR_Logical_Interface_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_Pi_FR_Logical_Interface_Type_Type.__name__ = "Integer32"
_Pi_FR_Logical_Interface_Type_Object = MibScalar
pi_FR_Logical_Interface_Type = _Pi_FR_Logical_Interface_Type_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 2, 1),
    _Pi_FR_Logical_Interface_Type_Type()
)
pi_FR_Logical_Interface_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pi_FR_Logical_Interface_Type.setStatus("mandatory")


class _Pi_FR_Max_RX_Frame_Type(Integer32):
    """Custom type pi_FR_Max_RX_Frame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              1024,
              1600,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("size-1024-bytes", 1024),
          ("size-1600-bytes", 1600),
          ("size-2048-bytes", 2048),
          ("size-256-bytes", 256),
          ("size-4096-bytes", 4096),
          ("size-512-bytes", 512))
    )


_Pi_FR_Max_RX_Frame_Type.__name__ = "Integer32"
_Pi_FR_Max_RX_Frame_Object = MibScalar
pi_FR_Max_RX_Frame = _Pi_FR_Max_RX_Frame_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 2, 2),
    _Pi_FR_Max_RX_Frame_Type()
)
pi_FR_Max_RX_Frame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_FR_Max_RX_Frame.setStatus("mandatory")


class _Pi_FR_Max_TX_Frame_Type(Integer32):
    """Custom type pi_FR_Max_TX_Frame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              1024,
              1600,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("size-1024-bytes", 1024),
          ("size-1600-bytes", 1600),
          ("size-2048-bytes", 2048),
          ("size-256-bytes", 256),
          ("size-4096-bytes", 4096),
          ("size-512-bytes", 512))
    )


_Pi_FR_Max_TX_Frame_Type.__name__ = "Integer32"
_Pi_FR_Max_TX_Frame_Object = MibScalar
pi_FR_Max_TX_Frame = _Pi_FR_Max_TX_Frame_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 2, 3),
    _Pi_FR_Max_TX_Frame_Type()
)
pi_FR_Max_TX_Frame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_FR_Max_TX_Frame.setStatus("mandatory")


class _Pi_FR_LMI_support_Type(Integer32):
    """Custom type pi_FR_LMI_support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("is-ANSI-T1-617", 3),
          ("is-ITU-T-Q933", 4),
          ("standard-LMI", 2))
    )


_Pi_FR_LMI_support_Type.__name__ = "Integer32"
_Pi_FR_LMI_support_Object = MibScalar
pi_FR_LMI_support = _Pi_FR_LMI_support_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 2, 4),
    _Pi_FR_LMI_support_Type()
)
pi_FR_LMI_support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_FR_LMI_support.setStatus("mandatory")
_Pi_FR_DLC_Ranges_Table_Object = MibTable
pi_FR_DLC_Ranges_Table = _Pi_FR_DLC_Ranges_Table_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3)
)
if mibBuilder.loadTexts:
    pi_FR_DLC_Ranges_Table.setStatus("mandatory")
_Pi_FR_DLC_Ranges_Entry_Object = MibTableRow
pi_FR_DLC_Ranges_Entry = _Pi_FR_DLC_Ranges_Entry_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1)
)
pi_FR_DLC_Ranges_Entry.setIndexNames(
    (0, "GDSFrameRelay-MIB", "piFRDLcRangeBand"),
)
if mibBuilder.loadTexts:
    pi_FR_DLC_Ranges_Entry.setStatus("mandatory")
_PiFRDLcRangeBand_Type = Integer32
_PiFRDLcRangeBand_Object = MibTableColumn
piFRDLcRangeBand = _PiFRDLcRangeBand_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1, 1),
    _PiFRDLcRangeBand_Type()
)
piFRDLcRangeBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piFRDLcRangeBand.setStatus("mandatory")


class _PiFRDLcRangeUse_Type(Integer32):
    """Custom type piFRDLcRangeUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("pvc", 2))
    )


_PiFRDLcRangeUse_Type.__name__ = "Integer32"
_PiFRDLcRangeUse_Object = MibTableColumn
piFRDLcRangeUse = _PiFRDLcRangeUse_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1, 2),
    _PiFRDLcRangeUse_Type()
)
piFRDLcRangeUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRDLcRangeUse.setStatus("mandatory")


class _PiFRDLcRangeMode_Type(Integer32):
    """Custom type piFRDLcRangeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bidirectional", 1)
    )


_PiFRDLcRangeMode_Type.__name__ = "Integer32"
_PiFRDLcRangeMode_Object = MibTableColumn
piFRDLcRangeMode = _PiFRDLcRangeMode_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1, 3),
    _PiFRDLcRangeMode_Type()
)
piFRDLcRangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piFRDLcRangeMode.setStatus("mandatory")


class _PiFRDLcRangeStart_Type(Integer32):
    """Custom type piFRDLcRangeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PiFRDLcRangeStart_Type.__name__ = "Integer32"
_PiFRDLcRangeStart_Object = MibTableColumn
piFRDLcRangeStart = _PiFRDLcRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1, 4),
    _PiFRDLcRangeStart_Type()
)
piFRDLcRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRDLcRangeStart.setStatus("mandatory")


class _PiFRDLcRangeEnd_set_to_activate_changes_Type(Integer32):
    """Custom type piFRDLcRangeEnd_set_to_activate_changes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PiFRDLcRangeEnd_set_to_activate_changes_Type.__name__ = "Integer32"
_PiFRDLcRangeEnd_set_to_activate_changes_Object = MibScalar
piFRDLcRangeEnd_set_to_activate_changes = _PiFRDLcRangeEnd_set_to_activate_changes_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 3, 1, 5),
    _PiFRDLcRangeEnd_set_to_activate_changes_Type()
)
piFRDLcRangeEnd_set_to_activate_changes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piFRDLcRangeEnd_set_to_activate_changes.setStatus("mandatory")
_PiRemotePorts_ObjectIdentity = ObjectIdentity
piRemotePorts = _PiRemotePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5)
)
_Pi_Remote_Port1_ObjectIdentity = ObjectIdentity
pi_Remote_Port1 = _Pi_Remote_Port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 1)
)
_Pi_Remote_Port1IP_Address_Type = IpAddress
_Pi_Remote_Port1IP_Address_Object = MibScalar
pi_Remote_Port1IP_Address = _Pi_Remote_Port1IP_Address_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 1, 1),
    _Pi_Remote_Port1IP_Address_Type()
)
pi_Remote_Port1IP_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port1IP_Address.setStatus("mandatory")
_Pi_Remote_Port1Subnet_mask_Type = IpAddress
_Pi_Remote_Port1Subnet_mask_Object = MibScalar
pi_Remote_Port1Subnet_mask = _Pi_Remote_Port1Subnet_mask_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 1, 2),
    _Pi_Remote_Port1Subnet_mask_Type()
)
pi_Remote_Port1Subnet_mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port1Subnet_mask.setStatus("mandatory")
_Pi_Remote_Port1Gateway_Address_Type = IpAddress
_Pi_Remote_Port1Gateway_Address_Object = MibScalar
pi_Remote_Port1Gateway_Address = _Pi_Remote_Port1Gateway_Address_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 1, 3),
    _Pi_Remote_Port1Gateway_Address_Type()
)
pi_Remote_Port1Gateway_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port1Gateway_Address.setStatus("mandatory")
_PiRemotePort2_ObjectIdentity = ObjectIdentity
piRemotePort2 = _PiRemotePort2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 2)
)
_Pi_Remote_Port3_ObjectIdentity = ObjectIdentity
pi_Remote_Port3 = _Pi_Remote_Port3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3)
)
_Pi_Remote_Port3IP_Address_Type = IpAddress
_Pi_Remote_Port3IP_Address_Object = MibScalar
pi_Remote_Port3IP_Address = _Pi_Remote_Port3IP_Address_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3, 1),
    _Pi_Remote_Port3IP_Address_Type()
)
pi_Remote_Port3IP_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port3IP_Address.setStatus("mandatory")
_Pi_Remote_Port3Subnet_mask_Type = IpAddress
_Pi_Remote_Port3Subnet_mask_Object = MibScalar
pi_Remote_Port3Subnet_mask = _Pi_Remote_Port3Subnet_mask_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3, 2),
    _Pi_Remote_Port3Subnet_mask_Type()
)
pi_Remote_Port3Subnet_mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port3Subnet_mask.setStatus("mandatory")
_Pi_Remote_Port3Gateway_Address_Type = IpAddress
_Pi_Remote_Port3Gateway_Address_Object = MibScalar
pi_Remote_Port3Gateway_Address = _Pi_Remote_Port3Gateway_Address_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3, 3),
    _Pi_Remote_Port3Gateway_Address_Type()
)
pi_Remote_Port3Gateway_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port3Gateway_Address.setStatus("mandatory")


class _Pi_Remote_Port3Data_link_protocol_Type(Integer32):
    """Custom type pi_Remote_Port3Data_link_protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            28
        )
    )
    namedValues = NamedValues(
        ("slip", 28)
    )


_Pi_Remote_Port3Data_link_protocol_Type.__name__ = "Integer32"
_Pi_Remote_Port3Data_link_protocol_Object = MibScalar
pi_Remote_Port3Data_link_protocol = _Pi_Remote_Port3Data_link_protocol_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3, 4),
    _Pi_Remote_Port3Data_link_protocol_Type()
)
pi_Remote_Port3Data_link_protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pi_Remote_Port3Data_link_protocol.setStatus("mandatory")


class _Pi_Remote_Port3Baudrate_Type(Integer32):
    """Custom type pi_Remote_Port3Baudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud-19200", 4),
          ("baud-2400", 1),
          ("baud-38400", 5),
          ("baud-4800", 2),
          ("baud-9600", 3))
    )


_Pi_Remote_Port3Baudrate_Type.__name__ = "Integer32"
_Pi_Remote_Port3Baudrate_Object = MibScalar
pi_Remote_Port3Baudrate = _Pi_Remote_Port3Baudrate_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 5, 3, 5),
    _Pi_Remote_Port3Baudrate_Type()
)
pi_Remote_Port3Baudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pi_Remote_Port3Baudrate.setStatus("mandatory")
_PiApplication_ObjectIdentity = ObjectIdentity
piApplication = _PiApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6)
)
_Pi_App_DLC_Cipher_Table_Object = MibTable
pi_App_DLC_Cipher_Table = _Pi_App_DLC_Cipher_Table_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1)
)
if mibBuilder.loadTexts:
    pi_App_DLC_Cipher_Table.setStatus("mandatory")
_Pi_App_DLC_Cipher_Entry_Object = MibTableRow
pi_App_DLC_Cipher_Entry = _Pi_App_DLC_Cipher_Entry_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1, 1)
)
pi_App_DLC_Cipher_Entry.setIndexNames(
    (0, "GDSFrameRelay-MIB", "piAppDLcCipherBand"),
)
if mibBuilder.loadTexts:
    pi_App_DLC_Cipher_Entry.setStatus("mandatory")
_PiAppDLcCipherBand_Type = Integer32
_PiAppDLcCipherBand_Object = MibTableColumn
piAppDLcCipherBand = _PiAppDLcCipherBand_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1, 1, 1),
    _PiAppDLcCipherBand_Type()
)
piAppDLcCipherBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    piAppDLcCipherBand.setStatus("mandatory")


class _PiAppDLcCipherUse_Type(Integer32):
    """Custom type piAppDLcCipherUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("plain", 1))
    )


_PiAppDLcCipherUse_Type.__name__ = "Integer32"
_PiAppDLcCipherUse_Object = MibTableColumn
piAppDLcCipherUse = _PiAppDLcCipherUse_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1, 1, 2),
    _PiAppDLcCipherUse_Type()
)
piAppDLcCipherUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piAppDLcCipherUse.setStatus("mandatory")


class _PiAppDLcCipherStart_Type(Integer32):
    """Custom type piAppDLcCipherStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PiAppDLcCipherStart_Type.__name__ = "Integer32"
_PiAppDLcCipherStart_Object = MibTableColumn
piAppDLcCipherStart = _PiAppDLcCipherStart_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1, 1, 3),
    _PiAppDLcCipherStart_Type()
)
piAppDLcCipherStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piAppDLcCipherStart.setStatus("mandatory")


class _PiAppDLcCipherEnd_set_to_activate_changes_Type(Integer32):
    """Custom type piAppDLcCipherEnd_set_to_activate_changes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_PiAppDLcCipherEnd_set_to_activate_changes_Type.__name__ = "Integer32"
_PiAppDLcCipherEnd_set_to_activate_changes_Object = MibScalar
piAppDLcCipherEnd_set_to_activate_changes = _PiAppDLcCipherEnd_set_to_activate_changes_Object(
    (1, 3, 6, 1, 4, 1, 1955, 5, 5, 3, 6, 1, 1, 4),
    _PiAppDLcCipherEnd_set_to_activate_changes_Type()
)
piAppDLcCipherEnd_set_to_activate_changes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    piAppDLcCipherEnd_set_to_activate_changes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDSFrameRelay-MIB",
    **{"gds": gds,
       "seriesfr": seriesfr,
       "is-GDS-frame-relay-device5": is_GDS_frame_relay_device5,
       "unit": unit,
       "uVersion-Strings": uVersion_Strings,
       "uMain-HW-Version": uMain_HW_Version,
       "uComm-HW-Version": uComm_HW_Version,
       "uMain-SW-Version": uMain_SW_Version,
       "uComm-SW-Version": uComm_SW_Version,
       "uAlgorithm": uAlgorithm,
       "uAccess-Table": uAccess_Table,
       "uConfigured": uConfigured,
       "uOwn-SID": uOwn_SID,
       "uDynamic": uDynamic,
       "uCurrent-Date": uCurrent_Date,
       "uCurrent-Time": uCurrent_Time,
       "uDevice-State": uDevice_State,
       "uComms-State": uComms_State,
       "uNMS-State": uNMS_State,
       "uSM-State": uSM_State,
       "uReady-Alarm-Led": uReady_Alarm_Led,
       "uBackground": uBackground,
       "uRAG-tests": uRAG_tests,
       "uRAG-fails": uRAG_fails,
       "uRAG-threshold": uRAG_threshold,
       "frame-relay": frame_relay,
       "reset-FR-statistic-counters": reset_FR_statistic_counters,
       "fR-Traffic-Table": fR_Traffic_Table,
       "fR-Traffic-Entry": fR_Traffic_Entry,
       "frPort-Index": frPort_Index,
       "frPort-Type": frPort_Type,
       "frGood-Frames": frGood_Frames,
       "frBad-Frames": frBad_Frames,
       "frInactive-DLCI": frInactive_DLCI,
       "frReceived-FECN": frReceived_FECN,
       "frReceived-BECN": frReceived_BECN,
       "frSent-Frames": frSent_Frames,
       "frDropped-Frames": frDropped_Frames,
       "fR-RX-Err-Table": fR_RX_Err_Table,
       "fR-RX-Err-Entry": fR_RX_Err_Entry,
       "frRxErrIndex": frRxErrIndex,
       "frRxErrShort-Frames": frRxErrShort_Frames,
       "frRxErrAborted-Frames": frRxErrAborted_Frames,
       "frRxErrResidual-Bits": frRxErrResidual_Bits,
       "frRxErrOverruns": frRxErrOverruns,
       "frRxErrCRC-Errors": frRxErrCRC_Errors,
       "configure": configure,
       "pi-FR-Layer1": pi_FR_Layer1,
       "piFRInterface-Installed": piFRInterface_Installed,
       "piFRTX-Clock-Source": piFRTX_Clock_Source,
       "piFRE1-Plain-Port-Impedance": piFRE1_Plain_Port_Impedance,
       "piFRE1-Cipher-Port-Impedance": piFRE1_Cipher_Port_Impedance,
       "piFRE1-Framing-Mode": piFRE1_Framing_Mode,
       "piFRE1-Time-Slot-Options": piFRE1_Time_Slot_Options,
       "piFRE1-Time-Slots": piFRE1_Time_Slots,
       "piFRT1-Plain-Port-Pulse": piFRT1_Plain_Port_Pulse,
       "piFRT1-Cipher-Port-Pulse": piFRT1_Cipher_Port_Pulse,
       "piFRT1-Framing-Mode": piFRT1_Framing_Mode,
       "piFRT1-Time-Slot-Options": piFRT1_Time_Slot_Options,
       "piFRT1-Time-Slots": piFRT1_Time_Slots,
       "pi-FR-Layer2": pi_FR_Layer2,
       "pi-FR-Logical-Interface-Type": pi_FR_Logical_Interface_Type,
       "pi-FR-Max-RX-Frame": pi_FR_Max_RX_Frame,
       "pi-FR-Max-TX-Frame": pi_FR_Max_TX_Frame,
       "pi-FR-LMI-support": pi_FR_LMI_support,
       "pi-FR-DLC-Ranges-Table": pi_FR_DLC_Ranges_Table,
       "pi-FR-DLC-Ranges-Entry": pi_FR_DLC_Ranges_Entry,
       "piFRDLcRangeBand": piFRDLcRangeBand,
       "piFRDLcRangeUse": piFRDLcRangeUse,
       "piFRDLcRangeMode": piFRDLcRangeMode,
       "piFRDLcRangeStart": piFRDLcRangeStart,
       "piFRDLcRangeEnd-set-to-activate-changes": piFRDLcRangeEnd_set_to_activate_changes,
       "piRemotePorts": piRemotePorts,
       "pi-Remote-Port1": pi_Remote_Port1,
       "pi-Remote-Port1IP-Address": pi_Remote_Port1IP_Address,
       "pi-Remote-Port1Subnet-mask": pi_Remote_Port1Subnet_mask,
       "pi-Remote-Port1Gateway-Address": pi_Remote_Port1Gateway_Address,
       "piRemotePort2": piRemotePort2,
       "pi-Remote-Port3": pi_Remote_Port3,
       "pi-Remote-Port3IP-Address": pi_Remote_Port3IP_Address,
       "pi-Remote-Port3Subnet-mask": pi_Remote_Port3Subnet_mask,
       "pi-Remote-Port3Gateway-Address": pi_Remote_Port3Gateway_Address,
       "pi-Remote-Port3Data-link-protocol": pi_Remote_Port3Data_link_protocol,
       "pi-Remote-Port3Baudrate": pi_Remote_Port3Baudrate,
       "piApplication": piApplication,
       "pi-App-DLC-Cipher-Table": pi_App_DLC_Cipher_Table,
       "pi-App-DLC-Cipher-Entry": pi_App_DLC_Cipher_Entry,
       "piAppDLcCipherBand": piAppDLcCipherBand,
       "piAppDLcCipherUse": piAppDLcCipherUse,
       "piAppDLcCipherStart": piAppDLcCipherStart,
       "piAppDLcCipherEnd-set-to-activate-changes": piAppDLcCipherEnd_set_to_activate_changes}
)
