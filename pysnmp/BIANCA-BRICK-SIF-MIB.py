# SNMP MIB module (BIANCA-BRICK-SIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-SIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:46 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpSifAliasAddressTable_Object = MibTable
ipSifAliasAddressTable = _IpSifAliasAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28)
)
if mibBuilder.loadTexts:
    ipSifAliasAddressTable.setStatus("mandatory")
_IpSifAliasAddressEntry_Object = MibTableRow
ipSifAliasAddressEntry = _IpSifAliasAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1)
)
ipSifAliasAddressEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifAliasAddressAlias"),
)
if mibBuilder.loadTexts:
    ipSifAliasAddressEntry.setStatus("mandatory")


class _IpSifAliasAddressIndex_Type(Integer32):
    """Custom type ipSifAliasAddressIndex based on Integer32"""
    defaultValue = 0


_IpSifAliasAddressIndex_Object = MibTableColumn
ipSifAliasAddressIndex = _IpSifAliasAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 1),
    _IpSifAliasAddressIndex_Type()
)
ipSifAliasAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifAliasAddressIndex.setStatus("mandatory")
_IpSifAliasAddressAlias_Type = DisplayString
_IpSifAliasAddressAlias_Object = MibTableColumn
ipSifAliasAddressAlias = _IpSifAliasAddressAlias_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 2),
    _IpSifAliasAddressAlias_Type()
)
ipSifAliasAddressAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressAlias.setStatus("mandatory")
_IpSifAliasAddressAddress_Type = IpAddress
_IpSifAliasAddressAddress_Object = MibTableColumn
ipSifAliasAddressAddress = _IpSifAliasAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 3),
    _IpSifAliasAddressAddress_Type()
)
ipSifAliasAddressAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressAddress.setStatus("mandatory")
_IpSifAliasAddressMask_Type = IpAddress
_IpSifAliasAddressMask_Object = MibTableColumn
ipSifAliasAddressMask = _IpSifAliasAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 4),
    _IpSifAliasAddressMask_Type()
)
ipSifAliasAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressMask.setStatus("mandatory")


class _IpSifAliasAddressInterface_Type(Integer32):
    """Custom type ipSifAliasAddressInterface based on Integer32"""
    defaultValue = 0


_IpSifAliasAddressInterface_Object = MibTableColumn
ipSifAliasAddressInterface = _IpSifAliasAddressInterface_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 5),
    _IpSifAliasAddressInterface_Type()
)
ipSifAliasAddressInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressInterface.setStatus("mandatory")


class _IpSifAliasAddressMode_Type(Integer32):
    """Custom type ipSifAliasAddressMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("address", 2),
          ("delete", 4),
          ("interface", 1),
          ("range", 3))
    )


_IpSifAliasAddressMode_Type.__name__ = "Integer32"
_IpSifAliasAddressMode_Object = MibTableColumn
ipSifAliasAddressMode = _IpSifAliasAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 6),
    _IpSifAliasAddressMode_Type()
)
ipSifAliasAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressMode.setStatus("mandatory")


class _IpSifAliasAddressRange_Type(Integer32):
    """Custom type ipSifAliasAddressRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSifAliasAddressRange_Type.__name__ = "Integer32"
_IpSifAliasAddressRange_Object = MibTableColumn
ipSifAliasAddressRange = _IpSifAliasAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 7),
    _IpSifAliasAddressRange_Type()
)
ipSifAliasAddressRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressRange.setStatus("mandatory")
_IpSifAliasAddressGroup_Type = Integer32
_IpSifAliasAddressGroup_Object = MibTableColumn
ipSifAliasAddressGroup = _IpSifAliasAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 28, 1, 8),
    _IpSifAliasAddressGroup_Type()
)
ipSifAliasAddressGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressGroup.setStatus("mandatory")
_IpSifAliasServiceTable_Object = MibTable
ipSifAliasServiceTable = _IpSifAliasServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29)
)
if mibBuilder.loadTexts:
    ipSifAliasServiceTable.setStatus("mandatory")
_IpSifAliasServiceEntry_Object = MibTableRow
ipSifAliasServiceEntry = _IpSifAliasServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1)
)
ipSifAliasServiceEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifAliasServiceAlias"),
)
if mibBuilder.loadTexts:
    ipSifAliasServiceEntry.setStatus("mandatory")


class _IpSifAliasServiceIndex_Type(Integer32):
    """Custom type ipSifAliasServiceIndex based on Integer32"""
    defaultValue = 0


_IpSifAliasServiceIndex_Object = MibTableColumn
ipSifAliasServiceIndex = _IpSifAliasServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 1),
    _IpSifAliasServiceIndex_Type()
)
ipSifAliasServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifAliasServiceIndex.setStatus("mandatory")
_IpSifAliasServiceAlias_Type = DisplayString
_IpSifAliasServiceAlias_Object = MibTableColumn
ipSifAliasServiceAlias = _IpSifAliasServiceAlias_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 2),
    _IpSifAliasServiceAlias_Type()
)
ipSifAliasServiceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceAlias.setStatus("mandatory")


