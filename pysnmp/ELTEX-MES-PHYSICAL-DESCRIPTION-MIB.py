# SNMP MIB module (ELTEX-MES-PHYSICAL-DESCRIPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-PHYSICAL-DESCRIPTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:57 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(JackType,) = mibBuilder.importSymbols(
    "MAU-MIB",
    "JackType")

(rlCascadeEntry,
 rlPhdUnitGenParamEntry) = mibBuilder.importSymbols(
    "RADLAN-Physicaldescription-MIB",
    "rlCascadeEntry",
    "rlPhdUnitGenParamEntry")

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
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesPhysicalDescription = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53)
)
eltMesPhysicalDescription.setRevisions(
        ("2015-09-14 00:00",
         "2013-03-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesPhdTransceiver_ObjectIdentity = ObjectIdentity
eltMesPhdTransceiver = _EltMesPhdTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1)
)
_EltPhdTransceiverInfoTable_Object = MibTable
eltPhdTransceiverInfoTable = _EltPhdTransceiverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1)
)
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoTable.setStatus("current")
_EltPhdTransceiverInfoEntry_Object = MibTableRow
eltPhdTransceiverInfoEntry = _EltPhdTransceiverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1)
)
eltPhdTransceiverInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoEntry.setStatus("current")


class _EltPhdTransceiverInfoConnectorType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              32,
              33,
              34,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("copper-pigtail", 33),
          ("fibre-ch-coaxial-headers", 5),
          ("fibre-ch-st1", 2),
          ("fibre-ch-st2", 3),
          ("fibrejack", 6),
          ("hssdc-ii", 32),
          ("lc", 7),
          ("mpo-parallel-optic", 12),
          ("mt-rj", 8),
          ("mu", 9),
          ("optical-pigtail", 11),
          ("rj45", 34),
          ("sc", 1),
          ("sg", 10),
          ("unallocated", 127),
          ("unknown", 0),
          ("vendorspec", 255))
    )


_EltPhdTransceiverInfoConnectorType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoConnectorType_Object = MibTableColumn
eltPhdTransceiverInfoConnectorType = _EltPhdTransceiverInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 1),
    _EltPhdTransceiverInfoConnectorType_Type()
)
eltPhdTransceiverInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoConnectorType.setStatus("current")


class _EltPhdTransceiverInfoType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              127,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dwdm-sfp", 11),
          ("gbic", 1),
          ("qsfp", 12),
          ("reserved", 127),
          ("sff", 2),
          ("sfp-sfpplus", 3),
          ("unknown", 0),
          ("vendorspec", 255),
          ("x2", 10),
          ("xbi-300-pin", 4),
          ("xenpak", 5),
          ("xff", 7),
          ("xfp", 6),
          ("xfp-e", 8),
          ("xpak", 9))
    )


_EltPhdTransceiverInfoType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoType_Object = MibTableColumn
eltPhdTransceiverInfoType = _EltPhdTransceiverInfoType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 2),
    _EltPhdTransceiverInfoType_Type()
)
eltPhdTransceiverInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoType.setStatus("current")
_EltPhdTransceiverInfoComplianceCode_Type = OctetString
_EltPhdTransceiverInfoComplianceCode_Object = MibTableColumn
eltPhdTransceiverInfoComplianceCode = _EltPhdTransceiverInfoComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 3),
    _EltPhdTransceiverInfoComplianceCode_Type()
)
eltPhdTransceiverInfoComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoComplianceCode.setStatus("current")
_EltPhdTransceiverInfoWaveLength_Type = Integer32
_EltPhdTransceiverInfoWaveLength_Object = MibTableColumn
eltPhdTransceiverInfoWaveLength = _EltPhdTransceiverInfoWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 4),
    _EltPhdTransceiverInfoWaveLength_Type()
)
eltPhdTransceiverInfoWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoWaveLength.setStatus("current")
_EltPhdTransceiverInfoVendorName_Type = OctetString
_EltPhdTransceiverInfoVendorName_Object = MibTableColumn
eltPhdTransceiverInfoVendorName = _EltPhdTransceiverInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 5),
    _EltPhdTransceiverInfoVendorName_Type()
)
eltPhdTransceiverInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoVendorName.setStatus("current")
_EltPhdTransceiverInfoSerialNumber_Type = OctetString
_EltPhdTransceiverInfoSerialNumber_Object = MibTableColumn
eltPhdTransceiverInfoSerialNumber = _EltPhdTransceiverInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 6),
    _EltPhdTransceiverInfoSerialNumber_Type()
)
eltPhdTransceiverInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoSerialNumber.setStatus("current")


