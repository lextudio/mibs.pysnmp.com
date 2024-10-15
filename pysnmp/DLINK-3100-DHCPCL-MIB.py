# SNMP MIB module (DLINK-3100-DHCPCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-DHCPCL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:53 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDhcpCl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76)
)
rlDhcpCl.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpClActionTable_Object = MibTable
rlDhcpClActionTable = _RlDhcpClActionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 3)
)
if mibBuilder.loadTexts:
    rlDhcpClActionTable.setStatus("current")
_RlDhcpClActionEntry_Object = MibTableRow
rlDhcpClActionEntry = _RlDhcpClActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 3, 1)
)
rlDhcpClActionEntry.setIndexNames(
    (0, "DLINK-3100-DHCPCL-MIB", "rlDhcpClActionIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClActionEntry.setStatus("current")
_RlDhcpClActionIfIndex_Type = InterfaceIndex
_RlDhcpClActionIfIndex_Object = MibTableColumn
rlDhcpClActionIfIndex = _RlDhcpClActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 3, 1, 1),
    _RlDhcpClActionIfIndex_Type()
)
rlDhcpClActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClActionIfIndex.setStatus("current")
_RlDhcpClActionStatus_Type = RowStatus
_RlDhcpClActionStatus_Object = MibTableColumn
rlDhcpClActionStatus = _RlDhcpClActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 3, 1, 2),
    _RlDhcpClActionStatus_Type()
)
rlDhcpClActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionStatus.setStatus("current")


class _RlDhcpClActionHostName_Type(SnmpAdminString):
    """Custom type rlDhcpClActionHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlDhcpClActionHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpClActionHostName_Object = MibTableColumn
rlDhcpClActionHostName = _RlDhcpClActionHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 3, 1, 3),
    _RlDhcpClActionHostName_Type()
)
rlDhcpClActionHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionHostName.setStatus("current")
_RlDhcpApprovalEnabled_Type = TruthValue
_RlDhcpApprovalEnabled_Object = MibScalar
rlDhcpApprovalEnabled = _RlDhcpApprovalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 4),
    _RlDhcpApprovalEnabled_Type()
)
rlDhcpApprovalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalEnabled.setStatus("current")
_RlDhcpApprovalWaitingTable_Object = MibTable
rlDhcpApprovalWaitingTable = _RlDhcpApprovalWaitingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingTable.setStatus("current")
_RlDhcpApprovalWaitingEntry_Object = MibTableRow
rlDhcpApprovalWaitingEntry = _RlDhcpApprovalWaitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5, 1)
)
rlDhcpApprovalWaitingEntry.setIndexNames(
    (0, "DLINK-3100-DHCPCL-MIB", "rlDhcpApprovalWaitingIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingEntry.setStatus("current")
_RlDhcpApprovalWaitingIfIndex_Type = InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object = MibTableColumn
rlDhcpApprovalWaitingIfIndex = _RlDhcpApprovalWaitingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5, 1, 1),
    _RlDhcpApprovalWaitingIfIndex_Type()
)
rlDhcpApprovalWaitingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingIfIndex.setStatus("current")
_RlDhcpApprovalWaitingAddress_Type = IpAddress
_RlDhcpApprovalWaitingAddress_Object = MibTableColumn
rlDhcpApprovalWaitingAddress = _RlDhcpApprovalWaitingAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5, 1, 2),
    _RlDhcpApprovalWaitingAddress_Type()
)
rlDhcpApprovalWaitingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingAddress.setStatus("current")
_RlDhcpApprovalWaitingMask_Type = IpAddress
_RlDhcpApprovalWaitingMask_Object = MibTableColumn
rlDhcpApprovalWaitingMask = _RlDhcpApprovalWaitingMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5, 1, 3),
    _RlDhcpApprovalWaitingMask_Type()
)
rlDhcpApprovalWaitingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingMask.setStatus("current")
_RlDhcpApprovalWaitingGateway_Type = IpAddress
_RlDhcpApprovalWaitingGateway_Object = MibTableColumn
rlDhcpApprovalWaitingGateway = _RlDhcpApprovalWaitingGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 5, 1, 4),
    _RlDhcpApprovalWaitingGateway_Type()
)
rlDhcpApprovalWaitingGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingGateway.setStatus("current")
_RlDhcpApprovalActionTable_Object = MibTable
rlDhcpApprovalActionTable = _RlDhcpApprovalActionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionTable.setStatus("current")
_RlDhcpApprovalActionEntry_Object = MibTableRow
rlDhcpApprovalActionEntry = _RlDhcpApprovalActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6, 1)
)
rlDhcpApprovalActionEntry.setIndexNames(
    (0, "DLINK-3100-DHCPCL-MIB", "rlDhcpApprovalActionIfIndex"),
    (0, "DLINK-3100-DHCPCL-MIB", "rlDhcpApprovalActionAddress"),
    (0, "DLINK-3100-DHCPCL-MIB", "rlDhcpApprovalActionMask"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionEntry.setStatus("current")
_RlDhcpApprovalActionIfIndex_Type = InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object = MibTableColumn
rlDhcpApprovalActionIfIndex = _RlDhcpApprovalActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6, 1, 1),
    _RlDhcpApprovalActionIfIndex_Type()
)
rlDhcpApprovalActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionIfIndex.setStatus("current")
_RlDhcpApprovalActionAddress_Type = IpAddress
_RlDhcpApprovalActionAddress_Object = MibTableColumn
rlDhcpApprovalActionAddress = _RlDhcpApprovalActionAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6, 1, 2),
    _RlDhcpApprovalActionAddress_Type()
)
rlDhcpApprovalActionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionAddress.setStatus("current")
_RlDhcpApprovalActionMask_Type = IpAddress
_RlDhcpApprovalActionMask_Object = MibTableColumn
rlDhcpApprovalActionMask = _RlDhcpApprovalActionMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6, 1, 3),
    _RlDhcpApprovalActionMask_Type()
)
rlDhcpApprovalActionMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionMask.setStatus("current")
_RlDhcpApprovalActionApprove_Type = TruthValue
_RlDhcpApprovalActionApprove_Object = MibTableColumn
rlDhcpApprovalActionApprove = _RlDhcpApprovalActionApprove_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 6, 1, 4),
    _RlDhcpApprovalActionApprove_Type()
)
rlDhcpApprovalActionApprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionApprove.setStatus("current")
_RlDhcpClCommandTable_Object = MibTable
rlDhcpClCommandTable = _RlDhcpClCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 7)
)
if mibBuilder.loadTexts:
    rlDhcpClCommandTable.setStatus("current")
_RlDhcpClCommandEntry_Object = MibTableRow
rlDhcpClCommandEntry = _RlDhcpClCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 7, 1)
)
rlDhcpClCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClCommandEntry.setStatus("current")


class _RlDhcpClCommandAction_Type(Integer32):
    """Custom type rlDhcpClCommandAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1),
          ("renewForceAutoconfig", 2))
    )


