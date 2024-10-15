# SNMP MIB module (CISCO-LECS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LECS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:57 2024
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

(AtmLaneAddress,
 VciInteger,
 VpiInteger) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "VciInteger",
    "VpiInteger")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 MacAddress,
 RowStatus,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLecsMIB_ObjectIdentity = ObjectIdentity
ciscoLecsMIB = _CiscoLecsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38)
)
_CiscoLecsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLecsMIBObjects = _CiscoLecsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1)
)
_Lecs_ObjectIdentity = ObjectIdentity
lecs = _Lecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1)
)
_LecsTable_Object = MibTable
lecsTable = _LecsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lecsTable.setStatus("mandatory")
_LecsEntry_Object = MibTableRow
lecsEntry = _LecsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1)
)
lecsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lecsEntry.setStatus("mandatory")


class _LecsConfigTableName_Type(DisplayString):
    """Custom type lecsConfigTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsConfigTableName_Type.__name__ = "DisplayString"
_LecsConfigTableName_Object = MibTableColumn
lecsConfigTableName = _LecsConfigTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 1),
    _LecsConfigTableName_Type()
)
lecsConfigTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfigTableName.setStatus("mandatory")
_LecsUpTime_Type = TimeStamp
_LecsUpTime_Object = MibTableColumn
lecsUpTime = _LecsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 2),
    _LecsUpTime_Type()
)
lecsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsUpTime.setStatus("mandatory")
_LecsInConfigReqs_Type = Counter32
_LecsInConfigReqs_Object = MibTableColumn
lecsInConfigReqs = _LecsInConfigReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 3),
    _LecsInConfigReqs_Type()
)
lecsInConfigReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsInConfigReqs.setStatus("mandatory")
_LecsInConfigErrors_Type = Counter32
_LecsInConfigErrors_Object = MibTableColumn
lecsInConfigErrors = _LecsInConfigErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 4),
    _LecsInConfigErrors_Type()
)
lecsInConfigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsInConfigErrors.setStatus("mandatory")
_LecsOutConfigFails_Type = Counter32
_LecsOutConfigFails_Object = MibTableColumn
lecsOutConfigFails = _LecsOutConfigFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 5),
    _LecsOutConfigFails_Type()
)
lecsOutConfigFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsOutConfigFails.setStatus("mandatory")
_LecsLastFailCause_Type = Integer32
_LecsLastFailCause_Object = MibTableColumn
lecsLastFailCause = _LecsLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 6),
    _LecsLastFailCause_Type()
)
lecsLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLastFailCause.setStatus("mandatory")
_LecsLastFailLec_Type = AtmLaneAddress
_LecsLastFailLec_Object = MibTableColumn
lecsLastFailLec = _LecsLastFailLec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 7),
    _LecsLastFailLec_Type()
)
lecsLastFailLec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLastFailLec.setStatus("mandatory")


class _LecsOperStatus_Type(Integer32):
    """Custom type lecsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LecsOperStatus_Type.__name__ = "Integer32"
_LecsOperStatus_Object = MibTableColumn
lecsOperStatus = _LecsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 8),
    _LecsOperStatus_Type()
)
lecsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsOperStatus.setStatus("mandatory")


class _LecsAdminStatus_Type(Integer32):
    """Custom type lecsAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LecsAdminStatus_Type.__name__ = "Integer32"
_LecsAdminStatus_Object = MibTableColumn
lecsAdminStatus = _LecsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 9),
    _LecsAdminStatus_Type()
)
lecsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAdminStatus.setStatus("mandatory")
_LecsStatus_Type = RowStatus
_LecsStatus_Object = MibTableColumn
lecsStatus = _LecsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 10),
    _LecsStatus_Type()
)
lecsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsStatus.setStatus("mandatory")
_LecsMasterState_Type = TruthValue
_LecsMasterState_Object = MibTableColumn
lecsMasterState = _LecsMasterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 1, 1, 11),
    _LecsMasterState_Type()
)
lecsMasterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsMasterState.setStatus("mandatory")
_LecsAtmAddrTable_Object = MibTable
lecsAtmAddrTable = _LecsAtmAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lecsAtmAddrTable.setStatus("mandatory")
_LecsAtmAddrEntry_Object = MibTableRow
lecsAtmAddrEntry = _LecsAtmAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1)
)
lecsAtmAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrIndex"),
)
if mibBuilder.loadTexts:
    lecsAtmAddrEntry.setStatus("mandatory")


class _LecsAtmAddrIndex_Type(Integer32):
    """Custom type lecsAtmAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LecsAtmAddrIndex_Type.__name__ = "Integer32"
