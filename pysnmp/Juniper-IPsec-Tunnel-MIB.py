# SNMP MIB module (Juniper-IPsec-Tunnel-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IPsec-Tunnel-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:36 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName",
    "JuniNextIfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniIpsecTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70)
)
juniIpsecTunnelMIB.setRevisions(
        ("2004-04-06 22:26",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniIpsecIdentityType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("idDerAsn1Gn", 10),
          ("idDn", 9),
          ("idFqdn", 2),
          ("idIpv4Addr", 1),
          ("idIpv4AddrRange", 7),
          ("idIpv4AddrSubnet", 4),
          ("idIpv6Addr", 5),
          ("idIpv6AddrRange", 8),
          ("idIpv6AddrSubnet", 6),
          ("idKeyId", 11),
          ("idUserFqdn", 3),
          ("reserved", 0))
    )



class JuniIpsecTransformType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ahMd5", 1),
          ("ahSha", 2),
          ("esp3DesMd5", 4),
          ("esp3DesNullAuth", 10),
          ("esp3DesSha", 6),
          ("espDesMd5", 3),
          ("espDesNullAuth", 9),
          ("espDesSha", 5),
          ("espNullMd5", 7),
          ("espNullSha", 8),
          ("reserved", 0))
    )



class JuniIpsecPfsGroup(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("noGroup", 0))
    )



class JuniIpsecTunnelType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manualTunnel", 1),
          ("signaledTunnel", 0))
    )



class Spi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_JuniIpsecObjects_ObjectIdentity = ObjectIdentity
juniIpsecObjects = _JuniIpsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1)
)
_JuniIpsecTunnel_ObjectIdentity = ObjectIdentity
juniIpsecTunnel = _JuniIpsecTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1)
)
_JuniIpsecTunnelNextIfIndex_Type = JuniNextIfIndex
_JuniIpsecTunnelNextIfIndex_Object = MibScalar
juniIpsecTunnelNextIfIndex = _JuniIpsecTunnelNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 1),
    _JuniIpsecTunnelNextIfIndex_Type()
)
juniIpsecTunnelNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelNextIfIndex.setStatus("current")
_JuniIpsecTunnelInterfaceTable_Object = MibTable
juniIpsecTunnelInterfaceTable = _JuniIpsecTunnelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelInterfaceTable.setStatus("current")
_JuniIpsecTunnelInterfaceEntry_Object = MibTableRow
juniIpsecTunnelInterfaceEntry = _JuniIpsecTunnelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1)
)
juniIpsecTunnelInterfaceEntry.setIndexNames(
    (0, "Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    juniIpsecTunnelInterfaceEntry.setStatus("current")
_JuniIpsecTunnelIfIndex_Type = InterfaceIndex
_JuniIpsecTunnelIfIndex_Object = MibTableColumn
juniIpsecTunnelIfIndex = _JuniIpsecTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 1),
    _JuniIpsecTunnelIfIndex_Type()
)
juniIpsecTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpsecTunnelIfIndex.setStatus("current")


class _JuniIpsecTunnelName_Type(DisplayString):
    """Custom type juniIpsecTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpsecTunnelName_Type.__name__ = "DisplayString"
_JuniIpsecTunnelName_Object = MibTableColumn
juniIpsecTunnelName = _JuniIpsecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 2),
    _JuniIpsecTunnelName_Type()
)
juniIpsecTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelName.setStatus("current")


class _JuniIpsecTunnelType_Type(JuniIpsecTunnelType):
    """Custom type juniIpsecTunnelType based on JuniIpsecTunnelType"""


_JuniIpsecTunnelType_Object = MibTableColumn
juniIpsecTunnelType = _JuniIpsecTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 3),
    _JuniIpsecTunnelType_Type()
)
juniIpsecTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelType.setStatus("current")


class _JuniIpsecTunnelTransportVirtualRouter_Type(JuniName):
    """Custom type juniIpsecTunnelTransportVirtualRouter based on JuniName"""
    defaultValue = OctetString("default")


_JuniIpsecTunnelTransportVirtualRouter_Object = MibTableColumn
juniIpsecTunnelTransportVirtualRouter = _JuniIpsecTunnelTransportVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 4),
    _JuniIpsecTunnelTransportVirtualRouter_Type()
)
juniIpsecTunnelTransportVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransportVirtualRouter.setStatus("current")
_JuniIpsecTunnelLocalEndPt_Type = IpAddress
_JuniIpsecTunnelLocalEndPt_Object = MibTableColumn
juniIpsecTunnelLocalEndPt = _JuniIpsecTunnelLocalEndPt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 5),
    _JuniIpsecTunnelLocalEndPt_Type()
)
juniIpsecTunnelLocalEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelLocalEndPt.setStatus("current")
_JuniIpsecTunnelRemoteEndPt_Type = IpAddress
_JuniIpsecTunnelRemoteEndPt_Object = MibTableColumn
juniIpsecTunnelRemoteEndPt = _JuniIpsecTunnelRemoteEndPt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 6),
    _JuniIpsecTunnelRemoteEndPt_Type()
)
juniIpsecTunnelRemoteEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelRemoteEndPt.setStatus("current")


class _JuniIpsecTunnelTransformSet_Type(DisplayString):
    """Custom type juniIpsecTunnelTransformSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniIpsecTunnelTransformSet_Type.__name__ = "DisplayString"
_JuniIpsecTunnelTransformSet_Object = MibTableColumn
juniIpsecTunnelTransformSet = _JuniIpsecTunnelTransformSet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 7),
    _JuniIpsecTunnelTransformSet_Type()
)
juniIpsecTunnelTransformSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransformSet.setStatus("current")


class _JuniIpsecTunnelSrcType_Type(JuniIpsecIdentityType):
    """Custom type juniIpsecTunnelSrcType based on JuniIpsecIdentityType"""


_JuniIpsecTunnelSrcType_Object = MibTableColumn
juniIpsecTunnelSrcType = _JuniIpsecTunnelSrcType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 8),
    _JuniIpsecTunnelSrcType_Type()
)
juniIpsecTunnelSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelSrcType.setStatus("current")
_JuniIpsecTunnelSrcAddr_Type = IpAddress
_JuniIpsecTunnelSrcAddr_Object = MibTableColumn
juniIpsecTunnelSrcAddr = _JuniIpsecTunnelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 9),
    _JuniIpsecTunnelSrcAddr_Type()
)
juniIpsecTunnelSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelSrcAddr.setStatus("current")


