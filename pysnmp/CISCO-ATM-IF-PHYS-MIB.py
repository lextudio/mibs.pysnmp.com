# SNMP MIB module (CISCO-ATM-IF-PHYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-IF-PHYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:53 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtmIfPhysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 45)
)
ciscoAtmIfPhysMIB.setRevisions(
        ("1996-09-19 00:00",
         "1996-08-08 00:00",
         "1995-12-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmIfPhysMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmIfPhysMIBObjects = _CiscoAtmIfPhysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1)
)
_CiscoAtmIfPhysTable_Object = MibTable
ciscoAtmIfPhysTable = _CiscoAtmIfPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysTable.setStatus("current")
_CiscoAtmIfPhysEntry_Object = MibTableRow
ciscoAtmIfPhysEntry = _CiscoAtmIfPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1)
)
ciscoAtmIfPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysEntry.setStatus("current")


class _CiscoAtmIfPhysStatus_Type(Integer32):
    """Custom type ciscoAtmIfPhysStatus based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ais", 5),
          ("idle", 9),
          ("loc", 4),
          ("lof", 3),
          ("lop", 8),
          ("los", 2),
          ("maFERF", 13),
          ("normal", 1),
          ("ocd", 15),
          ("pathAis", 14),
          ("plcpLOF", 11),
          ("plcpYellow", 12),
          ("yellowAlarm", 10),
          ("yellowLine", 6),
          ("yellowPath", 7))
    )


_CiscoAtmIfPhysStatus_Type.__name__ = "Integer32"
_CiscoAtmIfPhysStatus_Object = MibTableColumn
ciscoAtmIfPhysStatus = _CiscoAtmIfPhysStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 1),
    _CiscoAtmIfPhysStatus_Type()
)
ciscoAtmIfPhysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysStatus.setStatus("current")
_CiscoAtmIfPhysSectionParityErrors_Type = Counter32
_CiscoAtmIfPhysSectionParityErrors_Object = MibTableColumn
ciscoAtmIfPhysSectionParityErrors = _CiscoAtmIfPhysSectionParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 2),
    _CiscoAtmIfPhysSectionParityErrors_Type()
)
ciscoAtmIfPhysSectionParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysSectionParityErrors.setStatus("current")
_CiscoAtmIfPhysLineParityErrors_Type = Counter32
_CiscoAtmIfPhysLineParityErrors_Object = MibTableColumn
ciscoAtmIfPhysLineParityErrors = _CiscoAtmIfPhysLineParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 3),
    _CiscoAtmIfPhysLineParityErrors_Type()
)
ciscoAtmIfPhysLineParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLineParityErrors.setStatus("current")
_CiscoAtmIfPhysPathParityErrors_Type = Counter32
_CiscoAtmIfPhysPathParityErrors_Object = MibTableColumn
ciscoAtmIfPhysPathParityErrors = _CiscoAtmIfPhysPathParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 4),
    _CiscoAtmIfPhysPathParityErrors_Type()
)
ciscoAtmIfPhysPathParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysPathParityErrors.setStatus("current")
_CiscoAtmIfPhysLcvErrors_Type = Counter32
_CiscoAtmIfPhysLcvErrors_Object = MibTableColumn
ciscoAtmIfPhysLcvErrors = _CiscoAtmIfPhysLcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 5),
    _CiscoAtmIfPhysLcvErrors_Type()
)
ciscoAtmIfPhysLcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLcvErrors.setStatus("current")
_CiscoAtmIfPhysCBitParityErrors_Type = Counter32
_CiscoAtmIfPhysCBitParityErrors_Object = MibTableColumn
ciscoAtmIfPhysCBitParityErrors = _CiscoAtmIfPhysCBitParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 6),
    _CiscoAtmIfPhysCBitParityErrors_Type()
)
ciscoAtmIfPhysCBitParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysCBitParityErrors.setStatus("current")
_CiscoAtmIfPhysPBitParityErrors_Type = Counter32
_CiscoAtmIfPhysPBitParityErrors_Object = MibTableColumn
ciscoAtmIfPhysPBitParityErrors = _CiscoAtmIfPhysPBitParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 7),
    _CiscoAtmIfPhysPBitParityErrors_Type()
)
ciscoAtmIfPhysPBitParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysPBitParityErrors.setStatus("current")
_CiscoAtmIfPhysPlcpBipViolations_Type = Counter32
_CiscoAtmIfPhysPlcpBipViolations_Object = MibTableColumn
ciscoAtmIfPhysPlcpBipViolations = _CiscoAtmIfPhysPlcpBipViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 8),
    _CiscoAtmIfPhysPlcpBipViolations_Type()
)
ciscoAtmIfPhysPlcpBipViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysPlcpBipViolations.setStatus("current")
_CiscoAtmIfPhysLineFebeErrors_Type = Counter32
_CiscoAtmIfPhysLineFebeErrors_Object = MibTableColumn
ciscoAtmIfPhysLineFebeErrors = _CiscoAtmIfPhysLineFebeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 9),
    _CiscoAtmIfPhysLineFebeErrors_Type()
)
ciscoAtmIfPhysLineFebeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLineFebeErrors.setStatus("current")
_CiscoAtmIfPhysPathFebeErrors_Type = Counter32
_CiscoAtmIfPhysPathFebeErrors_Object = MibTableColumn
ciscoAtmIfPhysPathFebeErrors = _CiscoAtmIfPhysPathFebeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 10),
    _CiscoAtmIfPhysPathFebeErrors_Type()
)
ciscoAtmIfPhysPathFebeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysPathFebeErrors.setStatus("current")


class _CiscoAtmIfPhysCellPayloadScrambling_Type(Integer32):
    """Custom type ciscoAtmIfPhysCellPayloadScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CiscoAtmIfPhysCellPayloadScrambling_Type.__name__ = "Integer32"