_LecsAtmAddrIndex_Object = MibTableColumn
lecsAtmAddrIndex = _LecsAtmAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 1),
    _LecsAtmAddrIndex_Type()
)
lecsAtmAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrIndex.setStatus("mandatory")
_LecsAtmAddrSpec_Type = AtmLaneAddress
_LecsAtmAddrSpec_Object = MibTableColumn
lecsAtmAddrSpec = _LecsAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 2),
    _LecsAtmAddrSpec_Type()
)
lecsAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAtmAddrSpec.setStatus("mandatory")


class _LecsAtmAddrMask_Type(OctetString):
    """Custom type lecsAtmAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LecsAtmAddrMask_Type.__name__ = "OctetString"
_LecsAtmAddrMask_Object = MibTableColumn
lecsAtmAddrMask = _LecsAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 3),
    _LecsAtmAddrMask_Type()
)
lecsAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAtmAddrMask.setStatus("mandatory")
_LecsAtmAddrActual_Type = AtmLaneAddress
_LecsAtmAddrActual_Object = MibTableColumn
lecsAtmAddrActual = _LecsAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 4),
    _LecsAtmAddrActual_Type()
)
lecsAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrActual.setStatus("mandatory")


class _LecsAtmAddrState_Type(Integer32):
    """Custom type lecsAtmAddrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("actualValueInvalid", 1),
          ("actualValueValid", 2),
          ("regIlmiAndValid", 6),
          ("regSigAndValid", 4),
          ("regSigIlmiAndValid", 8),
          ("regSigandIlmi", 7),
          ("registeredWithIlmi", 5),
          ("registeredWithSignalling", 3))
    )


_LecsAtmAddrState_Type.__name__ = "Integer32"
_LecsAtmAddrState_Object = MibTableColumn
lecsAtmAddrState = _LecsAtmAddrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 5),
    _LecsAtmAddrState_Type()
)
lecsAtmAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrState.setStatus("mandatory")
_LecsAtmAddrStatus_Type = RowStatus
_LecsAtmAddrStatus_Object = MibTableColumn
lecsAtmAddrStatus = _LecsAtmAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 2, 1, 6),
    _LecsAtmAddrStatus_Type()
)
lecsAtmAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAtmAddrStatus.setStatus("mandatory")
_LecsConfigDirectConnTable_Object = MibTable
lecsConfigDirectConnTable = _LecsConfigDirectConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lecsConfigDirectConnTable.setStatus("mandatory")
_LecsConfigDirectConnEntry_Object = MibTableRow
lecsConfigDirectConnEntry = _LecsConfigDirectConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1)
)
lecsConfigDirectConnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LECS-MIB", "lecsConfigDirectConnVpi"),
    (0, "CISCO-LECS-MIB", "lecsConfigDirectConnVci"),
)
if mibBuilder.loadTexts:
    lecsConfigDirectConnEntry.setStatus("mandatory")
_LecsConfigDirectConnVpi_Type = VpiInteger
_LecsConfigDirectConnVpi_Object = MibTableColumn
lecsConfigDirectConnVpi = _LecsConfigDirectConnVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 1),
    _LecsConfigDirectConnVpi_Type()
)
lecsConfigDirectConnVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVpi.setStatus("mandatory")
_LecsConfigDirectConnVci_Type = VciInteger
_LecsConfigDirectConnVci_Object = MibTableColumn
lecsConfigDirectConnVci = _LecsConfigDirectConnVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 2),
    _LecsConfigDirectConnVci_Type()
)
lecsConfigDirectConnVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVci.setStatus("mandatory")