class _IpSifAliasServiceProtocol_Type(Integer32):
    """Custom type ipSifAliasServiceProtocol based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9,
              12,
              16,
              17,
              20,
              22,
              27,
              41,
              46,
              47,
              50,
              51,
              56,
              57,
              65,
              80,
              88,
              89,
              94,
              103,
              111,
              112,
              115,
              250,
              251,
              252,
              253,
              254,
              255,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("any", 254),
          ("chaos", 16),
          ("delete", 255),
          ("dont-verify", 256),
          ("egp", 8),
          ("esp", 50),
          ("ggp", 3),
          ("gre", 47),
          ("hmp", 20),
          ("icmp", 1),
          ("igmp", 2),
          ("igp", 9),
          ("igrp", 88),
          ("internet", 251),
          ("ip", 4),
          ("ipip", 94),
          ("ipv6", 41),
          ("ipx-in-ip", 111),
          ("iso-ip", 80),
          ("kryptolan", 65),
          ("l2tp", 115),
          ("local", 250),
          ("netmeeting", 252),
          ("ospf", 89),
          ("pim", 103),
          ("pup", 12),
          ("rdp", 27),
          ("rsvp", 46),
          ("skip", 57),
          ("tcp", 6),
          ("tlsp", 56),
          ("udp", 17),
          ("udptcp", 253),
          ("vrrp", 112),
          ("xns-idp", 22))
    )


_IpSifAliasServiceProtocol_Type.__name__ = "Integer32"
_IpSifAliasServiceProtocol_Object = MibTableColumn
ipSifAliasServiceProtocol = _IpSifAliasServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 3),
    _IpSifAliasServiceProtocol_Type()
)
ipSifAliasServiceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceProtocol.setStatus("mandatory")


class _IpSifAliasServicePort_Type(Integer32):
    """Custom type ipSifAliasServicePort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpSifAliasServicePort_Type.__name__ = "Integer32"
_IpSifAliasServicePort_Object = MibTableColumn
ipSifAliasServicePort = _IpSifAliasServicePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 4),
    _IpSifAliasServicePort_Type()
)
ipSifAliasServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServicePort.setStatus("mandatory")


class _IpSifAliasServiceRange_Type(Integer32):
    """Custom type ipSifAliasServiceRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_IpSifAliasServiceRange_Type.__name__ = "Integer32"
_IpSifAliasServiceRange_Object = MibTableColumn
ipSifAliasServiceRange = _IpSifAliasServiceRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 5),
    _IpSifAliasServiceRange_Type()
)
ipSifAliasServiceRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceRange.setStatus("mandatory")


class _IpSifAliasServiceType_Type(Integer32):
    """Custom type ipSifAliasServiceType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("predefined", 1))
    )


_IpSifAliasServiceType_Type.__name__ = "Integer32"
_IpSifAliasServiceType_Object = MibTableColumn
ipSifAliasServiceType = _IpSifAliasServiceType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 6),
    _IpSifAliasServiceType_Type()
)
ipSifAliasServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifAliasServiceType.setStatus("mandatory")
_IpSifAliasServiceGroup_Type = Integer32
_IpSifAliasServiceGroup_Object = MibTableColumn
ipSifAliasServiceGroup = _IpSifAliasServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 7),
    _IpSifAliasServiceGroup_Type()
)
ipSifAliasServiceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceGroup.setStatus("mandatory")


class _IpSifAliasServiceSourcePort_Type(Integer32):
    """Custom type ipSifAliasServiceSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpSifAliasServiceSourcePort_Type.__name__ = "Integer32"
_IpSifAliasServiceSourcePort_Object = MibTableColumn
ipSifAliasServiceSourcePort = _IpSifAliasServiceSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 8),
    _IpSifAliasServiceSourcePort_Type()
)
ipSifAliasServiceSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceSourcePort.setStatus("mandatory")


class _IpSifAliasServiceSourceRange_Type(Integer32):
    """Custom type ipSifAliasServiceSourceRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_IpSifAliasServiceSourceRange_Type.__name__ = "Integer32"
_IpSifAliasServiceSourceRange_Object = MibTableColumn
ipSifAliasServiceSourceRange = _IpSifAliasServiceSourceRange_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 9),
    _IpSifAliasServiceSourceRange_Type()
)
ipSifAliasServiceSourceRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceSourceRange.setStatus("mandatory")


class _IpSifAliasServiceIcmpType_Type(Integer32):
    """Custom type ipSifAliasServiceIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_IpSifAliasServiceIcmpType_Type.__name__ = "Integer32"
_IpSifAliasServiceIcmpType_Object = MibTableColumn
ipSifAliasServiceIcmpType = _IpSifAliasServiceIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 10),
    _IpSifAliasServiceIcmpType_Type()
)
ipSifAliasServiceIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceIcmpType.setStatus("mandatory")


class _IpSifAliasServiceIcmpCode_Type(Integer32):
    """Custom type ipSifAliasServiceIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_IpSifAliasServiceIcmpCode_Type.__name__ = "Integer32"
_IpSifAliasServiceIcmpCode_Object = MibTableColumn
ipSifAliasServiceIcmpCode = _IpSifAliasServiceIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 29, 1, 11),
    _IpSifAliasServiceIcmpCode_Type()
)
ipSifAliasServiceIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceIcmpCode.setStatus("mandatory")
_IpSifAliasTable_Object = MibTable
ipSifAliasTable = _IpSifAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30)
)
if mibBuilder.loadTexts:
    ipSifAliasTable.setStatus("mandatory")
_IpSifAliasEntry_Object = MibTableRow
ipSifAliasEntry = _IpSifAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1)
)
ipSifAliasEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifAliasOrder"),
)
if mibBuilder.loadTexts:
    ipSifAliasEntry.setStatus("mandatory")
_IpSifAliasOrder_Type = Integer32
_IpSifAliasOrder_Object = MibTableColumn
ipSifAliasOrder = _IpSifAliasOrder_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 1),
    _IpSifAliasOrder_Type()
)
ipSifAliasOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasOrder.setStatus("mandatory")
_IpSifAliasSource_Type = Integer32
_IpSifAliasSource_Object = MibTableColumn
ipSifAliasSource = _IpSifAliasSource_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 2),
    _IpSifAliasSource_Type()
)
ipSifAliasSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasSource.setStatus("mandatory")
_IpSifAliasDestination_Type = Integer32
_IpSifAliasDestination_Object = MibTableColumn
ipSifAliasDestination = _IpSifAliasDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 3),
    _IpSifAliasDestination_Type()
)
ipSifAliasDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasDestination.setStatus("mandatory")
_IpSifAliasService_Type = Integer32
_IpSifAliasService_Object = MibTableColumn
ipSifAliasService = _IpSifAliasService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 4),
    _IpSifAliasService_Type()
)
ipSifAliasService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasService.setStatus("mandatory")