_CiscoAtmIfPhysCellPayloadScrambling_Object = MibTableColumn
ciscoAtmIfPhysCellPayloadScrambling = _CiscoAtmIfPhysCellPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 11),
    _CiscoAtmIfPhysCellPayloadScrambling_Type()
)
ciscoAtmIfPhysCellPayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysCellPayloadScrambling.setStatus("current")


class _CiscoAtmIfPhysStsStreamScrambling_Type(Integer32):
    """Custom type ciscoAtmIfPhysStsStreamScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CiscoAtmIfPhysStsStreamScrambling_Type.__name__ = "Integer32"
_CiscoAtmIfPhysStsStreamScrambling_Object = MibTableColumn
ciscoAtmIfPhysStsStreamScrambling = _CiscoAtmIfPhysStsStreamScrambling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 12),
    _CiscoAtmIfPhysStsStreamScrambling_Type()
)
ciscoAtmIfPhysStsStreamScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysStsStreamScrambling.setStatus("current")


class _CiscoAtmIfPhysFramingMode_Type(Integer32):
    """Custom type ciscoAtmIfPhysFramingMode based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("ds1esfadm", 11),
          ("ds1esfplcp", 13),
          ("ds1sfadm", 10),
          ("ds1sfplcp", 12),
          ("ds3cbitadm", 5),
          ("ds3cbitplcp", 6),
          ("ds3m23adm", 3),
          ("ds3m23plcp", 4),
          ("e1adm", 14),
          ("e1crcadm", 16),
          ("e1crcplcp", 17),
          ("e1plcp", 15),
          ("e3g751adm", 8),
          ("e3g751plcp", 9),
          ("e3g832adm", 7),
          ("sdh", 2),
          ("sonet", 1))
    )


_CiscoAtmIfPhysFramingMode_Type.__name__ = "Integer32"
_CiscoAtmIfPhysFramingMode_Object = MibTableColumn
ciscoAtmIfPhysFramingMode = _CiscoAtmIfPhysFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 13),
    _CiscoAtmIfPhysFramingMode_Type()
)
ciscoAtmIfPhysFramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysFramingMode.setStatus("current")