class _LecsConfigDirectConnVCType_Type(Integer32):
    """Custom type lecsConfigDirectConnVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_LecsConfigDirectConnVCType_Type.__name__ = "Integer32"
_LecsConfigDirectConnVCType_Object = MibTableColumn
lecsConfigDirectConnVCType = _LecsConfigDirectConnVCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 3),
    _LecsConfigDirectConnVCType_Type()
)
lecsConfigDirectConnVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnVCType.setStatus("mandatory")
_LecsConfigDirectConnSrc_Type = AtmLaneAddress
_LecsConfigDirectConnSrc_Object = MibTableColumn
lecsConfigDirectConnSrc = _LecsConfigDirectConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 4),
    _LecsConfigDirectConnSrc_Type()
)
lecsConfigDirectConnSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnSrc.setStatus("mandatory")
_LecsConfigDirectConnDst_Type = AtmLaneAddress
_LecsConfigDirectConnDst_Object = MibTableColumn
lecsConfigDirectConnDst = _LecsConfigDirectConnDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 5),
    _LecsConfigDirectConnDst_Type()
)
lecsConfigDirectConnDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectConnDst.setStatus("mandatory")


class _LecsConfigDirectDstType_Type(Integer32):
    """Custom type lecsConfigDirectDstType based on Integer32"""
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
        *(("laneClient", 1),
          ("laneConfig", 3),
          ("laneServer", 2),
          ("unknown", 4))
    )


_LecsConfigDirectDstType_Type.__name__ = "Integer32"
_LecsConfigDirectDstType_Object = MibTableColumn
lecsConfigDirectDstType = _LecsConfigDirectDstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 1, 3, 1, 6),
    _LecsConfigDirectDstType_Type()
)
lecsConfigDirectDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsConfigDirectDstType.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2)
)
_LecsConfigTblTable_Object = MibTable
lecsConfigTblTable = _LecsConfigTblTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lecsConfigTblTable.setStatus("mandatory")
_LecsConfigTblEntry_Object = MibTableRow
lecsConfigTblEntry = _LecsConfigTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1)
)
lecsConfigTblEntry.setIndexNames(
    (1, "CISCO-LECS-MIB", "lecsConfigTblName"),
)
if mibBuilder.loadTexts:
    lecsConfigTblEntry.setStatus("mandatory")


class _LecsConfigTblName_Type(DisplayString):
    """Custom type lecsConfigTblName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsConfigTblName_Type.__name__ = "DisplayString"
_LecsConfigTblName_Object = MibTableColumn
lecsConfigTblName = _LecsConfigTblName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 1),
    _LecsConfigTblName_Type()
)
lecsConfigTblName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsConfigTblName.setStatus("mandatory")


class _LecsConfigTblDefaultElanName_Type(DisplayString):
    """Custom type lecsConfigTblDefaultElanName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecsConfigTblDefaultElanName_Type.__name__ = "DisplayString"
_LecsConfigTblDefaultElanName_Object = MibTableColumn
lecsConfigTblDefaultElanName = _LecsConfigTblDefaultElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 2),
    _LecsConfigTblDefaultElanName_Type()
)
lecsConfigTblDefaultElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfigTblDefaultElanName.setStatus("mandatory")
_LecsConfigTblStatus_Type = RowStatus
_LecsConfigTblStatus_Object = MibTableColumn
lecsConfigTblStatus = _LecsConfigTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 1, 1, 3),
    _LecsConfigTblStatus_Type()
)
lecsConfigTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfigTblStatus.setStatus("mandatory")
_LecsElanConfigTable_Object = MibTable
lecsElanConfigTable = _LecsElanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lecsElanConfigTable.setStatus("mandatory")
_LecsElanConfigEntry_Object = MibTableRow
lecsElanConfigEntry = _LecsElanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1)
)
lecsElanConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (1, "CISCO-LECS-MIB", "lecsElanConfigName"),
)
if mibBuilder.loadTexts:
    lecsElanConfigEntry.setStatus("mandatory")


class _LecsElanConfigName_Type(DisplayString):
    """Custom type lecsElanConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsElanConfigName_Type.__name__ = "DisplayString"
_LecsElanConfigName_Object = MibTableColumn
lecsElanConfigName = _LecsElanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 1),
    _LecsElanConfigName_Type()
)
lecsElanConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsElanConfigName.setStatus("mandatory")
_LecsElanLesAtmAddr_Type = AtmLaneAddress
_LecsElanLesAtmAddr_Object = MibTableColumn
lecsElanLesAtmAddr = _LecsElanLesAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 2),
    _LecsElanLesAtmAddr_Type()
)
lecsElanLesAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsElanLesAtmAddr.setStatus("mandatory")


