# SNMP MIB module (CISCO-RMON-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RMON-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:39 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Dscp")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(portCopyEntry,) = mibBuilder.importSymbols(
    "SMON-MIB",
    "portCopyEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoRmonConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103)
)
ciscoRmonConfigMIB.setRevisions(
        ("2010-08-03 00:00",
         "2008-05-02 00:00",
         "2008-04-04 00:00",
         "2006-02-21 00:00",
         "2005-09-28 12:10",
         "2005-05-02 00:00",
         "2005-01-24 00:00",
         "2004-02-04 00:00",
         "2004-02-03 00:00",
         "2003-04-29 00:00",
         "2002-10-08 00:00",
         "2001-04-01 00:00",
         "2001-02-22 00:00",
         "1998-12-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SpanTxReplicationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 1),
          ("distributed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoRmonConfigObjects_ObjectIdentity = ObjectIdentity
ciscoRmonConfigObjects = _CiscoRmonConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1)
)
_CiscoRmon2ConfigObjects_ObjectIdentity = ObjectIdentity
ciscoRmon2ConfigObjects = _CiscoRmon2ConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 1)
)


class _RmonTimeFilterMode_Type(Integer32):
    """Custom type rmonTimeFilterMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopAfterAll", 2),
          ("stopAfterOne", 1))
    )


_RmonTimeFilterMode_Type.__name__ = "Integer32"
_RmonTimeFilterMode_Object = MibScalar
rmonTimeFilterMode = _RmonTimeFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 1, 1),
    _RmonTimeFilterMode_Type()
)
rmonTimeFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonTimeFilterMode.setStatus("current")
_CiscoSmonConfigObjects_ObjectIdentity = ObjectIdentity
ciscoSmonConfigObjects = _CiscoSmonConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2)
)
_PortCopyXTable_Object = MibTable
portCopyXTable = _PortCopyXTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portCopyXTable.setStatus("current")
_PortCopyXEntry_Object = MibTableRow
portCopyXEntry = _PortCopyXEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    portCopyXEntry.setStatus("current")


class _PortCopyLoVlanMask_Type(OctetString):
    """Custom type portCopyLoVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortCopyLoVlanMask_Type.__name__ = "OctetString"
_PortCopyLoVlanMask_Object = MibTableColumn
portCopyLoVlanMask = _PortCopyLoVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 1),
    _PortCopyLoVlanMask_Type()
)
portCopyLoVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyLoVlanMask.setStatus("current")


class _PortCopyHiVlanMask_Type(OctetString):
    """Custom type portCopyHiVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortCopyHiVlanMask_Type.__name__ = "OctetString"
_PortCopyHiVlanMask_Object = MibTableColumn
portCopyHiVlanMask = _PortCopyHiVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 2),
    _PortCopyHiVlanMask_Type()
)
portCopyHiVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyHiVlanMask.setStatus("current")


class _PortCopyDestLoVlanMask_Type(OctetString):
    """Custom type portCopyDestLoVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortCopyDestLoVlanMask_Type.__name__ = "OctetString"
_PortCopyDestLoVlanMask_Object = MibTableColumn
portCopyDestLoVlanMask = _PortCopyDestLoVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 3),
    _PortCopyDestLoVlanMask_Type()
)
portCopyDestLoVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyDestLoVlanMask.setStatus("current")


class _PortCopyDestHiVlanMask_Type(OctetString):
    """Custom type portCopyDestHiVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortCopyDestHiVlanMask_Type.__name__ = "OctetString"
_PortCopyDestHiVlanMask_Object = MibTableColumn
portCopyDestHiVlanMask = _PortCopyDestHiVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 4),
    _PortCopyDestHiVlanMask_Type()
)
portCopyDestHiVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyDestHiVlanMask.setStatus("current")


class _PortCopyOption_Type(Bits):
    """Custom type portCopyOption based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("badDisable", 8),
          ("broadcastDisable", 6),
          ("dot1q", 2),
          ("goodDisable", 7),
          ("inpkts", 0),
          ("isl", 3),
          ("learningDisable", 1),
          ("multicast", 4),
          ("unicastDisable", 5))
    )

_PortCopyOption_Type.__name__ = "Bits"
_PortCopyOption_Object = MibTableColumn
portCopyOption = _PortCopyOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 5),
    _PortCopyOption_Type()
)
portCopyOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyOption.setStatus("current")


class _PortCopySessionNo_Type(Integer32):
    """Custom type portCopySessionNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortCopySessionNo_Type.__name__ = "Integer32"
_PortCopySessionNo_Object = MibTableColumn
portCopySessionNo = _PortCopySessionNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 6),
    _PortCopySessionNo_Type()
)
portCopySessionNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopySessionNo.setStatus("current")


class _PortCopySessionType_Type(Integer32):
    """Custom type portCopySessionType based on Integer32"""
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
        *(("local", 2),
          ("localTx", 5),
          ("notSpecified", 1),
          ("remoteDestination", 4),
          ("remoteSource", 3))
    )


_PortCopySessionType_Type.__name__ = "Integer32"
_PortCopySessionType_Object = MibTableColumn
portCopySessionType = _PortCopySessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 7),
    _PortCopySessionType_Type()
)
portCopySessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopySessionType.setStatus("current")


class _PortCopyRemoveSrc_Type(TruthValue):
    """Custom type portCopyRemoveSrc based on TruthValue"""


_PortCopyRemoveSrc_Object = MibTableColumn
portCopyRemoveSrc = _PortCopyRemoveSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 8),
    _PortCopyRemoveSrc_Type()
)
portCopyRemoveSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyRemoveSrc.setStatus("current")
_PortCopyReflectorPort_Type = InterfaceIndex
_PortCopyReflectorPort_Object = MibTableColumn
portCopyReflectorPort = _PortCopyReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 9),
    _PortCopyReflectorPort_Type()
)
portCopyReflectorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyReflectorPort.setStatus("current")


class _PortCopyInpktVlan_Type(Unsigned32):
    """Custom type portCopyInpktVlan based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PortCopyInpktVlan_Type.__name__ = "Unsigned32"