class _CiscoAtmIfPhysLoopbackConfig_Type(Integer32):
    """Custom type ciscoAtmIfPhysLoopbackConfig based on Integer32"""
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
        *(("diagnosticLoop", 2),
          ("lineLoop", 3),
          ("noLoop", 1),
          ("otherLoop", 4))
    )


_CiscoAtmIfPhysLoopbackConfig_Type.__name__ = "Integer32"
_CiscoAtmIfPhysLoopbackConfig_Object = MibTableColumn
ciscoAtmIfPhysLoopbackConfig = _CiscoAtmIfPhysLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 14),
    _CiscoAtmIfPhysLoopbackConfig_Type()
)
ciscoAtmIfPhysLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLoopbackConfig.setStatus("current")


class _CiscoAtmIfPhysLineBuildOut_Type(Integer32):
    """Custom type ciscoAtmIfPhysLineBuildOut based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ds1Cables0To110", 4),
          ("ds1Cables110To220", 5),
          ("ds1Cables220To330", 6),
          ("ds1Cables330To440", 7),
          ("ds1Cables440To550", 8),
          ("ds1Cables550To660", 9),
          ("ds1CablesOver600", 10),
          ("ds3CablesOver225", 3),
          ("ds3CablesUnder225", 2),
          ("e1AllCables", 11),
          ("e3AllCables", 1))
    )


_CiscoAtmIfPhysLineBuildOut_Type.__name__ = "Integer32"
_CiscoAtmIfPhysLineBuildOut_Object = MibTableColumn
ciscoAtmIfPhysLineBuildOut = _CiscoAtmIfPhysLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 15),
    _CiscoAtmIfPhysLineBuildOut_Type()
)
ciscoAtmIfPhysLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLineBuildOut.setStatus("current")


class _CiscoAtmIfPhysTransmitClockSource_Type(Integer32):
    """Custom type ciscoAtmIfPhysTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeRunning", 2),
          ("loopTiming", 1),
          ("networkDerived", 3))
    )


_CiscoAtmIfPhysTransmitClockSource_Type.__name__ = "Integer32"
_CiscoAtmIfPhysTransmitClockSource_Object = MibTableColumn
ciscoAtmIfPhysTransmitClockSource = _CiscoAtmIfPhysTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 16),
    _CiscoAtmIfPhysTransmitClockSource_Type()
)
ciscoAtmIfPhysTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysTransmitClockSource.setStatus("current")


class _CiscoAtmIfPhysClockSourcePriority_Type(Integer32):
    """Custom type ciscoAtmIfPhysClockSourcePriority based on Integer32"""
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
        *(("notConfigured", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5))
    )


_CiscoAtmIfPhysClockSourcePriority_Type.__name__ = "Integer32"
_CiscoAtmIfPhysClockSourcePriority_Object = MibTableColumn
ciscoAtmIfPhysClockSourcePriority = _CiscoAtmIfPhysClockSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 17),
    _CiscoAtmIfPhysClockSourcePriority_Type()
)
ciscoAtmIfPhysClockSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysClockSourcePriority.setStatus("current")


class _CiscoAtmIfPhysClockSourceStatus_Type(Integer32):
    """Custom type ciscoAtmIfPhysClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelected", 1),
          ("selected", 2))
    )


_CiscoAtmIfPhysClockSourceStatus_Type.__name__ = "Integer32"
_CiscoAtmIfPhysClockSourceStatus_Object = MibTableColumn
ciscoAtmIfPhysClockSourceStatus = _CiscoAtmIfPhysClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 18),
    _CiscoAtmIfPhysClockSourceStatus_Type()
)
ciscoAtmIfPhysClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysClockSourceStatus.setStatus("current")
_CiscoAtmIfPhysDS1BitErrors_Type = Counter32
_CiscoAtmIfPhysDS1BitErrors_Object = MibTableColumn
ciscoAtmIfPhysDS1BitErrors = _CiscoAtmIfPhysDS1BitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 19),
    _CiscoAtmIfPhysDS1BitErrors_Type()
)
ciscoAtmIfPhysDS1BitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysDS1BitErrors.setStatus("current")
_CiscoAtmIfPhysE1CrcErrors_Type = Counter32
_CiscoAtmIfPhysE1CrcErrors_Object = MibTableColumn
ciscoAtmIfPhysE1CrcErrors = _CiscoAtmIfPhysE1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 20),
    _CiscoAtmIfPhysE1CrcErrors_Type()
)
ciscoAtmIfPhysE1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysE1CrcErrors.setStatus("current")


class _CiscoAtmIfPhysLineCode_Type(Integer32):
    """Custom type ciscoAtmIfPhysLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_CiscoAtmIfPhysLineCode_Type.__name__ = "Integer32"