class _LecsElanAccess_Type(Integer32):
    """Custom type lecsElanAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_LecsElanAccess_Type.__name__ = "Integer32"
_LecsElanAccess_Object = MibTableColumn
lecsElanAccess = _LecsElanAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 3),
    _LecsElanAccess_Type()
)
lecsElanAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsElanAccess.setStatus("mandatory")
_LecsElanConfigStatus_Type = RowStatus
_LecsElanConfigStatus_Object = MibTableColumn
lecsElanConfigStatus = _LecsElanConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 4),
    _LecsElanConfigStatus_Type()
)
lecsElanConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsElanConfigStatus.setStatus("mandatory")


class _LecsElanSegmentId_Type(Integer32):
    """Custom type lecsElanSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecsElanSegmentId_Type.__name__ = "Integer32"
_LecsElanSegmentId_Object = MibTableColumn
lecsElanSegmentId = _LecsElanSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 2, 1, 5),
    _LecsElanSegmentId_Type()
)
lecsElanSegmentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsElanSegmentId.setStatus("mandatory")
_LecsMacConfigTable_Object = MibTable
lecsMacConfigTable = _LecsMacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lecsMacConfigTable.setStatus("mandatory")
_LecsMacConfigEntry_Object = MibTableRow
lecsMacConfigEntry = _LecsMacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1)
)
lecsMacConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsMacConfigAddress"),
)
if mibBuilder.loadTexts:
    lecsMacConfigEntry.setStatus("mandatory")
_LecsMacConfigAddress_Type = MacAddress
_LecsMacConfigAddress_Object = MibTableColumn
lecsMacConfigAddress = _LecsMacConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 1),
    _LecsMacConfigAddress_Type()
)
lecsMacConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsMacConfigAddress.setStatus("mandatory")


class _LecsMacConfigElanName_Type(DisplayString):
    """Custom type lecsMacConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsMacConfigElanName_Type.__name__ = "DisplayString"
_LecsMacConfigElanName_Object = MibTableColumn
lecsMacConfigElanName = _LecsMacConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 2),
    _LecsMacConfigElanName_Type()
)
lecsMacConfigElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsMacConfigElanName.setStatus("mandatory")
_LecsMacConfigLastUsed_Type = TimeStamp
_LecsMacConfigLastUsed_Object = MibTableColumn
lecsMacConfigLastUsed = _LecsMacConfigLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 3),
    _LecsMacConfigLastUsed_Type()
)
lecsMacConfigLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsMacConfigLastUsed.setStatus("mandatory")
_LecsMacConfigStatus_Type = RowStatus
_LecsMacConfigStatus_Object = MibTableColumn
lecsMacConfigStatus = _LecsMacConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 3, 1, 4),
    _LecsMacConfigStatus_Type()
)
lecsMacConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsMacConfigStatus.setStatus("mandatory")
_LecsAtmAddrConfigTable_Object = MibTable
lecsAtmAddrConfigTable = _LecsAtmAddrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lecsAtmAddrConfigTable.setStatus("mandatory")
_LecsAtmAddrConfigEntry_Object = MibTableRow
lecsAtmAddrConfigEntry = _LecsAtmAddrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1)
)
lecsAtmAddrConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrConfigAddress"),
    (0, "CISCO-LECS-MIB", "lecsAtmAddrConfigMask"),
)
if mibBuilder.loadTexts:
    lecsAtmAddrConfigEntry.setStatus("mandatory")


class _LecsAtmAddrConfigAddress_Type(OctetString):
    """Custom type lecsAtmAddrConfigAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LecsAtmAddrConfigAddress_Type.__name__ = "OctetString"
_LecsAtmAddrConfigAddress_Object = MibTableColumn
lecsAtmAddrConfigAddress = _LecsAtmAddrConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 1),
    _LecsAtmAddrConfigAddress_Type()
)
lecsAtmAddrConfigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigAddress.setStatus("mandatory")


