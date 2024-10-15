# SNMP MIB module (NETSCREEN-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:52 2024
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

(netscreenService,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenService")

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

netscreenServiceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 13, 0)
)
netscreenServiceMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsServiceTable_Object = MibTable
nsServiceTable = _NsServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1)
)
if mibBuilder.loadTexts:
    nsServiceTable.setStatus("current")
_NsServiceEntry_Object = MibTableRow
nsServiceEntry = _NsServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1)
)
nsServiceEntry.setIndexNames(
    (0, "NETSCREEN-SERVICE-MIB", "nsServiceIndex"),
)
if mibBuilder.loadTexts:
    nsServiceEntry.setStatus("current")


class _NsServiceIndex_Type(Integer32):
    """Custom type nsServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsServiceIndex_Type.__name__ = "Integer32"
_NsServiceIndex_Object = MibTableColumn
nsServiceIndex = _NsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 1),
    _NsServiceIndex_Type()
)
nsServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceIndex.setStatus("current")


class _NsServiceName_Type(DisplayString):
    """Custom type nsServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsServiceName_Type.__name__ = "DisplayString"
_NsServiceName_Object = MibTableColumn
nsServiceName = _NsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 2),
    _NsServiceName_Type()
)
nsServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceName.setStatus("current")


class _NsServiceCategory_Type(Integer32):
    """Custom type nsServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("email", 2),
          ("infoseek", 3),
          ("other", 5),
          ("remote", 1),
          ("security", 4))
    )


_NsServiceCategory_Type.__name__ = "Integer32"
_NsServiceCategory_Object = MibTableColumn
nsServiceCategory = _NsServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 3),
    _NsServiceCategory_Type()
)
nsServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceCategory.setStatus("current")


class _NsServiceTransProto_Type(Integer32):
    """Custom type nsServiceTransProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              8,
              9,
              17,
              46,
              47,
              89)
        )
    )
    namedValues = NamedValues(
        *(("egp", 8),
          ("gre", 47),
          ("icmp", 1),
          ("igp", 9),
          ("ospf", 89),
          ("other", 0),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17))
    )


_NsServiceTransProto_Type.__name__ = "Integer32"
_NsServiceTransProto_Object = MibTableColumn
nsServiceTransProto = _NsServiceTransProto_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 4),
    _NsServiceTransProto_Type()
)
nsServiceTransProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceTransProto.setStatus("current")
_NsServiceSrcPortLow_Type = Integer32
_NsServiceSrcPortLow_Object = MibTableColumn
nsServiceSrcPortLow = _NsServiceSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 5),
    _NsServiceSrcPortLow_Type()
)
nsServiceSrcPortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceSrcPortLow.setStatus("current")
_NsServiceSrcPortHigh_Type = Integer32
_NsServiceSrcPortHigh_Object = MibTableColumn
nsServiceSrcPortHigh = _NsServiceSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 6),
    _NsServiceSrcPortHigh_Type()
)
nsServiceSrcPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceSrcPortHigh.setStatus("current")
_NsServiceDstPortLow_Type = Integer32
_NsServiceDstPortLow_Object = MibTableColumn
nsServiceDstPortLow = _NsServiceDstPortLow_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 7),
    _NsServiceDstPortLow_Type()
)
nsServiceDstPortLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceDstPortLow.setStatus("current")
_NsServiceDstPortHigh_Type = Integer32
_NsServiceDstPortHigh_Object = MibTableColumn
nsServiceDstPortHigh = _NsServiceDstPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 8),
    _NsServiceDstPortHigh_Type()
)
nsServiceDstPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceDstPortHigh.setStatus("current")


class _NsServiceFlag_Type(Integer32):
    """Custom type nsServiceFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pre-define", 0),
          ("usr-define", 1))
    )


_NsServiceFlag_Type.__name__ = "Integer32"
_NsServiceFlag_Object = MibTableColumn
nsServiceFlag = _NsServiceFlag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 9),
    _NsServiceFlag_Type()
)
nsServiceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceFlag.setStatus("current")
_NsServiceVsys_Type = Integer32
_NsServiceVsys_Object = MibTableColumn
nsServiceVsys = _NsServiceVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 10),
    _NsServiceVsys_Type()
)
nsServiceVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceVsys.setStatus("current")
_NsServiceGroupTable_Object = MibTable
nsServiceGroupTable = _NsServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2)
)
if mibBuilder.loadTexts:
    nsServiceGroupTable.setStatus("current")
_NsServiceGroupEntry_Object = MibTableRow
nsServiceGroupEntry = _NsServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1)
)
nsServiceGroupEntry.setIndexNames(
    (0, "NETSCREEN-SERVICE-MIB", "nsServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    nsServiceGroupEntry.setStatus("current")


class _NsServiceGroupIndex_Type(Integer32):
    """Custom type nsServiceGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsServiceGroupIndex_Type.__name__ = "Integer32"
_NsServiceGroupIndex_Object = MibTableColumn
nsServiceGroupIndex = _NsServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 1),
    _NsServiceGroupIndex_Type()
)
nsServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupIndex.setStatus("current")