class _IpSifAliasAction_Type(Integer32):
    """Custom type ipSifAliasAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("delete", 255),
          ("deny", 2),
          ("reject", 3))
    )


_IpSifAliasAction_Type.__name__ = "Integer32"
_IpSifAliasAction_Object = MibTableColumn
ipSifAliasAction = _IpSifAliasAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 5),
    _IpSifAliasAction_Type()
)
ipSifAliasAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAction.setStatus("mandatory")


class _IpSifAliasStatus_Type(Integer32):
    """Custom type ipSifAliasStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpSifAliasStatus_Type.__name__ = "Integer32"
_IpSifAliasStatus_Object = MibTableColumn
ipSifAliasStatus = _IpSifAliasStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 6),
    _IpSifAliasStatus_Type()
)
ipSifAliasStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasStatus.setStatus("mandatory")


class _IpSifAliasPriority_Type(Integer32):
    """Custom type ipSifAliasPriority based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("high", 3),
          ("low", 5),
          ("low-latency", 2),
          ("medium", 4))
    )


_IpSifAliasPriority_Type.__name__ = "Integer32"
_IpSifAliasPriority_Object = MibTableColumn
ipSifAliasPriority = _IpSifAliasPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 7),
    _IpSifAliasPriority_Type()
)
ipSifAliasPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasPriority.setStatus("mandatory")


class _IpSifAliasClassId_Type(Integer32):
    """Custom type ipSifAliasClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpSifAliasClassId_Type.__name__ = "Integer32"
_IpSifAliasClassId_Object = MibTableColumn
ipSifAliasClassId = _IpSifAliasClassId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 30, 1, 8),
    _IpSifAliasClassId_Type()
)
ipSifAliasClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasClassId.setStatus("mandatory")
_IpSifRejectTable_Object = MibTable
ipSifRejectTable = _IpSifRejectTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31)
)
if mibBuilder.loadTexts:
    ipSifRejectTable.setStatus("mandatory")
_IpSifRejectEntry_Object = MibTableRow
ipSifRejectEntry = _IpSifRejectEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1)
)
ipSifRejectEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifRejectIndex"),
)
if mibBuilder.loadTexts:
    ipSifRejectEntry.setStatus("mandatory")
_IpSifRejectIndex_Type = Integer32
_IpSifRejectIndex_Object = MibTableColumn
ipSifRejectIndex = _IpSifRejectIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 1),
    _IpSifRejectIndex_Type()
)
ipSifRejectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectIndex.setStatus("mandatory")
_IpSifRejectSource_Type = IpAddress
_IpSifRejectSource_Object = MibTableColumn
ipSifRejectSource = _IpSifRejectSource_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 2),
    _IpSifRejectSource_Type()
)
ipSifRejectSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectSource.setStatus("mandatory")
_IpSifRejectDestination_Type = IpAddress
_IpSifRejectDestination_Object = MibTableColumn
ipSifRejectDestination = _IpSifRejectDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 3),
    _IpSifRejectDestination_Type()
)
ipSifRejectDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectDestination.setStatus("mandatory")
_IpSifRejectRejects_Type = Integer32
_IpSifRejectRejects_Object = MibTableColumn
ipSifRejectRejects = _IpSifRejectRejects_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 4),
    _IpSifRejectRejects_Type()
)
ipSifRejectRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectRejects.setStatus("mandatory")
_IpSifRejectSilence_Type = Integer32
_IpSifRejectSilence_Object = MibTableColumn
ipSifRejectSilence = _IpSifRejectSilence_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 5),
    _IpSifRejectSilence_Type()
)
ipSifRejectSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectSilence.setStatus("mandatory")


class _IpSifRejectProtocol_Type(Integer32):
    """Custom type ipSifRejectProtocol based on Integer32"""
    defaultValue = 0


_IpSifRejectProtocol_Object = MibTableColumn
ipSifRejectProtocol = _IpSifRejectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 6),
    _IpSifRejectProtocol_Type()
)
ipSifRejectProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectProtocol.setStatus("mandatory")


class _IpSifRejectPortLo_Type(Integer32):
    """Custom type ipSifRejectPortLo based on Integer32"""
    defaultValue = 0


_IpSifRejectPortLo_Object = MibTableColumn
ipSifRejectPortLo = _IpSifRejectPortLo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 7),
    _IpSifRejectPortLo_Type()
)
ipSifRejectPortLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectPortLo.setStatus("mandatory")


class _IpSifRejectPortHigh_Type(Integer32):
    """Custom type ipSifRejectPortHigh based on Integer32"""
    defaultValue = 0


_IpSifRejectPortHigh_Object = MibTableColumn
ipSifRejectPortHigh = _IpSifRejectPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 31, 1, 8),
    _IpSifRejectPortHigh_Type()
)
ipSifRejectPortHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifRejectPortHigh.setStatus("mandatory")
_IpSifExpectTable_Object = MibTable
ipSifExpectTable = _IpSifExpectTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35)
)
if mibBuilder.loadTexts:
    ipSifExpectTable.setStatus("mandatory")
_IpSifExpectEntry_Object = MibTableRow
ipSifExpectEntry = _IpSifExpectEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1)
)
ipSifExpectEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifExpectIndex"),
)
if mibBuilder.loadTexts:
    ipSifExpectEntry.setStatus("mandatory")
_IpSifExpectIndex_Type = Integer32
_IpSifExpectIndex_Object = MibTableColumn
ipSifExpectIndex = _IpSifExpectIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 1),
    _IpSifExpectIndex_Type()
)
ipSifExpectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectIndex.setStatus("mandatory")
_IpSifExpectSource_Type = IpAddress
_IpSifExpectSource_Object = MibTableColumn
ipSifExpectSource = _IpSifExpectSource_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 2),
    _IpSifExpectSource_Type()
)
ipSifExpectSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectSource.setStatus("mandatory")
_IpSifExpectDestination_Type = IpAddress
_IpSifExpectDestination_Object = MibTableColumn
ipSifExpectDestination = _IpSifExpectDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 3),
    _IpSifExpectDestination_Type()
)
ipSifExpectDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectDestination.setStatus("mandatory")