class _EltPhdTransceiverInfoFiberDiameterType_Type(Integer32):
    """Custom type eltPhdTransceiverInfoFiberDiameterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("copper", 4),
          ("fiber50", 2),
          ("fiber625", 3),
          ("fiber9", 1),
          ("unknown", 65535))
    )


_EltPhdTransceiverInfoFiberDiameterType_Type.__name__ = "Integer32"
_EltPhdTransceiverInfoFiberDiameterType_Object = MibTableColumn
eltPhdTransceiverInfoFiberDiameterType = _EltPhdTransceiverInfoFiberDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 7),
    _EltPhdTransceiverInfoFiberDiameterType_Type()
)
eltPhdTransceiverInfoFiberDiameterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoFiberDiameterType.setStatus("current")
_EltPhdTransceiverInfoTransferDistance_Type = Integer32
_EltPhdTransceiverInfoTransferDistance_Object = MibTableColumn
eltPhdTransceiverInfoTransferDistance = _EltPhdTransceiverInfoTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 8),
    _EltPhdTransceiverInfoTransferDistance_Type()
)
eltPhdTransceiverInfoTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoTransferDistance.setStatus("current")
_EltPhdTransceiverInfoDiagnostic_Type = TruthValue
_EltPhdTransceiverInfoDiagnostic_Object = MibTableColumn
eltPhdTransceiverInfoDiagnostic = _EltPhdTransceiverInfoDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 1, 1, 9),
    _EltPhdTransceiverInfoDiagnostic_Type()
)
eltPhdTransceiverInfoDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdTransceiverInfoDiagnostic.setStatus("current")
_EltPhdTransceiverThresholdTable_Object = MibTable
eltPhdTransceiverThresholdTable = _EltPhdTransceiverThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2)
)
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdTable.setStatus("current")
_EltPhdTransceiverThresholdEntry_Object = MibTableRow
eltPhdTransceiverThresholdEntry = _EltPhdTransceiverThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1)
)
eltPhdTransceiverThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-PHYSICAL-DESCRIPTION-MIB", "eltPhdTransceiverThresholdType"),
)
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdEntry.setStatus("current")


class _EltPhdTransceiverThresholdType_Type(Integer32):
    """Custom type eltPhdTransceiverThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rxOpticalPower", 4),
          ("supply", 1),
          ("temperature", 0),
          ("txBias", 2),
          ("txOutput", 3))
    )


_EltPhdTransceiverThresholdType_Type.__name__ = "Integer32"
_EltPhdTransceiverThresholdType_Object = MibTableColumn
eltPhdTransceiverThresholdType = _EltPhdTransceiverThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 1),
    _EltPhdTransceiverThresholdType_Type()
)
eltPhdTransceiverThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdType.setStatus("current")


