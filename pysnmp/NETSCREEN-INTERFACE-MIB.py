# SNMP MIB module (NETSCREEN-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:45 2024
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

(netscreenInterface,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenInterface")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netscreenInterfaceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 9, 0)
)
netscreenInterfaceMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2001-09-28 00:00",
         "2001-05-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsIfTable_Object = MibTable
nsIfTable = _NsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1)
)
if mibBuilder.loadTexts:
    nsIfTable.setStatus("current")
_NsIfEntry_Object = MibTableRow
nsIfEntry = _NsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1)
)
nsIfEntry.setIndexNames(
    (0, "NETSCREEN-INTERFACE-MIB", "nsIfIndex"),
)
if mibBuilder.loadTexts:
    nsIfEntry.setStatus("current")


class _NsIfIndex_Type(Integer32):
    """Custom type nsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfIndex_Type.__name__ = "Integer32"
_NsIfIndex_Object = MibTableColumn
nsIfIndex = _NsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 1),
    _NsIfIndex_Type()
)
nsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfIndex.setStatus("current")


class _NsIfName_Type(DisplayString):
    """Custom type nsIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsIfName_Type.__name__ = "DisplayString"
_NsIfName_Object = MibTableColumn
nsIfName = _NsIfName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 2),
    _NsIfName_Type()
)
nsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfName.setStatus("current")
_NsIfVsys_Type = Integer32
_NsIfVsys_Object = MibTableColumn
nsIfVsys = _NsIfVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 3),
    _NsIfVsys_Type()
)
nsIfVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfVsys.setStatus("current")
_NsIfZone_Type = Integer32
_NsIfZone_Object = MibTableColumn
nsIfZone = _NsIfZone_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 4),
    _NsIfZone_Type()
)
nsIfZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfZone.setStatus("current")


class _NsIfStatus_Type(Integer32):
    """Custom type nsIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("inactive", 3),
          ("ready", 2),
          ("up", 1))
    )


_NsIfStatus_Type.__name__ = "Integer32"
_NsIfStatus_Object = MibTableColumn
nsIfStatus = _NsIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 5),
    _NsIfStatus_Type()
)
nsIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfStatus.setStatus("current")
_NsIfIp_Type = IpAddress
_NsIfIp_Object = MibTableColumn
nsIfIp = _NsIfIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 6),
    _NsIfIp_Type()
)
nsIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfIp.setStatus("current")
_NsIfNetmask_Type = IpAddress
_NsIfNetmask_Object = MibTableColumn
nsIfNetmask = _NsIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 7),
    _NsIfNetmask_Type()
)
nsIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfNetmask.setStatus("current")
_NsIfGateway_Type = IpAddress
_NsIfGateway_Object = MibTableColumn
nsIfGateway = _NsIfGateway_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 8),
    _NsIfGateway_Type()
)
nsIfGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfGateway.setStatus("current")
_NsIfMngIp_Type = IpAddress
_NsIfMngIp_Object = MibTableColumn
nsIfMngIp = _NsIfMngIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 9),
    _NsIfMngIp_Type()
)
nsIfMngIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngIp.setStatus("current")


class _NsIfMode_Type(Integer32):
    """Custom type nsIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nat", 1),
          ("not-applicable", 3),
          ("route", 2),
          ("transparent", 0))
    )


_NsIfMode_Type.__name__ = "Integer32"
_NsIfMode_Object = MibTableColumn
nsIfMode = _NsIfMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 10),
    _NsIfMode_Type()
)
nsIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMode.setStatus("current")
_NsIfMAC_Type = PhysAddress
_NsIfMAC_Object = MibTableColumn
nsIfMAC = _NsIfMAC_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 11),
    _NsIfMAC_Type()
)
nsIfMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMAC.setStatus("current")