class _JuniIpsecTunnelSrcName_Type(DisplayString):
    """Custom type juniIpsecTunnelSrcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpsecTunnelSrcName_Type.__name__ = "DisplayString"
_JuniIpsecTunnelSrcName_Object = MibTableColumn
juniIpsecTunnelSrcName = _JuniIpsecTunnelSrcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 10),
    _JuniIpsecTunnelSrcName_Type()
)
juniIpsecTunnelSrcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelSrcName.setStatus("current")


class _JuniIpsecTunnelDstType_Type(JuniIpsecIdentityType):
    """Custom type juniIpsecTunnelDstType based on JuniIpsecIdentityType"""


_JuniIpsecTunnelDstType_Object = MibTableColumn
juniIpsecTunnelDstType = _JuniIpsecTunnelDstType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 11),
    _JuniIpsecTunnelDstType_Type()
)
juniIpsecTunnelDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelDstType.setStatus("current")
_JuniIpsecTunnelDstAddr_Type = IpAddress
_JuniIpsecTunnelDstAddr_Object = MibTableColumn
juniIpsecTunnelDstAddr = _JuniIpsecTunnelDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 12),
    _JuniIpsecTunnelDstAddr_Type()
)
juniIpsecTunnelDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelDstAddr.setStatus("current")


class _JuniIpsecTunnelDstName_Type(DisplayString):
    """Custom type juniIpsecTunnelDstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpsecTunnelDstName_Type.__name__ = "DisplayString"
_JuniIpsecTunnelDstName_Object = MibTableColumn
juniIpsecTunnelDstName = _JuniIpsecTunnelDstName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 13),
    _JuniIpsecTunnelDstName_Type()
)
juniIpsecTunnelDstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelDstName.setStatus("current")


class _JuniIpsecTunnelBackupDstType_Type(JuniIpsecIdentityType):
    """Custom type juniIpsecTunnelBackupDstType based on JuniIpsecIdentityType"""


_JuniIpsecTunnelBackupDstType_Object = MibTableColumn
juniIpsecTunnelBackupDstType = _JuniIpsecTunnelBackupDstType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 14),
    _JuniIpsecTunnelBackupDstType_Type()
)
juniIpsecTunnelBackupDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelBackupDstType.setStatus("current")
_JuniIpsecTunnelBackupDstAddr_Type = IpAddress
_JuniIpsecTunnelBackupDstAddr_Object = MibTableColumn
juniIpsecTunnelBackupDstAddr = _JuniIpsecTunnelBackupDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 15),
    _JuniIpsecTunnelBackupDstAddr_Type()
)
juniIpsecTunnelBackupDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelBackupDstAddr.setStatus("current")


class _JuniIpsecTunnelBackupDstName_Type(DisplayString):
    """Custom type juniIpsecTunnelBackupDstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpsecTunnelBackupDstName_Type.__name__ = "DisplayString"
_JuniIpsecTunnelBackupDstName_Object = MibTableColumn
juniIpsecTunnelBackupDstName = _JuniIpsecTunnelBackupDstName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 16),
    _JuniIpsecTunnelBackupDstName_Type()
)
juniIpsecTunnelBackupDstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelBackupDstName.setStatus("current")


class _JuniIpsecTunnelLocalIdType_Type(JuniIpsecIdentityType):
    """Custom type juniIpsecTunnelLocalIdType based on JuniIpsecIdentityType"""


_JuniIpsecTunnelLocalIdType_Object = MibTableColumn
juniIpsecTunnelLocalIdType = _JuniIpsecTunnelLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 17),
    _JuniIpsecTunnelLocalIdType_Type()
)
juniIpsecTunnelLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelLocalIdType.setStatus("current")
_JuniIpsecTunnelLocalIdAddr1_Type = IpAddress
_JuniIpsecTunnelLocalIdAddr1_Object = MibTableColumn
juniIpsecTunnelLocalIdAddr1 = _JuniIpsecTunnelLocalIdAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 18),
    _JuniIpsecTunnelLocalIdAddr1_Type()
)
juniIpsecTunnelLocalIdAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelLocalIdAddr1.setStatus("current")
_JuniIpsecTunnelLocalIdAddr2_Type = IpAddress
_JuniIpsecTunnelLocalIdAddr2_Object = MibTableColumn
juniIpsecTunnelLocalIdAddr2 = _JuniIpsecTunnelLocalIdAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 19),
    _JuniIpsecTunnelLocalIdAddr2_Type()
)
juniIpsecTunnelLocalIdAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelLocalIdAddr2.setStatus("current")


class _JuniIpsecTunnelRemoteIdType_Type(JuniIpsecIdentityType):
    """Custom type juniIpsecTunnelRemoteIdType based on JuniIpsecIdentityType"""


_JuniIpsecTunnelRemoteIdType_Object = MibTableColumn
juniIpsecTunnelRemoteIdType = _JuniIpsecTunnelRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 20),
    _JuniIpsecTunnelRemoteIdType_Type()
)
juniIpsecTunnelRemoteIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelRemoteIdType.setStatus("current")
_JuniIpsecTunnelRemoteIdAddr1_Type = IpAddress
_JuniIpsecTunnelRemoteIdAddr1_Object = MibTableColumn
juniIpsecTunnelRemoteIdAddr1 = _JuniIpsecTunnelRemoteIdAddr1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 21),
    _JuniIpsecTunnelRemoteIdAddr1_Type()
)
juniIpsecTunnelRemoteIdAddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelRemoteIdAddr1.setStatus("current")
_JuniIpsecTunnelRemoteIdAddr2_Type = IpAddress
_JuniIpsecTunnelRemoteIdAddr2_Object = MibTableColumn
juniIpsecTunnelRemoteIdAddr2 = _JuniIpsecTunnelRemoteIdAddr2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 22),
    _JuniIpsecTunnelRemoteIdAddr2_Type()
)
juniIpsecTunnelRemoteIdAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelRemoteIdAddr2.setStatus("current")


class _JuniIpsecTunnelLifeTimeSecs_Type(Unsigned32):
    """Custom type juniIpsecTunnelLifeTimeSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 864000),
    )