_PortCopyInpktVlan_Object = MibTableColumn
portCopyInpktVlan = _PortCopyInpktVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 1, 1, 10),
    _PortCopyInpktVlan_Type()
)
portCopyInpktVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyInpktVlan.setStatus("current")


class _PortCopyMaxIngressSessions_Type(Integer32):
    """Custom type portCopyMaxIngressSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortCopyMaxIngressSessions_Type.__name__ = "Integer32"
_PortCopyMaxIngressSessions_Object = MibScalar
portCopyMaxIngressSessions = _PortCopyMaxIngressSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 2),
    _PortCopyMaxIngressSessions_Type()
)
portCopyMaxIngressSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCopyMaxIngressSessions.setStatus("current")


class _PortCopyMaxEgressSessions_Type(Integer32):
    """Custom type portCopyMaxEgressSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortCopyMaxEgressSessions_Type.__name__ = "Integer32"
_PortCopyMaxEgressSessions_Object = MibScalar
portCopyMaxEgressSessions = _PortCopyMaxEgressSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 3),
    _PortCopyMaxEgressSessions_Type()
)
portCopyMaxEgressSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCopyMaxEgressSessions.setStatus("current")
_CrcSpanSessionTable_Object = MibTable
crcSpanSessionTable = _CrcSpanSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4)
)
if mibBuilder.loadTexts:
    crcSpanSessionTable.setStatus("current")
_CrcSpanSessionEntry_Object = MibTableRow
crcSpanSessionEntry = _CrcSpanSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4, 1)
)
crcSpanSessionEntry.setIndexNames(
    (0, "CISCO-RMON-CONFIG-MIB", "crcSpanSessionNo"),
)
if mibBuilder.loadTexts:
    crcSpanSessionEntry.setStatus("current")
_CrcSpanSessionNo_Type = Unsigned32
_CrcSpanSessionNo_Object = MibTableColumn
crcSpanSessionNo = _CrcSpanSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4, 1, 1),
    _CrcSpanSessionNo_Type()
)
crcSpanSessionNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crcSpanSessionNo.setStatus("current")


class _CrcSpanSessionType_Type(Integer32):
    """Custom type crcSpanSessionType based on Integer32"""
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
        *(("erspan", 3),
          ("local", 1),
          ("other", 5),
          ("remote", 2),
          ("service", 4))
    )


_CrcSpanSessionType_Type.__name__ = "Integer32"
_CrcSpanSessionType_Object = MibTableColumn
crcSpanSessionType = _CrcSpanSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4, 1, 2),
    _CrcSpanSessionType_Type()
)
crcSpanSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanSessionType.setStatus("current")


class _CrcSpanSessionEnabled_Type(TruthValue):
    """Custom type crcSpanSessionEnabled based on TruthValue"""


_CrcSpanSessionEnabled_Object = MibTableColumn
crcSpanSessionEnabled = _CrcSpanSessionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4, 1, 3),
    _CrcSpanSessionEnabled_Type()
)
crcSpanSessionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcSpanSessionEnabled.setStatus("current")
_CrcSpanSessionDescr_Type = SnmpAdminString
_CrcSpanSessionDescr_Object = MibTableColumn
crcSpanSessionDescr = _CrcSpanSessionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 4, 1, 4),
    _CrcSpanSessionDescr_Type()
)
crcSpanSessionDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcSpanSessionDescr.setStatus("current")
_CrcERSpanSessionTable_Object = MibTable
crcERSpanSessionTable = _CrcERSpanSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5)
)
if mibBuilder.loadTexts:
    crcERSpanSessionTable.setStatus("current")
_CrcERSpanSessionEntry_Object = MibTableRow
crcERSpanSessionEntry = _CrcERSpanSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1)
)
crcERSpanSessionEntry.setIndexNames(
    (0, "CISCO-RMON-CONFIG-MIB", "crcERSpanSessionNo"),
)
if mibBuilder.loadTexts:
    crcERSpanSessionEntry.setStatus("current")
_CrcERSpanSessionNo_Type = Unsigned32
_CrcERSpanSessionNo_Object = MibTableColumn
crcERSpanSessionNo = _CrcERSpanSessionNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 1),
    _CrcERSpanSessionNo_Type()
)
crcERSpanSessionNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crcERSpanSessionNo.setStatus("current")