class _NsIfMngTelnet_Type(Integer32):
    """Custom type nsIfMngTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngTelnet_Type.__name__ = "Integer32"
_NsIfMngTelnet_Object = MibTableColumn
nsIfMngTelnet = _NsIfMngTelnet_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 12),
    _NsIfMngTelnet_Type()
)
nsIfMngTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngTelnet.setStatus("current")


class _NsIfMngSCS_Type(Integer32):
    """Custom type nsIfMngSCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngSCS_Type.__name__ = "Integer32"
_NsIfMngSCS_Object = MibTableColumn
nsIfMngSCS = _NsIfMngSCS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 13),
    _NsIfMngSCS_Type()
)
nsIfMngSCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngSCS.setStatus("current")


class _NsIfMngWEB_Type(Integer32):
    """Custom type nsIfMngWEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngWEB_Type.__name__ = "Integer32"
_NsIfMngWEB_Object = MibTableColumn
nsIfMngWEB = _NsIfMngWEB_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 14),
    _NsIfMngWEB_Type()
)
nsIfMngWEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngWEB.setStatus("current")


class _NsIfMngSSL_Type(Integer32):
    """Custom type nsIfMngSSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngSSL_Type.__name__ = "Integer32"
_NsIfMngSSL_Object = MibTableColumn
nsIfMngSSL = _NsIfMngSSL_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 15),
    _NsIfMngSSL_Type()
)
nsIfMngSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngSSL.setStatus("current")


class _NsIfMngSNMP_Type(Integer32):
    """Custom type nsIfMngSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngSNMP_Type.__name__ = "Integer32"
_NsIfMngSNMP_Object = MibTableColumn
nsIfMngSNMP = _NsIfMngSNMP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 16),
    _NsIfMngSNMP_Type()
)
nsIfMngSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngSNMP.setStatus("current")


class _NsIfMngGlobal_Type(Integer32):
    """Custom type nsIfMngGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngGlobal_Type.__name__ = "Integer32"
_NsIfMngGlobal_Object = MibTableColumn
nsIfMngGlobal = _NsIfMngGlobal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 17),
    _NsIfMngGlobal_Type()
)
nsIfMngGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngGlobal.setStatus("current")


class _NsIfMngGlobalPro_Type(Integer32):
    """Custom type nsIfMngGlobalPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngGlobalPro_Type.__name__ = "Integer32"
_NsIfMngGlobalPro_Object = MibTableColumn
nsIfMngGlobalPro = _NsIfMngGlobalPro_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 18),
    _NsIfMngGlobalPro_Type()
)
nsIfMngGlobalPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngGlobalPro.setStatus("current")


class _NsIfMngPing_Type(Integer32):
    """Custom type nsIfMngPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngPing_Type.__name__ = "Integer32"
_NsIfMngPing_Object = MibTableColumn
nsIfMngPing = _NsIfMngPing_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 19),
    _NsIfMngPing_Type()
)
nsIfMngPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngPing.setStatus("current")


class _NsIfMngIdentReset_Type(Integer32):
    """Custom type nsIfMngIdentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsIfMngIdentReset_Type.__name__ = "Integer32"
_NsIfMngIdentReset_Object = MibTableColumn
nsIfMngIdentReset = _NsIfMngIdentReset_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 20),
    _NsIfMngIdentReset_Type()
)
nsIfMngIdentReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMngIdentReset.setStatus("current")


class _NsIfInfo_Type(Integer32):
    """Custom type nsIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfInfo_Type.__name__ = "Integer32"
_NsIfInfo_Object = MibTableColumn
nsIfInfo = _NsIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 21),
    _NsIfInfo_Type()
)
nsIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfInfo.setStatus("current")


