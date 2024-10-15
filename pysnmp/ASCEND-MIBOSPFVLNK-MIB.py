# SNMP MIB module (ASCEND-MIBOSPFVLNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBOSPFVLNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:00 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibospfVirtIntfProfile_ObjectIdentity = ObjectIdentity
mibospfVirtIntfProfile = _MibospfVirtIntfProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 99)
)
_MibospfVirtIntfProfileTable_Object = MibTable
mibospfVirtIntfProfileTable = _MibospfVirtIntfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1)
)
if mibBuilder.loadTexts:
    mibospfVirtIntfProfileTable.setStatus("mandatory")
_MibospfVirtIntfProfileEntry_Object = MibTableRow
mibospfVirtIntfProfileEntry = _MibospfVirtIntfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1)
)
mibospfVirtIntfProfileEntry.setIndexNames(
    (0, "ASCEND-MIBOSPFVLNK-MIB", "ospfVirtIntfProfile-NeighborRouterId"),
)
if mibBuilder.loadTexts:
    mibospfVirtIntfProfileEntry.setStatus("mandatory")
_OspfVirtIntfProfile_NeighborRouterId_Type = IpAddress
_OspfVirtIntfProfile_NeighborRouterId_Object = MibScalar
ospfVirtIntfProfile_NeighborRouterId = _OspfVirtIntfProfile_NeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 1),
    _OspfVirtIntfProfile_NeighborRouterId_Type()
)
ospfVirtIntfProfile_NeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_NeighborRouterId.setStatus("mandatory")
_OspfVirtIntfProfile_TransitAreaId_Type = IpAddress
_OspfVirtIntfProfile_TransitAreaId_Object = MibScalar
ospfVirtIntfProfile_TransitAreaId = _OspfVirtIntfProfile_TransitAreaId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 2),
    _OspfVirtIntfProfile_TransitAreaId_Type()
)
ospfVirtIntfProfile_TransitAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_TransitAreaId.setStatus("mandatory")
_OspfVirtIntfProfile_RexmitDelay_Type = Integer32
_OspfVirtIntfProfile_RexmitDelay_Object = MibScalar
ospfVirtIntfProfile_RexmitDelay = _OspfVirtIntfProfile_RexmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 3),
    _OspfVirtIntfProfile_RexmitDelay_Type()
)
ospfVirtIntfProfile_RexmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_RexmitDelay.setStatus("mandatory")
_OspfVirtIntfProfile_XmitDelay_Type = Integer32
_OspfVirtIntfProfile_XmitDelay_Object = MibScalar
ospfVirtIntfProfile_XmitDelay = _OspfVirtIntfProfile_XmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 4),
    _OspfVirtIntfProfile_XmitDelay_Type()
)
ospfVirtIntfProfile_XmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_XmitDelay.setStatus("mandatory")
_OspfVirtIntfProfile_HelloInterval_Type = Integer32
_OspfVirtIntfProfile_HelloInterval_Object = MibScalar
ospfVirtIntfProfile_HelloInterval = _OspfVirtIntfProfile_HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 5),
    _OspfVirtIntfProfile_HelloInterval_Type()
)
ospfVirtIntfProfile_HelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_HelloInterval.setStatus("mandatory")
_OspfVirtIntfProfile_DeadInterval_Type = Integer32
_OspfVirtIntfProfile_DeadInterval_Object = MibScalar
ospfVirtIntfProfile_DeadInterval = _OspfVirtIntfProfile_DeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 6),
    _OspfVirtIntfProfile_DeadInterval_Type()
)
ospfVirtIntfProfile_DeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_DeadInterval.setStatus("mandatory")


class _OspfVirtIntfProfile_AuthenType_Type(Integer32):
    """Custom type ospfVirtIntfProfile_AuthenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("simple", 2))
    )


_OspfVirtIntfProfile_AuthenType_Type.__name__ = "Integer32"
_OspfVirtIntfProfile_AuthenType_Object = MibScalar
ospfVirtIntfProfile_AuthenType = _OspfVirtIntfProfile_AuthenType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 7),
    _OspfVirtIntfProfile_AuthenType_Type()
)
ospfVirtIntfProfile_AuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_AuthenType.setStatus("mandatory")
_OspfVirtIntfProfile_AuthenKey_Type = DisplayString
_OspfVirtIntfProfile_AuthenKey_Object = MibScalar
ospfVirtIntfProfile_AuthenKey = _OspfVirtIntfProfile_AuthenKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 8),
    _OspfVirtIntfProfile_AuthenKey_Type()
)
ospfVirtIntfProfile_AuthenKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_AuthenKey.setStatus("mandatory")
_OspfVirtIntfProfile_KeyId_Type = Integer32
_OspfVirtIntfProfile_KeyId_Object = MibScalar
ospfVirtIntfProfile_KeyId = _OspfVirtIntfProfile_KeyId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 9),
    _OspfVirtIntfProfile_KeyId_Type()
)
ospfVirtIntfProfile_KeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_KeyId.setStatus("mandatory")
_OspfVirtIntfProfile_Md5AuthenKey_Type = DisplayString
_OspfVirtIntfProfile_Md5AuthenKey_Object = MibScalar
ospfVirtIntfProfile_Md5AuthenKey = _OspfVirtIntfProfile_Md5AuthenKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 10),
    _OspfVirtIntfProfile_Md5AuthenKey_Type()
)
ospfVirtIntfProfile_Md5AuthenKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_Md5AuthenKey.setStatus("mandatory")


class _OspfVirtIntfProfile_Action_o_Type(Integer32):
    """Custom type ospfVirtIntfProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_OspfVirtIntfProfile_Action_o_Type.__name__ = "Integer32"
_OspfVirtIntfProfile_Action_o_Object = MibScalar
ospfVirtIntfProfile_Action_o = _OspfVirtIntfProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 99, 1, 1, 11),
    _OspfVirtIntfProfile_Action_o_Type()
)
ospfVirtIntfProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIntfProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBOSPFVLNK-MIB",
    **{"DisplayString": DisplayString,
       "mibospfVirtIntfProfile": mibospfVirtIntfProfile,
       "mibospfVirtIntfProfileTable": mibospfVirtIntfProfileTable,
       "mibospfVirtIntfProfileEntry": mibospfVirtIntfProfileEntry,
       "ospfVirtIntfProfile-NeighborRouterId": ospfVirtIntfProfile_NeighborRouterId,
       "ospfVirtIntfProfile-TransitAreaId": ospfVirtIntfProfile_TransitAreaId,
       "ospfVirtIntfProfile-RexmitDelay": ospfVirtIntfProfile_RexmitDelay,
       "ospfVirtIntfProfile-XmitDelay": ospfVirtIntfProfile_XmitDelay,
       "ospfVirtIntfProfile-HelloInterval": ospfVirtIntfProfile_HelloInterval,
       "ospfVirtIntfProfile-DeadInterval": ospfVirtIntfProfile_DeadInterval,
       "ospfVirtIntfProfile-AuthenType": ospfVirtIntfProfile_AuthenType,
       "ospfVirtIntfProfile-AuthenKey": ospfVirtIntfProfile_AuthenKey,
       "ospfVirtIntfProfile-KeyId": ospfVirtIntfProfile_KeyId,
       "ospfVirtIntfProfile-Md5AuthenKey": ospfVirtIntfProfile_Md5AuthenKey,
       "ospfVirtIntfProfile-Action-o": ospfVirtIntfProfile_Action_o}
)
