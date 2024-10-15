# SNMP MIB module (ALANTEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALANTEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:28 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alantec_ObjectIdentity = ObjectIdentity
alantec = _Alantec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 1)
)
_Powerhub_ObjectIdentity = ObjectIdentity
powerhub = _Powerhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 1, 1)
)
_Powerbits_ObjectIdentity = ObjectIdentity
powerbits = _Powerbits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 1, 2)
)
_Powerhub7000_ObjectIdentity = ObjectIdentity
powerhub7000 = _Powerhub7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 1, 3)
)
_Alchassis_ObjectIdentity = ObjectIdentity
alchassis = _Alchassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1)
)
_AlSlotTable_Object = MibTable
alSlotTable = _AlSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alSlotTable.setStatus("mandatory")
_AlSlotEntry_Object = MibTableRow
alSlotEntry = _AlSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1)
)
alSlotEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alSlotNumber"),
)
if mibBuilder.loadTexts:
    alSlotEntry.setStatus("mandatory")
_AlSlotNumber_Type = Integer32
_AlSlotNumber_Object = MibTableColumn
alSlotNumber = _AlSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 1),
    _AlSlotNumber_Type()
)
alSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotNumber.setStatus("mandatory")


class _AlSlotCardType_Type(Integer32):
    """Custom type alSlotCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cddi-concentrator", 11),
          ("fast-thernet", 12),
          ("fddi-concentrator", 10),
          ("fddi-dual-das", 4),
          ("fddi-dual-universal", 8),
          ("fddi-single-das", 5),
          ("fddi-single-universal", 9),
          ("universal-ethernet", 1),
          ("utp-13X1", 7),
          ("utp-16X1", 6),
          ("utp-4X4", 2),
          ("utp-4X6", 3))
    )


_AlSlotCardType_Type.__name__ = "Integer32"
_AlSlotCardType_Object = MibTableColumn
alSlotCardType = _AlSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 2),
    _AlSlotCardType_Type()
)
alSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotCardType.setStatus("mandatory")


class _AlSlotStatus_Type(Integer32):
    """Custom type alSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-equipped", 1),
          ("not-present", 2))
    )


_AlSlotStatus_Type.__name__ = "Integer32"
_AlSlotStatus_Object = MibTableColumn
alSlotStatus = _AlSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 3),
    _AlSlotStatus_Type()
)
alSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotStatus.setStatus("mandatory")
_AlSlotModel_Type = DisplayString
_AlSlotModel_Object = MibTableColumn
alSlotModel = _AlSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 4),
    _AlSlotModel_Type()
)
alSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotModel.setStatus("mandatory")
_AlSlotRevision_Type = DisplayString
_AlSlotRevision_Object = MibTableColumn
alSlotRevision = _AlSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 5),
    _AlSlotRevision_Type()
)
alSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotRevision.setStatus("mandatory")
_AlSlotIssue_Type = DisplayString
_AlSlotIssue_Object = MibTableColumn
alSlotIssue = _AlSlotIssue_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 6),
    _AlSlotIssue_Type()
)
alSlotIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotIssue.setStatus("mandatory")
_AlSlotDeviation_Type = DisplayString
_AlSlotDeviation_Object = MibTableColumn
alSlotDeviation = _AlSlotDeviation_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 7),
    _AlSlotDeviation_Type()
)
alSlotDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotDeviation.setStatus("mandatory")
_AlSlotSerialNumber_Type = DisplayString
_AlSlotSerialNumber_Object = MibTableColumn
alSlotSerialNumber = _AlSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 8),
    _AlSlotSerialNumber_Type()
)
alSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotSerialNumber.setStatus("mandatory")
_AlSlotPower5_Type = Integer32
_AlSlotPower5_Object = MibTableColumn
alSlotPower5 = _AlSlotPower5_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 9),
    _AlSlotPower5_Type()
)
alSlotPower5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower5.setStatus("mandatory")
_AlSlotPower12_Type = Integer32
_AlSlotPower12_Object = MibTableColumn
alSlotPower12 = _AlSlotPower12_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 10),
    _AlSlotPower12_Type()
)
alSlotPower12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower12.setStatus("mandatory")
_AlSlotPower33_Type = Integer32
_AlSlotPower33_Object = MibTableColumn
alSlotPower33 = _AlSlotPower33_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 11),
    _AlSlotPower33_Type()
)
alSlotPower33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPower33.setStatus("mandatory")
_AlSlotPowerOther_Type = Integer32
_AlSlotPowerOther_Object = MibTableColumn
alSlotPowerOther = _AlSlotPowerOther_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 1, 1, 12),
    _AlSlotPowerOther_Type()
)
alSlotPowerOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotPowerOther.setStatus("mandatory")
_AlVportTable_Object = MibTable
alVportTable = _AlVportTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alVportTable.setStatus("mandatory")
_AlVportEntry_Object = MibTableRow
alVportEntry = _AlVportEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1)
)
alVportEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alVportNumber"),
)
if mibBuilder.loadTexts:
    alVportEntry.setStatus("mandatory")
_AlVportNumber_Type = Integer32
_AlVportNumber_Object = MibTableColumn
alVportNumber = _AlVportNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 1),
    _AlVportNumber_Type()
)
alVportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportNumber.setStatus("mandatory")
_AlVportSlotNumber_Type = Integer32
_AlVportSlotNumber_Object = MibTableColumn
alVportSlotNumber = _AlVportSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 2),
    _AlVportSlotNumber_Type()
)
alVportSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportSlotNumber.setStatus("mandatory")
_AlVportPortNumber_Type = Integer32
_AlVportPortNumber_Object = MibTableColumn
alVportPortNumber = _AlVportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 3),
    _AlVportPortNumber_Type()
)
alVportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportPortNumber.setStatus("mandatory")


class _AlVportPortType_Type(Integer32):
    """Custom type alVportPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aui", 3),
          ("bnc", 1),
          ("fiber", 2),
          ("not-stuffed", 7))
    )


_AlVportPortType_Type.__name__ = "Integer32"
_AlVportPortType_Object = MibTableColumn
alVportPortType = _AlVportPortType_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 4),
    _AlVportPortType_Type()
)
alVportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportPortType.setStatus("mandatory")


class _AlVportStatus_Type(Integer32):
    """Custom type alVportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("removed", 2))
    )


_AlVportStatus_Type.__name__ = "Integer32"
_AlVportStatus_Object = MibTableColumn
alVportStatus = _AlVportStatus_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 5),
    _AlVportStatus_Type()
)
alVportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportStatus.setStatus("mandatory")
_AlVportControllerType_Type = Integer32
_AlVportControllerType_Object = MibTableColumn
alVportControllerType = _AlVportControllerType_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 2, 1, 6),
    _AlVportControllerType_Type()
)
alVportControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alVportControllerType.setStatus("mandatory")
_AlSlotToVportTable_Object = MibTable
alSlotToVportTable = _AlSlotToVportTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    alSlotToVportTable.setStatus("mandatory")
_AlSlotVportEntry_Object = MibTableRow
alSlotVportEntry = _AlSlotVportEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1)
)
alSlotVportEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alSlotVportSlotNumber"),
    (0, "ALANTEC-MIB", "alSlotVportPortNumber"),
)
if mibBuilder.loadTexts:
    alSlotVportEntry.setStatus("mandatory")
_AlSlotVportSlotNumber_Type = Integer32
_AlSlotVportSlotNumber_Object = MibTableColumn
alSlotVportSlotNumber = _AlSlotVportSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 1),
    _AlSlotVportSlotNumber_Type()
)
alSlotVportSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportSlotNumber.setStatus("mandatory")
_AlSlotVportPortNumber_Type = Integer32
_AlSlotVportPortNumber_Object = MibTableColumn
alSlotVportPortNumber = _AlSlotVportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 2),
    _AlSlotVportPortNumber_Type()
)
alSlotVportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportPortNumber.setStatus("mandatory")
_AlSlotVportNumber_Type = Integer32
_AlSlotVportNumber_Object = MibTableColumn
alSlotVportNumber = _AlSlotVportNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 3),
    _AlSlotVportNumber_Type()
)
alSlotVportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportNumber.setStatus("mandatory")
_AlSlotVportPortType_Type = Integer32
_AlSlotVportPortType_Object = MibTableColumn
alSlotVportPortType = _AlSlotVportPortType_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 4),
    _AlSlotVportPortType_Type()
)
alSlotVportPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportPortType.setStatus("mandatory")
_AlSlotVportStatus_Type = Integer32
_AlSlotVportStatus_Object = MibTableColumn
alSlotVportStatus = _AlSlotVportStatus_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 5),
    _AlSlotVportStatus_Type()
)
alSlotVportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportStatus.setStatus("mandatory")
_AlSlotVportControllerType_Type = Integer32
_AlSlotVportControllerType_Object = MibTableColumn
alSlotVportControllerType = _AlSlotVportControllerType_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 3, 1, 6),
    _AlSlotVportControllerType_Type()
)
alSlotVportControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSlotVportControllerType.setStatus("mandatory")
_AlPSTable_Object = MibTable
alPSTable = _AlPSTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    alPSTable.setStatus("mandatory")
_AlPSEntry_Object = MibTableRow
alPSEntry = _AlPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 4, 1)
)
alPSEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alPSNumber"),
)
if mibBuilder.loadTexts:
    alPSEntry.setStatus("mandatory")
_AlPSNumber_Type = Integer32
_AlPSNumber_Object = MibTableColumn
alPSNumber = _AlPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 4, 1, 1),
    _AlPSNumber_Type()
)
alPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPSNumber.setStatus("mandatory")
_AlPSStatus_Type = Integer32
_AlPSStatus_Object = MibTableColumn
alPSStatus = _AlPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 4, 1, 2),
    _AlPSStatus_Type()
)
alPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPSStatus.setStatus("mandatory")
_AlCpuSlot_Type = Integer32
_AlCpuSlot_Object = MibScalar
alCpuSlot = _AlCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 390, 1, 3, 1, 5),
    _AlCpuSlot_Type()
)
alCpuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCpuSlot.setStatus("mandatory")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2)
)
_Alsystem_ObjectIdentity = ObjectIdentity
alsystem = _Alsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 1)
)


