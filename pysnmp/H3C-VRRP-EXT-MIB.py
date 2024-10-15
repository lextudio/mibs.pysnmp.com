# SNMP MIB module (H3C-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:52 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cVrrpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVrrpExtMibObject_ObjectIdentity = ObjectIdentity
h3cVrrpExtMibObject = _H3cVrrpExtMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1)
)
_H3cVrrpExtTable_Object = MibTable
h3cVrrpExtTable = _H3cVrrpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVrrpExtTable.setStatus("current")
_H3cVrrpExtEntry_Object = MibTableRow
h3cVrrpExtEntry = _H3cVrrpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1)
)
h3cVrrpExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "H3C-VRRP-EXT-MIB", "h3cVrrpExtTrackInterface"),
)
if mibBuilder.loadTexts:
    h3cVrrpExtEntry.setStatus("current")


class _H3cVrrpExtTrackInterface_Type(Integer32):
    """Custom type h3cVrrpExtTrackInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cVrrpExtTrackInterface_Type.__name__ = "Integer32"
_H3cVrrpExtTrackInterface_Object = MibTableColumn
h3cVrrpExtTrackInterface = _H3cVrrpExtTrackInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 1),
    _H3cVrrpExtTrackInterface_Type()
)
h3cVrrpExtTrackInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVrrpExtTrackInterface.setStatus("current")


class _H3cVrrpExtPriorityReduce_Type(Integer32):
    """Custom type h3cVrrpExtPriorityReduce based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cVrrpExtPriorityReduce_Type.__name__ = "Integer32"
_H3cVrrpExtPriorityReduce_Object = MibTableColumn
h3cVrrpExtPriorityReduce = _H3cVrrpExtPriorityReduce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 2),
    _H3cVrrpExtPriorityReduce_Type()
)
h3cVrrpExtPriorityReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVrrpExtPriorityReduce.setStatus("current")
_H3cVrrpExtRowStatus_Type = RowStatus
_H3cVrrpExtRowStatus_Object = MibTableColumn
h3cVrrpExtRowStatus = _H3cVrrpExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 24, 1, 1, 1, 3),
    _H3cVrrpExtRowStatus_Type()
)
h3cVrrpExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVrrpExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VRRP-EXT-MIB",
    **{"h3cVrrpExt": h3cVrrpExt,
       "h3cVrrpExtMibObject": h3cVrrpExtMibObject,
       "h3cVrrpExtTable": h3cVrrpExtTable,
       "h3cVrrpExtEntry": h3cVrrpExtEntry,
       "h3cVrrpExtTrackInterface": h3cVrrpExtTrackInterface,
       "h3cVrrpExtPriorityReduce": h3cVrrpExtPriorityReduce,
       "h3cVrrpExtRowStatus": h3cVrrpExtRowStatus}
)