_CiscoAtmIfPhysLineCode_Object = MibTableColumn
ciscoAtmIfPhysLineCode = _CiscoAtmIfPhysLineCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 1, 1, 1, 21),
    _CiscoAtmIfPhysLineCode_Type()
)
ciscoAtmIfPhysLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfPhysLineCode.setStatus("current")
_CiscoAtmIfPhysMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmIfPhysMIBConformance = _CiscoAtmIfPhysMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3)
)
_CiscoAtmIfPhysMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmIfPhysMIBCompliances = _CiscoAtmIfPhysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 1)
)
_CiscoAtmIfPhysMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmIfPhysMIBGroups = _CiscoAtmIfPhysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2)
)

# Managed Objects groups

ciscoAtmIfPhysMIBCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 1)
)
ciscoAtmIfPhysMIBCommonGroup.setObjects(
    ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysStatus")
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBCommonGroup.setStatus("current")

ciscoAtmIfPhysMIBSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 2)
)
ciscoAtmIfPhysMIBSonetGroup.setObjects(
      *(("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysSectionParityErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLineParityErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysPathParityErrors"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBSonetGroup.setStatus("current")

ciscoAtmIfPhysMIBDs3E3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 3)
)
ciscoAtmIfPhysMIBDs3E3Group.setObjects(
      *(("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLcvErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysCBitParityErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysPBitParityErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysPlcpBipViolations"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBDs3E3Group.setStatus("current")

ciscoAtmIfPhysMIBCommonGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 4)
)
ciscoAtmIfPhysMIBCommonGroup2.setObjects(
      *(("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysCellPayloadScrambling"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysFramingMode"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLoopbackConfig"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysTransmitClockSource"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysClockSourcePriority"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysClockSourceStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBCommonGroup2.setStatus("current")

ciscoAtmIfPhysMIBSonetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 5)
)
ciscoAtmIfPhysMIBSonetGroup2.setObjects(
      *(("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLineFebeErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysPathFebeErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysStsStreamScrambling"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBSonetGroup2.setStatus("current")

ciscoAtmIfPhysMIBDs3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 6)
)
ciscoAtmIfPhysMIBDs3Group.setObjects(
    ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLineBuildOut")
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBDs3Group.setStatus("current")

ciscoAtmIfPhysMIBDs1E1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 7)
)
ciscoAtmIfPhysMIBDs1E1Group.setObjects(
      *(("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLcvErrors"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysPlcpBipViolations"),
        ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysLineCode"))
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBDs1E1Group.setStatus("current")

ciscoAtmIfPhysMIBDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 8)
)
ciscoAtmIfPhysMIBDs1Group.setObjects(
    ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysDS1BitErrors")
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBDs1Group.setStatus("current")

ciscoAtmIfPhysMIBE1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 2, 9)
)
ciscoAtmIfPhysMIBE1Group.setObjects(
    ("CISCO-ATM-IF-PHYS-MIB", "ciscoAtmIfPhysE1CrcErrors")
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBE1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmIfPhysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBCompliance.setStatus(
        "obsolete"
    )

ciscoAtmIfPhysMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBCompliance2.setStatus(
        "obsolete"
    )

ciscoAtmIfPhysMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 45, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAtmIfPhysMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-IF-PHYS-MIB",
    **{"ciscoAtmIfPhysMIB": ciscoAtmIfPhysMIB,
       "ciscoAtmIfPhysMIBObjects": ciscoAtmIfPhysMIBObjects,
       "ciscoAtmIfPhysTable": ciscoAtmIfPhysTable,
       "ciscoAtmIfPhysEntry": ciscoAtmIfPhysEntry,
       "ciscoAtmIfPhysStatus": ciscoAtmIfPhysStatus,
       "ciscoAtmIfPhysSectionParityErrors": ciscoAtmIfPhysSectionParityErrors,
       "ciscoAtmIfPhysLineParityErrors": ciscoAtmIfPhysLineParityErrors,
       "ciscoAtmIfPhysPathParityErrors": ciscoAtmIfPhysPathParityErrors,
       "ciscoAtmIfPhysLcvErrors": ciscoAtmIfPhysLcvErrors,
       "ciscoAtmIfPhysCBitParityErrors": ciscoAtmIfPhysCBitParityErrors,
       "ciscoAtmIfPhysPBitParityErrors": ciscoAtmIfPhysPBitParityErrors,
       "ciscoAtmIfPhysPlcpBipViolations": ciscoAtmIfPhysPlcpBipViolations,
       "ciscoAtmIfPhysLineFebeErrors": ciscoAtmIfPhysLineFebeErrors,
       "ciscoAtmIfPhysPathFebeErrors": ciscoAtmIfPhysPathFebeErrors,
       "ciscoAtmIfPhysCellPayloadScrambling": ciscoAtmIfPhysCellPayloadScrambling,
       "ciscoAtmIfPhysStsStreamScrambling": ciscoAtmIfPhysStsStreamScrambling,
       "ciscoAtmIfPhysFramingMode": ciscoAtmIfPhysFramingMode,
       "ciscoAtmIfPhysLoopbackConfig": ciscoAtmIfPhysLoopbackConfig,
       "ciscoAtmIfPhysLineBuildOut": ciscoAtmIfPhysLineBuildOut,
       "ciscoAtmIfPhysTransmitClockSource": ciscoAtmIfPhysTransmitClockSource,
       "ciscoAtmIfPhysClockSourcePriority": ciscoAtmIfPhysClockSourcePriority,
       "ciscoAtmIfPhysClockSourceStatus": ciscoAtmIfPhysClockSourceStatus,
       "ciscoAtmIfPhysDS1BitErrors": ciscoAtmIfPhysDS1BitErrors,
       "ciscoAtmIfPhysE1CrcErrors": ciscoAtmIfPhysE1CrcErrors,
       "ciscoAtmIfPhysLineCode": ciscoAtmIfPhysLineCode,
       "ciscoAtmIfPhysMIBConformance": ciscoAtmIfPhysMIBConformance,
       "ciscoAtmIfPhysMIBCompliances": ciscoAtmIfPhysMIBCompliances,
       "ciscoAtmIfPhysMIBCompliance": ciscoAtmIfPhysMIBCompliance,
       "ciscoAtmIfPhysMIBCompliance2": ciscoAtmIfPhysMIBCompliance2,
       "ciscoAtmIfPhysMIBCompliance3": ciscoAtmIfPhysMIBCompliance3,
       "ciscoAtmIfPhysMIBGroups": ciscoAtmIfPhysMIBGroups,
       "ciscoAtmIfPhysMIBCommonGroup": ciscoAtmIfPhysMIBCommonGroup,
       "ciscoAtmIfPhysMIBSonetGroup": ciscoAtmIfPhysMIBSonetGroup,
       "ciscoAtmIfPhysMIBDs3E3Group": ciscoAtmIfPhysMIBDs3E3Group,
       "ciscoAtmIfPhysMIBCommonGroup2": ciscoAtmIfPhysMIBCommonGroup2,
       "ciscoAtmIfPhysMIBSonetGroup2": ciscoAtmIfPhysMIBSonetGroup2,
       "ciscoAtmIfPhysMIBDs3Group": ciscoAtmIfPhysMIBDs3Group,
       "ciscoAtmIfPhysMIBDs1E1Group": ciscoAtmIfPhysMIBDs1E1Group,
       "ciscoAtmIfPhysMIBDs1Group": ciscoAtmIfPhysMIBDs1Group,
       "ciscoAtmIfPhysMIBE1Group": ciscoAtmIfPhysMIBE1Group}
)