class _EltPhdTransceiverThresholdAction_Type(Integer32):
    """Custom type eltPhdTransceiverThresholdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("none", 0),
          ("send-trap", 2))
    )


_EltPhdTransceiverThresholdAction_Type.__name__ = "Integer32"
_EltPhdTransceiverThresholdAction_Object = MibTableColumn
eltPhdTransceiverThresholdAction = _EltPhdTransceiverThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 2),
    _EltPhdTransceiverThresholdAction_Type()
)
eltPhdTransceiverThresholdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdAction.setStatus("current")
_EltPhdTransceiverThresholdHighAlarm_Type = Integer32
_EltPhdTransceiverThresholdHighAlarm_Object = MibTableColumn
eltPhdTransceiverThresholdHighAlarm = _EltPhdTransceiverThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 3),
    _EltPhdTransceiverThresholdHighAlarm_Type()
)
eltPhdTransceiverThresholdHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdHighAlarm.setStatus("current")
_EltPhdTransceiverThresholdHighWarning_Type = Integer32
_EltPhdTransceiverThresholdHighWarning_Object = MibTableColumn
eltPhdTransceiverThresholdHighWarning = _EltPhdTransceiverThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 4),
    _EltPhdTransceiverThresholdHighWarning_Type()
)
eltPhdTransceiverThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdHighWarning.setStatus("current")
_EltPhdTransceiverThresholdLowWarning_Type = Integer32
_EltPhdTransceiverThresholdLowWarning_Object = MibTableColumn
eltPhdTransceiverThresholdLowWarning = _EltPhdTransceiverThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 5),
    _EltPhdTransceiverThresholdLowWarning_Type()
)
eltPhdTransceiverThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdLowWarning.setStatus("current")
_EltPhdTransceiverThresholdLowAlarm_Type = Integer32
_EltPhdTransceiverThresholdLowAlarm_Object = MibTableColumn
eltPhdTransceiverThresholdLowAlarm = _EltPhdTransceiverThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 2, 1, 6),
    _EltPhdTransceiverThresholdLowAlarm_Type()
)
eltPhdTransceiverThresholdLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdLowAlarm.setStatus("current")


class _EltPhdTransceiverThresholdTimer_Type(Integer32):
    """Custom type eltPhdTransceiverThresholdTimer based on Integer32"""
    defaultValue = 120


_EltPhdTransceiverThresholdTimer_Object = MibScalar
eltPhdTransceiverThresholdTimer = _EltPhdTransceiverThresholdTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 1, 3),
    _EltPhdTransceiverThresholdTimer_Type()
)
eltPhdTransceiverThresholdTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPhdTransceiverThresholdTimer.setStatus("current")
_EltPhdUnitGenParamTable_Object = MibTable
eltPhdUnitGenParamTable = _EltPhdUnitGenParamTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2)
)
if mibBuilder.loadTexts:
    eltPhdUnitGenParamTable.setStatus("current")
_EltPhdUnitGenParamEntry_Object = MibTableRow
eltPhdUnitGenParamEntry = _EltPhdUnitGenParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1)
)
if mibBuilder.loadTexts:
    eltPhdUnitGenParamEntry.setStatus("current")
_EltPhdUnitGenParamCommitHash_Type = DisplayString
_EltPhdUnitGenParamCommitHash_Object = MibTableColumn
eltPhdUnitGenParamCommitHash = _EltPhdUnitGenParamCommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 2, 1, 1),
    _EltPhdUnitGenParamCommitHash_Type()
)
eltPhdUnitGenParamCommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhdUnitGenParamCommitHash.setStatus("current")
_EltCascadeTable_Object = MibTable
eltCascadeTable = _EltCascadeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3)
)
if mibBuilder.loadTexts:
    eltCascadeTable.setStatus("current")
_EltCascadeEntry_Object = MibTableRow
eltCascadeEntry = _EltCascadeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1)
)
if mibBuilder.loadTexts:
    eltCascadeEntry.setStatus("current")
_EltCascadeLastChange_Type = TimeTicks
_EltCascadeLastChange_Object = MibTableColumn
eltCascadeLastChange = _EltCascadeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 53, 3, 1, 1),
    _EltCascadeLastChange_Type()
)
eltCascadeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCascadeLastChange.setStatus("current")
rlPhdUnitGenParamEntry.registerAugmentions(
    ("ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
     "eltPhdUnitGenParamEntry")
)
eltPhdUnitGenParamEntry.setIndexNames(*rlPhdUnitGenParamEntry.getIndexNames())
rlCascadeEntry.registerAugmentions(
    ("ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
     "eltCascadeEntry")
)
eltCascadeEntry.setIndexNames(*rlCascadeEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-PHYSICAL-DESCRIPTION-MIB",
    **{"eltMesPhysicalDescription": eltMesPhysicalDescription,
       "eltMesPhdTransceiver": eltMesPhdTransceiver,
       "eltPhdTransceiverInfoTable": eltPhdTransceiverInfoTable,
       "eltPhdTransceiverInfoEntry": eltPhdTransceiverInfoEntry,
       "eltPhdTransceiverInfoConnectorType": eltPhdTransceiverInfoConnectorType,
       "eltPhdTransceiverInfoType": eltPhdTransceiverInfoType,
       "eltPhdTransceiverInfoComplianceCode": eltPhdTransceiverInfoComplianceCode,
       "eltPhdTransceiverInfoWaveLength": eltPhdTransceiverInfoWaveLength,
       "eltPhdTransceiverInfoVendorName": eltPhdTransceiverInfoVendorName,
       "eltPhdTransceiverInfoSerialNumber": eltPhdTransceiverInfoSerialNumber,
       "eltPhdTransceiverInfoFiberDiameterType": eltPhdTransceiverInfoFiberDiameterType,
       "eltPhdTransceiverInfoTransferDistance": eltPhdTransceiverInfoTransferDistance,
       "eltPhdTransceiverInfoDiagnostic": eltPhdTransceiverInfoDiagnostic,
       "eltPhdTransceiverThresholdTable": eltPhdTransceiverThresholdTable,
       "eltPhdTransceiverThresholdEntry": eltPhdTransceiverThresholdEntry,
       "eltPhdTransceiverThresholdType": eltPhdTransceiverThresholdType,
       "eltPhdTransceiverThresholdAction": eltPhdTransceiverThresholdAction,
       "eltPhdTransceiverThresholdHighAlarm": eltPhdTransceiverThresholdHighAlarm,
       "eltPhdTransceiverThresholdHighWarning": eltPhdTransceiverThresholdHighWarning,
       "eltPhdTransceiverThresholdLowWarning": eltPhdTransceiverThresholdLowWarning,
       "eltPhdTransceiverThresholdLowAlarm": eltPhdTransceiverThresholdLowAlarm,
       "eltPhdTransceiverThresholdTimer": eltPhdTransceiverThresholdTimer,
       "eltPhdUnitGenParamTable": eltPhdUnitGenParamTable,
       "eltPhdUnitGenParamEntry": eltPhdUnitGenParamEntry,
       "eltPhdUnitGenParamCommitHash": eltPhdUnitGenParamCommitHash,
       "eltCascadeTable": eltCascadeTable,
       "eltCascadeEntry": eltCascadeEntry,
       "eltCascadeLastChange": eltCascadeLastChange}
)