class _AlChassisType_Type(Integer32):
    """Custom type alChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("model3100", 1),
          ("model3200", 2),
          ("model3300", 3),
          ("model3401", 5),
          ("model3402", 6),
          ("model3403", 7),
          ("model3404", 8),
          ("model3405", 9),
          ("model3406", 10),
          ("model3407", 11),
          ("model3410", 12),
          ("model3411", 13),
          ("model3412", 14),
          ("model3420", 15),
          ("model3421", 16),
          ("model3422", 17),
          ("model3423", 18),
          ("model3424", 19),
          ("model3425", 20),
          ("model3500", 4),
          ("model5001", 21),
          ("model5002", 22),
          ("model5003", 23),
          ("model5004", 24),
          ("model5005", 25),
          ("model5006", 26))
    )


_AlChassisType_Type.__name__ = "Integer32"
_AlChassisType_Object = MibScalar
alChassisType = _AlChassisType_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 1),
    _AlChassisType_Type()
)
alChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alChassisType.setStatus("mandatory")
_AlMcpuRtVer_Type = DisplayString
_AlMcpuRtVer_Object = MibScalar
alMcpuRtVer = _AlMcpuRtVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 2),
    _AlMcpuRtVer_Type()
)
alMcpuRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMcpuRtVer.setStatus("mandatory")
_AlMcpuPromVer_Type = DisplayString
_AlMcpuPromVer_Object = MibScalar
alMcpuPromVer = _AlMcpuPromVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 3),
    _AlMcpuPromVer_Type()
)
alMcpuPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMcpuPromVer.setStatus("mandatory")
_AlFcpuOneRtVer_Type = DisplayString
_AlFcpuOneRtVer_Object = MibScalar
alFcpuOneRtVer = _AlFcpuOneRtVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 4),
    _AlFcpuOneRtVer_Type()
)
alFcpuOneRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuOneRtVer.setStatus("mandatory")
_AlFcpuTwoRtVer_Type = DisplayString
_AlFcpuTwoRtVer_Object = MibScalar
alFcpuTwoRtVer = _AlFcpuTwoRtVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 5),
    _AlFcpuTwoRtVer_Type()
)
alFcpuTwoRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuTwoRtVer.setStatus("mandatory")
_AlFcpuOnePromVer_Type = DisplayString
_AlFcpuOnePromVer_Object = MibScalar
alFcpuOnePromVer = _AlFcpuOnePromVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 6),
    _AlFcpuOnePromVer_Type()
)
alFcpuOnePromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuOnePromVer.setStatus("mandatory")
_AlFcpuTwoPromVer_Type = DisplayString
_AlFcpuTwoPromVer_Object = MibScalar
alFcpuTwoPromVer = _AlFcpuTwoPromVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 7),
    _AlFcpuTwoPromVer_Type()
)
alFcpuTwoPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFcpuTwoPromVer.setStatus("mandatory")
_AlRcpuOneRtVer_Type = DisplayString
_AlRcpuOneRtVer_Object = MibScalar
alRcpuOneRtVer = _AlRcpuOneRtVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 8),
    _AlRcpuOneRtVer_Type()
)
alRcpuOneRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuOneRtVer.setStatus("mandatory")
_AlRcpuTwoRtVer_Type = DisplayString
_AlRcpuTwoRtVer_Object = MibScalar
alRcpuTwoRtVer = _AlRcpuTwoRtVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 9),
    _AlRcpuTwoRtVer_Type()
)
alRcpuTwoRtVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuTwoRtVer.setStatus("mandatory")
_AlRcpuOnePromVer_Type = DisplayString
_AlRcpuOnePromVer_Object = MibScalar
alRcpuOnePromVer = _AlRcpuOnePromVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 10),
    _AlRcpuOnePromVer_Type()
)
alRcpuOnePromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuOnePromVer.setStatus("mandatory")
_AlRcpuTwoPromVer_Type = DisplayString
_AlRcpuTwoPromVer_Object = MibScalar
alRcpuTwoPromVer = _AlRcpuTwoPromVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 1, 11),
    _AlRcpuTwoPromVer_Type()
)
alRcpuTwoPromVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRcpuTwoPromVer.setStatus("mandatory")
_Albridge_ObjectIdentity = ObjectIdentity
albridge = _Albridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 2)
)
_AlBridgeTable_Object = MibTable
alBridgeTable = _AlBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alBridgeTable.setStatus("mandatory")
_AlBridgeEntry_Object = MibTableRow
alBridgeEntry = _AlBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1)
)
alBridgeEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alBridgeEntryAddress"),
)
if mibBuilder.loadTexts:
    alBridgeEntry.setStatus("mandatory")
_AlBridgeEntryAddress_Type = MacAddress
_AlBridgeEntryAddress_Object = MibTableColumn
alBridgeEntryAddress = _AlBridgeEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1, 1),
    _AlBridgeEntryAddress_Type()
)
alBridgeEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryAddress.setStatus("mandatory")
_AlBridgeEntryPort_Type = Integer32
_AlBridgeEntryPort_Object = MibTableColumn
alBridgeEntryPort = _AlBridgeEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1, 2),
    _AlBridgeEntryPort_Type()
)
alBridgeEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryPort.setStatus("mandatory")
_AlBridgeEntryLink_Type = Integer32
_AlBridgeEntryLink_Object = MibTableColumn
alBridgeEntryLink = _AlBridgeEntryLink_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1, 3),
    _AlBridgeEntryLink_Type()
)
alBridgeEntryLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryLink.setStatus("mandatory")
_AlBridgeEntryRule_Type = Integer32
_AlBridgeEntryRule_Object = MibTableColumn
alBridgeEntryRule = _AlBridgeEntryRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1, 4),
    _AlBridgeEntryRule_Type()
)
alBridgeEntryRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeEntryRule.setStatus("mandatory")
_AlBridgeEntryFlags_Type = Integer32
_AlBridgeEntryFlags_Object = MibTableColumn
alBridgeEntryFlags = _AlBridgeEntryFlags_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 1, 1, 5),
    _AlBridgeEntryFlags_Type()
)
alBridgeEntryFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBridgeEntryFlags.setStatus("mandatory")
_AlBridgeTblClear_Type = Integer32
_AlBridgeTblClear_Object = MibScalar
alBridgeTblClear = _AlBridgeTblClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 2),
    _AlBridgeTblClear_Type()
)
alBridgeTblClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeTblClear.setStatus("mandatory")
_AlBrFlushCache_Type = Integer32
_AlBrFlushCache_Object = MibScalar
alBrFlushCache = _AlBrFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 3),
    _AlBrFlushCache_Type()
)
alBrFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBrFlushCache.setStatus("mandatory")
_AlPortStatsTable_Object = MibTable
alPortStatsTable = _AlPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4)
)
if mibBuilder.loadTexts:
    alPortStatsTable.setStatus("mandatory")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1)
)
portStatsEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portStatsPort"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("mandatory")
_PortStatsPort_Type = Integer32
_PortStatsPort_Object = MibTableColumn
portStatsPort = _PortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 1),
    _PortStatsPort_Type()
)
portStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPort.setStatus("mandatory")
_PortStatsPktsIn_Type = Integer32
_PortStatsPktsIn_Object = MibTableColumn
portStatsPktsIn = _PortStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 2),
    _PortStatsPktsIn_Type()
)
portStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsIn.setStatus("mandatory")
_PortStatsPktsOut_Type = Integer32
_PortStatsPktsOut_Object = MibTableColumn
portStatsPktsOut = _PortStatsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 3),
    _PortStatsPktsOut_Type()
)
portStatsPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPktsOut.setStatus("mandatory")
_PortStatsOctetsIn_Type = Integer32
_PortStatsOctetsIn_Object = MibTableColumn
portStatsOctetsIn = _PortStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 4),
    _PortStatsOctetsIn_Type()
)
portStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOctetsIn.setStatus("mandatory")
_PortStatsOctetsOut_Type = Integer32
_PortStatsOctetsOut_Object = MibTableColumn
portStatsOctetsOut = _PortStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 5),
    _PortStatsOctetsOut_Type()
)
portStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsOctetsOut.setStatus("mandatory")
_PortStatsMultiCastPktsIn_Type = Integer32
_PortStatsMultiCastPktsIn_Object = MibTableColumn
portStatsMultiCastPktsIn = _PortStatsMultiCastPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 6),
    _PortStatsMultiCastPktsIn_Type()
)
portStatsMultiCastPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsMultiCastPktsIn.setStatus("mandatory")
_PortStatsMulticastPktsOut_Type = Integer32
_PortStatsMulticastPktsOut_Object = MibTableColumn
portStatsMulticastPktsOut = _PortStatsMulticastPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 7),
    _PortStatsMulticastPktsOut_Type()
)
portStatsMulticastPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsMulticastPktsOut.setStatus("mandatory")
_PortStatsTableMisses_Type = Integer32
_PortStatsTableMisses_Object = MibTableColumn
portStatsTableMisses = _PortStatsTableMisses_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 8),
    _PortStatsTableMisses_Type()
)
portStatsTableMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsTableMisses.setStatus("mandatory")
_PortStatsRcvBuffErrs_Type = Integer32
_PortStatsRcvBuffErrs_Object = MibTableColumn
portStatsRcvBuffErrs = _PortStatsRcvBuffErrs_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 9),
    _PortStatsRcvBuffErrs_Type()
)
portStatsRcvBuffErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsRcvBuffErrs.setStatus("mandatory")
_PortStatsXmitBuffErrs_Type = Integer32
_PortStatsXmitBuffErrs_Object = MibTableColumn
portStatsXmitBuffErrs = _PortStatsXmitBuffErrs_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 10),
    _PortStatsXmitBuffErrs_Type()
)
portStatsXmitBuffErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitBuffErrs.setStatus("mandatory")
_PortStatsTotalCollisions_Type = Integer32
_PortStatsTotalCollisions_Object = MibTableColumn
portStatsTotalCollisions = _PortStatsTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 11),
    _PortStatsTotalCollisions_Type()
)
portStatsTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsTotalCollisions.setStatus("mandatory")
_PortStatsRcvCollisions_Type = Integer32
_PortStatsRcvCollisions_Object = MibTableColumn
portStatsRcvCollisions = _PortStatsRcvCollisions_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 12),
    _PortStatsRcvCollisions_Type()
)
portStatsRcvCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsRcvCollisions.setStatus("mandatory")
_PortStatsXmitCollisions_Type = Integer32
_PortStatsXmitCollisions_Object = MibTableColumn
portStatsXmitCollisions = _PortStatsXmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 13),
    _PortStatsXmitCollisions_Type()
)
portStatsXmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitCollisions.setStatus("mandatory")
_PortStatsXmitQLen_Type = Integer32
_PortStatsXmitQLen_Object = MibTableColumn
portStatsXmitQLen = _PortStatsXmitQLen_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 14),
    _PortStatsXmitQLen_Type()
)
portStatsXmitQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsXmitQLen.setStatus("mandatory")
_PortStatsPeakUtilization_Type = Integer32
_PortStatsPeakUtilization_Object = MibTableColumn
portStatsPeakUtilization = _PortStatsPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 15),
    _PortStatsPeakUtilization_Type()
)
portStatsPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsPeakUtilization.setStatus("mandatory")
_PortStatsCurrUtilization_Type = Integer32
_PortStatsCurrUtilization_Object = MibTableColumn
portStatsCurrUtilization = _PortStatsCurrUtilization_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 16),
    _PortStatsCurrUtilization_Type()
)
portStatsCurrUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsCurrUtilization.setStatus("mandatory")
_PortStatsLossOfCarrier_Type = Integer32
_PortStatsLossOfCarrier_Object = MibTableColumn
portStatsLossOfCarrier = _PortStatsLossOfCarrier_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 17),
    _PortStatsLossOfCarrier_Type()
)
portStatsLossOfCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsLossOfCarrier.setStatus("mandatory")
_PortStatsExcessRetries_Type = Integer32
_PortStatsExcessRetries_Object = MibTableColumn
portStatsExcessRetries = _PortStatsExcessRetries_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 4, 1, 18),
    _PortStatsExcessRetries_Type()
)
portStatsExcessRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatsExcessRetries.setStatus("mandatory")
_AlBridgeStatsClear_Type = Integer32
_AlBridgeStatsClear_Object = MibScalar
alBridgeStatsClear = _AlBridgeStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 5),
    _AlBridgeStatsClear_Type()
)
alBridgeStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeStatsClear.setStatus("mandatory")


class _AlBridgePPControl_Type(Integer32):
    """Custom type alBridgePPControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("enable", 1))
    )


_AlBridgePPControl_Type.__name__ = "Integer32"
_AlBridgePPControl_Object = MibScalar
alBridgePPControl = _AlBridgePPControl_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 6),
    _AlBridgePPControl_Type()
)
alBridgePPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgePPControl.setStatus("mandatory")
_AlPortToPortTable_Object = MibTable
alPortToPortTable = _AlPortToPortTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7)
)
if mibBuilder.loadTexts:
    alPortToPortTable.setStatus("mandatory")
_PortToPortEntry_Object = MibTableRow
portToPortEntry = _PortToPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7, 1)
)
portToPortEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alPPSourecPort"),
    (0, "ALANTEC-MIB", "alPPDestinationPort"),
)
if mibBuilder.loadTexts:
    portToPortEntry.setStatus("mandatory")
_AlPPSourecPort_Type = Integer32
_AlPPSourecPort_Object = MibTableColumn
alPPSourecPort = _AlPPSourecPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7, 1, 1),
    _AlPPSourecPort_Type()
)
alPPSourecPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPSourecPort.setStatus("mandatory")
_AlPPDestinationPort_Type = Integer32
_AlPPDestinationPort_Object = MibTableColumn
alPPDestinationPort = _AlPPDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7, 1, 2),
    _AlPPDestinationPort_Type()
)
alPPDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPDestinationPort.setStatus("mandatory")
_PortToPortPackets_Type = Integer32
_PortToPortPackets_Object = MibTableColumn
portToPortPackets = _PortToPortPackets_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7, 1, 3),
    _PortToPortPackets_Type()
)
portToPortPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToPortPackets.setStatus("mandatory")
_PortToPortOctets_Type = Integer32
_PortToPortOctets_Object = MibTableColumn
portToPortOctets = _PortToPortOctets_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 7, 1, 4),
    _PortToPortOctets_Type()
)
portToPortOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portToPortOctets.setStatus("mandatory")
_AlPortConfigTable_Object = MibTable
alPortConfigTable = _AlPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8)
)
if mibBuilder.loadTexts:
    alPortConfigTable.setStatus("mandatory")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8, 1)
)
portConfigEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portConfigPort"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("mandatory")
_PortConfigPort_Type = Integer32
_PortConfigPort_Object = MibTableColumn
portConfigPort = _PortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8, 1, 1),
    _PortConfigPort_Type()
)
portConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigPort.setStatus("mandatory")
_PortConfigSrcRule_Type = Integer32
_PortConfigSrcRule_Object = MibTableColumn
portConfigSrcRule = _PortConfigSrcRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8, 1, 2),
    _PortConfigSrcRule_Type()
)
portConfigSrcRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigSrcRule.setStatus("mandatory")
_PortConfigDstRule_Type = Integer32
_PortConfigDstRule_Object = MibTableColumn
portConfigDstRule = _PortConfigDstRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8, 1, 3),
    _PortConfigDstRule_Type()
)
portConfigDstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDstRule.setStatus("mandatory")
_PortConfigBlockLearnedEntries_Type = Integer32
_PortConfigBlockLearnedEntries_Object = MibTableColumn
portConfigBlockLearnedEntries = _PortConfigBlockLearnedEntries_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 8, 1, 4),
    _PortConfigBlockLearnedEntries_Type()
)
portConfigBlockLearnedEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBlockLearnedEntries.setStatus("mandatory")
_AlBridgeIpBridging_Type = Integer32
_AlBridgeIpBridging_Object = MibScalar
alBridgeIpBridging = _AlBridgeIpBridging_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 9),
    _AlBridgeIpBridging_Type()
)
alBridgeIpBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeIpBridging.setStatus("mandatory")
_AlBrTemplateTable_Object = MibTable
alBrTemplateTable = _AlBrTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10)
)
if mibBuilder.loadTexts:
    alBrTemplateTable.setStatus("mandatory")
_BrTemplateEntry_Object = MibTableRow
brTemplateEntry = _BrTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1)
)
brTemplateEntry.setIndexNames(
    (0, "ALANTEC-MIB", "brTemplateNumber"),
)
if mibBuilder.loadTexts:
    brTemplateEntry.setStatus("mandatory")