_JuniIpsecTunnelLifeTimeSecs_Type.__name__ = "Unsigned32"
_JuniIpsecTunnelLifeTimeSecs_Object = MibTableColumn
juniIpsecTunnelLifeTimeSecs = _JuniIpsecTunnelLifeTimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 23),
    _JuniIpsecTunnelLifeTimeSecs_Type()
)
juniIpsecTunnelLifeTimeSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelLifeTimeSecs.setStatus("current")
if mibBuilder.loadTexts:
    juniIpsecTunnelLifeTimeSecs.setUnits("seconds")


class _JuniIpsecTunnelLifeTimeKBs_Type(Unsigned32):
    """Custom type juniIpsecTunnelLifeTimeKBs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(102400, 4294967295),
    )


_JuniIpsecTunnelLifeTimeKBs_Type.__name__ = "Unsigned32"
_JuniIpsecTunnelLifeTimeKBs_Object = MibTableColumn
juniIpsecTunnelLifeTimeKBs = _JuniIpsecTunnelLifeTimeKBs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 24),
    _JuniIpsecTunnelLifeTimeKBs_Type()
)
juniIpsecTunnelLifeTimeKBs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelLifeTimeKBs.setStatus("current")
if mibBuilder.loadTexts:
    juniIpsecTunnelLifeTimeKBs.setUnits("kilobytes")
_JuniIpsecTunnelPfsGroup_Type = JuniIpsecPfsGroup
_JuniIpsecTunnelPfsGroup_Object = MibTableColumn
juniIpsecTunnelPfsGroup = _JuniIpsecTunnelPfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 25),
    _JuniIpsecTunnelPfsGroup_Type()
)
juniIpsecTunnelPfsGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelPfsGroup.setStatus("current")


class _JuniIpsecTunnelMtu_Type(Unsigned32):
    """Custom type juniIpsecTunnelMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 9000),
    )


_JuniIpsecTunnelMtu_Type.__name__ = "Unsigned32"
_JuniIpsecTunnelMtu_Object = MibTableColumn
juniIpsecTunnelMtu = _JuniIpsecTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 26),
    _JuniIpsecTunnelMtu_Type()
)
juniIpsecTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelMtu.setStatus("current")
_JuniIpsecTunnelInboundSpi1_Type = Spi
_JuniIpsecTunnelInboundSpi1_Object = MibTableColumn
juniIpsecTunnelInboundSpi1 = _JuniIpsecTunnelInboundSpi1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 27),
    _JuniIpsecTunnelInboundSpi1_Type()
)
juniIpsecTunnelInboundSpi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundSpi1.setStatus("current")
_JuniIpsecTunnelInboundTransform1_Type = JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform1_Object = MibTableColumn
juniIpsecTunnelInboundTransform1 = _JuniIpsecTunnelInboundTransform1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 28),
    _JuniIpsecTunnelInboundTransform1_Type()
)
juniIpsecTunnelInboundTransform1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundTransform1.setStatus("current")
_JuniIpsecTunnelInboundSpi2_Type = Spi
_JuniIpsecTunnelInboundSpi2_Object = MibTableColumn
juniIpsecTunnelInboundSpi2 = _JuniIpsecTunnelInboundSpi2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 29),
    _JuniIpsecTunnelInboundSpi2_Type()
)
juniIpsecTunnelInboundSpi2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundSpi2.setStatus("current")
_JuniIpsecTunnelInboundTransform2_Type = JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform2_Object = MibTableColumn
juniIpsecTunnelInboundTransform2 = _JuniIpsecTunnelInboundTransform2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 30),
    _JuniIpsecTunnelInboundTransform2_Type()
)
juniIpsecTunnelInboundTransform2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundTransform2.setStatus("current")
_JuniIpsecTunnelInboundSpi3_Type = Spi
_JuniIpsecTunnelInboundSpi3_Object = MibTableColumn
juniIpsecTunnelInboundSpi3 = _JuniIpsecTunnelInboundSpi3_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 31),
    _JuniIpsecTunnelInboundSpi3_Type()
)
juniIpsecTunnelInboundSpi3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundSpi3.setStatus("current")
_JuniIpsecTunnelInboundTransform3_Type = JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform3_Object = MibTableColumn
juniIpsecTunnelInboundTransform3 = _JuniIpsecTunnelInboundTransform3_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 32),
    _JuniIpsecTunnelInboundTransform3_Type()
)
juniIpsecTunnelInboundTransform3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundTransform3.setStatus("current")
_JuniIpsecTunnelInboundSpi4_Type = Spi
_JuniIpsecTunnelInboundSpi4_Object = MibTableColumn
juniIpsecTunnelInboundSpi4 = _JuniIpsecTunnelInboundSpi4_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 33),
    _JuniIpsecTunnelInboundSpi4_Type()
)
juniIpsecTunnelInboundSpi4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundSpi4.setStatus("current")
_JuniIpsecTunnelInboundTransform4_Type = JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform4_Object = MibTableColumn
juniIpsecTunnelInboundTransform4 = _JuniIpsecTunnelInboundTransform4_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 34),
    _JuniIpsecTunnelInboundTransform4_Type()
)
juniIpsecTunnelInboundTransform4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelInboundTransform4.setStatus("current")
_JuniIpsecTunnelOutboundSpi_Type = Spi
_JuniIpsecTunnelOutboundSpi_Object = MibTableColumn
juniIpsecTunnelOutboundSpi = _JuniIpsecTunnelOutboundSpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 35),
    _JuniIpsecTunnelOutboundSpi_Type()
)
juniIpsecTunnelOutboundSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelOutboundSpi.setStatus("current")
_JuniIpsecTunnelOutboundTransform_Type = JuniIpsecTransformType
_JuniIpsecTunnelOutboundTransform_Object = MibTableColumn
juniIpsecTunnelOutboundTransform = _JuniIpsecTunnelOutboundTransform_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 36),
    _JuniIpsecTunnelOutboundTransform_Type()
)
juniIpsecTunnelOutboundTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelOutboundTransform.setStatus("current")
_JuniIpsecTunnelRowStatus_Type = RowStatus
_JuniIpsecTunnelRowStatus_Object = MibTableColumn
juniIpsecTunnelRowStatus = _JuniIpsecTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 2, 1, 37),
    _JuniIpsecTunnelRowStatus_Type()
)
juniIpsecTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelRowStatus.setStatus("current")
_JuniIpsecTunnelStatTable_Object = MibTable
juniIpsecTunnelStatTable = _JuniIpsecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelStatTable.setStatus("current")
_JuniIpsecTunnelStatEntry_Object = MibTableRow
juniIpsecTunnelStatEntry = _JuniIpsecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1)
)
juniIpsecTunnelStatEntry.setIndexNames(
    (0, "Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatIfIndex"),
)
if mibBuilder.loadTexts:
    juniIpsecTunnelStatEntry.setStatus("current")