class _NsIfDescr_Type(DisplayString):
    """Custom type nsIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsIfDescr_Type.__name__ = "DisplayString"
_NsIfDescr_Object = MibTableColumn
nsIfDescr = _NsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 1, 1, 22),
    _NsIfDescr_Type()
)
nsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfDescr.setStatus("current")
_NsIfSecondaryIpTable_Object = MibTable
nsIfSecondaryIpTable = _NsIfSecondaryIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2)
)
if mibBuilder.loadTexts:
    nsIfSecondaryIpTable.setStatus("current")
_NsIfSecondaryIpEntry_Object = MibTableRow
nsIfSecondaryIpEntry = _NsIfSecondaryIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1)
)
nsIfSecondaryIpEntry.setIndexNames(
    (0, "NETSCREEN-INTERFACE-MIB", "nsIfSecondaryIpIndex"),
)
if mibBuilder.loadTexts:
    nsIfSecondaryIpEntry.setStatus("current")


class _NsIfSecondaryIpIndex_Type(Integer32):
    """Custom type nsIfSecondaryIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfSecondaryIpIndex_Type.__name__ = "Integer32"
_NsIfSecondaryIpIndex_Object = MibTableColumn
nsIfSecondaryIpIndex = _NsIfSecondaryIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 1),
    _NsIfSecondaryIpIndex_Type()
)
nsIfSecondaryIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpIndex.setStatus("current")
_NsIfSecondaryIpIfIdx_Type = Integer32
_NsIfSecondaryIpIfIdx_Object = MibTableColumn
nsIfSecondaryIpIfIdx = _NsIfSecondaryIpIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 2),
    _NsIfSecondaryIpIfIdx_Type()
)
nsIfSecondaryIpIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpIfIdx.setStatus("current")
_NsIfSecondaryIpVsys_Type = Integer32
_NsIfSecondaryIpVsys_Object = MibTableColumn
nsIfSecondaryIpVsys = _NsIfSecondaryIpVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 3),
    _NsIfSecondaryIpVsys_Type()
)
nsIfSecondaryIpVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpVsys.setStatus("current")
_NsIfSecondaryIpZone_Type = Integer32
_NsIfSecondaryIpZone_Object = MibTableColumn
nsIfSecondaryIpZone = _NsIfSecondaryIpZone_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 4),
    _NsIfSecondaryIpZone_Type()
)
nsIfSecondaryIpZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpZone.setStatus("current")
_NsIfSecondaryIpAddress_Type = IpAddress
_NsIfSecondaryIpAddress_Object = MibTableColumn
nsIfSecondaryIpAddress = _NsIfSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 5),
    _NsIfSecondaryIpAddress_Type()
)
nsIfSecondaryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpAddress.setStatus("current")
_NsIfSecondaryIpNetmask_Type = IpAddress
_NsIfSecondaryIpNetmask_Object = MibTableColumn
nsIfSecondaryIpNetmask = _NsIfSecondaryIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 6),
    _NsIfSecondaryIpNetmask_Type()
)
nsIfSecondaryIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpNetmask.setStatus("current")


class _NsIfSecondaryIpIfInfo_Type(Integer32):
    """Custom type nsIfSecondaryIpIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfSecondaryIpIfInfo_Type.__name__ = "Integer32"
_NsIfSecondaryIpIfInfo_Object = MibTableColumn
nsIfSecondaryIpIfInfo = _NsIfSecondaryIpIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 2, 1, 7),
    _NsIfSecondaryIpIfInfo_Type()
)
nsIfSecondaryIpIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfSecondaryIpIfInfo.setStatus("current")
_NsIfFlowTable_Object = MibTable
nsIfFlowTable = _NsIfFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3)
)
if mibBuilder.loadTexts:
    nsIfFlowTable.setStatus("current")
_NsIfFlowEntry_Object = MibTableRow
nsIfFlowEntry = _NsIfFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1)
)
nsIfFlowEntry.setIndexNames(
    (0, "NETSCREEN-INTERFACE-MIB", "nsIfFlowIfIdx"),
)
if mibBuilder.loadTexts:
    nsIfFlowEntry.setStatus("current")


class _NsIfFlowIfIdx_Type(Integer32):
    """Custom type nsIfFlowIfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfFlowIfIdx_Type.__name__ = "Integer32"