_BrTemplateNumber_Type = Integer32
_BrTemplateNumber_Object = MibTableColumn
brTemplateNumber = _BrTemplateNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1, 1),
    _BrTemplateNumber_Type()
)
brTemplateNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateNumber.setStatus("mandatory")
_BrTemplateOffset_Type = Integer32
_BrTemplateOffset_Object = MibTableColumn
brTemplateOffset = _BrTemplateOffset_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1, 2),
    _BrTemplateOffset_Type()
)
brTemplateOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateOffset.setStatus("mandatory")
_BrTemplateMask_Type = Counter32
_BrTemplateMask_Object = MibTableColumn
brTemplateMask = _BrTemplateMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1, 3),
    _BrTemplateMask_Type()
)
brTemplateMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateMask.setStatus("mandatory")
_BrTemplateComparator_Type = Counter32
_BrTemplateComparator_Object = MibTableColumn
brTemplateComparator = _BrTemplateComparator_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1, 4),
    _BrTemplateComparator_Type()
)
brTemplateComparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateComparator.setStatus("mandatory")
_BrTemplateOption_Type = Integer32
_BrTemplateOption_Object = MibTableColumn
brTemplateOption = _BrTemplateOption_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 10, 1, 5),
    _BrTemplateOption_Type()
)
brTemplateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brTemplateOption.setStatus("mandatory")
_AlBrRuleTable_Object = MibTable
alBrRuleTable = _AlBrRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 11)
)
if mibBuilder.loadTexts:
    alBrRuleTable.setStatus("mandatory")
_BrRuleEntry_Object = MibTableRow
brRuleEntry = _BrRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 11, 1)
)
brRuleEntry.setIndexNames(
    (0, "ALANTEC-MIB", "brRuleNumber"),
)
if mibBuilder.loadTexts:
    brRuleEntry.setStatus("mandatory")
_BrRuleNumber_Type = Integer32
_BrRuleNumber_Object = MibTableColumn
brRuleNumber = _BrRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 11, 1, 1),
    _BrRuleNumber_Type()
)
brRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleNumber.setStatus("mandatory")
_BrRuleStatement_Type = DisplayString
_BrRuleStatement_Object = MibTableColumn
brRuleStatement = _BrRuleStatement_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 11, 1, 2),
    _BrRuleStatement_Type()
)
brRuleStatement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleStatement.setStatus("mandatory")
_AlBrRuleToNodeTable_Object = MibTable
alBrRuleToNodeTable = _AlBrRuleToNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 12)
)
if mibBuilder.loadTexts:
    alBrRuleToNodeTable.setStatus("mandatory")
_AlBrRuleToNodeEntry_Object = MibTableRow
alBrRuleToNodeEntry = _AlBrRuleToNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 12, 1)
)
alBrRuleToNodeEntry.setIndexNames(
    (0, "ALANTEC-MIB", "brRuleToNodePort"),
)
if mibBuilder.loadTexts:
    alBrRuleToNodeEntry.setStatus("mandatory")
_BrRuleToNodePort_Type = Integer32
_BrRuleToNodePort_Object = MibTableColumn
brRuleToNodePort = _BrRuleToNodePort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 12, 1, 1),
    _BrRuleToNodePort_Type()
)
brRuleToNodePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodePort.setStatus("mandatory")
_BrRuleToNodeMacAddr_Type = PhysAddress
_BrRuleToNodeMacAddr_Object = MibTableColumn
brRuleToNodeMacAddr = _BrRuleToNodeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 12, 1, 2),
    _BrRuleToNodeMacAddr_Type()
)
brRuleToNodeMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodeMacAddr.setStatus("mandatory")
_BrRuleToNodeRule_Type = Integer32
_BrRuleToNodeRule_Object = MibTableColumn
brRuleToNodeRule = _BrRuleToNodeRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 12, 1, 3),
    _BrRuleToNodeRule_Type()
)
brRuleToNodeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brRuleToNodeRule.setStatus("mandatory")
_AlBrGroupTable_Object = MibTable
alBrGroupTable = _AlBrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 13)
)
if mibBuilder.loadTexts:
    alBrGroupTable.setStatus("mandatory")
_AlBrGroupEntry_Object = MibTableRow
alBrGroupEntry = _AlBrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 13, 1)
)
alBrGroupEntry.setIndexNames(
    (0, "ALANTEC-MIB", "brGroupNumber"),
)
if mibBuilder.loadTexts:
    alBrGroupEntry.setStatus("mandatory")
_BrGroupNumber_Type = Integer32
_BrGroupNumber_Object = MibTableColumn
brGroupNumber = _BrGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 13, 1, 1),
    _BrGroupNumber_Type()
)
brGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brGroupNumber.setStatus("mandatory")
_BrGroupPortsMask_Type = Integer32
_BrGroupPortsMask_Object = MibTableColumn
brGroupPortsMask = _BrGroupPortsMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 13, 1, 2),
    _BrGroupPortsMask_Type()
)
brGroupPortsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brGroupPortsMask.setStatus("mandatory")
_BrGroupName_Type = OctetString
_BrGroupName_Object = MibTableColumn
brGroupName = _BrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 13, 1, 3),
    _BrGroupName_Type()
)
brGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brGroupName.setStatus("mandatory")
_AlBridgeSTPControl_Type = Integer32
_AlBridgeSTPControl_Object = MibScalar
alBridgeSTPControl = _AlBridgeSTPControl_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 14),
    _AlBridgeSTPControl_Type()
)
alBridgeSTPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alBridgeSTPControl.setStatus("mandatory")
_AlPortStateTable_Object = MibTable
alPortStateTable = _AlPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15)
)
if mibBuilder.loadTexts:
    alPortStateTable.setStatus("mandatory")
_PortStateEntry_Object = MibTableRow
portStateEntry = _PortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1)
)
portStateEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portStatePort"),
)
if mibBuilder.loadTexts:
    portStateEntry.setStatus("mandatory")
_PortStatePort_Type = Integer32
_PortStatePort_Object = MibTableColumn
portStatePort = _PortStatePort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1, 1),
    _PortStatePort_Type()
)
portStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatePort.setStatus("mandatory")
_PortStateDiag_Type = Integer32
_PortStateDiag_Object = MibTableColumn
portStateDiag = _PortStateDiag_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1, 2),
    _PortStateDiag_Type()
)
portStateDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateDiag.setStatus("mandatory")
_PortStateMgmt_Type = Integer32
_PortStateMgmt_Object = MibTableColumn
portStateMgmt = _PortStateMgmt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1, 3),
    _PortStateMgmt_Type()
)
portStateMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateMgmt.setStatus("mandatory")
_PortStateStp_Type = Integer32
_PortStateStp_Object = MibTableColumn
portStateStp = _PortStateStp_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1, 4),
    _PortStateStp_Type()
)
portStateStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStateStp.setStatus("mandatory")
_PortStatePortName_Type = DisplayString
_PortStatePortName_Object = MibTableColumn
portStatePortName = _PortStatePortName_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 2, 15, 1, 5),
    _PortStatePortName_Type()
)
portStatePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatePortName.setStatus("mandatory")
_Almgmt_ObjectIdentity = ObjectIdentity
almgmt = _Almgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 3)
)
_AlLinkStatsCollect_Type = Integer32
_AlLinkStatsCollect_Object = MibScalar
alLinkStatsCollect = _AlLinkStatsCollect_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 2),
    _AlLinkStatsCollect_Type()
)
alLinkStatsCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLinkStatsCollect.setStatus("mandatory")
_AlLinkStatsClear_Type = Integer32
_AlLinkStatsClear_Object = MibScalar
alLinkStatsClear = _AlLinkStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 3),
    _AlLinkStatsClear_Type()
)
alLinkStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alLinkStatsClear.setStatus("mandatory")
_AlLinkStatsTable_Object = MibTable
alLinkStatsTable = _AlLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4)
)
if mibBuilder.loadTexts:
    alLinkStatsTable.setStatus("mandatory")
_LinkStatsEntry_Object = MibTableRow
linkStatsEntry = _LinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1)
)
linkStatsEntry.setIndexNames(
    (0, "ALANTEC-MIB", "linkStatsPort"),
    (0, "ALANTEC-MIB", "linkStatsLink"),
)
if mibBuilder.loadTexts:
    linkStatsEntry.setStatus("mandatory")
_LinkStatsPort_Type = Integer32
_LinkStatsPort_Object = MibTableColumn
linkStatsPort = _LinkStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 1),
    _LinkStatsPort_Type()
)
linkStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsPort.setStatus("mandatory")
_LinkStatsLink_Type = Integer32
_LinkStatsLink_Object = MibTableColumn
linkStatsLink = _LinkStatsLink_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 2),
    _LinkStatsLink_Type()
)
linkStatsLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsLink.setStatus("mandatory")
_LinkStatsPktsIn_Type = Integer32
_LinkStatsPktsIn_Object = MibTableColumn
linkStatsPktsIn = _LinkStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 3),
    _LinkStatsPktsIn_Type()
)
linkStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsPktsIn.setStatus("mandatory")
_LinkStatsOctetsIn_Type = Integer32
_LinkStatsOctetsIn_Object = MibTableColumn
linkStatsOctetsIn = _LinkStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 4),
    _LinkStatsOctetsIn_Type()
)
linkStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsOctetsIn.setStatus("mandatory")
_LinkStatsBMCastPktsIn_Type = Integer32
_LinkStatsBMCastPktsIn_Object = MibTableColumn
linkStatsBMCastPktsIn = _LinkStatsBMCastPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 5),
    _LinkStatsBMCastPktsIn_Type()
)
linkStatsBMCastPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsBMCastPktsIn.setStatus("mandatory")
_LinkStatsGiantPkts_Type = Integer32
_LinkStatsGiantPkts_Object = MibTableColumn
linkStatsGiantPkts = _LinkStatsGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 6),
    _LinkStatsGiantPkts_Type()
)
linkStatsGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsGiantPkts.setStatus("mandatory")
_LinkStatsFrameErrs_Type = Integer32
_LinkStatsFrameErrs_Object = MibTableColumn
linkStatsFrameErrs = _LinkStatsFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 7),
    _LinkStatsFrameErrs_Type()
)
linkStatsFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsFrameErrs.setStatus("mandatory")
_LinkStatsFCSErrs_Type = Integer32
_LinkStatsFCSErrs_Object = MibTableColumn
linkStatsFCSErrs = _LinkStatsFCSErrs_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 8),
    _LinkStatsFCSErrs_Type()
)
linkStatsFCSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsFCSErrs.setStatus("mandatory")
_LinkStatsRcvCollisions_Type = Integer32
_LinkStatsRcvCollisions_Object = MibTableColumn
linkStatsRcvCollisions = _LinkStatsRcvCollisions_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 4, 1, 9),
    _LinkStatsRcvCollisions_Type()
)
linkStatsRcvCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatsRcvCollisions.setStatus("mandatory")
_AlLinkControlTable_Object = MibTable
alLinkControlTable = _AlLinkControlTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5)
)
if mibBuilder.loadTexts:
    alLinkControlTable.setStatus("mandatory")
_LinkControlEntry_Object = MibTableRow
linkControlEntry = _LinkControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1)
)
linkControlEntry.setIndexNames(
    (0, "ALANTEC-MIB", "linkControlPort"),
    (0, "ALANTEC-MIB", "linkControlLink"),
)
if mibBuilder.loadTexts:
    linkControlEntry.setStatus("mandatory")
_LinkControlPort_Type = Integer32
_LinkControlPort_Object = MibTableColumn
linkControlPort = _LinkControlPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 1),
    _LinkControlPort_Type()
)
linkControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPort.setStatus("mandatory")
_LinkControlLink_Type = Integer32
_LinkControlLink_Object = MibTableColumn
linkControlLink = _LinkControlLink_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 2),
    _LinkControlLink_Type()
)
linkControlLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlLink.setStatus("mandatory")
_LinkControlEnlState_Type = Integer32
_LinkControlEnlState_Object = MibTableColumn
linkControlEnlState = _LinkControlEnlState_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 3),
    _LinkControlEnlState_Type()
)
linkControlEnlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlEnlState.setStatus("mandatory")
_LinkControlLinkTest_Type = Integer32
_LinkControlLinkTest_Object = MibTableColumn
linkControlLinkTest = _LinkControlLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 4),
    _LinkControlLinkTest_Type()
)
linkControlLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlLinkTest.setStatus("mandatory")
_LinkControlPartition_Type = Integer32
_LinkControlPartition_Object = MibTableColumn
linkControlPartition = _LinkControlPartition_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 5),
    _LinkControlPartition_Type()
)
linkControlPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPartition.setStatus("mandatory")
_LinkControlPolarity_Type = Integer32
_LinkControlPolarity_Object = MibTableColumn
linkControlPolarity = _LinkControlPolarity_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 6),
    _LinkControlPolarity_Type()
)
linkControlPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkControlPolarity.setStatus("mandatory")
_LinkControlEnable_Type = Integer32
_LinkControlEnable_Object = MibTableColumn
linkControlEnable = _LinkControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 5, 1, 7),
    _LinkControlEnable_Type()
)
linkControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkControlEnable.setStatus("mandatory")
_AlPortLinkTable_Object = MibTable
alPortLinkTable = _AlPortLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 6)
)
if mibBuilder.loadTexts:
    alPortLinkTable.setStatus("mandatory")