_JuniIpsecTunnelStatIfIndex_Type = InterfaceIndex
_JuniIpsecTunnelStatIfIndex_Object = MibTableColumn
juniIpsecTunnelStatIfIndex = _JuniIpsecTunnelStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 1),
    _JuniIpsecTunnelStatIfIndex_Type()
)
juniIpsecTunnelStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatIfIndex.setStatus("current")
_JuniIpsecTunnelStatInbUserRecvPkts_Type = Counter64
_JuniIpsecTunnelStatInbUserRecvPkts_Object = MibTableColumn
juniIpsecTunnelStatInbUserRecvPkts = _JuniIpsecTunnelStatInbUserRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 2),
    _JuniIpsecTunnelStatInbUserRecvPkts_Type()
)
juniIpsecTunnelStatInbUserRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbUserRecvPkts.setStatus("current")
_JuniIpsecTunnelStatInbUserRecvOctets_Type = Counter64
_JuniIpsecTunnelStatInbUserRecvOctets_Object = MibTableColumn
juniIpsecTunnelStatInbUserRecvOctets = _JuniIpsecTunnelStatInbUserRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 3),
    _JuniIpsecTunnelStatInbUserRecvOctets_Type()
)
juniIpsecTunnelStatInbUserRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbUserRecvOctets.setStatus("current")
_JuniIpsecTunnelStatInbAccRecvPkts_Type = Counter64
_JuniIpsecTunnelStatInbAccRecvPkts_Object = MibTableColumn
juniIpsecTunnelStatInbAccRecvPkts = _JuniIpsecTunnelStatInbAccRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 4),
    _JuniIpsecTunnelStatInbAccRecvPkts_Type()
)
juniIpsecTunnelStatInbAccRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbAccRecvPkts.setStatus("current")
_JuniIpsecTunnelStatInbAccRecvOctets_Type = Counter64
_JuniIpsecTunnelStatInbAccRecvOctets_Object = MibTableColumn
juniIpsecTunnelStatInbAccRecvOctets = _JuniIpsecTunnelStatInbAccRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 5),
    _JuniIpsecTunnelStatInbAccRecvOctets_Type()
)
juniIpsecTunnelStatInbAccRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbAccRecvOctets.setStatus("current")
_JuniIpsecTunnelStatInbAuthErrs_Type = Counter32
_JuniIpsecTunnelStatInbAuthErrs_Object = MibTableColumn
juniIpsecTunnelStatInbAuthErrs = _JuniIpsecTunnelStatInbAuthErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 6),
    _JuniIpsecTunnelStatInbAuthErrs_Type()
)
juniIpsecTunnelStatInbAuthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbAuthErrs.setStatus("current")
_JuniIpsecTunnelStatInbReplayErrs_Type = Counter32
_JuniIpsecTunnelStatInbReplayErrs_Object = MibTableColumn
juniIpsecTunnelStatInbReplayErrs = _JuniIpsecTunnelStatInbReplayErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 7),
    _JuniIpsecTunnelStatInbReplayErrs_Type()
)
juniIpsecTunnelStatInbReplayErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbReplayErrs.setStatus("current")
_JuniIpsecTunnelStatInbPolicyErrs_Type = Counter32
_JuniIpsecTunnelStatInbPolicyErrs_Object = MibTableColumn
juniIpsecTunnelStatInbPolicyErrs = _JuniIpsecTunnelStatInbPolicyErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 8),
    _JuniIpsecTunnelStatInbPolicyErrs_Type()
)
juniIpsecTunnelStatInbPolicyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbPolicyErrs.setStatus("current")
_JuniIpsecTunnelStatInbOtherRecvErrs_Type = Counter32
_JuniIpsecTunnelStatInbOtherRecvErrs_Object = MibTableColumn
juniIpsecTunnelStatInbOtherRecvErrs = _JuniIpsecTunnelStatInbOtherRecvErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 9),
    _JuniIpsecTunnelStatInbOtherRecvErrs_Type()
)
juniIpsecTunnelStatInbOtherRecvErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbOtherRecvErrs.setStatus("current")
_JuniIpsecTunnelStatInbDecryptErrs_Type = Counter32
_JuniIpsecTunnelStatInbDecryptErrs_Object = MibTableColumn
juniIpsecTunnelStatInbDecryptErrs = _JuniIpsecTunnelStatInbDecryptErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 10),
    _JuniIpsecTunnelStatInbDecryptErrs_Type()
)
juniIpsecTunnelStatInbDecryptErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbDecryptErrs.setStatus("current")
_JuniIpsecTunnelStatInbPadErrs_Type = Counter32
_JuniIpsecTunnelStatInbPadErrs_Object = MibTableColumn
juniIpsecTunnelStatInbPadErrs = _JuniIpsecTunnelStatInbPadErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 11),
    _JuniIpsecTunnelStatInbPadErrs_Type()
)
juniIpsecTunnelStatInbPadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatInbPadErrs.setStatus("current")
_JuniIpsecTunnelStatOutbUserRecvPkts_Type = Counter64
_JuniIpsecTunnelStatOutbUserRecvPkts_Object = MibTableColumn
juniIpsecTunnelStatOutbUserRecvPkts = _JuniIpsecTunnelStatOutbUserRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 12),
    _JuniIpsecTunnelStatOutbUserRecvPkts_Type()
)
juniIpsecTunnelStatOutbUserRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatOutbUserRecvPkts.setStatus("current")
_JuniIpsecTunnelStatOutbUserRecvOctets_Type = Counter64
_JuniIpsecTunnelStatOutbUserRecvOctets_Object = MibTableColumn
juniIpsecTunnelStatOutbUserRecvOctets = _JuniIpsecTunnelStatOutbUserRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 13),
    _JuniIpsecTunnelStatOutbUserRecvOctets_Type()
)
juniIpsecTunnelStatOutbUserRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatOutbUserRecvOctets.setStatus("current")
_JuniIpsecTunnelStatOutbAccRecvPkts_Type = Counter64
_JuniIpsecTunnelStatOutbAccRecvPkts_Object = MibTableColumn
juniIpsecTunnelStatOutbAccRecvPkts = _JuniIpsecTunnelStatOutbAccRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 14),
    _JuniIpsecTunnelStatOutbAccRecvPkts_Type()
)
juniIpsecTunnelStatOutbAccRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatOutbAccRecvPkts.setStatus("current")
_JuniIpsecTunnelStatOutbAccRecvOctets_Type = Counter64
_JuniIpsecTunnelStatOutbAccRecvOctets_Object = MibTableColumn
juniIpsecTunnelStatOutbAccRecvOctets = _JuniIpsecTunnelStatOutbAccRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 15),
    _JuniIpsecTunnelStatOutbAccRecvOctets_Type()
)
juniIpsecTunnelStatOutbAccRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelStatOutbAccRecvOctets.setStatus("current")
_JuniIpsecTunnelOutbOtherTxErrs_Type = Counter32
_JuniIpsecTunnelOutbOtherTxErrs_Object = MibTableColumn
juniIpsecTunnelOutbOtherTxErrs = _JuniIpsecTunnelOutbOtherTxErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 16),
    _JuniIpsecTunnelOutbOtherTxErrs_Type()
)
juniIpsecTunnelOutbOtherTxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelOutbOtherTxErrs.setStatus("current")
_JuniIpsecTunnelOutbPolicyErrs_Type = Counter32
_JuniIpsecTunnelOutbPolicyErrs_Object = MibTableColumn
juniIpsecTunnelOutbPolicyErrs = _JuniIpsecTunnelOutbPolicyErrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 3, 1, 17),
    _JuniIpsecTunnelOutbPolicyErrs_Type()
)
juniIpsecTunnelOutbPolicyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecTunnelOutbPolicyErrs.setStatus("current")
_JuniIpsecTunnelTransformSetTable_Object = MibTable
juniIpsecTunnelTransformSetTable = _JuniIpsecTunnelTransformSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelTransformSetTable.setStatus("current")
_JuniIpsecTunnelTransformSetEntry_Object = MibTableRow
juniIpsecTunnelTransformSetEntry = _JuniIpsecTunnelTransformSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1)
)
juniIpsecTunnelTransformSetEntry.setIndexNames(
    (0, "Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransformSetName"),
)
if mibBuilder.loadTexts:
    juniIpsecTunnelTransformSetEntry.setStatus("current")