class _CrcERSpanSessionType_Type(Integer32):
    """Custom type crcERSpanSessionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eRSpanDestination", 2),
          ("eRSpanSource", 1))
    )


_CrcERSpanSessionType_Type.__name__ = "Integer32"
_CrcERSpanSessionType_Object = MibTableColumn
crcERSpanSessionType = _CrcERSpanSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 2),
    _CrcERSpanSessionType_Type()
)
crcERSpanSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanSessionType.setStatus("current")


class _CrcERSpanSessionDescr_Type(SnmpAdminString):
    """Custom type crcERSpanSessionDescr based on SnmpAdminString"""
    defaultHexValue = ""


_CrcERSpanSessionDescr_Object = MibTableColumn
crcERSpanSessionDescr = _CrcERSpanSessionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 3),
    _CrcERSpanSessionDescr_Type()
)
crcERSpanSessionDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanSessionDescr.setStatus("current")
_CrcERSpanEncapID_Type = Unsigned32
_CrcERSpanEncapID_Object = MibTableColumn
crcERSpanEncapID = _CrcERSpanEncapID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 4),
    _CrcERSpanEncapID_Type()
)
crcERSpanEncapID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanEncapID.setStatus("current")


class _CrcERSpanIpType_Type(InetAddressType):
    """Custom type crcERSpanIpType based on InetAddressType"""


_CrcERSpanIpType_Object = MibTableColumn
crcERSpanIpType = _CrcERSpanIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 5),
    _CrcERSpanIpType_Type()
)
crcERSpanIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIpType.setStatus("current")
_CrcERSpanIp_Type = InetAddress
_CrcERSpanIp_Object = MibTableColumn
crcERSpanIp = _CrcERSpanIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 6),
    _CrcERSpanIp_Type()
)
crcERSpanIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIp.setStatus("current")


class _CrcSrcERSpanIpTTL_Type(Unsigned32):
    """Custom type crcSrcERSpanIpTTL based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CrcSrcERSpanIpTTL_Type.__name__ = "Unsigned32"
_CrcSrcERSpanIpTTL_Object = MibTableColumn
crcSrcERSpanIpTTL = _CrcSrcERSpanIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 7),
    _CrcSrcERSpanIpTTL_Type()
)
crcSrcERSpanIpTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanIpTTL.setStatus("current")


class _CrcSrcERSpanDscpOrPrec_Type(Integer32):
    """Custom type crcSrcERSpanDscpOrPrec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("precedence", 2))
    )


_CrcSrcERSpanDscpOrPrec_Type.__name__ = "Integer32"
_CrcSrcERSpanDscpOrPrec_Object = MibTableColumn
crcSrcERSpanDscpOrPrec = _CrcSrcERSpanDscpOrPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 8),
    _CrcSrcERSpanDscpOrPrec_Type()
)
crcSrcERSpanDscpOrPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanDscpOrPrec.setStatus("current")


class _CrcSrcERSpanIpPrec_Type(Unsigned32):
    """Custom type crcSrcERSpanIpPrec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CrcSrcERSpanIpPrec_Type.__name__ = "Unsigned32"
_CrcSrcERSpanIpPrec_Object = MibTableColumn
crcSrcERSpanIpPrec = _CrcSrcERSpanIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 9),
    _CrcSrcERSpanIpPrec_Type()
)
crcSrcERSpanIpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanIpPrec.setStatus("current")


class _CrcSrcERSpanIpDscp_Type(Dscp):
    """Custom type crcSrcERSpanIpDscp based on Dscp"""
    defaultValue = 0


_CrcSrcERSpanIpDscp_Object = MibTableColumn
crcSrcERSpanIpDscp = _CrcSrcERSpanIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 10),
    _CrcSrcERSpanIpDscp_Type()
)
crcSrcERSpanIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanIpDscp.setStatus("current")


class _CrcERSpanIpVRF_Type(SnmpAdminString):
    """Custom type crcERSpanIpVRF based on SnmpAdminString"""
    defaultHexValue = ""


_CrcERSpanIpVRF_Object = MibTableColumn
crcERSpanIpVRF = _CrcERSpanIpVRF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 11),
    _CrcERSpanIpVRF_Type()
)
crcERSpanIpVRF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIpVRF.setStatus("current")


class _CrcSrcERSpanLoVlanMask_Type(OctetString):
    """Custom type crcSrcERSpanLoVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CrcSrcERSpanLoVlanMask_Type.__name__ = "OctetString"
_CrcSrcERSpanLoVlanMask_Object = MibTableColumn
crcSrcERSpanLoVlanMask = _CrcSrcERSpanLoVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 12),
    _CrcSrcERSpanLoVlanMask_Type()
)
crcSrcERSpanLoVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanLoVlanMask.setStatus("current")


class _CrcSrcERSpanHiVlanMask_Type(OctetString):
    """Custom type crcSrcERSpanHiVlanMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CrcSrcERSpanHiVlanMask_Type.__name__ = "OctetString"
_CrcSrcERSpanHiVlanMask_Object = MibTableColumn
crcSrcERSpanHiVlanMask = _CrcSrcERSpanHiVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 13),
    _CrcSrcERSpanHiVlanMask_Type()
)
crcSrcERSpanHiVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanHiVlanMask.setStatus("current")


class _CrcSrcERSpanOrigIpType_Type(InetAddressType):
    """Custom type crcSrcERSpanOrigIpType based on InetAddressType"""


_CrcSrcERSpanOrigIpType_Object = MibTableColumn
crcSrcERSpanOrigIpType = _CrcSrcERSpanOrigIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 14),
    _CrcSrcERSpanOrigIpType_Type()
)
crcSrcERSpanOrigIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanOrigIpType.setStatus("current")
_CrcSrcERSpanOrigIp_Type = InetAddress
_CrcSrcERSpanOrigIp_Object = MibTableColumn
crcSrcERSpanOrigIp = _CrcSrcERSpanOrigIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 15),
    _CrcSrcERSpanOrigIp_Type()
)
crcSrcERSpanOrigIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSrcERSpanOrigIp.setStatus("current")


