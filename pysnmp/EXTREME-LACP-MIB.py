# SNMP MIB module (EXTREME-LACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-LACP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:48 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeLacp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpGroupId(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class LacpMemberPort(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeLacpTable_Object = MibTable
extremeLacpTable = _ExtremeLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1)
)
if mibBuilder.loadTexts:
    extremeLacpTable.setStatus("current")
_ExtremeLacpEntry_Object = MibTableRow
extremeLacpEntry = _ExtremeLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1)
)
extremeLacpEntry.setIndexNames(
    (0, "EXTREME-LACP-MIB", "extremeLacpGroup"),
    (0, "EXTREME-LACP-MIB", "extremeLacpMemberPort"),
)
if mibBuilder.loadTexts:
    extremeLacpEntry.setStatus("current")
_ExtremeLacpGroup_Type = LacpGroupId
_ExtremeLacpGroup_Object = MibTableColumn
extremeLacpGroup = _ExtremeLacpGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 1),
    _ExtremeLacpGroup_Type()
)
extremeLacpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpGroup.setStatus("current")
_ExtremeLacpMemberPort_Type = LacpMemberPort
_ExtremeLacpMemberPort_Object = MibTableColumn
extremeLacpMemberPort = _ExtremeLacpMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 2),
    _ExtremeLacpMemberPort_Type()
)
extremeLacpMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpMemberPort.setStatus("current")
_ExtremeLacpAggStatus_Type = TruthValue
_ExtremeLacpAggStatus_Object = MibTableColumn
extremeLacpAggStatus = _ExtremeLacpAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 3),
    _ExtremeLacpAggStatus_Type()
)
extremeLacpAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpAggStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-LACP-MIB",
    **{"LacpGroupId": LacpGroupId,
       "LacpMemberPort": LacpMemberPort,
       "extremeLacp": extremeLacp,
       "extremeLacpTable": extremeLacpTable,
       "extremeLacpEntry": extremeLacpEntry,
       "extremeLacpGroup": extremeLacpGroup,
       "extremeLacpMemberPort": extremeLacpMemberPort,
       "extremeLacpAggStatus": extremeLacpAggStatus}
)