class _NsServiceGroupName_Type(DisplayString):
    """Custom type nsServiceGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsServiceGroupName_Type.__name__ = "DisplayString"
_NsServiceGroupName_Object = MibTableColumn
nsServiceGroupName = _NsServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 2),
    _NsServiceGroupName_Type()
)
nsServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupName.setStatus("current")
_NsServiceGroupMember_Type = Integer32
_NsServiceGroupMember_Object = MibTableColumn
nsServiceGroupMember = _NsServiceGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 3),
    _NsServiceGroupMember_Type()
)
nsServiceGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupMember.setStatus("current")


class _NsServiceGroupComment_Type(DisplayString):
    """Custom type nsServiceGroupComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsServiceGroupComment_Type.__name__ = "DisplayString"
_NsServiceGroupComment_Object = MibTableColumn
nsServiceGroupComment = _NsServiceGroupComment_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 4),
    _NsServiceGroupComment_Type()
)
nsServiceGroupComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupComment.setStatus("current")
_NsServiceGroupVsys_Type = Integer32
_NsServiceGroupVsys_Object = MibTableColumn
nsServiceGroupVsys = _NsServiceGroupVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 5),
    _NsServiceGroupVsys_Type()
)
nsServiceGroupVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupVsys.setStatus("current")
_NsServiceGrpMemberTable_Object = MibTable
nsServiceGrpMemberTable = _NsServiceGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3)
)
if mibBuilder.loadTexts:
    nsServiceGrpMemberTable.setStatus("current")
_NsServiceGrpMemberEntry_Object = MibTableRow
nsServiceGrpMemberEntry = _NsServiceGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3, 1)
)
nsServiceGrpMemberEntry.setIndexNames(
    (0, "NETSCREEN-SERVICE-MIB", "nsServiceGrpMemberIndex"),
)
if mibBuilder.loadTexts:
    nsServiceGrpMemberEntry.setStatus("current")


class _NsServiceGrpMemberIndex_Type(Integer32):
    """Custom type nsServiceGrpMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsServiceGrpMemberIndex_Type.__name__ = "Integer32"
_NsServiceGrpMemberIndex_Object = MibTableColumn
nsServiceGrpMemberIndex = _NsServiceGrpMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 1),
    _NsServiceGrpMemberIndex_Type()
)
nsServiceGrpMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGrpMemberIndex.setStatus("current")


class _NsServiceGrpName_Type(DisplayString):
    """Custom type nsServiceGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsServiceGrpName_Type.__name__ = "DisplayString"
_NsServiceGrpName_Object = MibTableColumn
nsServiceGrpName = _NsServiceGrpName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 2),
    _NsServiceGrpName_Type()
)
nsServiceGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGrpName.setStatus("current")


class _NsServiceGroupMemberName_Type(DisplayString):
    """Custom type nsServiceGroupMemberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsServiceGroupMemberName_Type.__name__ = "DisplayString"
_NsServiceGroupMemberName_Object = MibTableColumn
nsServiceGroupMemberName = _NsServiceGroupMemberName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 3),
    _NsServiceGroupMemberName_Type()
)
nsServiceGroupMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupMemberName.setStatus("current")
_NsServiceGroupMemberVsys_Type = Integer32
_NsServiceGroupMemberVsys_Object = MibTableColumn
nsServiceGroupMemberVsys = _NsServiceGroupMemberVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 4),
    _NsServiceGroupMemberVsys_Type()
)
nsServiceGroupMemberVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsServiceGroupMemberVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SERVICE-MIB",
    **{"netscreenServiceMibModule": netscreenServiceMibModule,
       "nsServiceTable": nsServiceTable,
       "nsServiceEntry": nsServiceEntry,
       "nsServiceIndex": nsServiceIndex,
       "nsServiceName": nsServiceName,
       "nsServiceCategory": nsServiceCategory,
       "nsServiceTransProto": nsServiceTransProto,
       "nsServiceSrcPortLow": nsServiceSrcPortLow,
       "nsServiceSrcPortHigh": nsServiceSrcPortHigh,
       "nsServiceDstPortLow": nsServiceDstPortLow,
       "nsServiceDstPortHigh": nsServiceDstPortHigh,
       "nsServiceFlag": nsServiceFlag,
       "nsServiceVsys": nsServiceVsys,
       "nsServiceGroupTable": nsServiceGroupTable,
       "nsServiceGroupEntry": nsServiceGroupEntry,
       "nsServiceGroupIndex": nsServiceGroupIndex,
       "nsServiceGroupName": nsServiceGroupName,
       "nsServiceGroupMember": nsServiceGroupMember,
       "nsServiceGroupComment": nsServiceGroupComment,
       "nsServiceGroupVsys": nsServiceGroupVsys,
       "nsServiceGrpMemberTable": nsServiceGrpMemberTable,
       "nsServiceGrpMemberEntry": nsServiceGrpMemberEntry,
       "nsServiceGrpMemberIndex": nsServiceGrpMemberIndex,
       "nsServiceGrpName": nsServiceGrpName,
       "nsServiceGroupMemberName": nsServiceGroupMemberName,
       "nsServiceGroupMemberVsys": nsServiceGroupMemberVsys}
)