class _JuniIpsecTunnelTransformSetName_Type(DisplayString):
    """Custom type juniIpsecTunnelTransformSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniIpsecTunnelTransformSetName_Type.__name__ = "DisplayString"
_JuniIpsecTunnelTransformSetName_Object = MibTableColumn
juniIpsecTunnelTransformSetName = _JuniIpsecTunnelTransformSetName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 1),
    _JuniIpsecTunnelTransformSetName_Type()
)
juniIpsecTunnelTransformSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransformSetName.setStatus("current")


class _JuniIpsecTunnelTransform1_Type(JuniIpsecTransformType):
    """Custom type juniIpsecTunnelTransform1 based on JuniIpsecTransformType"""


_JuniIpsecTunnelTransform1_Object = MibTableColumn
juniIpsecTunnelTransform1 = _JuniIpsecTunnelTransform1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 2),
    _JuniIpsecTunnelTransform1_Type()
)
juniIpsecTunnelTransform1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform1.setStatus("current")


class _JuniIpsecTunnelTransform2_Type(JuniIpsecTransformType):
    """Custom type juniIpsecTunnelTransform2 based on JuniIpsecTransformType"""


_JuniIpsecTunnelTransform2_Object = MibTableColumn
juniIpsecTunnelTransform2 = _JuniIpsecTunnelTransform2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 3),
    _JuniIpsecTunnelTransform2_Type()
)
juniIpsecTunnelTransform2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform2.setStatus("current")


class _JuniIpsecTunnelTransform3_Type(JuniIpsecTransformType):
    """Custom type juniIpsecTunnelTransform3 based on JuniIpsecTransformType"""


_JuniIpsecTunnelTransform3_Object = MibTableColumn
juniIpsecTunnelTransform3 = _JuniIpsecTunnelTransform3_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 4),
    _JuniIpsecTunnelTransform3_Type()
)
juniIpsecTunnelTransform3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform3.setStatus("current")
_JuniIpsecTunnelTransform4_Type = JuniIpsecTransformType
_JuniIpsecTunnelTransform4_Object = MibTableColumn
juniIpsecTunnelTransform4 = _JuniIpsecTunnelTransform4_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 5),
    _JuniIpsecTunnelTransform4_Type()
)
juniIpsecTunnelTransform4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform4.setStatus("current")


class _JuniIpsecTunnelTransform5_Type(JuniIpsecTransformType):
    """Custom type juniIpsecTunnelTransform5 based on JuniIpsecTransformType"""


_JuniIpsecTunnelTransform5_Object = MibTableColumn
juniIpsecTunnelTransform5 = _JuniIpsecTunnelTransform5_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 6),
    _JuniIpsecTunnelTransform5_Type()
)
juniIpsecTunnelTransform5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform5.setStatus("current")


class _JuniIpsecTunnelTransform6_Type(JuniIpsecTransformType):
    """Custom type juniIpsecTunnelTransform6 based on JuniIpsecTransformType"""


_JuniIpsecTunnelTransform6_Object = MibTableColumn
juniIpsecTunnelTransform6 = _JuniIpsecTunnelTransform6_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 7),
    _JuniIpsecTunnelTransform6_Type()
)
juniIpsecTunnelTransform6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransform6.setStatus("current")
_JuniIpsecTunnelTransformSetRowStatus_Type = RowStatus
_JuniIpsecTunnelTransformSetRowStatus_Object = MibTableColumn
juniIpsecTunnelTransformSetRowStatus = _JuniIpsecTunnelTransformSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 4, 1, 8),
    _JuniIpsecTunnelTransformSetRowStatus_Type()
)
juniIpsecTunnelTransformSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransformSetRowStatus.setStatus("current")
_JuniIpsecTunnelGlobalLocalEndpointTable_Object = MibTable
juniIpsecTunnelGlobalLocalEndpointTable = _JuniIpsecTunnelGlobalLocalEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelGlobalLocalEndpointTable.setStatus("current")
_JuniIpsecTunnelGlobalLocalEndpointEntry_Object = MibTableRow
juniIpsecTunnelGlobalLocalEndpointEntry = _JuniIpsecTunnelGlobalLocalEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 5, 1)
)
juniIpsecTunnelGlobalLocalEndpointEntry.setIndexNames(
    (0, "Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransportVrRouterIdx"),
)
if mibBuilder.loadTexts:
    juniIpsecTunnelGlobalLocalEndpointEntry.setStatus("current")
_JuniIpsecTunnelTransportVrRouterIdx_Type = Unsigned32
_JuniIpsecTunnelTransportVrRouterIdx_Object = MibTableColumn
juniIpsecTunnelTransportVrRouterIdx = _JuniIpsecTunnelTransportVrRouterIdx_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 5, 1, 1),
    _JuniIpsecTunnelTransportVrRouterIdx_Type()
)
juniIpsecTunnelTransportVrRouterIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpsecTunnelTransportVrRouterIdx.setStatus("current")
_JuniIpsecTunnelGlobalLocalEndpoint_Type = IpAddress
_JuniIpsecTunnelGlobalLocalEndpoint_Object = MibTableColumn
juniIpsecTunnelGlobalLocalEndpoint = _JuniIpsecTunnelGlobalLocalEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 5, 1, 2),
    _JuniIpsecTunnelGlobalLocalEndpoint_Type()
)
juniIpsecTunnelGlobalLocalEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelGlobalLocalEndpoint.setStatus("current")
_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Type = RowStatus
_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Object = MibTableColumn
juniIpsecTunnelGlobalLocalEndpointRowStatus = _JuniIpsecTunnelGlobalLocalEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 1, 5, 1, 3),
    _JuniIpsecTunnelGlobalLocalEndpointRowStatus_Type()
)
juniIpsecTunnelGlobalLocalEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpsecTunnelGlobalLocalEndpointRowStatus.setStatus("current")
_JuniIpsecSystem_ObjectIdentity = ObjectIdentity
juniIpsecSystem = _JuniIpsecSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2)
)
_JuniIpsecTunnelSystemStats_ObjectIdentity = ObjectIdentity
juniIpsecTunnelSystemStats = _JuniIpsecTunnelSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1)
)
_JuniIpsecSummaryStatsTotalTunnels_Type = Counter32
_JuniIpsecSummaryStatsTotalTunnels_Object = MibScalar
juniIpsecSummaryStatsTotalTunnels = _JuniIpsecSummaryStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 1),
    _JuniIpsecSummaryStatsTotalTunnels_Type()
)
juniIpsecSummaryStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsTotalTunnels.setStatus("current")
_JuniIpsecSummaryStatsAdminStatusEnabled_Type = Counter32
_JuniIpsecSummaryStatsAdminStatusEnabled_Object = MibScalar
juniIpsecSummaryStatsAdminStatusEnabled = _JuniIpsecSummaryStatsAdminStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 2),
    _JuniIpsecSummaryStatsAdminStatusEnabled_Type()
)
juniIpsecSummaryStatsAdminStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsAdminStatusEnabled.setStatus("current")
_JuniIpsecSummaryStatsAdminStatusDisabled_Type = Counter32
_JuniIpsecSummaryStatsAdminStatusDisabled_Object = MibScalar
juniIpsecSummaryStatsAdminStatusDisabled = _JuniIpsecSummaryStatsAdminStatusDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 3),
    _JuniIpsecSummaryStatsAdminStatusDisabled_Type()
)
juniIpsecSummaryStatsAdminStatusDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsAdminStatusDisabled.setStatus("current")
_JuniIpsecSummaryStatsOperStatusUp_Type = Counter32
_JuniIpsecSummaryStatsOperStatusUp_Object = MibScalar
juniIpsecSummaryStatsOperStatusUp = _JuniIpsecSummaryStatsOperStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 4),
    _JuniIpsecSummaryStatsOperStatusUp_Type()
)
juniIpsecSummaryStatsOperStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsOperStatusUp.setStatus("current")
_JuniIpsecSummaryStatsOperStatusDown_Type = Counter32
_JuniIpsecSummaryStatsOperStatusDown_Object = MibScalar
juniIpsecSummaryStatsOperStatusDown = _JuniIpsecSummaryStatsOperStatusDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 5),
    _JuniIpsecSummaryStatsOperStatusDown_Type()
)
juniIpsecSummaryStatsOperStatusDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsOperStatusDown.setStatus("current")
_JuniIpsecSummaryStatsOperStatusNotPresent_Type = Counter32
_JuniIpsecSummaryStatsOperStatusNotPresent_Object = MibScalar
juniIpsecSummaryStatsOperStatusNotPresent = _JuniIpsecSummaryStatsOperStatusNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 1, 2, 1, 6),
    _JuniIpsecSummaryStatsOperStatusNotPresent_Type()
)
juniIpsecSummaryStatsOperStatusNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpsecSummaryStatsOperStatusNotPresent.setStatus("current")
_JuniIpsecTunnelMIBConformance_ObjectIdentity = ObjectIdentity
juniIpsecTunnelMIBConformance = _JuniIpsecTunnelMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2)
)
_JuniIpsecTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
juniIpsecTunnelMIBCompliances = _JuniIpsecTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 1)
)
_JuniIpsecTunnelMIBGroups_ObjectIdentity = ObjectIdentity
juniIpsecTunnelMIBGroups = _JuniIpsecTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2)
)

# Managed Objects groups

juniIpsecTunnelConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2, 1)
)
juniIpsecTunnelConfigGroup.setObjects(
      *(("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelNextIfIndex"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelName"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransportVirtualRouter"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLocalEndPt"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelRemoteEndPt"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransformSet"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelSrcType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelSrcAddr"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelSrcName"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelDstType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelDstAddr"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelDstName"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelBackupDstType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelBackupDstAddr"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelBackupDstName"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLocalIdType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLocalIdAddr1"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLocalIdAddr2"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelRemoteIdType"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelRemoteIdAddr1"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelRemoteIdAddr2"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLifeTimeSecs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelLifeTimeKBs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelPfsGroup"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelMtu"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundSpi1"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundTransform1"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundSpi2"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundTransform2"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundSpi3"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundTransform3"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundSpi4"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelInboundTransform4"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelOutboundSpi"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelOutboundTransform"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpsecTunnelConfigGroup.setStatus("current")

juniIpsecTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2, 2)
)
juniIpsecTunnelStatsGroup.setObjects(
      *(("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbUserRecvPkts"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbUserRecvOctets"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbAccRecvPkts"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbAccRecvOctets"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbAuthErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbReplayErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbPolicyErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbOtherRecvErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbDecryptErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatInbPadErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatOutbUserRecvPkts"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatOutbUserRecvOctets"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatOutbAccRecvPkts"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelStatOutbAccRecvOctets"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelOutbOtherTxErrs"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelOutbPolicyErrs"))
)
if mibBuilder.loadTexts:
    juniIpsecTunnelStatsGroup.setStatus("current")

juniIpsecTransformSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2, 3)
)
juniIpsecTransformSetGroup.setObjects(
      *(("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform1"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform2"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform3"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform4"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform5"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransform6"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelTransformSetRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpsecTransformSetGroup.setStatus("current")

juniIpsecGlobalLocalEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2, 4)
)
juniIpsecGlobalLocalEndpointGroup.setObjects(
      *(("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelGlobalLocalEndpoint"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecTunnelGlobalLocalEndpointRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpsecGlobalLocalEndpointGroup.setStatus("current")

juniIpsecTunnelSystemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 2, 5)
)
juniIpsecTunnelSystemStatsGroup.setObjects(
      *(("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsTotalTunnels"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsAdminStatusEnabled"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsAdminStatusDisabled"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsOperStatusUp"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsOperStatusDown"),
        ("Juniper-IPsec-Tunnel-MIB", "juniIpsecSummaryStatsOperStatusNotPresent"))
)
if mibBuilder.loadTexts:
    juniIpsecTunnelSystemStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIpsecTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelCompliance.setStatus(
        "obsolete"
    )

juniIpsecTunnelCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 70, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpsecTunnelCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IPsec-Tunnel-MIB",
    **{"JuniIpsecIdentityType": JuniIpsecIdentityType,
       "JuniIpsecTransformType": JuniIpsecTransformType,
       "JuniIpsecPfsGroup": JuniIpsecPfsGroup,
       "JuniIpsecTunnelType": JuniIpsecTunnelType,
       "Spi": Spi,
       "juniIpsecTunnelMIB": juniIpsecTunnelMIB,
       "juniIpsecObjects": juniIpsecObjects,
       "juniIpsecTunnel": juniIpsecTunnel,
       "juniIpsecTunnelNextIfIndex": juniIpsecTunnelNextIfIndex,
       "juniIpsecTunnelInterfaceTable": juniIpsecTunnelInterfaceTable,
       "juniIpsecTunnelInterfaceEntry": juniIpsecTunnelInterfaceEntry,
       "juniIpsecTunnelIfIndex": juniIpsecTunnelIfIndex,
       "juniIpsecTunnelName": juniIpsecTunnelName,
       "juniIpsecTunnelType": juniIpsecTunnelType,
       "juniIpsecTunnelTransportVirtualRouter": juniIpsecTunnelTransportVirtualRouter,
       "juniIpsecTunnelLocalEndPt": juniIpsecTunnelLocalEndPt,
       "juniIpsecTunnelRemoteEndPt": juniIpsecTunnelRemoteEndPt,
       "juniIpsecTunnelTransformSet": juniIpsecTunnelTransformSet,
       "juniIpsecTunnelSrcType": juniIpsecTunnelSrcType,
       "juniIpsecTunnelSrcAddr": juniIpsecTunnelSrcAddr,
       "juniIpsecTunnelSrcName": juniIpsecTunnelSrcName,
       "juniIpsecTunnelDstType": juniIpsecTunnelDstType,
       "juniIpsecTunnelDstAddr": juniIpsecTunnelDstAddr,
       "juniIpsecTunnelDstName": juniIpsecTunnelDstName,
       "juniIpsecTunnelBackupDstType": juniIpsecTunnelBackupDstType,
       "juniIpsecTunnelBackupDstAddr": juniIpsecTunnelBackupDstAddr,
       "juniIpsecTunnelBackupDstName": juniIpsecTunnelBackupDstName,
       "juniIpsecTunnelLocalIdType": juniIpsecTunnelLocalIdType,
       "juniIpsecTunnelLocalIdAddr1": juniIpsecTunnelLocalIdAddr1,
       "juniIpsecTunnelLocalIdAddr2": juniIpsecTunnelLocalIdAddr2,
       "juniIpsecTunnelRemoteIdType": juniIpsecTunnelRemoteIdType,
       "juniIpsecTunnelRemoteIdAddr1": juniIpsecTunnelRemoteIdAddr1,
       "juniIpsecTunnelRemoteIdAddr2": juniIpsecTunnelRemoteIdAddr2,
       "juniIpsecTunnelLifeTimeSecs": juniIpsecTunnelLifeTimeSecs,
       "juniIpsecTunnelLifeTimeKBs": juniIpsecTunnelLifeTimeKBs,
       "juniIpsecTunnelPfsGroup": juniIpsecTunnelPfsGroup,
       "juniIpsecTunnelMtu": juniIpsecTunnelMtu,
       "juniIpsecTunnelInboundSpi1": juniIpsecTunnelInboundSpi1,
       "juniIpsecTunnelInboundTransform1": juniIpsecTunnelInboundTransform1,
       "juniIpsecTunnelInboundSpi2": juniIpsecTunnelInboundSpi2,
       "juniIpsecTunnelInboundTransform2": juniIpsecTunnelInboundTransform2,
       "juniIpsecTunnelInboundSpi3": juniIpsecTunnelInboundSpi3,
       "juniIpsecTunnelInboundTransform3": juniIpsecTunnelInboundTransform3,
       "juniIpsecTunnelInboundSpi4": juniIpsecTunnelInboundSpi4,
       "juniIpsecTunnelInboundTransform4": juniIpsecTunnelInboundTransform4,
       "juniIpsecTunnelOutboundSpi": juniIpsecTunnelOutboundSpi,
       "juniIpsecTunnelOutboundTransform": juniIpsecTunnelOutboundTransform,
       "juniIpsecTunnelRowStatus": juniIpsecTunnelRowStatus,
       "juniIpsecTunnelStatTable": juniIpsecTunnelStatTable,
       "juniIpsecTunnelStatEntry": juniIpsecTunnelStatEntry,
       "juniIpsecTunnelStatIfIndex": juniIpsecTunnelStatIfIndex,
       "juniIpsecTunnelStatInbUserRecvPkts": juniIpsecTunnelStatInbUserRecvPkts,
       "juniIpsecTunnelStatInbUserRecvOctets": juniIpsecTunnelStatInbUserRecvOctets,
       "juniIpsecTunnelStatInbAccRecvPkts": juniIpsecTunnelStatInbAccRecvPkts,
       "juniIpsecTunnelStatInbAccRecvOctets": juniIpsecTunnelStatInbAccRecvOctets,
       "juniIpsecTunnelStatInbAuthErrs": juniIpsecTunnelStatInbAuthErrs,
       "juniIpsecTunnelStatInbReplayErrs": juniIpsecTunnelStatInbReplayErrs,
       "juniIpsecTunnelStatInbPolicyErrs": juniIpsecTunnelStatInbPolicyErrs,
       "juniIpsecTunnelStatInbOtherRecvErrs": juniIpsecTunnelStatInbOtherRecvErrs,
       "juniIpsecTunnelStatInbDecryptErrs": juniIpsecTunnelStatInbDecryptErrs,
       "juniIpsecTunnelStatInbPadErrs": juniIpsecTunnelStatInbPadErrs,
       "juniIpsecTunnelStatOutbUserRecvPkts": juniIpsecTunnelStatOutbUserRecvPkts,
       "juniIpsecTunnelStatOutbUserRecvOctets": juniIpsecTunnelStatOutbUserRecvOctets,
       "juniIpsecTunnelStatOutbAccRecvPkts": juniIpsecTunnelStatOutbAccRecvPkts,
       "juniIpsecTunnelStatOutbAccRecvOctets": juniIpsecTunnelStatOutbAccRecvOctets,
       "juniIpsecTunnelOutbOtherTxErrs": juniIpsecTunnelOutbOtherTxErrs,
       "juniIpsecTunnelOutbPolicyErrs": juniIpsecTunnelOutbPolicyErrs,
       "juniIpsecTunnelTransformSetTable": juniIpsecTunnelTransformSetTable,
       "juniIpsecTunnelTransformSetEntry": juniIpsecTunnelTransformSetEntry,
       "juniIpsecTunnelTransformSetName": juniIpsecTunnelTransformSetName,
       "juniIpsecTunnelTransform1": juniIpsecTunnelTransform1,
       "juniIpsecTunnelTransform2": juniIpsecTunnelTransform2,
       "juniIpsecTunnelTransform3": juniIpsecTunnelTransform3,
       "juniIpsecTunnelTransform4": juniIpsecTunnelTransform4,
       "juniIpsecTunnelTransform5": juniIpsecTunnelTransform5,
       "juniIpsecTunnelTransform6": juniIpsecTunnelTransform6,
       "juniIpsecTunnelTransformSetRowStatus": juniIpsecTunnelTransformSetRowStatus,
       "juniIpsecTunnelGlobalLocalEndpointTable": juniIpsecTunnelGlobalLocalEndpointTable,
       "juniIpsecTunnelGlobalLocalEndpointEntry": juniIpsecTunnelGlobalLocalEndpointEntry,
       "juniIpsecTunnelTransportVrRouterIdx": juniIpsecTunnelTransportVrRouterIdx,
       "juniIpsecTunnelGlobalLocalEndpoint": juniIpsecTunnelGlobalLocalEndpoint,
       "juniIpsecTunnelGlobalLocalEndpointRowStatus": juniIpsecTunnelGlobalLocalEndpointRowStatus,
       "juniIpsecSystem": juniIpsecSystem,
       "juniIpsecTunnelSystemStats": juniIpsecTunnelSystemStats,
       "juniIpsecSummaryStatsTotalTunnels": juniIpsecSummaryStatsTotalTunnels,
       "juniIpsecSummaryStatsAdminStatusEnabled": juniIpsecSummaryStatsAdminStatusEnabled,
       "juniIpsecSummaryStatsAdminStatusDisabled": juniIpsecSummaryStatsAdminStatusDisabled,
       "juniIpsecSummaryStatsOperStatusUp": juniIpsecSummaryStatsOperStatusUp,
       "juniIpsecSummaryStatsOperStatusDown": juniIpsecSummaryStatsOperStatusDown,
       "juniIpsecSummaryStatsOperStatusNotPresent": juniIpsecSummaryStatsOperStatusNotPresent,
       "juniIpsecTunnelMIBConformance": juniIpsecTunnelMIBConformance,
       "juniIpsecTunnelMIBCompliances": juniIpsecTunnelMIBCompliances,
       "juniIpsecTunnelCompliance": juniIpsecTunnelCompliance,
       "juniIpsecTunnelCompliance2": juniIpsecTunnelCompliance2,
       "juniIpsecTunnelMIBGroups": juniIpsecTunnelMIBGroups,
       "juniIpsecTunnelConfigGroup": juniIpsecTunnelConfigGroup,
       "juniIpsecTunnelStatsGroup": juniIpsecTunnelStatsGroup,
       "juniIpsecTransformSetGroup": juniIpsecTransformSetGroup,
       "juniIpsecGlobalLocalEndpointGroup": juniIpsecGlobalLocalEndpointGroup,
       "juniIpsecTunnelSystemStatsGroup": juniIpsecTunnelSystemStatsGroup}
)