class _LecsAtmAddrConfigMask_Type(OctetString):
    """Custom type lecsAtmAddrConfigMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LecsAtmAddrConfigMask_Type.__name__ = "OctetString"
_LecsAtmAddrConfigMask_Object = MibTableColumn
lecsAtmAddrConfigMask = _LecsAtmAddrConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 2),
    _LecsAtmAddrConfigMask_Type()
)
lecsAtmAddrConfigMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigMask.setStatus("mandatory")


class _LecsAtmAddrConfigElanName_Type(DisplayString):
    """Custom type lecsAtmAddrConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsAtmAddrConfigElanName_Type.__name__ = "DisplayString"
_LecsAtmAddrConfigElanName_Object = MibTableColumn
lecsAtmAddrConfigElanName = _LecsAtmAddrConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 3),
    _LecsAtmAddrConfigElanName_Type()
)
lecsAtmAddrConfigElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigElanName.setStatus("mandatory")
_LecsAtmAddrLastUsed_Type = TimeStamp
_LecsAtmAddrLastUsed_Object = MibTableColumn
lecsAtmAddrLastUsed = _LecsAtmAddrLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 4),
    _LecsAtmAddrLastUsed_Type()
)
lecsAtmAddrLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsAtmAddrLastUsed.setStatus("mandatory")
_LecsAtmAddrConfigStatus_Type = RowStatus
_LecsAtmAddrConfigStatus_Object = MibTableColumn
lecsAtmAddrConfigStatus = _LecsAtmAddrConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 4, 1, 5),
    _LecsAtmAddrConfigStatus_Type()
)
lecsAtmAddrConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsAtmAddrConfigStatus.setStatus("mandatory")
_LecsLesConfigTable_Object = MibTable
lecsLesConfigTable = _LecsLesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5)
)
if mibBuilder.loadTexts:
    lecsLesConfigTable.setStatus("mandatory")
_LecsLesConfigEntry_Object = MibTableRow
lecsLesConfigEntry = _LecsLesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1)
)
lecsLesConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsElanConfigName"),
    (0, "CISCO-LECS-MIB", "lecsLesAtmAddr"),
)
if mibBuilder.loadTexts:
    lecsLesConfigEntry.setStatus("mandatory")


class _LecsLesAtmAddr_Type(OctetString):
    """Custom type lecsLesAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LecsLesAtmAddr_Type.__name__ = "OctetString"
_LecsLesAtmAddr_Object = MibTableColumn
lecsLesAtmAddr = _LecsLesAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 1),
    _LecsLesAtmAddr_Type()
)
lecsLesAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsLesAtmAddr.setStatus("mandatory")


class _LecsLesPriority_Type(Integer32):
    """Custom type lecsLesPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_LecsLesPriority_Type.__name__ = "Integer32"
_LecsLesPriority_Object = MibTableColumn
lecsLesPriority = _LecsLesPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 2),
    _LecsLesPriority_Type()
)
lecsLesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsLesPriority.setStatus("mandatory")


class _LecsLesConnState_Type(Integer32):
    """Custom type lecsLesConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notConnected", 3))
    )


_LecsLesConnState_Type.__name__ = "Integer32"
_LecsLesConnState_Object = MibTableColumn
lecsLesConnState = _LecsLesConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 3),
    _LecsLesConnState_Type()
)
lecsLesConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsLesConnState.setStatus("mandatory")
_LecsLesConfigStatus_Type = RowStatus
_LecsLesConfigStatus_Object = MibTableColumn
lecsLesConfigStatus = _LecsLesConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 5, 1, 4),
    _LecsLesConfigStatus_Type()
)
lecsLesConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsLesConfigStatus.setStatus("mandatory")
_LecsRDConfigTable_Object = MibTable
lecsRDConfigTable = _LecsRDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6)
)
if mibBuilder.loadTexts:
    lecsRDConfigTable.setStatus("mandatory")
_LecsRDConfigEntry_Object = MibTableRow
lecsRDConfigEntry = _LecsRDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1)
)
lecsRDConfigEntry.setIndexNames(
    (0, "CISCO-LECS-MIB", "lecsConfigTblName"),
    (0, "CISCO-LECS-MIB", "lecsRDConfigSegmentId"),
    (0, "CISCO-LECS-MIB", "lecsRDConfigBridgeNum"),
)
if mibBuilder.loadTexts:
    lecsRDConfigEntry.setStatus("mandatory")


class _LecsRDConfigSegmentId_Type(Integer32):
    """Custom type lecsRDConfigSegmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecsRDConfigSegmentId_Type.__name__ = "Integer32"