class _IpSifExpectProtocol_Type(Integer32):
    """Custom type ipSifExpectProtocol based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("delete", 255),
          ("igmp", 2),
          ("ip", 4),
          ("tcp", 6),
          ("udp", 17))
    )


_IpSifExpectProtocol_Type.__name__ = "Integer32"
_IpSifExpectProtocol_Object = MibTableColumn
ipSifExpectProtocol = _IpSifExpectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 4),
    _IpSifExpectProtocol_Type()
)
ipSifExpectProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifExpectProtocol.setStatus("mandatory")


class _IpSifExpectSourcePort_Type(Integer32):
    """Custom type ipSifExpectSourcePort based on Integer32"""
    defaultValue = 0


_IpSifExpectSourcePort_Object = MibTableColumn
ipSifExpectSourcePort = _IpSifExpectSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 5),
    _IpSifExpectSourcePort_Type()
)
ipSifExpectSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectSourcePort.setStatus("mandatory")


class _IpSifExpectDestPort_Type(Integer32):
    """Custom type ipSifExpectDestPort based on Integer32"""
    defaultValue = 0


_IpSifExpectDestPort_Object = MibTableColumn
ipSifExpectDestPort = _IpSifExpectDestPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 6),
    _IpSifExpectDestPort_Type()
)
ipSifExpectDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectDestPort.setStatus("mandatory")


class _IpSifExpectPriority_Type(Integer32):
    """Custom type ipSifExpectPriority based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("high", 3),
          ("low", 5),
          ("low-latency", 2),
          ("medium", 4))
    )


_IpSifExpectPriority_Type.__name__ = "Integer32"
_IpSifExpectPriority_Object = MibTableColumn
ipSifExpectPriority = _IpSifExpectPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 7),
    _IpSifExpectPriority_Type()
)
ipSifExpectPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectPriority.setStatus("mandatory")


class _IpSifExpectClassId_Type(Integer32):
    """Custom type ipSifExpectClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpSifExpectClassId_Type.__name__ = "Integer32"
_IpSifExpectClassId_Object = MibTableColumn
ipSifExpectClassId = _IpSifExpectClassId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 8),
    _IpSifExpectClassId_Type()
)
ipSifExpectClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectClassId.setStatus("mandatory")


class _IpSifExpectIfIndex_Type(Integer32):
    """Custom type ipSifExpectIfIndex based on Integer32"""
    defaultValue = 0


_IpSifExpectIfIndex_Object = MibTableColumn
ipSifExpectIfIndex = _IpSifExpectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 35, 1, 9),
    _IpSifExpectIfIndex_Type()
)
ipSifExpectIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifExpectIfIndex.setStatus("mandatory")
_IpSif_ObjectIdentity = ObjectIdentity
ipSif = _IpSif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37)
)


class _IpSifAdminStatus_Type(Integer32):
    """Custom type ipSifAdminStatus based on Integer32"""
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


_IpSifAdminStatus_Type.__name__ = "Integer32"
_IpSifAdminStatus_Object = MibScalar
ipSifAdminStatus = _IpSifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 1),
    _IpSifAdminStatus_Type()
)
ipSifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAdminStatus.setStatus("mandatory")


class _IpSifLocalFilter_Type(Integer32):
    """Custom type ipSifLocalFilter based on Integer32"""
    defaultValue = 2

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


_IpSifLocalFilter_Type.__name__ = "Integer32"
_IpSifLocalFilter_Object = MibScalar
ipSifLocalFilter = _IpSifLocalFilter_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 2),
    _IpSifLocalFilter_Type()
)
ipSifLocalFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifLocalFilter.setStatus("mandatory")


class _IpSifInterfaceFilter_Type(Integer32):
    """Custom type ipSifInterfaceFilter based on Integer32"""
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


_IpSifInterfaceFilter_Type.__name__ = "Integer32"
_IpSifInterfaceFilter_Object = MibScalar
ipSifInterfaceFilter = _IpSifInterfaceFilter_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 3),
    _IpSifInterfaceFilter_Type()
)
ipSifInterfaceFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifInterfaceFilter.setStatus("mandatory")


class _IpSifSysloglevel_Type(Integer32):
    """Custom type ipSifSysloglevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("deny", 1),
          ("none", 4),
          ("verbose", 3))
    )


_IpSifSysloglevel_Type.__name__ = "Integer32"
_IpSifSysloglevel_Object = MibScalar
ipSifSysloglevel = _IpSifSysloglevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 4),
    _IpSifSysloglevel_Type()
)
ipSifSysloglevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifSysloglevel.setStatus("mandatory")


class _IpSifUdpTimeout_Type(Integer32):
    """Custom type ipSifUdpTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_IpSifUdpTimeout_Type.__name__ = "Integer32"
_IpSifUdpTimeout_Object = MibScalar
ipSifUdpTimeout = _IpSifUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 5),
    _IpSifUdpTimeout_Type()
)
ipSifUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifUdpTimeout.setStatus("mandatory")


class _IpSifTcpTimeout_Type(Integer32):
    """Custom type ipSifTcpTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_IpSifTcpTimeout_Type.__name__ = "Integer32"
_IpSifTcpTimeout_Object = MibScalar
ipSifTcpTimeout = _IpSifTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 6),
    _IpSifTcpTimeout_Type()
)
ipSifTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifTcpTimeout.setStatus("mandatory")


class _IpSifPPTPTimeout_Type(Integer32):
    """Custom type ipSifPPTPTimeout based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_IpSifPPTPTimeout_Type.__name__ = "Integer32"
_IpSifPPTPTimeout_Object = MibScalar
ipSifPPTPTimeout = _IpSifPPTPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 7),
    _IpSifPPTPTimeout_Type()
)
ipSifPPTPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPPTPTimeout.setStatus("mandatory")


class _IpSifDefaultTimeout_Type(Integer32):
    """Custom type ipSifDefaultTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_IpSifDefaultTimeout_Type.__name__ = "Integer32"