_NsIfFlowIfIdx_Object = MibTableColumn
nsIfFlowIfIdx = _NsIfFlowIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 1),
    _NsIfFlowIfIdx_Type()
)
nsIfFlowIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowIfIdx.setStatus("current")
_NsIfFlowVsys_Type = Integer32
_NsIfFlowVsys_Object = MibTableColumn
nsIfFlowVsys = _NsIfFlowVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 2),
    _NsIfFlowVsys_Type()
)
nsIfFlowVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowVsys.setStatus("current")
_NsIfFlowInByte_Type = Counter32
_NsIfFlowInByte_Object = MibTableColumn
nsIfFlowInByte = _NsIfFlowInByte_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 3),
    _NsIfFlowInByte_Type()
)
nsIfFlowInByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowInByte.setStatus("current")
_NsIfFlowInPacket_Type = Counter32
_NsIfFlowInPacket_Object = MibTableColumn
nsIfFlowInPacket = _NsIfFlowInPacket_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 4),
    _NsIfFlowInPacket_Type()
)
nsIfFlowInPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowInPacket.setStatus("current")
_NsIfFlowOutByte_Type = Counter32
_NsIfFlowOutByte_Object = MibTableColumn
nsIfFlowOutByte = _NsIfFlowOutByte_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 5),
    _NsIfFlowOutByte_Type()
)
nsIfFlowOutByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowOutByte.setStatus("current")
_NsIfFlowOutPacket_Type = Counter32
_NsIfFlowOutPacket_Object = MibTableColumn
nsIfFlowOutPacket = _NsIfFlowOutPacket_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 6),
    _NsIfFlowOutPacket_Type()
)
nsIfFlowOutPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowOutPacket.setStatus("current")
_NsIfFlowInVpn_Type = Counter32
_NsIfFlowInVpn_Object = MibTableColumn
nsIfFlowInVpn = _NsIfFlowInVpn_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 7),
    _NsIfFlowInVpn_Type()
)
nsIfFlowInVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowInVpn.setStatus("current")
_NsIfInVlan_Type = Counter32
_NsIfInVlan_Object = MibTableColumn
nsIfInVlan = _NsIfInVlan_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 8),
    _NsIfInVlan_Type()
)
nsIfInVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfInVlan.setStatus("current")
_NsIfOutVlan_Type = Counter32
_NsIfOutVlan_Object = MibTableColumn
nsIfOutVlan = _NsIfOutVlan_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 9),
    _NsIfOutVlan_Type()
)
nsIfOutVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfOutVlan.setStatus("current")


class _NsIfFlowIfInfo_Type(Integer32):
    """Custom type nsIfFlowIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfFlowIfInfo_Type.__name__ = "Integer32"
_NsIfFlowIfInfo_Object = MibTableColumn
nsIfFlowIfInfo = _NsIfFlowIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 3, 1, 10),
    _NsIfFlowIfInfo_Type()
)
nsIfFlowIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfFlowIfInfo.setStatus("current")
_NsIfMonTable_Object = MibTable
nsIfMonTable = _NsIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4)
)
if mibBuilder.loadTexts:
    nsIfMonTable.setStatus("current")
_NsIfMonEntry_Object = MibTableRow
nsIfMonEntry = _NsIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1)
)
nsIfMonEntry.setIndexNames(
    (0, "NETSCREEN-INTERFACE-MIB", "nsIfMonIfIdx"),
)
if mibBuilder.loadTexts:
    nsIfMonEntry.setStatus("current")


class _NsIfMonIfIdx_Type(Integer32):
    """Custom type nsIfMonIfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfMonIfIdx_Type.__name__ = "Integer32"