_PortLinkEntry_Object = MibTableRow
portLinkEntry = _PortLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 6, 1)
)
portLinkEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portLinkPort"),
)
if mibBuilder.loadTexts:
    portLinkEntry.setStatus("mandatory")
_PortLinkPort_Type = Integer32
_PortLinkPort_Object = MibTableColumn
portLinkPort = _PortLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 6, 1, 1),
    _PortLinkPort_Type()
)
portLinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkPort.setStatus("mandatory")


class _PortLinkType_Type(Integer32):
    """Custom type portLinkType based on Integer32"""
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
        *(("aui", 1),
          ("bnc", 2),
          ("bnct", 3),
          ("fiber", 5),
          ("unknown", 6),
          ("utp", 4))
    )


_PortLinkType_Type.__name__ = "Integer32"
_PortLinkType_Object = MibTableColumn
portLinkType = _PortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 6, 1, 2),
    _PortLinkType_Type()
)
portLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkType.setStatus("mandatory")
_AlFiberStatsTable_Object = MibTable
alFiberStatsTable = _AlFiberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 7)
)
if mibBuilder.loadTexts:
    alFiberStatsTable.setStatus("mandatory")
_FiberStatsEntry_Object = MibTableRow
fiberStatsEntry = _FiberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 7, 1)
)
fiberStatsEntry.setIndexNames(
    (0, "ALANTEC-MIB", "fiberStatsPort"),
)
if mibBuilder.loadTexts:
    fiberStatsEntry.setStatus("mandatory")
_FiberStatsPort_Type = Integer32
_FiberStatsPort_Object = MibTableColumn
fiberStatsPort = _FiberStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 7, 1, 1),
    _FiberStatsPort_Type()
)
fiberStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberStatsPort.setStatus("mandatory")
_FiberAuiStatus_Type = Integer32
_FiberAuiStatus_Object = MibTableColumn
fiberAuiStatus = _FiberAuiStatus_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 7, 1, 2),
    _FiberAuiStatus_Type()
)
fiberAuiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberAuiStatus.setStatus("mandatory")


class _FiberSecurityViolation_Type(Integer32):
    """Custom type fiberSecurityViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("detect", 1),
          ("ignore", 2))
    )


_FiberSecurityViolation_Type.__name__ = "Integer32"
_FiberSecurityViolation_Object = MibTableColumn
fiberSecurityViolation = _FiberSecurityViolation_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 7, 1, 3),
    _FiberSecurityViolation_Type()
)
fiberSecurityViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberSecurityViolation.setStatus("mandatory")
_AlPortMonitorClose_Type = Integer32
_AlPortMonitorClose_Object = MibScalar
alPortMonitorClose = _AlPortMonitorClose_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 8),
    _AlPortMonitorClose_Type()
)
alPortMonitorClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPortMonitorClose.setStatus("mandatory")
_AlPortMonitorTable_Object = MibTable
alPortMonitorTable = _AlPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 9)
)
if mibBuilder.loadTexts:
    alPortMonitorTable.setStatus("mandatory")
_PortMonitorEntry_Object = MibTableRow
portMonitorEntry = _PortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 9, 1)
)
portMonitorEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portMonSrcPort"),
    (0, "ALANTEC-MIB", "portMonDstPort"),
)
if mibBuilder.loadTexts:
    portMonitorEntry.setStatus("mandatory")
_PortMonSrcPort_Type = Integer32
_PortMonSrcPort_Object = MibTableColumn
portMonSrcPort = _PortMonSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 9, 1, 1),
    _PortMonSrcPort_Type()
)
portMonSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonSrcPort.setStatus("mandatory")
_PortMonDstPort_Type = Integer32
_PortMonDstPort_Object = MibTableColumn
portMonDstPort = _PortMonDstPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 9, 1, 2),
    _PortMonDstPort_Type()
)
portMonDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonDstPort.setStatus("mandatory")


class _PortMonTrafficType_Type(Integer32):
    """Custom type portMonTrafficType based on Integer32"""
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
        *(("all", 7),
          ("forwarded", 1),
          ("forwardedgenerated", 5),
          ("forwardedincoming", 3),
          ("generated", 4),
          ("incoming", 2),
          ("incominggenerated", 6))
    )


_PortMonTrafficType_Type.__name__ = "Integer32"
_PortMonTrafficType_Object = MibTableColumn
portMonTrafficType = _PortMonTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 9, 1, 3),
    _PortMonTrafficType_Type()
)
portMonTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonTrafficType.setStatus("mandatory")
_AlReboot_Type = Integer32
_AlReboot_Object = MibScalar
alReboot = _AlReboot_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 10),
    _AlReboot_Type()
)
alReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alReboot.setStatus("mandatory")
_AlPortMonitorViewTable_Object = MibTable
alPortMonitorViewTable = _AlPortMonitorViewTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 11)
)
if mibBuilder.loadTexts:
    alPortMonitorViewTable.setStatus("mandatory")
_PortMonitorViewEntry_Object = MibTableRow
portMonitorViewEntry = _PortMonitorViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 11, 1)
)
portMonitorViewEntry.setIndexNames(
    (0, "ALANTEC-MIB", "portMonViewSrcPort"),
    (0, "ALANTEC-MIB", "portMonViewDstPort"),
)
if mibBuilder.loadTexts:
    portMonitorViewEntry.setStatus("mandatory")
_PortMonViewSrcPort_Type = Integer32
_PortMonViewSrcPort_Object = MibTableColumn
portMonViewSrcPort = _PortMonViewSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 11, 1, 1),
    _PortMonViewSrcPort_Type()
)
portMonViewSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonViewSrcPort.setStatus("mandatory")
_PortMonViewDstPort_Type = Integer32
_PortMonViewDstPort_Object = MibTableColumn
portMonViewDstPort = _PortMonViewDstPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 11, 1, 2),
    _PortMonViewDstPort_Type()
)
portMonViewDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMonViewDstPort.setStatus("mandatory")
_PortMonViewMonitorPort_Type = Integer32
_PortMonViewMonitorPort_Object = MibTableColumn
portMonViewMonitorPort = _PortMonViewMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 3, 11, 1, 3),
    _PortMonViewMonitorPort_Type()
)
portMonViewMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonViewMonitorPort.setStatus("mandatory")
_Alrip_ObjectIdentity = ObjectIdentity
alrip = _Alrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 4)
)
_AlRipConfigTable_Object = MibTable
alRipConfigTable = _AlRipConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1)
)
if mibBuilder.loadTexts:
    alRipConfigTable.setStatus("mandatory")
_RipConfigEntry_Object = MibTableRow
ripConfigEntry = _RipConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1)
)
ripConfigEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ripConfigPort"),
)
if mibBuilder.loadTexts:
    ripConfigEntry.setStatus("mandatory")
_RipConfigPort_Type = Integer32
_RipConfigPort_Object = MibTableColumn
ripConfigPort = _RipConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 1),
    _RipConfigPort_Type()
)
ripConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigPort.setStatus("mandatory")
_RipConfigTalk_Type = Integer32
_RipConfigTalk_Object = MibTableColumn
ripConfigTalk = _RipConfigTalk_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 2),
    _RipConfigTalk_Type()
)
ripConfigTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigTalk.setStatus("mandatory")
_RipConfigListen_Type = Integer32
_RipConfigListen_Object = MibTableColumn
ripConfigListen = _RipConfigListen_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 3),
    _RipConfigListen_Type()
)
ripConfigListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigListen.setStatus("mandatory")
_RipConfigPoison_Type = Integer32
_RipConfigPoison_Object = MibTableColumn
ripConfigPoison = _RipConfigPoison_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 4),
    _RipConfigPoison_Type()
)
ripConfigPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigPoison.setStatus("mandatory")
_RipConfigRptStaticRt_Type = Integer32
_RipConfigRptStaticRt_Object = MibTableColumn
ripConfigRptStaticRt = _RipConfigRptStaticRt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 5),
    _RipConfigRptStaticRt_Type()
)
ripConfigRptStaticRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigRptStaticRt.setStatus("mandatory")
_RipConfigRptDefaultRt_Type = Integer32
_RipConfigRptDefaultRt_Object = MibTableColumn
ripConfigRptDefaultRt = _RipConfigRptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 6),
    _RipConfigRptDefaultRt_Type()
)
ripConfigRptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigRptDefaultRt.setStatus("mandatory")
_RipConfigAccptDefaultRt_Type = Integer32
_RipConfigAccptDefaultRt_Object = MibTableColumn
ripConfigAccptDefaultRt = _RipConfigAccptDefaultRt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 1, 1, 7),
    _RipConfigAccptDefaultRt_Type()
)
ripConfigAccptDefaultRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripConfigAccptDefaultRt.setStatus("mandatory")
_AlRipstatsClear_Type = Integer32
_AlRipstatsClear_Object = MibScalar
alRipstatsClear = _AlRipstatsClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 2),
    _AlRipstatsClear_Type()
)
alRipstatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alRipstatsClear.setStatus("mandatory")
_AlRipStatPktsRcvd_Type = Integer32
_AlRipStatPktsRcvd_Object = MibScalar
alRipStatPktsRcvd = _AlRipStatPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 3),
    _AlRipStatPktsRcvd_Type()
)
alRipStatPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsRcvd.setStatus("mandatory")
_AlRipStatPktsXmitted_Type = Integer32
_AlRipStatPktsXmitted_Object = MibScalar
alRipStatPktsXmitted = _AlRipStatPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 4),
    _AlRipStatPktsXmitted_Type()
)
alRipStatPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsXmitted.setStatus("mandatory")
_AlRipStatReqsRcvd_Type = Integer32
_AlRipStatReqsRcvd_Object = MibScalar
alRipStatReqsRcvd = _AlRipStatReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 5),
    _AlRipStatReqsRcvd_Type()
)
alRipStatReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatReqsRcvd.setStatus("mandatory")
_AlRipStatRespRcvd_Type = Integer32
_AlRipStatRespRcvd_Object = MibScalar
alRipStatRespRcvd = _AlRipStatRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 6),
    _AlRipStatRespRcvd_Type()
)
alRipStatRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRespRcvd.setStatus("mandatory")
_AlRipStatReqsXmitted_Type = Integer32
_AlRipStatReqsXmitted_Object = MibScalar
alRipStatReqsXmitted = _AlRipStatReqsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 7),
    _AlRipStatReqsXmitted_Type()
)
alRipStatReqsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatReqsXmitted.setStatus("mandatory")
_AlRipStatRespXmitted_Type = Integer32
_AlRipStatRespXmitted_Object = MibScalar
alRipStatRespXmitted = _AlRipStatRespXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 8),
    _AlRipStatRespXmitted_Type()
)
alRipStatRespXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRespXmitted.setStatus("mandatory")
_AlRipStatRouteTimeOuts_Type = Integer32
_AlRipStatRouteTimeOuts_Object = MibScalar
alRipStatRouteTimeOuts = _AlRipStatRouteTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 9),
    _AlRipStatRouteTimeOuts_Type()
)
alRipStatRouteTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatRouteTimeOuts.setStatus("mandatory")
_AlRipStatShortPkts_Type = Integer32
_AlRipStatShortPkts_Object = MibScalar
alRipStatShortPkts = _AlRipStatShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 10),
    _AlRipStatShortPkts_Type()
)
alRipStatShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatShortPkts.setStatus("mandatory")
_AlRipStatBadVer_Type = Integer32
_AlRipStatBadVer_Object = MibScalar
alRipStatBadVer = _AlRipStatBadVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 11),
    _AlRipStatBadVer_Type()
)
alRipStatBadVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadVer.setStatus("mandatory")
_AlRipStatBadZeroes_Type = Integer32
_AlRipStatBadZeroes_Object = MibScalar
alRipStatBadZeroes = _AlRipStatBadZeroes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 12),
    _AlRipStatBadZeroes_Type()
)
alRipStatBadZeroes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadZeroes.setStatus("mandatory")
_AlRipStatBadSrcPort_Type = Integer32
_AlRipStatBadSrcPort_Object = MibScalar
alRipStatBadSrcPort = _AlRipStatBadSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 13),
    _AlRipStatBadSrcPort_Type()
)
alRipStatBadSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadSrcPort.setStatus("mandatory")
_AlRipStatBadSrcIp_Type = Integer32
_AlRipStatBadSrcIp_Object = MibScalar
alRipStatBadSrcIp = _AlRipStatBadSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 14),
    _AlRipStatBadSrcIp_Type()
)
alRipStatBadSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatBadSrcIp.setStatus("mandatory")
_AlRipStatPktsSelf_Type = Integer32
_AlRipStatPktsSelf_Object = MibScalar
alRipStatPktsSelf = _AlRipStatPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 15),
    _AlRipStatPktsSelf_Type()
)
alRipStatPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsSelf.setStatus("mandatory")
_AlRipStatPktsQueued_Type = Integer32
_AlRipStatPktsQueued_Object = MibScalar
alRipStatPktsQueued = _AlRipStatPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 16),
    _AlRipStatPktsQueued_Type()
)
alRipStatPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatPktsQueued.setStatus("mandatory")
_AlRipStatFreeQueue_Type = Integer32
_AlRipStatFreeQueue_Object = MibScalar
alRipStatFreeQueue = _AlRipStatFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 17),
    _AlRipStatFreeQueue_Type()
)
alRipStatFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipStatFreeQueue.setStatus("mandatory")
_AlRipDynPktsRcvd_Type = Integer32
_AlRipDynPktsRcvd_Object = MibScalar
alRipDynPktsRcvd = _AlRipDynPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 18),
    _AlRipDynPktsRcvd_Type()
)
alRipDynPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsRcvd.setStatus("mandatory")
_AlRipDynPktsXmitted_Type = Integer32
_AlRipDynPktsXmitted_Object = MibScalar
alRipDynPktsXmitted = _AlRipDynPktsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 19),
    _AlRipDynPktsXmitted_Type()
)
alRipDynPktsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsXmitted.setStatus("mandatory")
_AlRipDynReqsRcvd_Type = Integer32
_AlRipDynReqsRcvd_Object = MibScalar
alRipDynReqsRcvd = _AlRipDynReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 20),
    _AlRipDynReqsRcvd_Type()
)
alRipDynReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynReqsRcvd.setStatus("mandatory")
_AlRipDynRespRcvd_Type = Integer32
_AlRipDynRespRcvd_Object = MibScalar
alRipDynRespRcvd = _AlRipDynRespRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 21),
    _AlRipDynRespRcvd_Type()
)
alRipDynRespRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRespRcvd.setStatus("mandatory")
_AlRipDynReqsXmitted_Type = Integer32
_AlRipDynReqsXmitted_Object = MibScalar
alRipDynReqsXmitted = _AlRipDynReqsXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 22),
    _AlRipDynReqsXmitted_Type()
)
alRipDynReqsXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynReqsXmitted.setStatus("mandatory")
_AlRipDynRespXmitted_Type = Integer32
_AlRipDynRespXmitted_Object = MibScalar
alRipDynRespXmitted = _AlRipDynRespXmitted_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 23),
    _AlRipDynRespXmitted_Type()
)
alRipDynRespXmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRespXmitted.setStatus("mandatory")
_AlRipDynRouteTimeOuts_Type = Integer32
_AlRipDynRouteTimeOuts_Object = MibScalar
alRipDynRouteTimeOuts = _AlRipDynRouteTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 24),
    _AlRipDynRouteTimeOuts_Type()
)
alRipDynRouteTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynRouteTimeOuts.setStatus("mandatory")
_AlRipDynShortPkts_Type = Integer32
_AlRipDynShortPkts_Object = MibScalar
alRipDynShortPkts = _AlRipDynShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 25),
    _AlRipDynShortPkts_Type()
)
alRipDynShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynShortPkts.setStatus("mandatory")
_AlRipDynBadVer_Type = Integer32
_AlRipDynBadVer_Object = MibScalar
alRipDynBadVer = _AlRipDynBadVer_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 26),
    _AlRipDynBadVer_Type()
)
alRipDynBadVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadVer.setStatus("mandatory")
_AlRipDynBadZeroes_Type = Integer32
_AlRipDynBadZeroes_Object = MibScalar
alRipDynBadZeroes = _AlRipDynBadZeroes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 27),
    _AlRipDynBadZeroes_Type()
)
alRipDynBadZeroes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadZeroes.setStatus("mandatory")
_AlRipDynBadSrcPort_Type = Integer32
_AlRipDynBadSrcPort_Object = MibScalar
alRipDynBadSrcPort = _AlRipDynBadSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 28),
    _AlRipDynBadSrcPort_Type()
)
alRipDynBadSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadSrcPort.setStatus("mandatory")
_AlRipDynBadSrcIp_Type = Integer32
_AlRipDynBadSrcIp_Object = MibScalar
alRipDynBadSrcIp = _AlRipDynBadSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 29),
    _AlRipDynBadSrcIp_Type()
)
alRipDynBadSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynBadSrcIp.setStatus("mandatory")
_AlRipDynPktsSelf_Type = Integer32
_AlRipDynPktsSelf_Object = MibScalar
alRipDynPktsSelf = _AlRipDynPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 30),
    _AlRipDynPktsSelf_Type()
)
alRipDynPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsSelf.setStatus("mandatory")
_AlRipDynPktsQueued_Type = Integer32
_AlRipDynPktsQueued_Object = MibScalar
alRipDynPktsQueued = _AlRipDynPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 31),
    _AlRipDynPktsQueued_Type()
)
alRipDynPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynPktsQueued.setStatus("mandatory")
_AlRipDynFreeQueue_Type = Integer32
_AlRipDynFreeQueue_Object = MibScalar
alRipDynFreeQueue = _AlRipDynFreeQueue_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 32),
    _AlRipDynFreeQueue_Type()
)
alRipDynFreeQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRipDynFreeQueue.setStatus("mandatory")
_AlRipAccptFilTable_Object = MibTable
alRipAccptFilTable = _AlRipAccptFilTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33)
)
if mibBuilder.loadTexts:
    alRipAccptFilTable.setStatus("mandatory")
_RipAccptFilEntry_Object = MibTableRow
ripAccptFilEntry = _RipAccptFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33, 1)
)
ripAccptFilEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ripAccptFilNumber"),
)
if mibBuilder.loadTexts:
    ripAccptFilEntry.setStatus("mandatory")
_RipAccptFilNumber_Type = Integer32
_RipAccptFilNumber_Object = MibTableColumn
ripAccptFilNumber = _RipAccptFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33, 1, 1),
    _RipAccptFilNumber_Type()
)
ripAccptFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilNumber.setStatus("mandatory")
_RipAccptFilAddr_Type = IpAddress
_RipAccptFilAddr_Object = MibTableColumn
ripAccptFilAddr = _RipAccptFilAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33, 1, 2),
    _RipAccptFilAddr_Type()
)
ripAccptFilAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilAddr.setStatus("mandatory")
_RipAccptFilMask_Type = IpAddress
_RipAccptFilMask_Object = MibTableColumn
ripAccptFilMask = _RipAccptFilMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33, 1, 3),
    _RipAccptFilMask_Type()
)
ripAccptFilMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilMask.setStatus("mandatory")
_RipAccptFilPort_Type = Integer32
_RipAccptFilPort_Object = MibTableColumn
ripAccptFilPort = _RipAccptFilPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 33, 1, 4),
    _RipAccptFilPort_Type()
)
ripAccptFilPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripAccptFilPort.setStatus("mandatory")
_AlRipReportFilTable_Object = MibTable
alRipReportFilTable = _AlRipReportFilTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34)
)
if mibBuilder.loadTexts:
    alRipReportFilTable.setStatus("mandatory")
_RipReportFilEntry_Object = MibTableRow
ripReportFilEntry = _RipReportFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34, 1)
)
ripReportFilEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ripReportFilNumber"),
)
if mibBuilder.loadTexts:
    ripReportFilEntry.setStatus("mandatory")
_RipReportFilNumber_Type = Integer32
_RipReportFilNumber_Object = MibTableColumn
ripReportFilNumber = _RipReportFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34, 1, 1),
    _RipReportFilNumber_Type()
)
ripReportFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilNumber.setStatus("mandatory")
_RipReportFilAddr_Type = IpAddress
_RipReportFilAddr_Object = MibTableColumn
ripReportFilAddr = _RipReportFilAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34, 1, 2),
    _RipReportFilAddr_Type()
)
ripReportFilAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilAddr.setStatus("mandatory")
_RipReportFilMask_Type = IpAddress
_RipReportFilMask_Object = MibTableColumn
ripReportFilMask = _RipReportFilMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34, 1, 3),
    _RipReportFilMask_Type()
)
ripReportFilMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilMask.setStatus("mandatory")
_RipReportFilPort_Type = Integer32
_RipReportFilPort_Object = MibTableColumn
ripReportFilPort = _RipReportFilPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 4, 34, 1, 4),
    _RipReportFilPort_Type()
)
ripReportFilPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripReportFilPort.setStatus("mandatory")
_Altcp_ObjectIdentity = ObjectIdentity
altcp = _Altcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 5)
)
_AlTcpConnIdleTime_Type = Integer32
_AlTcpConnIdleTime_Object = MibScalar
alTcpConnIdleTime = _AlTcpConnIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 1),
    _AlTcpConnIdleTime_Type()
)
alTcpConnIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpConnIdleTime.setStatus("mandatory")
_AlTcpKeepAliveInt_Type = Integer32
_AlTcpKeepAliveInt_Object = MibScalar
alTcpKeepAliveInt = _AlTcpKeepAliveInt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 2),
    _AlTcpKeepAliveInt_Type()
)
alTcpKeepAliveInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpKeepAliveInt.setStatus("mandatory")
_AlTcpDisconnectInt_Type = Integer32
_AlTcpDisconnectInt_Object = MibScalar
alTcpDisconnectInt = _AlTcpDisconnectInt_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 3),
    _AlTcpDisconnectInt_Type()
)
alTcpDisconnectInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpDisconnectInt.setStatus("mandatory")
_AlTcpShortSegRcvd_Type = Integer32
_AlTcpShortSegRcvd_Object = MibScalar
alTcpShortSegRcvd = _AlTcpShortSegRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 4),
    _AlTcpShortSegRcvd_Type()
)
alTcpShortSegRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpShortSegRcvd.setStatus("mandatory")
_AlTcpStatsClear_Type = Integer32
_AlTcpStatsClear_Object = MibScalar
alTcpStatsClear = _AlTcpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 5),
    _AlTcpStatsClear_Type()
)
alTcpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpStatsClear.setStatus("mandatory")
_AlTcpConnTable_Object = MibTable
alTcpConnTable = _AlTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6)
)
if mibBuilder.loadTexts:
    alTcpConnTable.setStatus("mandatory")
_AlTcpConnEntry_Object = MibTableRow
alTcpConnEntry = _AlTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1)
)
alTcpConnEntry.setIndexNames(
    (0, "ALANTEC-MIB", "alTcpConnId"),
)
if mibBuilder.loadTexts:
    alTcpConnEntry.setStatus("mandatory")
_AlTcpConnId_Type = Integer32
_AlTcpConnId_Object = MibTableColumn
alTcpConnId = _AlTcpConnId_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 1),
    _AlTcpConnId_Type()
)
alTcpConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnId.setStatus("mandatory")


class _AlTcpConnState_Type(Integer32):
    """Custom type alTcpConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_AlTcpConnState_Type.__name__ = "Integer32"