_IpSifDefaultTimeout_Object = MibScalar
ipSifDefaultTimeout = _IpSifDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 8),
    _IpSifDefaultTimeout_Type()
)
ipSifDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifDefaultTimeout.setStatus("mandatory")


class _IpSifMaxSessions_Type(Integer32):
    """Custom type ipSifMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_IpSifMaxSessions_Type.__name__ = "Integer32"
_IpSifMaxSessions_Object = MibScalar
ipSifMaxSessions = _IpSifMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 9),
    _IpSifMaxSessions_Type()
)
ipSifMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifMaxSessions.setStatus("mandatory")


class _IpSifMaxRejectEntries_Type(Integer32):
    """Custom type ipSifMaxRejectEntries based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IpSifMaxRejectEntries_Type.__name__ = "Integer32"
_IpSifMaxRejectEntries_Object = MibScalar
ipSifMaxRejectEntries = _IpSifMaxRejectEntries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 14),
    _IpSifMaxRejectEntries_Type()
)
ipSifMaxRejectEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifMaxRejectEntries.setStatus("mandatory")


class _IpSifMaxRejectTtl_Type(Integer32):
    """Custom type ipSifMaxRejectTtl based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_IpSifMaxRejectTtl_Type.__name__ = "Integer32"
_IpSifMaxRejectTtl_Object = MibScalar
ipSifMaxRejectTtl = _IpSifMaxRejectTtl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 15),
    _IpSifMaxRejectTtl_Type()
)
ipSifMaxRejectTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifMaxRejectTtl.setStatus("mandatory")


class _IpSifInterfaceAliasAutoCreate_Type(Integer32):
    """Custom type ipSifInterfaceAliasAutoCreate based on Integer32"""
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


_IpSifInterfaceAliasAutoCreate_Type.__name__ = "Integer32"
_IpSifInterfaceAliasAutoCreate_Object = MibScalar
ipSifInterfaceAliasAutoCreate = _IpSifInterfaceAliasAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 37, 16),
    _IpSifInterfaceAliasAutoCreate_Type()
)
ipSifInterfaceAliasAutoCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifInterfaceAliasAutoCreate.setStatus("mandatory")
_IpSifStat_ObjectIdentity = ObjectIdentity
ipSifStat = _IpSifStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46)
)
_IpSifStatCurrSessions_Type = Counter32
_IpSifStatCurrSessions_Object = MibScalar
ipSifStatCurrSessions = _IpSifStatCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 1),
    _IpSifStatCurrSessions_Type()
)
ipSifStatCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatCurrSessions.setStatus("mandatory")
_IpSifStatCurrUdpSessions_Type = Counter32
_IpSifStatCurrUdpSessions_Object = MibScalar
ipSifStatCurrUdpSessions = _IpSifStatCurrUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 2),
    _IpSifStatCurrUdpSessions_Type()
)
ipSifStatCurrUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatCurrUdpSessions.setStatus("mandatory")
_IpSifStatCurrTcpSessions_Type = Counter32
_IpSifStatCurrTcpSessions_Object = MibScalar
ipSifStatCurrTcpSessions = _IpSifStatCurrTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 3),
    _IpSifStatCurrTcpSessions_Type()
)
ipSifStatCurrTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatCurrTcpSessions.setStatus("mandatory")
_IpSifStatCurrOtherSessions_Type = Counter32
_IpSifStatCurrOtherSessions_Object = MibScalar
ipSifStatCurrOtherSessions = _IpSifStatCurrOtherSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 4),
    _IpSifStatCurrOtherSessions_Type()
)
ipSifStatCurrOtherSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatCurrOtherSessions.setStatus("mandatory")
_IpSifStatCurrExpectedSessions_Type = Counter32
_IpSifStatCurrExpectedSessions_Object = MibScalar
ipSifStatCurrExpectedSessions = _IpSifStatCurrExpectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 5),
    _IpSifStatCurrExpectedSessions_Type()
)
ipSifStatCurrExpectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatCurrExpectedSessions.setStatus("mandatory")
_IpSifStatTotalUdpSessions_Type = Counter32
_IpSifStatTotalUdpSessions_Object = MibScalar
ipSifStatTotalUdpSessions = _IpSifStatTotalUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 6),
    _IpSifStatTotalUdpSessions_Type()
)
ipSifStatTotalUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatTotalUdpSessions.setStatus("mandatory")
_IpSifStatTotalTcpSessions_Type = Counter32
_IpSifStatTotalTcpSessions_Object = MibScalar
ipSifStatTotalTcpSessions = _IpSifStatTotalTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 7),
    _IpSifStatTotalTcpSessions_Type()
)
ipSifStatTotalTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatTotalTcpSessions.setStatus("mandatory")
_IpSifStatTotalOtherSessions_Type = Counter32
_IpSifStatTotalOtherSessions_Object = MibScalar
ipSifStatTotalOtherSessions = _IpSifStatTotalOtherSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 8),
    _IpSifStatTotalOtherSessions_Type()
)
ipSifStatTotalOtherSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatTotalOtherSessions.setStatus("mandatory")
_IpSifStatTotalExpectedSessions_Type = Counter32
_IpSifStatTotalExpectedSessions_Object = MibScalar
ipSifStatTotalExpectedSessions = _IpSifStatTotalExpectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 46, 9),
    _IpSifStatTotalExpectedSessions_Type()
)
ipSifStatTotalExpectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifStatTotalExpectedSessions.setStatus("mandatory")
_IpSifAliasAddressGroupTable_Object = MibTable
ipSifAliasAddressGroupTable = _IpSifAliasAddressGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47)
)
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupTable.setStatus("mandatory")
_IpSifAliasAddressGroupEntry_Object = MibTableRow
ipSifAliasAddressGroupEntry = _IpSifAliasAddressGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47, 1)
)
ipSifAliasAddressGroupEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifAliasAddressGroupId"),
)
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupEntry.setStatus("mandatory")
_IpSifAliasAddressGroupId_Type = Integer32
_IpSifAliasAddressGroupId_Object = MibTableColumn
ipSifAliasAddressGroupId = _IpSifAliasAddressGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47, 1, 1),
    _IpSifAliasAddressGroupId_Type()
)
ipSifAliasAddressGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupId.setStatus("mandatory")
_IpSifAliasAddressGroupAlias_Type = DisplayString
_IpSifAliasAddressGroupAlias_Object = MibTableColumn
ipSifAliasAddressGroupAlias = _IpSifAliasAddressGroupAlias_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47, 1, 2),
    _IpSifAliasAddressGroupAlias_Type()
)
ipSifAliasAddressGroupAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupAlias.setStatus("mandatory")
_IpSifAliasAddressGroupIndex_Type = Integer32
_IpSifAliasAddressGroupIndex_Object = MibTableColumn
ipSifAliasAddressGroupIndex = _IpSifAliasAddressGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47, 1, 3),
    _IpSifAliasAddressGroupIndex_Type()
)
ipSifAliasAddressGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupIndex.setStatus("mandatory")


class _IpSifAliasAddressGroupMode_Type(Integer32):
    """Custom type ipSifAliasAddressGroupMode based on Integer32"""
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
        *(("address", 2),
          ("delete", 3),
          ("interface", 1))
    )


_IpSifAliasAddressGroupMode_Type.__name__ = "Integer32"
_IpSifAliasAddressGroupMode_Object = MibTableColumn
ipSifAliasAddressGroupMode = _IpSifAliasAddressGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 47, 1, 4),
    _IpSifAliasAddressGroupMode_Type()
)
ipSifAliasAddressGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasAddressGroupMode.setStatus("mandatory")
_IpSifAliasServiceGroupTable_Object = MibTable
ipSifAliasServiceGroupTable = _IpSifAliasServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48)
)
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupTable.setStatus("mandatory")
_IpSifAliasServiceGroupEntry_Object = MibTableRow
ipSifAliasServiceGroupEntry = _IpSifAliasServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48, 1)
)
ipSifAliasServiceGroupEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifAliasServiceGroupId"),
)
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupEntry.setStatus("mandatory")
_IpSifAliasServiceGroupId_Type = Integer32
_IpSifAliasServiceGroupId_Object = MibTableColumn
ipSifAliasServiceGroupId = _IpSifAliasServiceGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48, 1, 1),
    _IpSifAliasServiceGroupId_Type()
)
ipSifAliasServiceGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupId.setStatus("mandatory")
_IpSifAliasServiceGroupAlias_Type = DisplayString
_IpSifAliasServiceGroupAlias_Object = MibTableColumn
ipSifAliasServiceGroupAlias = _IpSifAliasServiceGroupAlias_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48, 1, 2),
    _IpSifAliasServiceGroupAlias_Type()
)
ipSifAliasServiceGroupAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupAlias.setStatus("mandatory")
_IpSifAliasServiceGroupIndex_Type = Integer32
_IpSifAliasServiceGroupIndex_Object = MibTableColumn
ipSifAliasServiceGroupIndex = _IpSifAliasServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48, 1, 3),
    _IpSifAliasServiceGroupIndex_Type()
)
ipSifAliasServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupIndex.setStatus("mandatory")


class _IpSifAliasServiceGroupMode_Type(Integer32):
    """Custom type ipSifAliasServiceGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("service", 1))
    )


