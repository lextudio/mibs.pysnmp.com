# SNMP MIB module (HH3C-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:20 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(vrrpOperVrId,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperVrId")


# MODULE-IDENTITY

hh3cVrrpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVrrpExtMibObject_ObjectIdentity = ObjectIdentity
hh3cVrrpExtMibObject = _Hh3cVrrpExtMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1)
)
_Hh3cVrrpExtTable_Object = MibTable
hh3cVrrpExtTable = _Hh3cVrrpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVrrpExtTable.setStatus("current")
_Hh3cVrrpExtEntry_Object = MibTableRow
hh3cVrrpExtEntry = _Hh3cVrrpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1, 1, 1)
)
hh3cVrrpExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "HH3C-VRRP-EXT-MIB", "hh3cVrrpExtTrackInterface"),
)
if mibBuilder.loadTexts:
    hh3cVrrpExtEntry.setStatus("current")


class _Hh3cVrrpExtTrackInterface_Type(Integer32):
    """Custom type hh3cVrrpExtTrackInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cVrrpExtTrackInterface_Type.__name__ = "Integer32"
_Hh3cVrrpExtTrackInterface_Object = MibTableColumn
hh3cVrrpExtTrackInterface = _Hh3cVrrpExtTrackInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1, 1, 1, 1),
    _Hh3cVrrpExtTrackInterface_Type()
)
hh3cVrrpExtTrackInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVrrpExtTrackInterface.setStatus("current")


class _Hh3cVrrpExtPriorityReduce_Type(Integer32):
    """Custom type hh3cVrrpExtPriorityReduce based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cVrrpExtPriorityReduce_Type.__name__ = "Integer32"
_Hh3cVrrpExtPriorityReduce_Object = MibTableColumn
hh3cVrrpExtPriorityReduce = _Hh3cVrrpExtPriorityReduce_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1, 1, 1, 2),
    _Hh3cVrrpExtPriorityReduce_Type()
)
hh3cVrrpExtPriorityReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVrrpExtPriorityReduce.setStatus("current")
_Hh3cVrrpExtRowStatus_Type = RowStatus
_Hh3cVrrpExtRowStatus_Object = MibTableColumn
hh3cVrrpExtRowStatus = _Hh3cVrrpExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24, 1, 1, 1, 3),
    _Hh3cVrrpExtRowStatus_Type()
)
hh3cVrrpExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVrrpExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VRRP-EXT-MIB",
    **{"hh3cVrrpExt": hh3cVrrpExt,
       "hh3cVrrpExtMibObject": hh3cVrrpExtMibObject,
       "hh3cVrrpExtTable": hh3cVrrpExtTable,
       "hh3cVrrpExtEntry": hh3cVrrpExtEntry,
       "hh3cVrrpExtTrackInterface": hh3cVrrpExtTrackInterface,
       "hh3cVrrpExtPriorityReduce": hh3cVrrpExtPriorityReduce,
       "hh3cVrrpExtRowStatus": hh3cVrrpExtRowStatus}
)