_AlTcpConnState_Object = MibTableColumn
alTcpConnState = _AlTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 2),
    _AlTcpConnState_Type()
)
alTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alTcpConnState.setStatus("mandatory")
_AlTcpConnLocalAddress_Type = IpAddress
_AlTcpConnLocalAddress_Object = MibTableColumn
alTcpConnLocalAddress = _AlTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 3),
    _AlTcpConnLocalAddress_Type()
)
alTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnLocalAddress.setStatus("mandatory")
_AlTcpConnLocalPort_Type = Integer32
_AlTcpConnLocalPort_Object = MibTableColumn
alTcpConnLocalPort = _AlTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 4),
    _AlTcpConnLocalPort_Type()
)
alTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnLocalPort.setStatus("mandatory")
_AlTcpConnRemAddress_Type = IpAddress
_AlTcpConnRemAddress_Object = MibTableColumn
alTcpConnRemAddress = _AlTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 5),
    _AlTcpConnRemAddress_Type()
)
alTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnRemAddress.setStatus("mandatory")
_AlTcpConnRemPort_Type = Integer32
_AlTcpConnRemPort_Object = MibTableColumn
alTcpConnRemPort = _AlTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 6, 1, 6),
    _AlTcpConnRemPort_Type()
)
alTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTcpConnRemPort.setStatus("mandatory")
_AlTcpFilTable_Object = MibTable
alTcpFilTable = _AlTcpFilTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7)
)
if mibBuilder.loadTexts:
    alTcpFilTable.setStatus("mandatory")
_TcpFilEntry_Object = MibTableRow
tcpFilEntry = _TcpFilEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1)
)
tcpFilEntry.setIndexNames(
    (0, "ALANTEC-MIB", "tcpFilNumber"),
)
if mibBuilder.loadTexts:
    tcpFilEntry.setStatus("mandatory")