_IpSifAliasServiceGroupMode_Type.__name__ = "Integer32"
_IpSifAliasServiceGroupMode_Object = MibTableColumn
ipSifAliasServiceGroupMode = _IpSifAliasServiceGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 48, 1, 4),
    _IpSifAliasServiceGroupMode_Type()
)
ipSifAliasServiceGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifAliasServiceGroupMode.setStatus("mandatory")
_IpSifPolicyChkTable_Object = MibTable
ipSifPolicyChkTable = _IpSifPolicyChkTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49)
)
if mibBuilder.loadTexts:
    ipSifPolicyChkTable.setStatus("mandatory")
_IpSifPolicyChkEntry_Object = MibTableRow
ipSifPolicyChkEntry = _IpSifPolicyChkEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1)
)
ipSifPolicyChkEntry.setIndexNames(
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifPolicyChkProtocol"),
    (0, "BIANCA-BRICK-SIF-MIB", "ipSifPolicyChkDestPort"),
)
if mibBuilder.loadTexts:
    ipSifPolicyChkEntry.setStatus("mandatory")
_IpSifPolicyChkSourceIfIndex_Type = Integer32
_IpSifPolicyChkSourceIfIndex_Object = MibTableColumn
ipSifPolicyChkSourceIfIndex = _IpSifPolicyChkSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 1),
    _IpSifPolicyChkSourceIfIndex_Type()
)
ipSifPolicyChkSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkSourceIfIndex.setStatus("mandatory")
_IpSifPolicyChkDestIfIndex_Type = Integer32
_IpSifPolicyChkDestIfIndex_Object = MibTableColumn
ipSifPolicyChkDestIfIndex = _IpSifPolicyChkDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 2),
    _IpSifPolicyChkDestIfIndex_Type()
)
ipSifPolicyChkDestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkDestIfIndex.setStatus("mandatory")
_IpSifPolicyChkSource_Type = IpAddress
_IpSifPolicyChkSource_Object = MibTableColumn
ipSifPolicyChkSource = _IpSifPolicyChkSource_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 3),
    _IpSifPolicyChkSource_Type()
)
ipSifPolicyChkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkSource.setStatus("mandatory")
_IpSifPolicyChkDestination_Type = IpAddress
_IpSifPolicyChkDestination_Object = MibTableColumn
ipSifPolicyChkDestination = _IpSifPolicyChkDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 4),
    _IpSifPolicyChkDestination_Type()
)
ipSifPolicyChkDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkDestination.setStatus("mandatory")
_IpSifPolicyChkProtocol_Type = Integer32
_IpSifPolicyChkProtocol_Object = MibTableColumn
ipSifPolicyChkProtocol = _IpSifPolicyChkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 5),
    _IpSifPolicyChkProtocol_Type()
)
ipSifPolicyChkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkProtocol.setStatus("mandatory")
_IpSifPolicyChkDestPort_Type = Integer32
_IpSifPolicyChkDestPort_Object = MibTableColumn
ipSifPolicyChkDestPort = _IpSifPolicyChkDestPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 6),
    _IpSifPolicyChkDestPort_Type()
)
ipSifPolicyChkDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkDestPort.setStatus("mandatory")


