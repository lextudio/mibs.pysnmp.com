# SNMP MIB module (HPN-ICF-VRRP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VRRP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:13 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfVrrpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVrrpExtMibObject_ObjectIdentity = ObjectIdentity
hpnicfVrrpExtMibObject = _HpnicfVrrpExtMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1)
)
_HpnicfVrrpExtTable_Object = MibTable
hpnicfVrrpExtTable = _HpnicfVrrpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfVrrpExtTable.setStatus("current")
_HpnicfVrrpExtEntry_Object = MibTableRow
hpnicfVrrpExtEntry = _HpnicfVrrpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1)
)
hpnicfVrrpExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "HPN-ICF-VRRP-EXT-MIB", "hpnicfVrrpExtTrackInterface"),
)
if mibBuilder.loadTexts:
    hpnicfVrrpExtEntry.setStatus("current")


class _HpnicfVrrpExtTrackInterface_Type(Integer32):
    """Custom type hpnicfVrrpExtTrackInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfVrrpExtTrackInterface_Type.__name__ = "Integer32"
_HpnicfVrrpExtTrackInterface_Object = MibTableColumn
hpnicfVrrpExtTrackInterface = _HpnicfVrrpExtTrackInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 1),
    _HpnicfVrrpExtTrackInterface_Type()
)
hpnicfVrrpExtTrackInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVrrpExtTrackInterface.setStatus("current")


class _HpnicfVrrpExtPriorityReduce_Type(Integer32):
    """Custom type hpnicfVrrpExtPriorityReduce based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfVrrpExtPriorityReduce_Type.__name__ = "Integer32"
_HpnicfVrrpExtPriorityReduce_Object = MibTableColumn
hpnicfVrrpExtPriorityReduce = _HpnicfVrrpExtPriorityReduce_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 2),
    _HpnicfVrrpExtPriorityReduce_Type()
)
hpnicfVrrpExtPriorityReduce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVrrpExtPriorityReduce.setStatus("current")
_HpnicfVrrpExtRowStatus_Type = RowStatus
_HpnicfVrrpExtRowStatus_Object = MibTableColumn
hpnicfVrrpExtRowStatus = _HpnicfVrrpExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 3),
    _HpnicfVrrpExtRowStatus_Type()
)
hpnicfVrrpExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVrrpExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VRRP-EXT-MIB",
    **{"hpnicfVrrpExt": hpnicfVrrpExt,
       "hpnicfVrrpExtMibObject": hpnicfVrrpExtMibObject,
       "hpnicfVrrpExtTable": hpnicfVrrpExtTable,
       "hpnicfVrrpExtEntry": hpnicfVrrpExtEntry,
       "hpnicfVrrpExtTrackInterface": hpnicfVrrpExtTrackInterface,
       "hpnicfVrrpExtPriorityReduce": hpnicfVrrpExtPriorityReduce,
       "hpnicfVrrpExtRowStatus": hpnicfVrrpExtRowStatus}
)