_RlDhcpClCommandAction_Type.__name__ = "Integer32"
_RlDhcpClCommandAction_Object = MibTableColumn
rlDhcpClCommandAction = _RlDhcpClCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 7, 1, 2),
    _RlDhcpClCommandAction_Type()
)
rlDhcpClCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClCommandAction.setStatus("current")
_RlDhcpClConfigurationFileName_Type = DisplayString
_RlDhcpClConfigurationFileName_Object = MibScalar
rlDhcpClConfigurationFileName = _RlDhcpClConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 8),
    _RlDhcpClConfigurationFileName_Type()
)
rlDhcpClConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClConfigurationFileName.setStatus("current")


class _RlDhcpClOption67Enable_Type(Integer32):
    """Custom type rlDhcpClOption67Enable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlDhcpClOption67Enable_Type.__name__ = "Integer32"
_RlDhcpClOption67Enable_Object = MibScalar
rlDhcpClOption67Enable = _RlDhcpClOption67Enable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 76, 9),
    _RlDhcpClOption67Enable_Type()
)
rlDhcpClOption67Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClOption67Enable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-DHCPCL-MIB",
    **{"rlDhcpCl": rlDhcpCl,
       "rlDhcpClActionTable": rlDhcpClActionTable,
       "rlDhcpClActionEntry": rlDhcpClActionEntry,
       "rlDhcpClActionIfIndex": rlDhcpClActionIfIndex,
       "rlDhcpClActionStatus": rlDhcpClActionStatus,
       "rlDhcpClActionHostName": rlDhcpClActionHostName,
       "rlDhcpApprovalEnabled": rlDhcpApprovalEnabled,
       "rlDhcpApprovalWaitingTable": rlDhcpApprovalWaitingTable,
       "rlDhcpApprovalWaitingEntry": rlDhcpApprovalWaitingEntry,
       "rlDhcpApprovalWaitingIfIndex": rlDhcpApprovalWaitingIfIndex,
       "rlDhcpApprovalWaitingAddress": rlDhcpApprovalWaitingAddress,
       "rlDhcpApprovalWaitingMask": rlDhcpApprovalWaitingMask,
       "rlDhcpApprovalWaitingGateway": rlDhcpApprovalWaitingGateway,
       "rlDhcpApprovalActionTable": rlDhcpApprovalActionTable,
       "rlDhcpApprovalActionEntry": rlDhcpApprovalActionEntry,
       "rlDhcpApprovalActionIfIndex": rlDhcpApprovalActionIfIndex,
       "rlDhcpApprovalActionAddress": rlDhcpApprovalActionAddress,
       "rlDhcpApprovalActionMask": rlDhcpApprovalActionMask,
       "rlDhcpApprovalActionApprove": rlDhcpApprovalActionApprove,
       "rlDhcpClCommandTable": rlDhcpClCommandTable,
       "rlDhcpClCommandEntry": rlDhcpClCommandEntry,
       "rlDhcpClCommandAction": rlDhcpClCommandAction,
       "rlDhcpClConfigurationFileName": rlDhcpClConfigurationFileName,
       "rlDhcpClOption67Enable": rlDhcpClOption67Enable}
)