class _IpSifPolicyChkRule_Type(Integer32):
    """Custom type ipSifPolicyChkRule based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("deny", 2),
          ("reject", 3),
          ("unknown", 4))
    )


_IpSifPolicyChkRule_Type.__name__ = "Integer32"
_IpSifPolicyChkRule_Object = MibTableColumn
ipSifPolicyChkRule = _IpSifPolicyChkRule_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 7),
    _IpSifPolicyChkRule_Type()
)
ipSifPolicyChkRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifPolicyChkRule.setStatus("mandatory")
_IpSifPolicyChkRuleOrder_Type = Integer32
_IpSifPolicyChkRuleOrder_Object = MibTableColumn
ipSifPolicyChkRuleOrder = _IpSifPolicyChkRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 8),
    _IpSifPolicyChkRuleOrder_Type()
)
ipSifPolicyChkRuleOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifPolicyChkRuleOrder.setStatus("mandatory")


class _IpSifPolicyChkResult_Type(Integer32):
    """Custom type ipSifPolicyChkResult based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("deny", 2),
          ("unknown", 3))
    )


_IpSifPolicyChkResult_Type.__name__ = "Integer32"
_IpSifPolicyChkResult_Object = MibTableColumn
ipSifPolicyChkResult = _IpSifPolicyChkResult_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 9),
    _IpSifPolicyChkResult_Type()
)
ipSifPolicyChkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifPolicyChkResult.setStatus("mandatory")


class _IpSifPolicyChkState_Type(Integer32):
    """Custom type ipSifPolicyChkState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("done", 4),
          ("initial", 1),
          ("running", 3),
          ("trigger", 2))
    )


_IpSifPolicyChkState_Type.__name__ = "Integer32"
_IpSifPolicyChkState_Object = MibTableColumn
ipSifPolicyChkState = _IpSifPolicyChkState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 10),
    _IpSifPolicyChkState_Type()
)
ipSifPolicyChkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkState.setStatus("mandatory")


class _IpSifPolicyChkAdminStatus_Type(Integer32):
    """Custom type ipSifPolicyChkAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check", 1),
          ("ignore", 2))
    )


_IpSifPolicyChkAdminStatus_Type.__name__ = "Integer32"
_IpSifPolicyChkAdminStatus_Object = MibTableColumn
ipSifPolicyChkAdminStatus = _IpSifPolicyChkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 11),
    _IpSifPolicyChkAdminStatus_Type()
)
ipSifPolicyChkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkAdminStatus.setStatus("mandatory")


class _IpSifPolicyChkOperStatus_Type(Integer32):
    """Custom type ipSifPolicyChkOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check", 1),
          ("ignore", 2))
    )


_IpSifPolicyChkOperStatus_Type.__name__ = "Integer32"
_IpSifPolicyChkOperStatus_Object = MibTableColumn
ipSifPolicyChkOperStatus = _IpSifPolicyChkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 12),
    _IpSifPolicyChkOperStatus_Type()
)
ipSifPolicyChkOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSifPolicyChkOperStatus.setStatus("mandatory")


class _IpSifPolicyChkCurrOperStatus_Type(Integer32):
    """Custom type ipSifPolicyChkCurrOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IpSifPolicyChkCurrOperStatus_Type.__name__ = "Integer32"