class _CrcDstERSpanOption_Type(Bits):
    """Custom type crcDstERSpanOption based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("inpkts", 0),
          ("learningDisable", 1))
    )

_CrcDstERSpanOption_Type.__name__ = "Bits"
_CrcDstERSpanOption_Object = MibTableColumn
crcDstERSpanOption = _CrcDstERSpanOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 16),
    _CrcDstERSpanOption_Type()
)
crcDstERSpanOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcDstERSpanOption.setStatus("deprecated")
_CrcERSpanSessionRowStatus_Type = RowStatus
_CrcERSpanSessionRowStatus_Object = MibTableColumn
crcERSpanSessionRowStatus = _CrcERSpanSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 5, 1, 17),
    _CrcERSpanSessionRowStatus_Type()
)
crcERSpanSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanSessionRowStatus.setStatus("current")
_CrcERSpanIFTable_Object = MibTable
crcERSpanIFTable = _CrcERSpanIFTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6)
)
if mibBuilder.loadTexts:
    crcERSpanIFTable.setStatus("current")
_CrcERSpanIFEntry_Object = MibTableRow
crcERSpanIFEntry = _CrcERSpanIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6, 1)
)
crcERSpanIFEntry.setIndexNames(
    (0, "CISCO-RMON-CONFIG-MIB", "crcERSpanSessionNo"),
    (0, "CISCO-RMON-CONFIG-MIB", "crcERSpanIFIndex"),
)
if mibBuilder.loadTexts:
    crcERSpanIFEntry.setStatus("current")
_CrcERSpanIFIndex_Type = InterfaceIndex
_CrcERSpanIFIndex_Object = MibTableColumn
crcERSpanIFIndex = _CrcERSpanIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6, 1, 1),
    _CrcERSpanIFIndex_Type()
)
crcERSpanIFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crcERSpanIFIndex.setStatus("current")


class _CrcERSpanIFDirection_Type(Integer32):
    """Custom type crcERSpanIFDirection based on Integer32"""
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
        *(("copyBoth", 3),
          ("copyRxOnly", 1),
          ("copyTxOnly", 2))
    )


_CrcERSpanIFDirection_Type.__name__ = "Integer32"
_CrcERSpanIFDirection_Object = MibTableColumn
crcERSpanIFDirection = _CrcERSpanIFDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6, 1, 2),
    _CrcERSpanIFDirection_Type()
)
crcERSpanIFDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIFDirection.setStatus("current")
_CrcERSpanIFRowStatus_Type = RowStatus
_CrcERSpanIFRowStatus_Object = MibTableColumn
crcERSpanIFRowStatus = _CrcERSpanIFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6, 1, 3),
    _CrcERSpanIFRowStatus_Type()
)
crcERSpanIFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIFRowStatus.setStatus("current")


class _CrcERSpanIFOption_Type(Bits):
    """Custom type crcERSpanIFOption based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("inpkts", 0),
          ("learningDisable", 1))
    )

_CrcERSpanIFOption_Type.__name__ = "Bits"
_CrcERSpanIFOption_Object = MibTableColumn
crcERSpanIFOption = _CrcERSpanIFOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 6, 1, 4),
    _CrcERSpanIFOption_Type()
)
crcERSpanIFOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcERSpanIFOption.setStatus("current")
_CrcSpanDstPermitListEnabled_Type = TruthValue
_CrcSpanDstPermitListEnabled_Object = MibScalar
crcSpanDstPermitListEnabled = _CrcSpanDstPermitListEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 7),
    _CrcSpanDstPermitListEnabled_Type()
)
crcSpanDstPermitListEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcSpanDstPermitListEnabled.setStatus("current")
_CrcSpanDstPermitListTable_Object = MibTable
crcSpanDstPermitListTable = _CrcSpanDstPermitListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 8)
)
if mibBuilder.loadTexts:
    crcSpanDstPermitListTable.setStatus("current")
_CrcSpanDstPermitListEntry_Object = MibTableRow
crcSpanDstPermitListEntry = _CrcSpanDstPermitListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 8, 1)
)
crcSpanDstPermitListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    crcSpanDstPermitListEntry.setStatus("current")
_CrcSpanDstPermitListRowStatus_Type = RowStatus
_CrcSpanDstPermitListRowStatus_Object = MibTableColumn
crcSpanDstPermitListRowStatus = _CrcSpanDstPermitListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 2, 8, 1, 1),
    _CrcSpanDstPermitListRowStatus_Type()
)
crcSpanDstPermitListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crcSpanDstPermitListRowStatus.setStatus("current")
_CiscoSampleConfigObjects_ObjectIdentity = ObjectIdentity
ciscoSampleConfigObjects = _CiscoSampleConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 3)
)
_RmonSampleConfigTable_Object = MibTable
rmonSampleConfigTable = _RmonSampleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rmonSampleConfigTable.setStatus("current")
_RmonSampleConfigEntry_Object = MibTableRow
rmonSampleConfigEntry = _RmonSampleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 3, 1, 1)
)
rmonSampleConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rmonSampleConfigEntry.setStatus("current")


class _RmonSamplingEnabled_Type(TruthValue):
    """Custom type rmonSamplingEnabled based on TruthValue"""