_TcpFilNumber_Type = Integer32
_TcpFilNumber_Object = MibTableColumn
tcpFilNumber = _TcpFilNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1, 1),
    _TcpFilNumber_Type()
)
tcpFilNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilNumber.setStatus("mandatory")
_TcpFilSrcAddr_Type = IpAddress
_TcpFilSrcAddr_Object = MibTableColumn
tcpFilSrcAddr = _TcpFilSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1, 2),
    _TcpFilSrcAddr_Type()
)
tcpFilSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilSrcAddr.setStatus("mandatory")
_TcpFilSrcMask_Type = IpAddress
_TcpFilSrcMask_Object = MibTableColumn
tcpFilSrcMask = _TcpFilSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1, 3),
    _TcpFilSrcMask_Type()
)
tcpFilSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilSrcMask.setStatus("mandatory")
_TcpFilProtocol_Type = Integer32
_TcpFilProtocol_Object = MibTableColumn
tcpFilProtocol = _TcpFilProtocol_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1, 4),
    _TcpFilProtocol_Type()
)
tcpFilProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilProtocol.setStatus("mandatory")
_TcpFilDstPort_Type = Integer32
_TcpFilDstPort_Object = MibTableColumn
tcpFilDstPort = _TcpFilDstPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 5, 7, 1, 5),
    _TcpFilDstPort_Type()
)
tcpFilDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpFilDstPort.setStatus("mandatory")
_Alip_ObjectIdentity = ObjectIdentity
alip = _Alip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 6)
)
_AlArpTableClear_Type = Integer32
_AlArpTableClear_Object = MibScalar
alArpTableClear = _AlArpTableClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 1),
    _AlArpTableClear_Type()
)
alArpTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alArpTableClear.setStatus("mandatory")
_AlArpAge_Type = Integer32
_AlArpAge_Object = MibScalar
alArpAge = _AlArpAge_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 2),
    _AlArpAge_Type()
)
alArpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alArpAge.setStatus("mandatory")
_AlArpStatReqsRcvd_Type = Integer32
_AlArpStatReqsRcvd_Object = MibScalar
alArpStatReqsRcvd = _AlArpStatReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 3),
    _AlArpStatReqsRcvd_Type()
)
alArpStatReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatReqsRcvd.setStatus("mandatory")
_AlArpStatRepliesRcvd_Type = Integer32
_AlArpStatRepliesRcvd_Object = MibScalar
alArpStatRepliesRcvd = _AlArpStatRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 4),
    _AlArpStatRepliesRcvd_Type()
)
alArpStatRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRepliesRcvd.setStatus("mandatory")
_AlArpStatInvalidOpcodes_Type = Integer32
_AlArpStatInvalidOpcodes_Object = MibScalar
alArpStatInvalidOpcodes = _AlArpStatInvalidOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 5),
    _AlArpStatInvalidOpcodes_Type()
)
alArpStatInvalidOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatInvalidOpcodes.setStatus("mandatory")
_AlArpStatRequestsSent_Type = Integer32
_AlArpStatRequestsSent_Object = MibScalar
alArpStatRequestsSent = _AlArpStatRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 6),
    _AlArpStatRequestsSent_Type()
)
alArpStatRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRequestsSent.setStatus("mandatory")
_AlArpStatRepliesSent_Type = Integer32
_AlArpStatRepliesSent_Object = MibScalar
alArpStatRepliesSent = _AlArpStatRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 7),
    _AlArpStatRepliesSent_Type()
)
alArpStatRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpStatRepliesSent.setStatus("mandatory")
_AlArpDynReqsRcvd_Type = Integer32
_AlArpDynReqsRcvd_Object = MibScalar
alArpDynReqsRcvd = _AlArpDynReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 8),
    _AlArpDynReqsRcvd_Type()
)
alArpDynReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynReqsRcvd.setStatus("mandatory")
_AlArpDynRepliesRcvd_Type = Integer32
_AlArpDynRepliesRcvd_Object = MibScalar
alArpDynRepliesRcvd = _AlArpDynRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 9),
    _AlArpDynRepliesRcvd_Type()
)
alArpDynRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRepliesRcvd.setStatus("mandatory")
_AlArpDynInvalidOpcodes_Type = Integer32
_AlArpDynInvalidOpcodes_Object = MibScalar
alArpDynInvalidOpcodes = _AlArpDynInvalidOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 10),
    _AlArpDynInvalidOpcodes_Type()
)
alArpDynInvalidOpcodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynInvalidOpcodes.setStatus("mandatory")
_AlArpDynRequestsSent_Type = Integer32
_AlArpDynRequestsSent_Object = MibScalar
alArpDynRequestsSent = _AlArpDynRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 11),
    _AlArpDynRequestsSent_Type()
)
alArpDynRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRequestsSent.setStatus("mandatory")
_AlArpDynRepliesSent_Type = Integer32
_AlArpDynRepliesSent_Object = MibScalar
alArpDynRepliesSent = _AlArpDynRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 12),
    _AlArpDynRepliesSent_Type()
)
alArpDynRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alArpDynRepliesSent.setStatus("mandatory")
_AlArpProxyTable_Object = MibTable
alArpProxyTable = _AlArpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 13)
)
if mibBuilder.loadTexts:
    alArpProxyTable.setStatus("mandatory")
_ArpProxyEntry_Object = MibTableRow
arpProxyEntry = _ArpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 13, 1)
)
arpProxyEntry.setIndexNames(
    (0, "ALANTEC-MIB", "arpProxyPort"),
)
if mibBuilder.loadTexts:
    arpProxyEntry.setStatus("mandatory")
_ArpProxyPort_Type = Integer32
_ArpProxyPort_Object = MibTableColumn
arpProxyPort = _ArpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 13, 1, 1),
    _ArpProxyPort_Type()
)
arpProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpProxyPort.setStatus("mandatory")
_ArpProxyEnable_Type = Integer32
_ArpProxyEnable_Object = MibTableColumn
arpProxyEnable = _ArpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 13, 1, 2),
    _ArpProxyEnable_Type()
)
arpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpProxyEnable.setStatus("mandatory")
_AlIpTemplateTable_Object = MibTable
alIpTemplateTable = _AlIpTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14)
)
if mibBuilder.loadTexts:
    alIpTemplateTable.setStatus("mandatory")
_IpTemplateEntry_Object = MibTableRow
ipTemplateEntry = _IpTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1)
)
ipTemplateEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipTemplateNumber"),
)
if mibBuilder.loadTexts:
    ipTemplateEntry.setStatus("mandatory")
_IpTemplateNumber_Type = Integer32
_IpTemplateNumber_Object = MibTableColumn
ipTemplateNumber = _IpTemplateNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 1),
    _IpTemplateNumber_Type()
)
ipTemplateNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateNumber.setStatus("mandatory")
_IpTemplateDelete_Type = Integer32
_IpTemplateDelete_Object = MibTableColumn
ipTemplateDelete = _IpTemplateDelete_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 2),
    _IpTemplateDelete_Type()
)
ipTemplateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateDelete.setStatus("mandatory")