_IpSifPolicyChkCurrOperStatus_Object = MibTableColumn
ipSifPolicyChkCurrOperStatus = _IpSifPolicyChkCurrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 49, 1, 13),
    _IpSifPolicyChkCurrOperStatus_Type()
)
ipSifPolicyChkCurrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSifPolicyChkCurrOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-SIF-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipSifAliasAddressTable": ipSifAliasAddressTable,
       "ipSifAliasAddressEntry": ipSifAliasAddressEntry,
       "ipSifAliasAddressIndex": ipSifAliasAddressIndex,
       "ipSifAliasAddressAlias": ipSifAliasAddressAlias,
       "ipSifAliasAddressAddress": ipSifAliasAddressAddress,
       "ipSifAliasAddressMask": ipSifAliasAddressMask,
       "ipSifAliasAddressInterface": ipSifAliasAddressInterface,
       "ipSifAliasAddressMode": ipSifAliasAddressMode,
       "ipSifAliasAddressRange": ipSifAliasAddressRange,
       "ipSifAliasAddressGroup": ipSifAliasAddressGroup,
       "ipSifAliasServiceTable": ipSifAliasServiceTable,
       "ipSifAliasServiceEntry": ipSifAliasServiceEntry,
       "ipSifAliasServiceIndex": ipSifAliasServiceIndex,
       "ipSifAliasServiceAlias": ipSifAliasServiceAlias,
       "ipSifAliasServiceProtocol": ipSifAliasServiceProtocol,
       "ipSifAliasServicePort": ipSifAliasServicePort,
       "ipSifAliasServiceRange": ipSifAliasServiceRange,
       "ipSifAliasServiceType": ipSifAliasServiceType,
       "ipSifAliasServiceGroup": ipSifAliasServiceGroup,
       "ipSifAliasServiceSourcePort": ipSifAliasServiceSourcePort,
       "ipSifAliasServiceSourceRange": ipSifAliasServiceSourceRange,
       "ipSifAliasServiceIcmpType": ipSifAliasServiceIcmpType,
       "ipSifAliasServiceIcmpCode": ipSifAliasServiceIcmpCode,
       "ipSifAliasTable": ipSifAliasTable,
       "ipSifAliasEntry": ipSifAliasEntry,
       "ipSifAliasOrder": ipSifAliasOrder,
       "ipSifAliasSource": ipSifAliasSource,
       "ipSifAliasDestination": ipSifAliasDestination,
       "ipSifAliasService": ipSifAliasService,
       "ipSifAliasAction": ipSifAliasAction,
       "ipSifAliasStatus": ipSifAliasStatus,
       "ipSifAliasPriority": ipSifAliasPriority,
       "ipSifAliasClassId": ipSifAliasClassId,
       "ipSifRejectTable": ipSifRejectTable,
       "ipSifRejectEntry": ipSifRejectEntry,
       "ipSifRejectIndex": ipSifRejectIndex,
       "ipSifRejectSource": ipSifRejectSource,
       "ipSifRejectDestination": ipSifRejectDestination,
       "ipSifRejectRejects": ipSifRejectRejects,
       "ipSifRejectSilence": ipSifRejectSilence,
       "ipSifRejectProtocol": ipSifRejectProtocol,
       "ipSifRejectPortLo": ipSifRejectPortLo,
       "ipSifRejectPortHigh": ipSifRejectPortHigh,
       "ipSifExpectTable": ipSifExpectTable,
       "ipSifExpectEntry": ipSifExpectEntry,
       "ipSifExpectIndex": ipSifExpectIndex,
       "ipSifExpectSource": ipSifExpectSource,
       "ipSifExpectDestination": ipSifExpectDestination,
       "ipSifExpectProtocol": ipSifExpectProtocol,
       "ipSifExpectSourcePort": ipSifExpectSourcePort,
       "ipSifExpectDestPort": ipSifExpectDestPort,
       "ipSifExpectPriority": ipSifExpectPriority,
       "ipSifExpectClassId": ipSifExpectClassId,
       "ipSifExpectIfIndex": ipSifExpectIfIndex,
       "ipSif": ipSif,
       "ipSifAdminStatus": ipSifAdminStatus,
       "ipSifLocalFilter": ipSifLocalFilter,
       "ipSifInterfaceFilter": ipSifInterfaceFilter,
       "ipSifSysloglevel": ipSifSysloglevel,
       "ipSifUdpTimeout": ipSifUdpTimeout,
       "ipSifTcpTimeout": ipSifTcpTimeout,
       "ipSifPPTPTimeout": ipSifPPTPTimeout,
       "ipSifDefaultTimeout": ipSifDefaultTimeout,
       "ipSifMaxSessions": ipSifMaxSessions,
       "ipSifMaxRejectEntries": ipSifMaxRejectEntries,
       "ipSifMaxRejectTtl": ipSifMaxRejectTtl,
       "ipSifInterfaceAliasAutoCreate": ipSifInterfaceAliasAutoCreate,
       "ipSifStat": ipSifStat,
       "ipSifStatCurrSessions": ipSifStatCurrSessions,
       "ipSifStatCurrUdpSessions": ipSifStatCurrUdpSessions,
       "ipSifStatCurrTcpSessions": ipSifStatCurrTcpSessions,
       "ipSifStatCurrOtherSessions": ipSifStatCurrOtherSessions,
       "ipSifStatCurrExpectedSessions": ipSifStatCurrExpectedSessions,
       "ipSifStatTotalUdpSessions": ipSifStatTotalUdpSessions,
       "ipSifStatTotalTcpSessions": ipSifStatTotalTcpSessions,
       "ipSifStatTotalOtherSessions": ipSifStatTotalOtherSessions,
       "ipSifStatTotalExpectedSessions": ipSifStatTotalExpectedSessions,
       "ipSifAliasAddressGroupTable": ipSifAliasAddressGroupTable,
       "ipSifAliasAddressGroupEntry": ipSifAliasAddressGroupEntry,
       "ipSifAliasAddressGroupId": ipSifAliasAddressGroupId,
       "ipSifAliasAddressGroupAlias": ipSifAliasAddressGroupAlias,
       "ipSifAliasAddressGroupIndex": ipSifAliasAddressGroupIndex,
       "ipSifAliasAddressGroupMode": ipSifAliasAddressGroupMode,
       "ipSifAliasServiceGroupTable": ipSifAliasServiceGroupTable,
       "ipSifAliasServiceGroupEntry": ipSifAliasServiceGroupEntry,
       "ipSifAliasServiceGroupId": ipSifAliasServiceGroupId,
       "ipSifAliasServiceGroupAlias": ipSifAliasServiceGroupAlias,
       "ipSifAliasServiceGroupIndex": ipSifAliasServiceGroupIndex,
       "ipSifAliasServiceGroupMode": ipSifAliasServiceGroupMode,
       "ipSifPolicyChkTable": ipSifPolicyChkTable,
       "ipSifPolicyChkEntry": ipSifPolicyChkEntry,
       "ipSifPolicyChkSourceIfIndex": ipSifPolicyChkSourceIfIndex,
       "ipSifPolicyChkDestIfIndex": ipSifPolicyChkDestIfIndex,
       "ipSifPolicyChkSource": ipSifPolicyChkSource,
       "ipSifPolicyChkDestination": ipSifPolicyChkDestination,
       "ipSifPolicyChkProtocol": ipSifPolicyChkProtocol,
       "ipSifPolicyChkDestPort": ipSifPolicyChkDestPort,
       "ipSifPolicyChkRule": ipSifPolicyChkRule,
       "ipSifPolicyChkRuleOrder": ipSifPolicyChkRuleOrder,
       "ipSifPolicyChkResult": ipSifPolicyChkResult,
       "ipSifPolicyChkState": ipSifPolicyChkState,
       "ipSifPolicyChkAdminStatus": ipSifPolicyChkAdminStatus,
       "ipSifPolicyChkOperStatus": ipSifPolicyChkOperStatus,
       "ipSifPolicyChkCurrOperStatus": ipSifPolicyChkCurrOperStatus}
)