_RmonSamplingEnabled_Object = MibTableColumn
rmonSamplingEnabled = _RmonSamplingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 3, 1, 1, 1),
    _RmonSamplingEnabled_Type()
)
rmonSamplingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonSamplingEnabled.setStatus("current")
_CiscoAlarmConfigObjects_ObjectIdentity = ObjectIdentity
ciscoAlarmConfigObjects = _CiscoAlarmConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 4)
)


class _RmonMaxAlarms_Type(Unsigned32):
    """Custom type rmonMaxAlarms based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmonMaxAlarms_Type.__name__ = "Unsigned32"
_RmonMaxAlarms_Object = MibScalar
rmonMaxAlarms = _RmonMaxAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 4, 1),
    _RmonMaxAlarms_Type()
)
rmonMaxAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonMaxAlarms.setStatus("current")


class _RmonAlarmEnable_Type(TruthValue):
    """Custom type rmonAlarmEnable based on TruthValue"""


_RmonAlarmEnable_Object = MibScalar
rmonAlarmEnable = _RmonAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 4, 2),
    _RmonAlarmEnable_Type()
)
rmonAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAlarmEnable.setStatus("current")
_RmonConfiguredAlarms_Type = Unsigned32
_RmonConfiguredAlarms_Object = MibScalar
rmonConfiguredAlarms = _RmonConfiguredAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 4, 3),
    _RmonConfiguredAlarms_Type()
)
rmonConfiguredAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonConfiguredAlarms.setStatus("current")
_RmonConfiguredHcAlarms_Type = Unsigned32
_RmonConfiguredHcAlarms_Object = MibScalar
rmonConfiguredHcAlarms = _RmonConfiguredHcAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 4, 4),
    _RmonConfiguredHcAlarms_Type()
)
rmonConfiguredHcAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonConfiguredHcAlarms.setStatus("current")
_CiscoSpanTxReplicationObjects_ObjectIdentity = ObjectIdentity
ciscoSpanTxReplicationObjects = _CiscoSpanTxReplicationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 5)
)
_CrcSpanEgressReplicationMode_Type = SpanTxReplicationMode
_CrcSpanEgressReplicationMode_Object = MibScalar
crcSpanEgressReplicationMode = _CrcSpanEgressReplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 5, 1),
    _CrcSpanEgressReplicationMode_Type()
)
crcSpanEgressReplicationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcSpanEgressReplicationMode.setStatus("current")
_CrcSpanSessionEgressModeTable_Object = MibTable
crcSpanSessionEgressModeTable = _CrcSpanSessionEgressModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 5, 2)
)
if mibBuilder.loadTexts:
    crcSpanSessionEgressModeTable.setStatus("current")
_CrcSpanSessionEgressModeEntry_Object = MibTableRow
crcSpanSessionEgressModeEntry = _CrcSpanSessionEgressModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 5, 2, 1)
)
crcSpanSessionEgressModeEntry.setIndexNames(
    (0, "CISCO-RMON-CONFIG-MIB", "crcSpanSessionNo"),
)
if mibBuilder.loadTexts:
    crcSpanSessionEgressModeEntry.setStatus("current")
_CrcSpanEgressReplicationOperMode_Type = SpanTxReplicationMode
_CrcSpanEgressReplicationOperMode_Object = MibTableColumn
crcSpanEgressReplicationOperMode = _CrcSpanEgressReplicationOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 5, 2, 1, 1),
    _CrcSpanEgressReplicationOperMode_Type()
)
crcSpanEgressReplicationOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanEgressReplicationOperMode.setStatus("current")
_CiscoSpanCapacityObjects_ObjectIdentity = ObjectIdentity
ciscoSpanCapacityObjects = _CiscoSpanCapacityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6)
)
_CrcSpanCapacityTable_Object = MibTable
crcSpanCapacityTable = _CrcSpanCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1)
)
if mibBuilder.loadTexts:
    crcSpanCapacityTable.setStatus("current")
_CrcSpanCapacityEntry_Object = MibTableRow
crcSpanCapacityEntry = _CrcSpanCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1, 1)
)
crcSpanCapacityEntry.setIndexNames(
    (0, "CISCO-RMON-CONFIG-MIB", "crcSpanCapacityType"),
)
if mibBuilder.loadTexts:
    crcSpanCapacityEntry.setStatus("current")


class _CrcSpanCapacityType_Type(Integer32):
    """Custom type crcSpanCapacityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("allDst", 2),
          ("allSrc", 1),
          ("capture", 11),
          ("erspanDst", 8),
          ("erspanSrc", 7),
          ("localSrc", 3),
          ("localTx", 4),
          ("oamLoopback", 10),
          ("reflector", 12),
          ("rspanDst", 6),
          ("rspanSrc", 5),
          ("serviceModule", 9))
    )


_CrcSpanCapacityType_Type.__name__ = "Integer32"
_CrcSpanCapacityType_Object = MibTableColumn
crcSpanCapacityType = _CrcSpanCapacityType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1, 1, 1),
    _CrcSpanCapacityType_Type()
)
crcSpanCapacityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crcSpanCapacityType.setStatus("current")


