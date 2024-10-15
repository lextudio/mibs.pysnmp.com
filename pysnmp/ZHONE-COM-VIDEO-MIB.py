# SNMP MIB module (ZHONE-COM-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:23 2024
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

(ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifPhysAddress")

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

(zhoneModules,
 zhoneVideo) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneVideo")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comVideo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 78)
)
comVideo.setRevisions(
        ("2003-10-28 11:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VideoInterfaceTable_Object = MibTable
videoInterfaceTable = _VideoInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 2)
)
if mibBuilder.loadTexts:
    videoInterfaceTable.setStatus("current")
_VideoInterfaceEntry_Object = MibTableRow
videoInterfaceEntry = _VideoInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1)
)
videoInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    videoInterfaceEntry.setStatus("current")
_VideoInterfaceRowStatus_Type = ZhoneRowStatus
_VideoInterfaceRowStatus_Object = MibTableColumn
videoInterfaceRowStatus = _VideoInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1, 1),
    _VideoInterfaceRowStatus_Type()
)
videoInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    videoInterfaceRowStatus.setStatus("current")


class _VideoInterfaceType_Type(Integer32):
    """Custom type videoInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 3),
          ("management", 1),
          ("stream", 2))
    )


_VideoInterfaceType_Type.__name__ = "Integer32"
_VideoInterfaceType_Object = MibTableColumn
videoInterfaceType = _VideoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 2, 1, 2),
    _VideoInterfaceType_Type()
)
videoInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    videoInterfaceType.setStatus("current")
_VideoMulticastSourceTable_Object = MibTable
videoMulticastSourceTable = _VideoMulticastSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3)
)
if mibBuilder.loadTexts:
    videoMulticastSourceTable.setStatus("current")
_VideoMulticastSourceEntry_Object = MibTableRow
videoMulticastSourceEntry = _VideoMulticastSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1)
)
videoMulticastSourceEntry.setIndexNames(
    (0, "ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIndex"),
)
if mibBuilder.loadTexts:
    videoMulticastSourceEntry.setStatus("current")


class _VideoMulticastSourceIndex_Type(Integer32):
    """Custom type videoMulticastSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VideoMulticastSourceIndex_Type.__name__ = "Integer32"
_VideoMulticastSourceIndex_Object = MibTableColumn
videoMulticastSourceIndex = _VideoMulticastSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 1),
    _VideoMulticastSourceIndex_Type()
)
videoMulticastSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    videoMulticastSourceIndex.setStatus("current")
_VideoMulticastSourceRowStatus_Type = ZhoneRowStatus
_VideoMulticastSourceRowStatus_Object = MibTableColumn
videoMulticastSourceRowStatus = _VideoMulticastSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 2),
    _VideoMulticastSourceRowStatus_Type()
)
videoMulticastSourceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoMulticastSourceRowStatus.setStatus("current")
_VideoMulticastSourceIpAddress_Type = IpAddress
_VideoMulticastSourceIpAddress_Object = MibTableColumn
videoMulticastSourceIpAddress = _VideoMulticastSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 3),
    _VideoMulticastSourceIpAddress_Type()
)
videoMulticastSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoMulticastSourceIpAddress.setStatus("current")
_VideoMulticastSourceNetMask_Type = IpAddress
_VideoMulticastSourceNetMask_Object = MibTableColumn
videoMulticastSourceNetMask = _VideoMulticastSourceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 3, 1, 4),
    _VideoMulticastSourceNetMask_Type()
)
videoMulticastSourceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoMulticastSourceNetMask.setStatus("current")


class _VideoMulticastSourceIndexNext_Type(Integer32):
    """Custom type videoMulticastSourceIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VideoMulticastSourceIndexNext_Type.__name__ = "Integer32"
_VideoMulticastSourceIndexNext_Object = MibScalar
videoMulticastSourceIndexNext = _VideoMulticastSourceIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 4),
    _VideoMulticastSourceIndexNext_Type()
)
videoMulticastSourceIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoMulticastSourceIndexNext.setStatus("current")

# Managed Objects groups

videoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 8, 1)
)
videoGroup.setObjects(
      *(("ZHONE-COM-VIDEO-MIB", "videoInterfaceRowStatus"),
        ("ZHONE-COM-VIDEO-MIB", "videoInterfaceType"),
        ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceRowStatus"),
        ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIpAddress"),
        ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceNetMask"),
        ("ZHONE-COM-VIDEO-MIB", "videoMulticastSourceIndexNext"))
)
if mibBuilder.loadTexts:
    videoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-VIDEO-MIB",
    **{"videoGroup": videoGroup,
       "videoInterfaceTable": videoInterfaceTable,
       "videoInterfaceEntry": videoInterfaceEntry,
       "videoInterfaceRowStatus": videoInterfaceRowStatus,
       "videoInterfaceType": videoInterfaceType,
       "videoMulticastSourceTable": videoMulticastSourceTable,
       "videoMulticastSourceEntry": videoMulticastSourceEntry,
       "videoMulticastSourceIndex": videoMulticastSourceIndex,
       "videoMulticastSourceRowStatus": videoMulticastSourceRowStatus,
       "videoMulticastSourceIpAddress": videoMulticastSourceIpAddress,
       "videoMulticastSourceNetMask": videoMulticastSourceNetMask,
       "videoMulticastSourceIndexNext": videoMulticastSourceIndexNext,
       "comVideo": comVideo}
)
