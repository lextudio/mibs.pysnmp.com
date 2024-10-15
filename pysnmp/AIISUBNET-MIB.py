# SNMP MIB module (AIISUBNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIISUBNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:11 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aiiSubnet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 3)
)


# Types definitions



class SubnetIndex(Integer32):
    """Custom type SubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLC2_ObjectIdentity = ObjectIdentity
aiSLC2 = _AiSLC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
_AiiSubnetTable_Object = MibTable
aiiSubnetTable = _AiiSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1)
)
if mibBuilder.loadTexts:
    aiiSubnetTable.setStatus("current")
_AiiSubnetEntry_Object = MibTableRow
aiiSubnetEntry = _AiiSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1)
)
aiiSubnetEntry.setIndexNames(
    (0, "AIISUBNET-MIB", "aiiSubnetIndex"),
)
if mibBuilder.loadTexts:
    aiiSubnetEntry.setStatus("current")
_AiiSubnetIndex_Type = SubnetIndex
_AiiSubnetIndex_Object = MibTableColumn
aiiSubnetIndex = _AiiSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 1),
    _AiiSubnetIndex_Type()
)
aiiSubnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiiSubnetIndex.setStatus("current")
_AiiSubnetEntryStatus_Type = RowStatus
_AiiSubnetEntryStatus_Object = MibTableColumn
aiiSubnetEntryStatus = _AiiSubnetEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 2),
    _AiiSubnetEntryStatus_Type()
)
aiiSubnetEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetEntryStatus.setStatus("current")
_AiiSubnetAddr_Type = IpAddress
_AiiSubnetAddr_Object = MibTableColumn
aiiSubnetAddr = _AiiSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 3),
    _AiiSubnetAddr_Type()
)
aiiSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetAddr.setStatus("current")
_AiiSubnetIfIndex_Type = Integer32
_AiiSubnetIfIndex_Object = MibTableColumn
aiiSubnetIfIndex = _AiiSubnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 4),
    _AiiSubnetIfIndex_Type()
)
aiiSubnetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetIfIndex.setStatus("current")
_AiiSubnetNetMask_Type = IpAddress
_AiiSubnetNetMask_Object = MibTableColumn
aiiSubnetNetMask = _AiiSubnetNetMask_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 5),
    _AiiSubnetNetMask_Type()
)
aiiSubnetNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetNetMask.setStatus("current")
_AiiSubnetBcastAddr_Type = Integer32
_AiiSubnetBcastAddr_Object = MibTableColumn
aiiSubnetBcastAddr = _AiiSubnetBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 6),
    _AiiSubnetBcastAddr_Type()
)
aiiSubnetBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetBcastAddr.setStatus("current")
_AiiSubnetType_Type = Integer32
_AiiSubnetType_Object = MibTableColumn
aiiSubnetType = _AiiSubnetType_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 7),
    _AiiSubnetType_Type()
)
aiiSubnetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetType.setStatus("current")
_AiiSubnetAdmnStatus_Type = Integer32
_AiiSubnetAdmnStatus_Object = MibTableColumn
aiiSubnetAdmnStatus = _AiiSubnetAdmnStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 1, 1, 8),
    _AiiSubnetAdmnStatus_Type()
)
aiiSubnetAdmnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetAdmnStatus.setStatus("current")
_AiiSubnetTable2_Object = MibTable
aiiSubnetTable2 = _AiiSubnetTable2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2)
)
if mibBuilder.loadTexts:
    aiiSubnetTable2.setStatus("current")
_AiiSubnetEntry2_Object = MibTableRow
aiiSubnetEntry2 = _AiiSubnetEntry2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2, 1)
)
aiiSubnetEntry2.setIndexNames(
    (0, "AIISUBNET-MIB", "aiiSubnetIndex2"),
)
if mibBuilder.loadTexts:
    aiiSubnetEntry2.setStatus("current")


class _AiiSubnetIndex2_Type(Integer32):
    """Custom type aiiSubnetIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AiiSubnetIndex2_Type.__name__ = "Integer32"
_AiiSubnetIndex2_Object = MibTableColumn
aiiSubnetIndex2 = _AiiSubnetIndex2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2, 1, 1),
    _AiiSubnetIndex2_Type()
)
aiiSubnetIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiiSubnetIndex2.setStatus("current")
_AiiIPAddr_Type = IpAddress
_AiiIPAddr_Object = MibTableColumn
aiiIPAddr = _AiiIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2, 1, 2),
    _AiiIPAddr_Type()
)
aiiIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiIPAddr.setStatus("current")


class _AiiSubnetRange_Type(Integer32):
    """Custom type aiiSubnetRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AiiSubnetRange_Type.__name__ = "Integer32"
_AiiSubnetRange_Object = MibTableColumn
aiiSubnetRange = _AiiSubnetRange_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2, 1, 3),
    _AiiSubnetRange_Type()
)
aiiSubnetRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetRange.setStatus("current")
_AiiSubnetMask_Type = IpAddress
_AiiSubnetMask_Object = MibTableColumn
aiiSubnetMask = _AiiSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 3, 2, 1, 4),
    _AiiSubnetMask_Type()
)
aiiSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiiSubnetMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIISUBNET-MIB",
    **{"SubnetIndex": SubnetIndex,
       "aii": aii,
       "aiSLC2": aiSLC2,
       "aiiSubnet": aiiSubnet,
       "aiiSubnetTable": aiiSubnetTable,
       "aiiSubnetEntry": aiiSubnetEntry,
       "aiiSubnetIndex": aiiSubnetIndex,
       "aiiSubnetEntryStatus": aiiSubnetEntryStatus,
       "aiiSubnetAddr": aiiSubnetAddr,
       "aiiSubnetIfIndex": aiiSubnetIfIndex,
       "aiiSubnetNetMask": aiiSubnetNetMask,
       "aiiSubnetBcastAddr": aiiSubnetBcastAddr,
       "aiiSubnetType": aiiSubnetType,
       "aiiSubnetAdmnStatus": aiiSubnetAdmnStatus,
       "aiiSubnetTable2": aiiSubnetTable2,
       "aiiSubnetEntry2": aiiSubnetEntry2,
       "aiiSubnetIndex2": aiiSubnetIndex2,
       "aiiIPAddr": aiiIPAddr,
       "aiiSubnetRange": aiiSubnetRange,
       "aiiSubnetMask": aiiSubnetMask}
)