class _CrcSpanCapacityShared_Type(Integer32):
    """Custom type crcSpanCapacityShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 3),
          ("none", 1),
          ("source", 2))
    )


_CrcSpanCapacityShared_Type.__name__ = "Integer32"
_CrcSpanCapacityShared_Object = MibTableColumn
crcSpanCapacityShared = _CrcSpanCapacityShared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1, 1, 2),
    _CrcSpanCapacityShared_Type()
)
crcSpanCapacityShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanCapacityShared.setStatus("current")
_CrcSpanMaxSession_Type = Unsigned32
_CrcSpanMaxSession_Object = MibTableColumn
crcSpanMaxSession = _CrcSpanMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1, 1, 3),
    _CrcSpanMaxSession_Type()
)
crcSpanMaxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanMaxSession.setStatus("current")
_CrcSpanUsedSession_Type = Unsigned32
_CrcSpanUsedSession_Object = MibTableColumn
crcSpanUsedSession = _CrcSpanUsedSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 1, 1, 4),
    _CrcSpanUsedSession_Type()
)
crcSpanUsedSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanUsedSession.setStatus("current")
_CrcSpanSharedSource_Type = Unsigned32
_CrcSpanSharedSource_Object = MibScalar
crcSpanSharedSource = _CrcSpanSharedSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 2),
    _CrcSpanSharedSource_Type()
)
crcSpanSharedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanSharedSource.setStatus("current")
_CrcSpanSharedDestination_Type = Unsigned32
_CrcSpanSharedDestination_Object = MibScalar
crcSpanSharedDestination = _CrcSpanSharedDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 1, 6, 3),
    _CrcSpanSharedDestination_Type()
)
crcSpanSharedDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crcSpanSharedDestination.setStatus("current")
_CiscoRmonConfigNotifications_ObjectIdentity = ObjectIdentity
ciscoRmonConfigNotifications = _CiscoRmonConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 2)
)
_CiscoRmonConfigConformance_ObjectIdentity = ObjectIdentity
ciscoRmonConfigConformance = _CiscoRmonConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3)
)
_CiscoRmonConfigCompliances_ObjectIdentity = ObjectIdentity
ciscoRmonConfigCompliances = _CiscoRmonConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1)
)
_CiscoRmonConfigGroups_ObjectIdentity = ObjectIdentity
ciscoRmonConfigGroups = _CiscoRmonConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2)
)
portCopyEntry.registerAugmentions(
    ("CISCO-RMON-CONFIG-MIB",
     "portCopyXEntry")
)
portCopyXEntry.setIndexNames(*portCopyEntry.getIndexNames())

# Managed Objects groups

rmon2ExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 1)
)
rmon2ExtensionsGroup.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "rmonTimeFilterMode")
)
if mibBuilder.loadTexts:
    rmon2ExtensionsGroup.setStatus("current")

smonExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 2)
)
smonExtensionsGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopyLoVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyHiVlanMask"))
)
if mibBuilder.loadTexts:
    smonExtensionsGroup.setStatus("current")

rmonSampleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 3)
)
rmonSampleConfigGroup.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "rmonSamplingEnabled")
)
if mibBuilder.loadTexts:
    rmonSampleConfigGroup.setStatus("current")

smonExtensions2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 4)
)
smonExtensions2Group.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopyDestLoVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyDestHiVlanMask"))
)
if mibBuilder.loadTexts:
    smonExtensions2Group.setStatus("current")

smonExtensions3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 5)
)
smonExtensions3Group.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "portCopyOption")
)
if mibBuilder.loadTexts:
    smonExtensions3Group.setStatus("deprecated")

smonExtensions4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 6)
)
smonExtensions4Group.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopySessionNo"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyRemoveSrc"))
)
if mibBuilder.loadTexts:
    smonExtensions4Group.setStatus("current")

smonExtensions5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 7)
)
smonExtensions5Group.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "portCopySessionType")
)
if mibBuilder.loadTexts:
    smonExtensions5Group.setStatus("current")

smonExtensions6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 8)
)
smonExtensions6Group.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopyMaxIngressSessions"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyMaxEgressSessions"))
)
if mibBuilder.loadTexts:
    smonExtensions6Group.setStatus("current")

smonExtensions7Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 9)
)
smonExtensions7Group.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopySessionType"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyReflectorPort"))
)
if mibBuilder.loadTexts:
    smonExtensions7Group.setStatus("current")

rmonAlarmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 10)
)
rmonAlarmConfigGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "rmonMaxAlarms"),
        ("CISCO-RMON-CONFIG-MIB", "rmonAlarmEnable"))
)
if mibBuilder.loadTexts:
    rmonAlarmConfigGroup.setStatus("current")

smonExtensions8Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 11)
)
smonExtensions8Group.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "portCopyOption"),
        ("CISCO-RMON-CONFIG-MIB", "portCopyInpktVlan"))
)
if mibBuilder.loadTexts:
    smonExtensions8Group.setStatus("current")

crcSpanSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 12)
)
crcSpanSessionGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcSpanSessionType"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanSessionEnabled"))
)
if mibBuilder.loadTexts:
    crcSpanSessionGroup.setStatus("current")

crcERSpanSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 13)
)
crcERSpanSessionGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionType"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionDescr"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanEncapID"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIpType"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIp"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpTTL"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanDscpOrPrec"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpPrec"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpDscp"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIpVRF"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanLoVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanHiVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanOrigIpType"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanOrigIp"),
        ("CISCO-RMON-CONFIG-MIB", "crcDstERSpanOption"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionRowStatus"))
)
if mibBuilder.loadTexts:
    crcERSpanSessionGroup.setStatus("deprecated")

crcERSpanIFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 14)
)
crcERSpanIFGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcERSpanIFDirection"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIFRowStatus"))
)
if mibBuilder.loadTexts:
    crcERSpanIFGroup.setStatus("current")

crcSpanDstPermitListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 15)
)
crcSpanDstPermitListGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcSpanDstPermitListEnabled"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanDstPermitListRowStatus"))
)
if mibBuilder.loadTexts:
    crcSpanDstPermitListGroup.setStatus("current")

smonExtensions9Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 16)
)
smonExtensions9Group.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "crcSpanSessionDescr")
)
if mibBuilder.loadTexts:
    smonExtensions9Group.setStatus("current")

crcERSpanIFOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 17)
)
crcERSpanIFOptionGroup.setObjects(
    ("CISCO-RMON-CONFIG-MIB", "crcERSpanIFOption")
)
if mibBuilder.loadTexts:
    crcERSpanIFOptionGroup.setStatus("current")

crcERSpanSessionGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 18)
)
crcERSpanSessionGroupRev1.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionType"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionDescr"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanEncapID"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIpType"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIp"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpTTL"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanDscpOrPrec"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpPrec"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanIpDscp"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanIpVRF"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanLoVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanHiVlanMask"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanOrigIpType"),
        ("CISCO-RMON-CONFIG-MIB", "crcSrcERSpanOrigIp"),
        ("CISCO-RMON-CONFIG-MIB", "crcERSpanSessionRowStatus"))
)
if mibBuilder.loadTexts:
    crcERSpanSessionGroupRev1.setStatus("current")

crcSpanEgressReplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 19)
)
crcSpanEgressReplicationGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcSpanEgressReplicationMode"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanEgressReplicationOperMode"))
)
if mibBuilder.loadTexts:
    crcSpanEgressReplicationGroup.setStatus("current")

crcSpanCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 20)
)
crcSpanCapacityGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "crcSpanCapacityShared"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanMaxSession"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanUsedSession"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanSharedSource"),
        ("CISCO-RMON-CONFIG-MIB", "crcSpanSharedDestination"))
)
if mibBuilder.loadTexts:
    crcSpanCapacityGroup.setStatus("current")

rmonAlarmCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 2, 21)
)
rmonAlarmCapacityGroup.setObjects(
      *(("CISCO-RMON-CONFIG-MIB", "rmonConfiguredAlarms"),
        ("CISCO-RMON-CONFIG-MIB", "rmonConfiguredHcAlarms"))
)
if mibBuilder.loadTexts:
    rmonAlarmCapacityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRmonConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigCompliance.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev1.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev2.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev3.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev4.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev5.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev6.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev7.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev8.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev9.setStatus(
        "deprecated"
    )

ciscoRmonConfigComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 103, 3, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoRmonConfigComplianceRev10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RMON-CONFIG-MIB",
    **{"SpanTxReplicationMode": SpanTxReplicationMode,
       "ciscoRmonConfigMIB": ciscoRmonConfigMIB,
       "ciscoRmonConfigObjects": ciscoRmonConfigObjects,
       "ciscoRmon2ConfigObjects": ciscoRmon2ConfigObjects,
       "rmonTimeFilterMode": rmonTimeFilterMode,
       "ciscoSmonConfigObjects": ciscoSmonConfigObjects,
       "portCopyXTable": portCopyXTable,
       "portCopyXEntry": portCopyXEntry,
       "portCopyLoVlanMask": portCopyLoVlanMask,
       "portCopyHiVlanMask": portCopyHiVlanMask,
       "portCopyDestLoVlanMask": portCopyDestLoVlanMask,
       "portCopyDestHiVlanMask": portCopyDestHiVlanMask,
       "portCopyOption": portCopyOption,
       "portCopySessionNo": portCopySessionNo,
       "portCopySessionType": portCopySessionType,
       "portCopyRemoveSrc": portCopyRemoveSrc,
       "portCopyReflectorPort": portCopyReflectorPort,
       "portCopyInpktVlan": portCopyInpktVlan,
       "portCopyMaxIngressSessions": portCopyMaxIngressSessions,
       "portCopyMaxEgressSessions": portCopyMaxEgressSessions,
       "crcSpanSessionTable": crcSpanSessionTable,
       "crcSpanSessionEntry": crcSpanSessionEntry,
       "crcSpanSessionNo": crcSpanSessionNo,
       "crcSpanSessionType": crcSpanSessionType,
       "crcSpanSessionEnabled": crcSpanSessionEnabled,
       "crcSpanSessionDescr": crcSpanSessionDescr,
       "crcERSpanSessionTable": crcERSpanSessionTable,
       "crcERSpanSessionEntry": crcERSpanSessionEntry,
       "crcERSpanSessionNo": crcERSpanSessionNo,
       "crcERSpanSessionType": crcERSpanSessionType,
       "crcERSpanSessionDescr": crcERSpanSessionDescr,
       "crcERSpanEncapID": crcERSpanEncapID,
       "crcERSpanIpType": crcERSpanIpType,
       "crcERSpanIp": crcERSpanIp,
       "crcSrcERSpanIpTTL": crcSrcERSpanIpTTL,
       "crcSrcERSpanDscpOrPrec": crcSrcERSpanDscpOrPrec,
       "crcSrcERSpanIpPrec": crcSrcERSpanIpPrec,
       "crcSrcERSpanIpDscp": crcSrcERSpanIpDscp,
       "crcERSpanIpVRF": crcERSpanIpVRF,
       "crcSrcERSpanLoVlanMask": crcSrcERSpanLoVlanMask,
       "crcSrcERSpanHiVlanMask": crcSrcERSpanHiVlanMask,
       "crcSrcERSpanOrigIpType": crcSrcERSpanOrigIpType,
       "crcSrcERSpanOrigIp": crcSrcERSpanOrigIp,
       "crcDstERSpanOption": crcDstERSpanOption,
       "crcERSpanSessionRowStatus": crcERSpanSessionRowStatus,
       "crcERSpanIFTable": crcERSpanIFTable,
       "crcERSpanIFEntry": crcERSpanIFEntry,
       "crcERSpanIFIndex": crcERSpanIFIndex,
       "crcERSpanIFDirection": crcERSpanIFDirection,
       "crcERSpanIFRowStatus": crcERSpanIFRowStatus,
       "crcERSpanIFOption": crcERSpanIFOption,
       "crcSpanDstPermitListEnabled": crcSpanDstPermitListEnabled,
       "crcSpanDstPermitListTable": crcSpanDstPermitListTable,
       "crcSpanDstPermitListEntry": crcSpanDstPermitListEntry,
       "crcSpanDstPermitListRowStatus": crcSpanDstPermitListRowStatus,
       "ciscoSampleConfigObjects": ciscoSampleConfigObjects,
       "rmonSampleConfigTable": rmonSampleConfigTable,
       "rmonSampleConfigEntry": rmonSampleConfigEntry,
       "rmonSamplingEnabled": rmonSamplingEnabled,
       "ciscoAlarmConfigObjects": ciscoAlarmConfigObjects,
       "rmonMaxAlarms": rmonMaxAlarms,
       "rmonAlarmEnable": rmonAlarmEnable,
       "rmonConfiguredAlarms": rmonConfiguredAlarms,
       "rmonConfiguredHcAlarms": rmonConfiguredHcAlarms,
       "ciscoSpanTxReplicationObjects": ciscoSpanTxReplicationObjects,
       "crcSpanEgressReplicationMode": crcSpanEgressReplicationMode,
       "crcSpanSessionEgressModeTable": crcSpanSessionEgressModeTable,
       "crcSpanSessionEgressModeEntry": crcSpanSessionEgressModeEntry,
       "crcSpanEgressReplicationOperMode": crcSpanEgressReplicationOperMode,
       "ciscoSpanCapacityObjects": ciscoSpanCapacityObjects,
       "crcSpanCapacityTable": crcSpanCapacityTable,
       "crcSpanCapacityEntry": crcSpanCapacityEntry,
       "crcSpanCapacityType": crcSpanCapacityType,
       "crcSpanCapacityShared": crcSpanCapacityShared,
       "crcSpanMaxSession": crcSpanMaxSession,
       "crcSpanUsedSession": crcSpanUsedSession,
       "crcSpanSharedSource": crcSpanSharedSource,
       "crcSpanSharedDestination": crcSpanSharedDestination,
       "ciscoRmonConfigNotifications": ciscoRmonConfigNotifications,
       "ciscoRmonConfigConformance": ciscoRmonConfigConformance,
       "ciscoRmonConfigCompliances": ciscoRmonConfigCompliances,
       "ciscoRmonConfigCompliance": ciscoRmonConfigCompliance,
       "ciscoRmonConfigComplianceRev1": ciscoRmonConfigComplianceRev1,
       "ciscoRmonConfigComplianceRev2": ciscoRmonConfigComplianceRev2,
       "ciscoRmonConfigComplianceRev3": ciscoRmonConfigComplianceRev3,
       "ciscoRmonConfigComplianceRev4": ciscoRmonConfigComplianceRev4,
       "ciscoRmonConfigComplianceRev5": ciscoRmonConfigComplianceRev5,
       "ciscoRmonConfigComplianceRev6": ciscoRmonConfigComplianceRev6,
       "ciscoRmonConfigComplianceRev7": ciscoRmonConfigComplianceRev7,
       "ciscoRmonConfigComplianceRev8": ciscoRmonConfigComplianceRev8,
       "ciscoRmonConfigComplianceRev9": ciscoRmonConfigComplianceRev9,
       "ciscoRmonConfigComplianceRev10": ciscoRmonConfigComplianceRev10,
       "ciscoRmonConfigGroups": ciscoRmonConfigGroups,
       "rmon2ExtensionsGroup": rmon2ExtensionsGroup,
       "smonExtensionsGroup": smonExtensionsGroup,
       "rmonSampleConfigGroup": rmonSampleConfigGroup,
       "smonExtensions2Group": smonExtensions2Group,
       "smonExtensions3Group": smonExtensions3Group,
       "smonExtensions4Group": smonExtensions4Group,
       "smonExtensions5Group": smonExtensions5Group,
       "smonExtensions6Group": smonExtensions6Group,
       "smonExtensions7Group": smonExtensions7Group,
       "rmonAlarmConfigGroup": rmonAlarmConfigGroup,
       "smonExtensions8Group": smonExtensions8Group,
       "crcSpanSessionGroup": crcSpanSessionGroup,
       "crcERSpanSessionGroup": crcERSpanSessionGroup,
       "crcERSpanIFGroup": crcERSpanIFGroup,
       "crcSpanDstPermitListGroup": crcSpanDstPermitListGroup,
       "smonExtensions9Group": smonExtensions9Group,
       "crcERSpanIFOptionGroup": crcERSpanIFOptionGroup,
       "crcERSpanSessionGroupRev1": crcERSpanSessionGroupRev1,
       "crcSpanEgressReplicationGroup": crcSpanEgressReplicationGroup,
       "crcSpanCapacityGroup": crcSpanCapacityGroup,
       "rmonAlarmCapacityGroup": rmonAlarmCapacityGroup}
)