class _IpTemplateAction_Type(Integer32):
    """Custom type ipTemplateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("forward", 1))
    )


_IpTemplateAction_Type.__name__ = "Integer32"
_IpTemplateAction_Object = MibTableColumn
ipTemplateAction = _IpTemplateAction_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 3),
    _IpTemplateAction_Type()
)
ipTemplateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateAction.setStatus("mandatory")
_IpTemplateSrcAddr_Type = IpAddress
_IpTemplateSrcAddr_Object = MibTableColumn
ipTemplateSrcAddr = _IpTemplateSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 4),
    _IpTemplateSrcAddr_Type()
)
ipTemplateSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateSrcAddr.setStatus("mandatory")
_IpTemplateSrcMask_Type = IpAddress
_IpTemplateSrcMask_Object = MibTableColumn
ipTemplateSrcMask = _IpTemplateSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 5),
    _IpTemplateSrcMask_Type()
)
ipTemplateSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateSrcMask.setStatus("mandatory")
_IpTemplateDstAddr_Type = IpAddress
_IpTemplateDstAddr_Object = MibTableColumn
ipTemplateDstAddr = _IpTemplateDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 6),
    _IpTemplateDstAddr_Type()
)
ipTemplateDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateDstAddr.setStatus("mandatory")
_IpTemplateDstMask_Type = IpAddress
_IpTemplateDstMask_Object = MibTableColumn
ipTemplateDstMask = _IpTemplateDstMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 7),
    _IpTemplateDstMask_Type()
)
ipTemplateDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateDstMask.setStatus("mandatory")
_IpTemplateProtocol_Type = Integer32
_IpTemplateProtocol_Object = MibTableColumn
ipTemplateProtocol = _IpTemplateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 8),
    _IpTemplateProtocol_Type()
)
ipTemplateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateProtocol.setStatus("mandatory")
_IpTemplateOperator_Type = DisplayString
_IpTemplateOperator_Object = MibTableColumn
ipTemplateOperator = _IpTemplateOperator_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 9),
    _IpTemplateOperator_Type()
)
ipTemplateOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateOperator.setStatus("mandatory")
_IpTemplateDstPort_Type = Integer32
_IpTemplateDstPort_Object = MibTableColumn
ipTemplateDstPort = _IpTemplateDstPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 14, 1, 10),
    _IpTemplateDstPort_Type()
)
ipTemplateDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTemplateDstPort.setStatus("mandatory")
_AlIpRuleTable_Object = MibTable
alIpRuleTable = _AlIpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 15)
)
if mibBuilder.loadTexts:
    alIpRuleTable.setStatus("mandatory")
_IpRuleEntry_Object = MibTableRow
ipRuleEntry = _IpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 15, 1)
)
ipRuleEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipRuleNumber"),
)
if mibBuilder.loadTexts:
    ipRuleEntry.setStatus("mandatory")
_IpRuleNumber_Type = Integer32
_IpRuleNumber_Object = MibTableColumn
ipRuleNumber = _IpRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 15, 1, 1),
    _IpRuleNumber_Type()
)
ipRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleNumber.setStatus("mandatory")
_IpRuleDelete_Type = Integer32
_IpRuleDelete_Object = MibTableColumn
ipRuleDelete = _IpRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 15, 1, 2),
    _IpRuleDelete_Type()
)
ipRuleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleDelete.setStatus("mandatory")
_IpRuleTemplates_Type = DisplayString
_IpRuleTemplates_Object = MibTableColumn
ipRuleTemplates = _IpRuleTemplates_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 15, 1, 3),
    _IpRuleTemplates_Type()
)
ipRuleTemplates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRuleTemplates.setStatus("mandatory")
_IpAcsCtrlTable_Object = MibTable
ipAcsCtrlTable = _IpAcsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16)
)
if mibBuilder.loadTexts:
    ipAcsCtrlTable.setStatus("mandatory")
_IpAcsCtrlEntry_Object = MibTableRow
ipAcsCtrlEntry = _IpAcsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16, 1)
)
ipAcsCtrlEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipAcsCtrlPort"),
)
if mibBuilder.loadTexts:
    ipAcsCtrlEntry.setStatus("mandatory")
_IpAcsCtrlPort_Type = Integer32
_IpAcsCtrlPort_Object = MibTableColumn
ipAcsCtrlPort = _IpAcsCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16, 1, 1),
    _IpAcsCtrlPort_Type()
)
ipAcsCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAcsCtrlPort.setStatus("mandatory")
_IpAcsCtrlDelete_Type = Integer32
_IpAcsCtrlDelete_Object = MibTableColumn
ipAcsCtrlDelete = _IpAcsCtrlDelete_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16, 1, 2),
    _IpAcsCtrlDelete_Type()
)
ipAcsCtrlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAcsCtrlDelete.setStatus("mandatory")
_IpAcsCtrlSrcRule_Type = Integer32
_IpAcsCtrlSrcRule_Object = MibTableColumn
ipAcsCtrlSrcRule = _IpAcsCtrlSrcRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16, 1, 3),
    _IpAcsCtrlSrcRule_Type()
)
ipAcsCtrlSrcRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAcsCtrlSrcRule.setStatus("mandatory")
_IpAcsCtrlDstRule_Type = Integer32
_IpAcsCtrlDstRule_Object = MibTableColumn
ipAcsCtrlDstRule = _IpAcsCtrlDstRule_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 16, 1, 4),
    _IpAcsCtrlDstRule_Type()
)
ipAcsCtrlDstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAcsCtrlDstRule.setStatus("mandatory")
_IpFilStatStatsTable_Object = MibTable
ipFilStatStatsTable = _IpFilStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17)
)
if mibBuilder.loadTexts:
    ipFilStatStatsTable.setStatus("mandatory")
_IpFilStatStatsEntry_Object = MibTableRow
ipFilStatStatsEntry = _IpFilStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1)
)
ipFilStatStatsEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipFilStatStatsTemplate"),
)
if mibBuilder.loadTexts:
    ipFilStatStatsEntry.setStatus("mandatory")
_IpFilStatStatsTemplate_Type = Integer32
_IpFilStatStatsTemplate_Object = MibTableColumn
ipFilStatStatsTemplate = _IpFilStatStatsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1, 1),
    _IpFilStatStatsTemplate_Type()
)
ipFilStatStatsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilStatStatsTemplate.setStatus("mandatory")
_IpFilStatStatsInPkts_Type = Integer32
_IpFilStatStatsInPkts_Object = MibTableColumn
ipFilStatStatsInPkts = _IpFilStatStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1, 2),
    _IpFilStatStatsInPkts_Type()
)
ipFilStatStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilStatStatsInPkts.setStatus("mandatory")
_IpFilStatStatsInBytes_Type = Integer32
_IpFilStatStatsInBytes_Object = MibTableColumn
ipFilStatStatsInBytes = _IpFilStatStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1, 3),
    _IpFilStatStatsInBytes_Type()
)
ipFilStatStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilStatStatsInBytes.setStatus("mandatory")
_IpFilStatStatsOutPkts_Type = Integer32
_IpFilStatStatsOutPkts_Object = MibTableColumn
ipFilStatStatsOutPkts = _IpFilStatStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1, 4),
    _IpFilStatStatsOutPkts_Type()
)
ipFilStatStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilStatStatsOutPkts.setStatus("mandatory")
_IpFilStatStatsOutBytes_Type = Integer32
_IpFilStatStatsOutBytes_Object = MibTableColumn
ipFilStatStatsOutBytes = _IpFilStatStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 17, 1, 5),
    _IpFilStatStatsOutBytes_Type()
)
ipFilStatStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilStatStatsOutBytes.setStatus("mandatory")
_IpFilDynStatsTable_Object = MibTable
ipFilDynStatsTable = _IpFilDynStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18)
)
if mibBuilder.loadTexts:
    ipFilDynStatsTable.setStatus("mandatory")
_IpFilDynStatsEntry_Object = MibTableRow
ipFilDynStatsEntry = _IpFilDynStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1)
)
ipFilDynStatsEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipFilDynStatsTemplate"),
)
if mibBuilder.loadTexts:
    ipFilDynStatsEntry.setStatus("mandatory")
_IpFilDynStatsTemplate_Type = Integer32
_IpFilDynStatsTemplate_Object = MibTableColumn
ipFilDynStatsTemplate = _IpFilDynStatsTemplate_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 1),
    _IpFilDynStatsTemplate_Type()
)
ipFilDynStatsTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilDynStatsTemplate.setStatus("mandatory")
_IpFilDynStatsInPkts_Type = Integer32
_IpFilDynStatsInPkts_Object = MibTableColumn
ipFilDynStatsInPkts = _IpFilDynStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 2),
    _IpFilDynStatsInPkts_Type()
)
ipFilDynStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilDynStatsInPkts.setStatus("mandatory")
_IpFilDynStatsInBytes_Type = Integer32
_IpFilDynStatsInBytes_Object = MibTableColumn
ipFilDynStatsInBytes = _IpFilDynStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 3),
    _IpFilDynStatsInBytes_Type()
)
ipFilDynStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilDynStatsInBytes.setStatus("mandatory")
_IpFilDynStatsOutPkts_Type = Integer32
_IpFilDynStatsOutPkts_Object = MibTableColumn
ipFilDynStatsOutPkts = _IpFilDynStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 4),
    _IpFilDynStatsOutPkts_Type()
)
ipFilDynStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilDynStatsOutPkts.setStatus("mandatory")
_IpFilDynStatsOutBytes_Type = Integer32
_IpFilDynStatsOutBytes_Object = MibTableColumn
ipFilDynStatsOutBytes = _IpFilDynStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 5),
    _IpFilDynStatsOutBytes_Type()
)
ipFilDynStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFilDynStatsOutBytes.setStatus("mandatory")
_IpFilDynStatsClear_Type = Integer32
_IpFilDynStatsClear_Object = MibTableColumn
ipFilDynStatsClear = _IpFilDynStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 18, 1, 6),
    _IpFilDynStatsClear_Type()
)
ipFilDynStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilDynStatsClear.setStatus("mandatory")
_AlIpInterfaceTable_Object = MibTable
alIpInterfaceTable = _AlIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19)
)
if mibBuilder.loadTexts:
    alIpInterfaceTable.setStatus("mandatory")
_AlIpInterfaceEntry_Object = MibTableRow
alIpInterfaceEntry = _AlIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1)
)
alIpInterfaceEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipInterfaceNumber"),
    (0, "ALANTEC-MIB", "ipInterfaceAddress"),
)
if mibBuilder.loadTexts:
    alIpInterfaceEntry.setStatus("mandatory")
_IpInterfaceNumber_Type = Integer32
_IpInterfaceNumber_Object = MibTableColumn
ipInterfaceNumber = _IpInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 1),
    _IpInterfaceNumber_Type()
)
ipInterfaceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNumber.setStatus("mandatory")
_IpInterfaceAddress_Type = IpAddress
_IpInterfaceAddress_Object = MibTableColumn
ipInterfaceAddress = _IpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 2),
    _IpInterfaceAddress_Type()
)
ipInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceAddress.setStatus("mandatory")
_IpInterfaceSubnetMask_Type = IpAddress
_IpInterfaceSubnetMask_Object = MibTableColumn
ipInterfaceSubnetMask = _IpInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 3),
    _IpInterfaceSubnetMask_Type()
)
ipInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceSubnetMask.setStatus("mandatory")
_IpInterfaceMtu_Type = Integer32
_IpInterfaceMtu_Object = MibTableColumn
ipInterfaceMtu = _IpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 4),
    _IpInterfaceMtu_Type()
)
ipInterfaceMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceMtu.setStatus("mandatory")
_IpInterfaceBroadCast_Type = Integer32
_IpInterfaceBroadCast_Object = MibTableColumn
ipInterfaceBroadCast = _IpInterfaceBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 5),
    _IpInterfaceBroadCast_Type()
)
ipInterfaceBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceBroadCast.setStatus("mandatory")
_IpInterfaceState_Type = Integer32
_IpInterfaceState_Object = MibTableColumn
ipInterfaceState = _IpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 6),
    _IpInterfaceState_Type()
)
ipInterfaceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceState.setStatus("mandatory")
_IpInterfaceCost_Type = Integer32
_IpInterfaceCost_Object = MibTableColumn
ipInterfaceCost = _IpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 7),
    _IpInterfaceCost_Type()
)
ipInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceCost.setStatus("mandatory")
_IpInterfacePktsIn_Type = Integer32
_IpInterfacePktsIn_Object = MibTableColumn
ipInterfacePktsIn = _IpInterfacePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 8),
    _IpInterfacePktsIn_Type()
)
ipInterfacePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfacePktsIn.setStatus("mandatory")
_IpInterfaceOctetsIn_Type = Integer32
_IpInterfaceOctetsIn_Object = MibTableColumn
ipInterfaceOctetsIn = _IpInterfaceOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 9),
    _IpInterfaceOctetsIn_Type()
)
ipInterfaceOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceOctetsIn.setStatus("mandatory")
_IpInterfacePktsOut_Type = Integer32
_IpInterfacePktsOut_Object = MibTableColumn
ipInterfacePktsOut = _IpInterfacePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 10),
    _IpInterfacePktsOut_Type()
)
ipInterfacePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfacePktsOut.setStatus("mandatory")
_IpInterfaceOctetsOut_Type = Integer32
_IpInterfaceOctetsOut_Object = MibTableColumn
ipInterfaceOctetsOut = _IpInterfaceOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 19, 1, 11),
    _IpInterfaceOctetsOut_Type()
)
ipInterfaceOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceOctetsOut.setStatus("mandatory")
_AlIpRtCacheTable_Object = MibTable
alIpRtCacheTable = _AlIpRtCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 20)
)
if mibBuilder.loadTexts:
    alIpRtCacheTable.setStatus("mandatory")
_AlIpRtCacheEntry_Object = MibTableRow
alIpRtCacheEntry = _AlIpRtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 20, 1)
)
alIpRtCacheEntry.setIndexNames(
    (0, "ALANTEC-MIB", "ipRtCachePort"),
    (0, "ALANTEC-MIB", "ipRtCacheDstAddress"),
)
if mibBuilder.loadTexts:
    alIpRtCacheEntry.setStatus("mandatory")
_IpRtCachePort_Type = Integer32
_IpRtCachePort_Object = MibTableColumn
ipRtCachePort = _IpRtCachePort_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 20, 1, 1),
    _IpRtCachePort_Type()
)
ipRtCachePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtCachePort.setStatus("mandatory")
_IpRtCacheDstAddress_Type = IpAddress
_IpRtCacheDstAddress_Object = MibTableColumn
ipRtCacheDstAddress = _IpRtCacheDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 20, 1, 2),
    _IpRtCacheDstAddress_Type()
)
ipRtCacheDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtCacheDstAddress.setStatus("mandatory")
_IpRtCacheClear_Type = Integer32
_IpRtCacheClear_Object = MibTableColumn
ipRtCacheClear = _IpRtCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 390, 2, 6, 20, 1, 3),
    _IpRtCacheClear_Type()
)
ipRtCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtCacheClear.setStatus("mandatory")
_Alat_ObjectIdentity = ObjectIdentity
alat = _Alat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 7)
)
_Aldecnet_ObjectIdentity = ObjectIdentity
aldecnet = _Aldecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 8)
)
_Alipx_ObjectIdentity = ObjectIdentity
alipx = _Alipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 9)
)
_Alsnmp_ObjectIdentity = ObjectIdentity
alsnmp = _Alsnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 390, 2, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALANTEC-MIB",
    **{"MacAddress": MacAddress,
       "alantec": alantec,
       "products": products,
       "powerhub": powerhub,
       "powerbits": powerbits,
       "powerhub7000": powerhub7000,
       "alchassis": alchassis,
       "alSlotTable": alSlotTable,
       "alSlotEntry": alSlotEntry,
       "alSlotNumber": alSlotNumber,
       "alSlotCardType": alSlotCardType,
       "alSlotStatus": alSlotStatus,
       "alSlotModel": alSlotModel,
       "alSlotRevision": alSlotRevision,
       "alSlotIssue": alSlotIssue,
       "alSlotDeviation": alSlotDeviation,
       "alSlotSerialNumber": alSlotSerialNumber,
       "alSlotPower5": alSlotPower5,
       "alSlotPower12": alSlotPower12,
       "alSlotPower33": alSlotPower33,
       "alSlotPowerOther": alSlotPowerOther,
       "alVportTable": alVportTable,
       "alVportEntry": alVportEntry,
       "alVportNumber": alVportNumber,
       "alVportSlotNumber": alVportSlotNumber,
       "alVportPortNumber": alVportPortNumber,
       "alVportPortType": alVportPortType,
       "alVportStatus": alVportStatus,
       "alVportControllerType": alVportControllerType,
       "alSlotToVportTable": alSlotToVportTable,
       "alSlotVportEntry": alSlotVportEntry,
       "alSlotVportSlotNumber": alSlotVportSlotNumber,
       "alSlotVportPortNumber": alSlotVportPortNumber,
       "alSlotVportNumber": alSlotVportNumber,
       "alSlotVportPortType": alSlotVportPortType,
       "alSlotVportStatus": alSlotVportStatus,
       "alSlotVportControllerType": alSlotVportControllerType,
       "alPSTable": alPSTable,
       "alPSEntry": alPSEntry,
       "alPSNumber": alPSNumber,
       "alPSStatus": alPSStatus,
       "alCpuSlot": alCpuSlot,
       "common": common,
       "alsystem": alsystem,
       "alChassisType": alChassisType,
       "alMcpuRtVer": alMcpuRtVer,
       "alMcpuPromVer": alMcpuPromVer,
       "alFcpuOneRtVer": alFcpuOneRtVer,
       "alFcpuTwoRtVer": alFcpuTwoRtVer,
       "alFcpuOnePromVer": alFcpuOnePromVer,
       "alFcpuTwoPromVer": alFcpuTwoPromVer,
       "alRcpuOneRtVer": alRcpuOneRtVer,
       "alRcpuTwoRtVer": alRcpuTwoRtVer,
       "alRcpuOnePromVer": alRcpuOnePromVer,
       "alRcpuTwoPromVer": alRcpuTwoPromVer,
       "albridge": albridge,
       "alBridgeTable": alBridgeTable,
       "alBridgeEntry": alBridgeEntry,
       "alBridgeEntryAddress": alBridgeEntryAddress,
       "alBridgeEntryPort": alBridgeEntryPort,
       "alBridgeEntryLink": alBridgeEntryLink,
       "alBridgeEntryRule": alBridgeEntryRule,
       "alBridgeEntryFlags": alBridgeEntryFlags,
       "alBridgeTblClear": alBridgeTblClear,
       "alBrFlushCache": alBrFlushCache,
       "alPortStatsTable": alPortStatsTable,
       "portStatsEntry": portStatsEntry,
       "portStatsPort": portStatsPort,
       "portStatsPktsIn": portStatsPktsIn,
       "portStatsPktsOut": portStatsPktsOut,
       "portStatsOctetsIn": portStatsOctetsIn,
       "portStatsOctetsOut": portStatsOctetsOut,
       "portStatsMultiCastPktsIn": portStatsMultiCastPktsIn,
       "portStatsMulticastPktsOut": portStatsMulticastPktsOut,
       "portStatsTableMisses": portStatsTableMisses,
       "portStatsRcvBuffErrs": portStatsRcvBuffErrs,
       "portStatsXmitBuffErrs": portStatsXmitBuffErrs,
       "portStatsTotalCollisions": portStatsTotalCollisions,
       "portStatsRcvCollisions": portStatsRcvCollisions,
       "portStatsXmitCollisions": portStatsXmitCollisions,
       "portStatsXmitQLen": portStatsXmitQLen,
       "portStatsPeakUtilization": portStatsPeakUtilization,
       "portStatsCurrUtilization": portStatsCurrUtilization,
       "portStatsLossOfCarrier": portStatsLossOfCarrier,
       "portStatsExcessRetries": portStatsExcessRetries,
       "alBridgeStatsClear": alBridgeStatsClear,
       "alBridgePPControl": alBridgePPControl,
       "alPortToPortTable": alPortToPortTable,
       "portToPortEntry": portToPortEntry,
       "alPPSourecPort": alPPSourecPort,
       "alPPDestinationPort": alPPDestinationPort,
       "portToPortPackets": portToPortPackets,
       "portToPortOctets": portToPortOctets,
       "alPortConfigTable": alPortConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigPort": portConfigPort,
       "portConfigSrcRule": portConfigSrcRule,
       "portConfigDstRule": portConfigDstRule,
       "portConfigBlockLearnedEntries": portConfigBlockLearnedEntries,
       "alBridgeIpBridging": alBridgeIpBridging,
       "alBrTemplateTable": alBrTemplateTable,
       "brTemplateEntry": brTemplateEntry,
       "brTemplateNumber": brTemplateNumber,
       "brTemplateOffset": brTemplateOffset,
       "brTemplateMask": brTemplateMask,
       "brTemplateComparator": brTemplateComparator,
       "brTemplateOption": brTemplateOption,
       "alBrRuleTable": alBrRuleTable,
       "brRuleEntry": brRuleEntry,
       "brRuleNumber": brRuleNumber,
       "brRuleStatement": brRuleStatement,
       "alBrRuleToNodeTable": alBrRuleToNodeTable,
       "alBrRuleToNodeEntry": alBrRuleToNodeEntry,
       "brRuleToNodePort": brRuleToNodePort,
       "brRuleToNodeMacAddr": brRuleToNodeMacAddr,
       "brRuleToNodeRule": brRuleToNodeRule,
       "alBrGroupTable": alBrGroupTable,
       "alBrGroupEntry": alBrGroupEntry,
       "brGroupNumber": brGroupNumber,
       "brGroupPortsMask": brGroupPortsMask,
       "brGroupName": brGroupName,
       "alBridgeSTPControl": alBridgeSTPControl,
       "alPortStateTable": alPortStateTable,
       "portStateEntry": portStateEntry,
       "portStatePort": portStatePort,
       "portStateDiag": portStateDiag,
       "portStateMgmt": portStateMgmt,
       "portStateStp": portStateStp,
       "portStatePortName": portStatePortName,
       "almgmt": almgmt,
       "alLinkStatsCollect": alLinkStatsCollect,
       "alLinkStatsClear": alLinkStatsClear,
       "alLinkStatsTable": alLinkStatsTable,
       "linkStatsEntry": linkStatsEntry,
       "linkStatsPort": linkStatsPort,
       "linkStatsLink": linkStatsLink,
       "linkStatsPktsIn": linkStatsPktsIn,
       "linkStatsOctetsIn": linkStatsOctetsIn,
       "linkStatsBMCastPktsIn": linkStatsBMCastPktsIn,
       "linkStatsGiantPkts": linkStatsGiantPkts,
       "linkStatsFrameErrs": linkStatsFrameErrs,
       "linkStatsFCSErrs": linkStatsFCSErrs,
       "linkStatsRcvCollisions": linkStatsRcvCollisions,
       "alLinkControlTable": alLinkControlTable,
       "linkControlEntry": linkControlEntry,
       "linkControlPort": linkControlPort,
       "linkControlLink": linkControlLink,
       "linkControlEnlState": linkControlEnlState,
       "linkControlLinkTest": linkControlLinkTest,
       "linkControlPartition": linkControlPartition,
       "linkControlPolarity": linkControlPolarity,
       "linkControlEnable": linkControlEnable,
       "alPortLinkTable": alPortLinkTable,
       "portLinkEntry": portLinkEntry,
       "portLinkPort": portLinkPort,
       "portLinkType": portLinkType,
       "alFiberStatsTable": alFiberStatsTable,
       "fiberStatsEntry": fiberStatsEntry,
       "fiberStatsPort": fiberStatsPort,
       "fiberAuiStatus": fiberAuiStatus,
       "fiberSecurityViolation": fiberSecurityViolation,
       "alPortMonitorClose": alPortMonitorClose,
       "alPortMonitorTable": alPortMonitorTable,
       "portMonitorEntry": portMonitorEntry,
       "portMonSrcPort": portMonSrcPort,
       "portMonDstPort": portMonDstPort,
       "portMonTrafficType": portMonTrafficType,
       "alReboot": alReboot,
       "alPortMonitorViewTable": alPortMonitorViewTable,
       "portMonitorViewEntry": portMonitorViewEntry,
       "portMonViewSrcPort": portMonViewSrcPort,
       "portMonViewDstPort": portMonViewDstPort,
       "portMonViewMonitorPort": portMonViewMonitorPort,
       "alrip": alrip,
       "alRipConfigTable": alRipConfigTable,
       "ripConfigEntry": ripConfigEntry,
       "ripConfigPort": ripConfigPort,
       "ripConfigTalk": ripConfigTalk,
       "ripConfigListen": ripConfigListen,
       "ripConfigPoison": ripConfigPoison,
       "ripConfigRptStaticRt": ripConfigRptStaticRt,
       "ripConfigRptDefaultRt": ripConfigRptDefaultRt,
       "ripConfigAccptDefaultRt": ripConfigAccptDefaultRt,
       "alRipstatsClear": alRipstatsClear,
       "alRipStatPktsRcvd": alRipStatPktsRcvd,
       "alRipStatPktsXmitted": alRipStatPktsXmitted,
       "alRipStatReqsRcvd": alRipStatReqsRcvd,
       "alRipStatRespRcvd": alRipStatRespRcvd,
       "alRipStatReqsXmitted": alRipStatReqsXmitted,
       "alRipStatRespXmitted": alRipStatRespXmitted,
       "alRipStatRouteTimeOuts": alRipStatRouteTimeOuts,
       "alRipStatShortPkts": alRipStatShortPkts,
       "alRipStatBadVer": alRipStatBadVer,
       "alRipStatBadZeroes": alRipStatBadZeroes,
       "alRipStatBadSrcPort": alRipStatBadSrcPort,
       "alRipStatBadSrcIp": alRipStatBadSrcIp,
       "alRipStatPktsSelf": alRipStatPktsSelf,
       "alRipStatPktsQueued": alRipStatPktsQueued,
       "alRipStatFreeQueue": alRipStatFreeQueue,
       "alRipDynPktsRcvd": alRipDynPktsRcvd,
       "alRipDynPktsXmitted": alRipDynPktsXmitted,
       "alRipDynReqsRcvd": alRipDynReqsRcvd,
       "alRipDynRespRcvd": alRipDynRespRcvd,
       "alRipDynReqsXmitted": alRipDynReqsXmitted,
       "alRipDynRespXmitted": alRipDynRespXmitted,
       "alRipDynRouteTimeOuts": alRipDynRouteTimeOuts,
       "alRipDynShortPkts": alRipDynShortPkts,
       "alRipDynBadVer": alRipDynBadVer,
       "alRipDynBadZeroes": alRipDynBadZeroes,
       "alRipDynBadSrcPort": alRipDynBadSrcPort,
       "alRipDynBadSrcIp": alRipDynBadSrcIp,
       "alRipDynPktsSelf": alRipDynPktsSelf,
       "alRipDynPktsQueued": alRipDynPktsQueued,
       "alRipDynFreeQueue": alRipDynFreeQueue,
       "alRipAccptFilTable": alRipAccptFilTable,
       "ripAccptFilEntry": ripAccptFilEntry,
       "ripAccptFilNumber": ripAccptFilNumber,
       "ripAccptFilAddr": ripAccptFilAddr,
       "ripAccptFilMask": ripAccptFilMask,
       "ripAccptFilPort": ripAccptFilPort,
       "alRipReportFilTable": alRipReportFilTable,
       "ripReportFilEntry": ripReportFilEntry,
       "ripReportFilNumber": ripReportFilNumber,
       "ripReportFilAddr": ripReportFilAddr,
       "ripReportFilMask": ripReportFilMask,
       "ripReportFilPort": ripReportFilPort,
       "altcp": altcp,
       "alTcpConnIdleTime": alTcpConnIdleTime,
       "alTcpKeepAliveInt": alTcpKeepAliveInt,
       "alTcpDisconnectInt": alTcpDisconnectInt,
       "alTcpShortSegRcvd": alTcpShortSegRcvd,
       "alTcpStatsClear": alTcpStatsClear,
       "alTcpConnTable": alTcpConnTable,
       "alTcpConnEntry": alTcpConnEntry,
       "alTcpConnId": alTcpConnId,
       "alTcpConnState": alTcpConnState,
       "alTcpConnLocalAddress": alTcpConnLocalAddress,
       "alTcpConnLocalPort": alTcpConnLocalPort,
       "alTcpConnRemAddress": alTcpConnRemAddress,
       "alTcpConnRemPort": alTcpConnRemPort,
       "alTcpFilTable": alTcpFilTable,
       "tcpFilEntry": tcpFilEntry,
       "tcpFilNumber": tcpFilNumber,
       "tcpFilSrcAddr": tcpFilSrcAddr,
       "tcpFilSrcMask": tcpFilSrcMask,
       "tcpFilProtocol": tcpFilProtocol,
       "tcpFilDstPort": tcpFilDstPort,
       "alip": alip,
       "alArpTableClear": alArpTableClear,
       "alArpAge": alArpAge,
       "alArpStatReqsRcvd": alArpStatReqsRcvd,
       "alArpStatRepliesRcvd": alArpStatRepliesRcvd,
       "alArpStatInvalidOpcodes": alArpStatInvalidOpcodes,
       "alArpStatRequestsSent": alArpStatRequestsSent,
       "alArpStatRepliesSent": alArpStatRepliesSent,
       "alArpDynReqsRcvd": alArpDynReqsRcvd,
       "alArpDynRepliesRcvd": alArpDynRepliesRcvd,
       "alArpDynInvalidOpcodes": alArpDynInvalidOpcodes,
       "alArpDynRequestsSent": alArpDynRequestsSent,
       "alArpDynRepliesSent": alArpDynRepliesSent,
       "alArpProxyTable": alArpProxyTable,
       "arpProxyEntry": arpProxyEntry,
       "arpProxyPort": arpProxyPort,
       "arpProxyEnable": arpProxyEnable,
       "alIpTemplateTable": alIpTemplateTable,
       "ipTemplateEntry": ipTemplateEntry,
       "ipTemplateNumber": ipTemplateNumber,
       "ipTemplateDelete": ipTemplateDelete,
       "ipTemplateAction": ipTemplateAction,
       "ipTemplateSrcAddr": ipTemplateSrcAddr,
       "ipTemplateSrcMask": ipTemplateSrcMask,
       "ipTemplateDstAddr": ipTemplateDstAddr,
       "ipTemplateDstMask": ipTemplateDstMask,
       "ipTemplateProtocol": ipTemplateProtocol,
       "ipTemplateOperator": ipTemplateOperator,
       "ipTemplateDstPort": ipTemplateDstPort,
       "alIpRuleTable": alIpRuleTable,
       "ipRuleEntry": ipRuleEntry,
       "ipRuleNumber": ipRuleNumber,
       "ipRuleDelete": ipRuleDelete,
       "ipRuleTemplates": ipRuleTemplates,
       "ipAcsCtrlTable": ipAcsCtrlTable,
       "ipAcsCtrlEntry": ipAcsCtrlEntry,
       "ipAcsCtrlPort": ipAcsCtrlPort,
       "ipAcsCtrlDelete": ipAcsCtrlDelete,
       "ipAcsCtrlSrcRule": ipAcsCtrlSrcRule,
       "ipAcsCtrlDstRule": ipAcsCtrlDstRule,
       "ipFilStatStatsTable": ipFilStatStatsTable,
       "ipFilStatStatsEntry": ipFilStatStatsEntry,
       "ipFilStatStatsTemplate": ipFilStatStatsTemplate,
       "ipFilStatStatsInPkts": ipFilStatStatsInPkts,
       "ipFilStatStatsInBytes": ipFilStatStatsInBytes,
       "ipFilStatStatsOutPkts": ipFilStatStatsOutPkts,
       "ipFilStatStatsOutBytes": ipFilStatStatsOutBytes,
       "ipFilDynStatsTable": ipFilDynStatsTable,
       "ipFilDynStatsEntry": ipFilDynStatsEntry,
       "ipFilDynStatsTemplate": ipFilDynStatsTemplate,
       "ipFilDynStatsInPkts": ipFilDynStatsInPkts,
       "ipFilDynStatsInBytes": ipFilDynStatsInBytes,
       "ipFilDynStatsOutPkts": ipFilDynStatsOutPkts,
       "ipFilDynStatsOutBytes": ipFilDynStatsOutBytes,
       "ipFilDynStatsClear": ipFilDynStatsClear,
       "alIpInterfaceTable": alIpInterfaceTable,
       "alIpInterfaceEntry": alIpInterfaceEntry,
       "ipInterfaceNumber": ipInterfaceNumber,
       "ipInterfaceAddress": ipInterfaceAddress,
       "ipInterfaceSubnetMask": ipInterfaceSubnetMask,
       "ipInterfaceMtu": ipInterfaceMtu,
       "ipInterfaceBroadCast": ipInterfaceBroadCast,
       "ipInterfaceState": ipInterfaceState,
       "ipInterfaceCost": ipInterfaceCost,
       "ipInterfacePktsIn": ipInterfacePktsIn,
       "ipInterfaceOctetsIn": ipInterfaceOctetsIn,
       "ipInterfacePktsOut": ipInterfacePktsOut,
       "ipInterfaceOctetsOut": ipInterfaceOctetsOut,
       "alIpRtCacheTable": alIpRtCacheTable,
       "alIpRtCacheEntry": alIpRtCacheEntry,
       "ipRtCachePort": ipRtCachePort,
       "ipRtCacheDstAddress": ipRtCacheDstAddress,
       "ipRtCacheClear": ipRtCacheClear,
       "alat": alat,
       "aldecnet": aldecnet,
       "alipx": alipx,
       "alsnmp": alsnmp}
)