_NsIfMonIfIdx_Object = MibTableColumn
nsIfMonIfIdx = _NsIfMonIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 1),
    _NsIfMonIfIdx_Type()
)
nsIfMonIfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonIfIdx.setStatus("current")
_NsIfMonVsys_Type = Integer32
_NsIfMonVsys_Object = MibTableColumn
nsIfMonVsys = _NsIfMonVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 2),
    _NsIfMonVsys_Type()
)
nsIfMonVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonVsys.setStatus("current")
_NsIfMonPlyDeny_Type = Counter32
_NsIfMonPlyDeny_Object = MibTableColumn
nsIfMonPlyDeny = _NsIfMonPlyDeny_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 3),
    _NsIfMonPlyDeny_Type()
)
nsIfMonPlyDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonPlyDeny.setStatus("current")
_NsIfMonAuthFail_Type = Counter32
_NsIfMonAuthFail_Object = MibTableColumn
nsIfMonAuthFail = _NsIfMonAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 4),
    _NsIfMonAuthFail_Type()
)
nsIfMonAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonAuthFail.setStatus("current")
_NsIfMonUrlBlock_Type = Counter32
_NsIfMonUrlBlock_Object = MibTableColumn
nsIfMonUrlBlock = _NsIfMonUrlBlock_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 5),
    _NsIfMonUrlBlock_Type()
)
nsIfMonUrlBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonUrlBlock.setStatus("current")
_NsIfMonTrMngQueue_Type = Counter32
_NsIfMonTrMngQueue_Object = MibTableColumn
nsIfMonTrMngQueue = _NsIfMonTrMngQueue_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 6),
    _NsIfMonTrMngQueue_Type()
)
nsIfMonTrMngQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonTrMngQueue.setStatus("current")
_NsIfMonTrMngDrop_Type = Counter32
_NsIfMonTrMngDrop_Object = MibTableColumn
nsIfMonTrMngDrop = _NsIfMonTrMngDrop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 7),
    _NsIfMonTrMngDrop_Type()
)
nsIfMonTrMngDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonTrMngDrop.setStatus("current")
_NsIfMonEncFail_Type = Counter32
_NsIfMonEncFail_Object = MibTableColumn
nsIfMonEncFail = _NsIfMonEncFail_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 8),
    _NsIfMonEncFail_Type()
)
nsIfMonEncFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonEncFail.setStatus("current")
_NsIfMonNoSa_Type = Counter32
_NsIfMonNoSa_Object = MibTableColumn
nsIfMonNoSa = _NsIfMonNoSa_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 9),
    _NsIfMonNoSa_Type()
)
nsIfMonNoSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonNoSa.setStatus("current")
_NsIfMonNoSaPly_Type = Counter32
_NsIfMonNoSaPly_Object = MibTableColumn
nsIfMonNoSaPly = _NsIfMonNoSaPly_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 10),
    _NsIfMonNoSaPly_Type()
)
nsIfMonNoSaPly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonNoSaPly.setStatus("current")
_NsIfMonSaInactive_Type = Counter32
_NsIfMonSaInactive_Object = MibTableColumn
nsIfMonSaInactive = _NsIfMonSaInactive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 11),
    _NsIfMonSaInactive_Type()
)
nsIfMonSaInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonSaInactive.setStatus("current")
_NsIfMonSaPolicyDeny_Type = Counter32
_NsIfMonSaPolicyDeny_Object = MibTableColumn
nsIfMonSaPolicyDeny = _NsIfMonSaPolicyDeny_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 12),
    _NsIfMonSaPolicyDeny_Type()
)
nsIfMonSaPolicyDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonSaPolicyDeny.setStatus("current")