_LecsRDConfigSegmentId_Object = MibTableColumn
lecsRDConfigSegmentId = _LecsRDConfigSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 1),
    _LecsRDConfigSegmentId_Type()
)
lecsRDConfigSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsRDConfigSegmentId.setStatus("mandatory")


class _LecsRDConfigBridgeNum_Type(Integer32):
    """Custom type lecsRDConfigBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LecsRDConfigBridgeNum_Type.__name__ = "Integer32"
_LecsRDConfigBridgeNum_Object = MibTableColumn
lecsRDConfigBridgeNum = _LecsRDConfigBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 2),
    _LecsRDConfigBridgeNum_Type()
)
lecsRDConfigBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecsRDConfigBridgeNum.setStatus("mandatory")


class _LecsRDConfigElanName_Type(DisplayString):
    """Custom type lecsRDConfigElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LecsRDConfigElanName_Type.__name__ = "DisplayString"
_LecsRDConfigElanName_Object = MibTableColumn
lecsRDConfigElanName = _LecsRDConfigElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 3),
    _LecsRDConfigElanName_Type()
)
lecsRDConfigElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsRDConfigElanName.setStatus("mandatory")
_LecsRDConfigLastUsed_Type = TimeStamp
_LecsRDConfigLastUsed_Object = MibTableColumn
lecsRDConfigLastUsed = _LecsRDConfigLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 4),
    _LecsRDConfigLastUsed_Type()
)
lecsRDConfigLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecsRDConfigLastUsed.setStatus("mandatory")
_LecsRDConfigStatus_Type = RowStatus
_LecsRDConfigStatus_Object = MibTableColumn
lecsRDConfigStatus = _LecsRDConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 1, 2, 6, 1, 5),
    _LecsRDConfigStatus_Type()
)
lecsRDConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsRDConfigStatus.setStatus("mandatory")
_LecsMIBConformance_ObjectIdentity = ObjectIdentity
lecsMIBConformance = _LecsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2)
)
_LecsMIBCompliances_ObjectIdentity = ObjectIdentity
lecsMIBCompliances = _LecsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 1)
)
_LecsMIBCompliance_ObjectIdentity = ObjectIdentity
lecsMIBCompliance = _LecsMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 1, 1)
)
_LecsMIBGroups_ObjectIdentity = ObjectIdentity
lecsMIBGroups = _LecsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2)
)
_LecsMIBGroup_ObjectIdentity = ObjectIdentity
lecsMIBGroup = _LecsMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 1)
)
_LecsTokenRingMIBGroup_ObjectIdentity = ObjectIdentity
lecsTokenRingMIBGroup = _LecsTokenRingMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 2)
)
_LecsRedundancyMIBGroup_ObjectIdentity = ObjectIdentity
lecsRedundancyMIBGroup = _LecsRedundancyMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 38, 2, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LECS-MIB",
    **{"ciscoLecsMIB": ciscoLecsMIB,
       "ciscoLecsMIBObjects": ciscoLecsMIBObjects,
       "lecs": lecs,
       "lecsTable": lecsTable,
       "lecsEntry": lecsEntry,
       "lecsConfigTableName": lecsConfigTableName,
       "lecsUpTime": lecsUpTime,
       "lecsInConfigReqs": lecsInConfigReqs,
       "lecsInConfigErrors": lecsInConfigErrors,
       "lecsOutConfigFails": lecsOutConfigFails,
       "lecsLastFailCause": lecsLastFailCause,
       "lecsLastFailLec": lecsLastFailLec,
       "lecsOperStatus": lecsOperStatus,
       "lecsAdminStatus": lecsAdminStatus,
       "lecsStatus": lecsStatus,
       "lecsMasterState": lecsMasterState,
       "lecsAtmAddrTable": lecsAtmAddrTable,
       "lecsAtmAddrEntry": lecsAtmAddrEntry,
       "lecsAtmAddrIndex": lecsAtmAddrIndex,
       "lecsAtmAddrSpec": lecsAtmAddrSpec,
       "lecsAtmAddrMask": lecsAtmAddrMask,
       "lecsAtmAddrActual": lecsAtmAddrActual,
       "lecsAtmAddrState": lecsAtmAddrState,
       "lecsAtmAddrStatus": lecsAtmAddrStatus,
       "lecsConfigDirectConnTable": lecsConfigDirectConnTable,
       "lecsConfigDirectConnEntry": lecsConfigDirectConnEntry,
       "lecsConfigDirectConnVpi": lecsConfigDirectConnVpi,
       "lecsConfigDirectConnVci": lecsConfigDirectConnVci,
       "lecsConfigDirectConnVCType": lecsConfigDirectConnVCType,
       "lecsConfigDirectConnSrc": lecsConfigDirectConnSrc,
       "lecsConfigDirectConnDst": lecsConfigDirectConnDst,
       "lecsConfigDirectDstType": lecsConfigDirectDstType,
       "config": config,
       "lecsConfigTblTable": lecsConfigTblTable,
       "lecsConfigTblEntry": lecsConfigTblEntry,
       "lecsConfigTblName": lecsConfigTblName,
       "lecsConfigTblDefaultElanName": lecsConfigTblDefaultElanName,
       "lecsConfigTblStatus": lecsConfigTblStatus,
       "lecsElanConfigTable": lecsElanConfigTable,
       "lecsElanConfigEntry": lecsElanConfigEntry,
       "lecsElanConfigName": lecsElanConfigName,
       "lecsElanLesAtmAddr": lecsElanLesAtmAddr,
       "lecsElanAccess": lecsElanAccess,
       "lecsElanConfigStatus": lecsElanConfigStatus,
       "lecsElanSegmentId": lecsElanSegmentId,
       "lecsMacConfigTable": lecsMacConfigTable,
       "lecsMacConfigEntry": lecsMacConfigEntry,
       "lecsMacConfigAddress": lecsMacConfigAddress,
       "lecsMacConfigElanName": lecsMacConfigElanName,
       "lecsMacConfigLastUsed": lecsMacConfigLastUsed,
       "lecsMacConfigStatus": lecsMacConfigStatus,
       "lecsAtmAddrConfigTable": lecsAtmAddrConfigTable,
       "lecsAtmAddrConfigEntry": lecsAtmAddrConfigEntry,
       "lecsAtmAddrConfigAddress": lecsAtmAddrConfigAddress,
       "lecsAtmAddrConfigMask": lecsAtmAddrConfigMask,
       "lecsAtmAddrConfigElanName": lecsAtmAddrConfigElanName,
       "lecsAtmAddrLastUsed": lecsAtmAddrLastUsed,
       "lecsAtmAddrConfigStatus": lecsAtmAddrConfigStatus,
       "lecsLesConfigTable": lecsLesConfigTable,
       "lecsLesConfigEntry": lecsLesConfigEntry,
       "lecsLesAtmAddr": lecsLesAtmAddr,
       "lecsLesPriority": lecsLesPriority,
       "lecsLesConnState": lecsLesConnState,
       "lecsLesConfigStatus": lecsLesConfigStatus,
       "lecsRDConfigTable": lecsRDConfigTable,
       "lecsRDConfigEntry": lecsRDConfigEntry,
       "lecsRDConfigSegmentId": lecsRDConfigSegmentId,
       "lecsRDConfigBridgeNum": lecsRDConfigBridgeNum,
       "lecsRDConfigElanName": lecsRDConfigElanName,
       "lecsRDConfigLastUsed": lecsRDConfigLastUsed,
       "lecsRDConfigStatus": lecsRDConfigStatus,
       "lecsMIBConformance": lecsMIBConformance,
       "lecsMIBCompliances": lecsMIBCompliances,
       "lecsMIBCompliance": lecsMIBCompliance,
       "lecsMIBGroups": lecsMIBGroups,
       "lecsMIBGroup": lecsMIBGroup,
       "lecsTokenRingMIBGroup": lecsTokenRingMIBGroup,
       "lecsRedundancyMIBGroup": lecsRedundancyMIBGroup}
)
