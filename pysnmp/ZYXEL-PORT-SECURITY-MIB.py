# SNMP MIB module (ZYXEL-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:36 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelPortSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPortSecuritySetup_ObjectIdentity = ObjectIdentity
zyxelPortSecuritySetup = _ZyxelPortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1)
)
_ZyPortSecurityState_Type = EnabledStatus
_ZyPortSecurityState_Object = MibScalar
zyPortSecurityState = _ZyPortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 1),
    _ZyPortSecurityState_Type()
)
zyPortSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityState.setStatus("current")
_ZyxelPortSecurityPortTable_Object = MibTable
zyxelPortSecurityPortTable = _ZyxelPortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelPortSecurityPortTable.setStatus("current")
_ZyxelPortSecurityPortEntry_Object = MibTableRow
zyxelPortSecurityPortEntry = _ZyxelPortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1)
)
zyxelPortSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelPortSecurityPortEntry.setStatus("current")
_ZyPortSecurityPortState_Type = EnabledStatus
_ZyPortSecurityPortState_Object = MibTableColumn
zyPortSecurityPortState = _ZyPortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 1),
    _ZyPortSecurityPortState_Type()
)
zyPortSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityPortState.setStatus("current")
_ZyPortSecurityPortLearnState_Type = EnabledStatus
_ZyPortSecurityPortLearnState_Object = MibTableColumn
zyPortSecurityPortLearnState = _ZyPortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 2),
    _ZyPortSecurityPortLearnState_Type()
)
zyPortSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityPortLearnState.setStatus("current")
_ZyPortSecurityPortMacLimit_Type = Integer32
_ZyPortSecurityPortMacLimit_Object = MibTableColumn
zyPortSecurityPortMacLimit = _ZyPortSecurityPortMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 2, 1, 3),
    _ZyPortSecurityPortMacLimit_Type()
)
zyPortSecurityPortMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityPortMacLimit.setStatus("current")
_ZyPortSecurityMacFreeze_Type = PortList
_ZyPortSecurityMacFreeze_Object = MibScalar
zyPortSecurityMacFreeze = _ZyPortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 3),
    _ZyPortSecurityMacFreeze_Type()
)
zyPortSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityMacFreeze.setStatus("current")
_ZyPortSecurityMaxNumberOfVMLs_Type = Integer32
_ZyPortSecurityMaxNumberOfVMLs_Object = MibScalar
zyPortSecurityMaxNumberOfVMLs = _ZyPortSecurityMaxNumberOfVMLs_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 4),
    _ZyPortSecurityMaxNumberOfVMLs_Type()
)
zyPortSecurityMaxNumberOfVMLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyPortSecurityMaxNumberOfVMLs.setStatus("current")
_ZyxelPortSecurityVMLTable_Object = MibTable
zyxelPortSecurityVMLTable = _ZyxelPortSecurityVMLTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelPortSecurityVMLTable.setStatus("current")
_ZyxelPortSecurityVMLEntry_Object = MibTableRow
zyxelPortSecurityVMLEntry = _ZyxelPortSecurityVMLEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1)
)
zyxelPortSecurityVMLEntry.setIndexNames(
    (0, "ZYXEL-PORT-SECURITY-MIB", "zyPortSecurityVMLPort"),
    (0, "ZYXEL-PORT-SECURITY-MIB", "zyPortSecurityVMLVID"),
)
if mibBuilder.loadTexts:
    zyxelPortSecurityVMLEntry.setStatus("current")
_ZyPortSecurityVMLPort_Type = Integer32
_ZyPortSecurityVMLPort_Object = MibTableColumn
zyPortSecurityVMLPort = _ZyPortSecurityVMLPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 1),
    _ZyPortSecurityVMLPort_Type()
)
zyPortSecurityVMLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPortSecurityVMLPort.setStatus("current")
_ZyPortSecurityVMLVID_Type = Integer32
_ZyPortSecurityVMLVID_Object = MibTableColumn
zyPortSecurityVMLVID = _ZyPortSecurityVMLVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 2),
    _ZyPortSecurityVMLVID_Type()
)
zyPortSecurityVMLVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyPortSecurityVMLVID.setStatus("current")
_ZyPortSecurityVMLMacLimit_Type = Integer32
_ZyPortSecurityVMLMacLimit_Object = MibTableColumn
zyPortSecurityVMLMacLimit = _ZyPortSecurityVMLMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 3),
    _ZyPortSecurityVMLMacLimit_Type()
)
zyPortSecurityVMLMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPortSecurityVMLMacLimit.setStatus("current")
_ZyPortSecurityVMLRowStatus_Type = RowStatus
_ZyPortSecurityVMLRowStatus_Object = MibTableColumn
zyPortSecurityVMLRowStatus = _ZyPortSecurityVMLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 66, 1, 5, 1, 4),
    _ZyPortSecurityVMLRowStatus_Type()
)
zyPortSecurityVMLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyPortSecurityVMLRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PORT-SECURITY-MIB",
    **{"zyxelPortSecurity": zyxelPortSecurity,
       "zyxelPortSecuritySetup": zyxelPortSecuritySetup,
       "zyPortSecurityState": zyPortSecurityState,
       "zyxelPortSecurityPortTable": zyxelPortSecurityPortTable,
       "zyxelPortSecurityPortEntry": zyxelPortSecurityPortEntry,
       "zyPortSecurityPortState": zyPortSecurityPortState,
       "zyPortSecurityPortLearnState": zyPortSecurityPortLearnState,
       "zyPortSecurityPortMacLimit": zyPortSecurityPortMacLimit,
       "zyPortSecurityMacFreeze": zyPortSecurityMacFreeze,
       "zyPortSecurityMaxNumberOfVMLs": zyPortSecurityMaxNumberOfVMLs,
       "zyxelPortSecurityVMLTable": zyxelPortSecurityVMLTable,
       "zyxelPortSecurityVMLEntry": zyxelPortSecurityVMLEntry,
       "zyPortSecurityVMLPort": zyPortSecurityVMLPort,
       "zyPortSecurityVMLVID": zyPortSecurityVMLVID,
       "zyPortSecurityVMLMacLimit": zyPortSecurityVMLMacLimit,
       "zyPortSecurityVMLRowStatus": zyPortSecurityVMLRowStatus}
)