class _NsIfMonIfInfo_Type(Integer32):
    """Custom type nsIfMonIfInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsIfMonIfInfo_Type.__name__ = "Integer32"
_NsIfMonIfInfo_Object = MibTableColumn
nsIfMonIfInfo = _NsIfMonIfInfo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 9, 4, 1, 13),
    _NsIfMonIfInfo_Type()
)
nsIfMonIfInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsIfMonIfInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-INTERFACE-MIB",
    **{"netscreenInterfaceMibModule": netscreenInterfaceMibModule,
       "nsIfTable": nsIfTable,
       "nsIfEntry": nsIfEntry,
       "nsIfIndex": nsIfIndex,
       "nsIfName": nsIfName,
       "nsIfVsys": nsIfVsys,
       "nsIfZone": nsIfZone,
       "nsIfStatus": nsIfStatus,
       "nsIfIp": nsIfIp,
       "nsIfNetmask": nsIfNetmask,
       "nsIfGateway": nsIfGateway,
       "nsIfMngIp": nsIfMngIp,
       "nsIfMode": nsIfMode,
       "nsIfMAC": nsIfMAC,
       "nsIfMngTelnet": nsIfMngTelnet,
       "nsIfMngSCS": nsIfMngSCS,
       "nsIfMngWEB": nsIfMngWEB,
       "nsIfMngSSL": nsIfMngSSL,
       "nsIfMngSNMP": nsIfMngSNMP,
       "nsIfMngGlobal": nsIfMngGlobal,
       "nsIfMngGlobalPro": nsIfMngGlobalPro,
       "nsIfMngPing": nsIfMngPing,
       "nsIfMngIdentReset": nsIfMngIdentReset,
       "nsIfInfo": nsIfInfo,
       "nsIfDescr": nsIfDescr,
       "nsIfSecondaryIpTable": nsIfSecondaryIpTable,
       "nsIfSecondaryIpEntry": nsIfSecondaryIpEntry,
       "nsIfSecondaryIpIndex": nsIfSecondaryIpIndex,
       "nsIfSecondaryIpIfIdx": nsIfSecondaryIpIfIdx,
       "nsIfSecondaryIpVsys": nsIfSecondaryIpVsys,
       "nsIfSecondaryIpZone": nsIfSecondaryIpZone,
       "nsIfSecondaryIpAddress": nsIfSecondaryIpAddress,
       "nsIfSecondaryIpNetmask": nsIfSecondaryIpNetmask,
       "nsIfSecondaryIpIfInfo": nsIfSecondaryIpIfInfo,
       "nsIfFlowTable": nsIfFlowTable,
       "nsIfFlowEntry": nsIfFlowEntry,
       "nsIfFlowIfIdx": nsIfFlowIfIdx,
       "nsIfFlowVsys": nsIfFlowVsys,
       "nsIfFlowInByte": nsIfFlowInByte,
       "nsIfFlowInPacket": nsIfFlowInPacket,
       "nsIfFlowOutByte": nsIfFlowOutByte,
       "nsIfFlowOutPacket": nsIfFlowOutPacket,
       "nsIfFlowInVpn": nsIfFlowInVpn,
       "nsIfInVlan": nsIfInVlan,
       "nsIfOutVlan": nsIfOutVlan,
       "nsIfFlowIfInfo": nsIfFlowIfInfo,
       "nsIfMonTable": nsIfMonTable,
       "nsIfMonEntry": nsIfMonEntry,
       "nsIfMonIfIdx": nsIfMonIfIdx,
       "nsIfMonVsys": nsIfMonVsys,
       "nsIfMonPlyDeny": nsIfMonPlyDeny,
       "nsIfMonAuthFail": nsIfMonAuthFail,
       "nsIfMonUrlBlock": nsIfMonUrlBlock,
       "nsIfMonTrMngQueue": nsIfMonTrMngQueue,
       "nsIfMonTrMngDrop": nsIfMonTrMngDrop,
       "nsIfMonEncFail": nsIfMonEncFail,
       "nsIfMonNoSa": nsIfMonNoSa,
       "nsIfMonNoSaPly": nsIfMonNoSaPly,
       "nsIfMonSaInactive": nsIfMonSaInactive,
       "nsIfMonSaPolicyDeny": nsIfMonSaPolicyDeny,
       "nsIfMonIfInfo": nsIfMonIfInfo}
)
