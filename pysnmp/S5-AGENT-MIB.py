# SNMP MIB module (S5-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:14 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(s5Agent,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Agent")

(IpxAddress,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "IpxAddress",
    "TimeIntervalSec")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

s5AgentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 8)
)
s5AgentMib.setRevisions(
        ("2015-03-17 00:00",
         "2015-03-10 00:00",
         "2015-03-02 00:00",
         "2015-01-07 00:00",
         "2014-12-19 00:00",
         "2014-08-20 00:00",
         "2014-04-09 00:00",
         "2014-04-07 00:00",
         "2013-11-28 00:00",
         "2013-11-26 00:00",
         "2013-07-29 00:00",
         "2013-04-24 00:00",
         "2013-04-04 00:00",
         "2013-03-05 00:00",
         "2013-02-13 00:00",
         "2013-01-17 00:00",
         "2012-11-28 00:00",
         "2012-10-10 00:00",
         "2012-10-04 00:00",
         "2012-09-13 00:00",
         "2012-09-13 00:00",
         "2012-08-14 00:00",
         "2012-07-17 00:00",
         "2012-07-03 00:00",
         "2012-06-26 00:00",
         "2012-06-01 00:00",
         "2012-05-07 00:00",
         "2012-04-06 00:00",
         "2012-03-29 00:00",
         "2012-03-09 00:00",
         "2012-02-21 00:00",
         "2012-02-17 00:00",
         "2011-09-13 00:00",
         "2011-03-25 00:00",
         "2011-02-08 00:00",
         "2010-12-01 00:00",
         "2010-11-03 00:00",
         "2010-10-14 00:00",
         "2010-09-20 00:00",
         "2010-09-14 00:00",
         "2010-08-11 00:00",
         "2010-08-10 00:00",
         "2010-07-21 00:00",
         "2010-04-15 00:00",
         "2010-01-29 00:00",
         "2009-12-14 00:00",
         "2009-11-16 00:00",
         "2009-10-23 00:00",
         "2009-10-20 00:00",
         "2009-09-24 00:00",
         "2009-09-10 00:00",
         "2009-07-23 00:00",
         "2009-07-13 00:00",
         "2009-06-07 00:00",
         "2009-01-05 00:00",
         "2008-10-21 00:00",
         "2008-07-24 00:01",
         "2008-07-24 00:00",
         "2008-03-04 00:00",
         "2008-01-28 00:00",
         "2008-01-25 00:00",
         "2007-12-10 00:00",
         "2007-12-05 00:00",
         "2007-11-04 00:00",
         "2007-09-19 00:00",
         "2007-09-04 00:00",
         "2007-08-21 00:00",
         "2007-05-11 00:00",
         "2007-05-03 00:00",
         "2007-03-05 00:00",
         "2007-02-27 00:00",
         "2007-02-16 00:00",
         "2007-01-08 00:00",
         "2006-11-07 00:00",
         "2006-09-19 00:00",
         "2006-08-28 00:00",
         "2006-08-14 00:00",
         "2006-08-07 00:00",
         "2006-04-05 00:00",
         "2006-03-22 00:00",
         "2006-03-07 00:00",
         "2006-02-14 00:00",
         "2005-10-11 00:00",
         "2005-09-30 00:00",
         "2005-05-13 00:00",
         "2005-05-11 00:00",
         "2005-05-04 00:00",
         "2005-04-22 00:00",
         "2005-03-24 00:00",
         "2005-03-22 00:00",
         "2004-12-09 00:00",
         "2004-11-09 00:00",
         "2004-09-30 00:00",
         "2004-06-18 00:00",
         "2003-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5AgentHw_ObjectIdentity = ObjectIdentity
s5AgentHw = _S5AgentHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 1)
)


class _S5AgMyGrpIndx_Type(Integer32):
    """Custom type s5AgMyGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5AgMyGrpIndx_Type.__name__ = "Integer32"
_S5AgMyGrpIndx_Object = MibScalar
s5AgMyGrpIndx = _S5AgMyGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 1, 1),
    _S5AgMyGrpIndx_Type()
)
s5AgMyGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyGrpIndx.setStatus("current")


class _S5AgMyComIndx_Type(Integer32):
    """Custom type s5AgMyComIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5AgMyComIndx_Type.__name__ = "Integer32"
_S5AgMyComIndx_Object = MibScalar
s5AgMyComIndx = _S5AgMyComIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 1, 2),
    _S5AgMyComIndx_Type()
)
s5AgMyComIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyComIndx.setStatus("current")
_S5AgentInfo_ObjectIdentity = ObjectIdentity
s5AgentInfo = _S5AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2)
)
_S5AgentGbl_ObjectIdentity = ObjectIdentity
s5AgentGbl = _S5AgentGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1)
)


class _S5AgInfoReBoot_Type(Integer32):
    """Custom type s5AgInfoReBoot based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("download", 6),
          ("downloadAndReboot", 8),
          ("downloadAndReset", 9),
          ("downloadAndRestart", 7),
          ("other", 1),
          ("reboot", 4),
          ("reset", 5),
          ("restart", 3),
          ("running", 2))
    )


_S5AgInfoReBoot_Type.__name__ = "Integer32"
_S5AgInfoReBoot_Object = MibScalar
s5AgInfoReBoot = _S5AgInfoReBoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 1),
    _S5AgInfoReBoot_Type()
)
s5AgInfoReBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoReBoot.setStatus("current")


class _S5AgInfoWriteCfg_Type(Integer32):
    """Custom type s5AgInfoWriteCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("valid", 2),
          ("write", 3))
    )


_S5AgInfoWriteCfg_Type.__name__ = "Integer32"
_S5AgInfoWriteCfg_Object = MibScalar
s5AgInfoWriteCfg = _S5AgInfoWriteCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 2),
    _S5AgInfoWriteCfg_Type()
)
s5AgInfoWriteCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoWriteCfg.setStatus("current")


class _S5AgInfoMgmtProtocolNxtBoot_Type(Integer32):
    """Custom type s5AgInfoMgmtProtocolNxtBoot based on Integer32"""
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
        *(("ipAndIpx", 4),
          ("ipOnly", 2),
          ("ipxOnly", 3),
          ("other", 1))
    )


_S5AgInfoMgmtProtocolNxtBoot_Type.__name__ = "Integer32"
_S5AgInfoMgmtProtocolNxtBoot_Object = MibScalar
s5AgInfoMgmtProtocolNxtBoot = _S5AgInfoMgmtProtocolNxtBoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 3),
    _S5AgInfoMgmtProtocolNxtBoot_Type()
)
s5AgInfoMgmtProtocolNxtBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoMgmtProtocolNxtBoot.setStatus("current")


class _S5AgInfoMgmtProtocolCur_Type(Integer32):
    """Custom type s5AgInfoMgmtProtocolCur based on Integer32"""
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
        *(("ipAndIpx", 4),
          ("ipOnly", 2),
          ("ipxOnly", 3),
          ("other", 1))
    )


_S5AgInfoMgmtProtocolCur_Type.__name__ = "Integer32"
_S5AgInfoMgmtProtocolCur_Object = MibScalar
s5AgInfoMgmtProtocolCur = _S5AgInfoMgmtProtocolCur_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 4),
    _S5AgInfoMgmtProtocolCur_Type()
)
s5AgInfoMgmtProtocolCur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoMgmtProtocolCur.setStatus("current")


class _S5AgInfoBootMode_Type(Integer32):
    """Custom type s5AgInfoBootMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 6),
          ("dhcpOrLastAddress", 8),
          ("dhcpWhenNeeded", 7),
          ("local", 2),
          ("net", 3),
          ("netOrLastAddress", 5),
          ("netWhenNeeded", 4),
          ("other", 1))
    )


_S5AgInfoBootMode_Type.__name__ = "Integer32"
_S5AgInfoBootMode_Object = MibScalar
s5AgInfoBootMode = _S5AgInfoBootMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 5),
    _S5AgInfoBootMode_Type()
)
s5AgInfoBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoBootMode.setStatus("current")


class _S5AgInfoCfgLoadMode_Type(Integer32):
    """Custom type s5AgInfoCfgLoadMode based on Integer32"""
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
        *(("locAsBk", 4),
          ("local", 2),
          ("net", 3),
          ("other", 1))
    )


_S5AgInfoCfgLoadMode_Type.__name__ = "Integer32"
_S5AgInfoCfgLoadMode_Object = MibScalar
s5AgInfoCfgLoadMode = _S5AgInfoCfgLoadMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 6),
    _S5AgInfoCfgLoadMode_Type()
)
s5AgInfoCfgLoadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoCfgLoadMode.setStatus("current")


class _S5AgInfoImgLoadMode_Type(Integer32):
    """Custom type s5AgInfoImgLoadMode based on Integer32"""
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
        *(("locAsBk", 4),
          ("local", 2),
          ("net", 3),
          ("netIfNewer", 5),
          ("other", 1))
    )


_S5AgInfoImgLoadMode_Type.__name__ = "Integer32"
_S5AgInfoImgLoadMode_Object = MibScalar
s5AgInfoImgLoadMode = _S5AgInfoImgLoadMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 7),
    _S5AgInfoImgLoadMode_Type()
)
s5AgInfoImgLoadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoImgLoadMode.setStatus("current")


class _S5AgInfoImgSaveMode_Type(Integer32):
    """Custom type s5AgInfoImgSaveMode based on Integer32"""
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
        *(("noWrite", 4),
          ("notAvail", 1),
          ("writeIfDiff", 2),
          ("writeIfNewer", 3))
    )


_S5AgInfoImgSaveMode_Type.__name__ = "Integer32"
_S5AgInfoImgSaveMode_Object = MibScalar
s5AgInfoImgSaveMode = _S5AgInfoImgSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 8),
    _S5AgInfoImgSaveMode_Type()
)
s5AgInfoImgSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoImgSaveMode.setStatus("current")


class _S5AgInfoImgSaveStatus_Type(Integer32):
    """Custom type s5AgInfoImgSaveStatus based on Integer32"""
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
        *(("noSave", 2),
          ("notAvail", 1),
          ("saveFailed", 4),
          ("saved", 3))
    )


_S5AgInfoImgSaveStatus_Type.__name__ = "Integer32"
_S5AgInfoImgSaveStatus_Object = MibScalar
s5AgInfoImgSaveStatus = _S5AgInfoImgSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 9),
    _S5AgInfoImgSaveStatus_Type()
)
s5AgInfoImgSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoImgSaveStatus.setStatus("current")


class _S5AgInfoVer_Type(DisplayString):
    """Custom type s5AgInfoVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5AgInfoVer_Type.__name__ = "DisplayString"
_S5AgInfoVer_Object = MibScalar
s5AgInfoVer = _S5AgInfoVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 10),
    _S5AgInfoVer_Type()
)
s5AgInfoVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoVer.setStatus("current")


class _S5AgInfoLocStorVer_Type(DisplayString):
    """Custom type s5AgInfoLocStorVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5AgInfoLocStorVer_Type.__name__ = "DisplayString"
_S5AgInfoLocStorVer_Object = MibScalar
s5AgInfoLocStorVer = _S5AgInfoLocStorVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 11),
    _S5AgInfoLocStorVer_Type()
)
s5AgInfoLocStorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoLocStorVer.setStatus("current")
_S5AgInfoNxtBootDfltGwAddr_Type = IpAddress
_S5AgInfoNxtBootDfltGwAddr_Object = MibScalar
s5AgInfoNxtBootDfltGwAddr = _S5AgInfoNxtBootDfltGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 12),
    _S5AgInfoNxtBootDfltGwAddr_Type()
)
s5AgInfoNxtBootDfltGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoNxtBootDfltGwAddr.setStatus("current")
_S5AgInfoCurDfltGwAddr_Type = IpAddress
_S5AgInfoCurDfltGwAddr_Object = MibScalar
s5AgInfoCurDfltGwAddr = _S5AgInfoCurDfltGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 13),
    _S5AgInfoCurDfltGwAddr_Type()
)
s5AgInfoCurDfltGwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoCurDfltGwAddr.setStatus("current")


class _S5AgInfoDramUsage_Type(Integer32):
    """Custom type s5AgInfoDramUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_S5AgInfoDramUsage_Type.__name__ = "Integer32"
_S5AgInfoDramUsage_Object = MibScalar
s5AgInfoDramUsage = _S5AgInfoDramUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 14),
    _S5AgInfoDramUsage_Type()
)
s5AgInfoDramUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoDramUsage.setStatus("current")


class _S5AgInfoLoadProtocolNxtBoot_Type(Integer32):
    """Custom type s5AgInfoLoadProtocolNxtBoot based on Integer32"""
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
        *(("auto", 4),
          ("ipOnly", 2),
          ("ipxOnly", 3),
          ("other", 1))
    )


_S5AgInfoLoadProtocolNxtBoot_Type.__name__ = "Integer32"
_S5AgInfoLoadProtocolNxtBoot_Object = MibScalar
s5AgInfoLoadProtocolNxtBoot = _S5AgInfoLoadProtocolNxtBoot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 15),
    _S5AgInfoLoadProtocolNxtBoot_Type()
)
s5AgInfoLoadProtocolNxtBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoLoadProtocolNxtBoot.setStatus("current")


class _S5AgInfoLoadProtocolLast_Type(Integer32):
    """Custom type s5AgInfoLoadProtocolLast based on Integer32"""
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
        *(("ip", 2),
          ("ipx", 3),
          ("local", 4),
          ("reserved", 1))
    )


_S5AgInfoLoadProtocolLast_Type.__name__ = "Integer32"
_S5AgInfoLoadProtocolLast_Object = MibScalar
s5AgInfoLoadProtocolLast = _S5AgInfoLoadProtocolLast_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 16),
    _S5AgInfoLoadProtocolLast_Type()
)
s5AgInfoLoadProtocolLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoLoadProtocolLast.setStatus("current")


class _S5AgInfoSlotScope_Type(OctetString):
    """Custom type s5AgInfoSlotScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_S5AgInfoSlotScope_Type.__name__ = "OctetString"
_S5AgInfoSlotScope_Object = MibScalar
s5AgInfoSlotScope = _S5AgInfoSlotScope_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 17),
    _S5AgInfoSlotScope_Type()
)
s5AgInfoSlotScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoSlotScope.setStatus("current")


class _S5AgInfoImgType_Type(Integer32):
    """Custom type s5AgInfoImgType based on Integer32"""
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
        *(("other", 1),
          ("typeA", 2),
          ("typeB", 3),
          ("typeC", 4))
    )


_S5AgInfoImgType_Type.__name__ = "Integer32"
_S5AgInfoImgType_Object = MibScalar
s5AgInfoImgType = _S5AgInfoImgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 18),
    _S5AgInfoImgType_Type()
)
s5AgInfoImgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoImgType.setStatus("current")


class _S5AgInfoScheduleBootTime_Type(Integer32):
    """Custom type s5AgInfoScheduleBootTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_S5AgInfoScheduleBootTime_Type.__name__ = "Integer32"
_S5AgInfoScheduleBootTime_Object = MibScalar
s5AgInfoScheduleBootTime = _S5AgInfoScheduleBootTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 19),
    _S5AgInfoScheduleBootTime_Type()
)
s5AgInfoScheduleBootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoScheduleBootTime.setStatus("current")


class _S5AgInfoScheduleBootCancel_Type(Integer32):
    """Custom type s5AgInfoScheduleBootCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("other", 1))
    )


_S5AgInfoScheduleBootCancel_Type.__name__ = "Integer32"
_S5AgInfoScheduleBootCancel_Object = MibScalar
s5AgInfoScheduleBootCancel = _S5AgInfoScheduleBootCancel_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 20),
    _S5AgInfoScheduleBootCancel_Type()
)
s5AgInfoScheduleBootCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoScheduleBootCancel.setStatus("current")


class _S5AgInfoNumBootBanks_Type(Integer32):
    """Custom type s5AgInfoNumBootBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgInfoNumBootBanks_Type.__name__ = "Integer32"
_S5AgInfoNumBootBanks_Object = MibScalar
s5AgInfoNumBootBanks = _S5AgInfoNumBootBanks_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 21),
    _S5AgInfoNumBootBanks_Type()
)
s5AgInfoNumBootBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoNumBootBanks.setStatus("current")


class _S5AgInfoNextBootBank_Type(Integer32):
    """Custom type s5AgInfoNextBootBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgInfoNextBootBank_Type.__name__ = "Integer32"
_S5AgInfoNextBootBank_Object = MibScalar
s5AgInfoNextBootBank = _S5AgInfoNextBootBank_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 22),
    _S5AgInfoNextBootBank_Type()
)
s5AgInfoNextBootBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoNextBootBank.setStatus("current")


class _S5AgInfoDstLoadBank_Type(Integer32):
    """Custom type s5AgInfoDstLoadBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgInfoDstLoadBank_Type.__name__ = "Integer32"
_S5AgInfoDstLoadBank_Object = MibScalar
s5AgInfoDstLoadBank = _S5AgInfoDstLoadBank_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 23),
    _S5AgInfoDstLoadBank_Type()
)
s5AgInfoDstLoadBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoDstLoadBank.setStatus("current")


class _S5AgInfoFileAction_Type(Integer32):
    """Custom type s5AgInfoFileAction based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("copyConfigToNvram", 22),
          ("dnldConfig", 2),
          ("dnldConfigFromSftp", 26),
          ("dnldConfigFromUsb", 16),
          ("dnldFw", 6),
          ("dnldFwFromSftp", 25),
          ("dnldFwFromSftpNoReset", 32),
          ("dnldFwFromUsb", 14),
          ("dnldFwNoReset", 11),
          ("dnldImg", 3),
          ("dnldImgFromSftp", 24),
          ("dnldImgFromSftpNoReset", 31),
          ("dnldImgFromUsb", 12),
          ("dnldImgFromUsbNoReset", 34),
          ("dnldImgIfNewer", 8),
          ("dnldImgIfNewerFromSftp", 38),
          ("dnldImgIfNewerFromSftpNoReset", 39),
          ("dnldImgIfNewerFromUsb", 36),
          ("dnldImgIfNewerFromUsbNoReset", 37),
          ("dnldImgIfNewerNoReset", 35),
          ("dnldImgNoReset", 10),
          ("dnldImgToDram", 9),
          ("dnldLicense", 18),
          ("dnldLicenseFromSftp", 33),
          ("dnldLicenseFromUsb", 20),
          ("dnldSshDsaAuthKeyFromSftp", 29),
          ("dnldSshDsaAuthKeyFromUsb", 23),
          ("dnldSshRsaAuthKeyFromSftp", 30),
          ("dnldSshRsaAuthKeyFromUsb", 28),
          ("other", 1),
          ("upldConfig", 4),
          ("upldConfigToSftp", 27),
          ("upldConfigToUsb", 17),
          ("upldFw", 7),
          ("upldFwToUsb", 15),
          ("upldImg", 5),
          ("upldImgToUsb", 13),
          ("upldLicense", 19),
          ("upldLicenseToUsb", 21))
    )


_S5AgInfoFileAction_Type.__name__ = "Integer32"
_S5AgInfoFileAction_Object = MibScalar
s5AgInfoFileAction = _S5AgInfoFileAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 24),
    _S5AgInfoFileAction_Type()
)
s5AgInfoFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoFileAction.setStatus("current")


class _S5AgInfoFileStatus_Type(Integer32):
    """Custom type s5AgInfoFileStatus based on Integer32"""
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
        *(("fail", 4),
          ("inProgress", 2),
          ("other", 1),
          ("success", 3))
    )


_S5AgInfoFileStatus_Type.__name__ = "Integer32"
_S5AgInfoFileStatus_Object = MibScalar
s5AgInfoFileStatus = _S5AgInfoFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 25),
    _S5AgInfoFileStatus_Type()
)
s5AgInfoFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoFileStatus.setStatus("current")


class _S5AgInfoStackBootpMACUsage_Type(Integer32):
    """Custom type s5AgInfoStackBootpMACUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("useBaseUnitMACAddress", 2),
          ("useStackMACAddress", 3))
    )


_S5AgInfoStackBootpMACUsage_Type.__name__ = "Integer32"
_S5AgInfoStackBootpMACUsage_Object = MibScalar
s5AgInfoStackBootpMACUsage = _S5AgInfoStackBootpMACUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 26),
    _S5AgInfoStackBootpMACUsage_Type()
)
s5AgInfoStackBootpMACUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgInfoStackBootpMACUsage.setStatus("current")


class _S5AgInfoImgDownloadStatus_Type(Integer32):
    """Custom type s5AgInfoImgDownloadStatus based on Integer32"""
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
        *(("downloading", 2),
          ("idle", 1),
          ("programming", 3),
          ("rebooting", 4),
          ("transferring", 5))
    )


_S5AgInfoImgDownloadStatus_Type.__name__ = "Integer32"
_S5AgInfoImgDownloadStatus_Object = MibScalar
s5AgInfoImgDownloadStatus = _S5AgInfoImgDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 27),
    _S5AgInfoImgDownloadStatus_Type()
)
s5AgInfoImgDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoImgDownloadStatus.setStatus("current")


class _S5AgInfoImgDownloadPercentComplete_Type(Unsigned32):
    """Custom type s5AgInfoImgDownloadPercentComplete based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_S5AgInfoImgDownloadPercentComplete_Type.__name__ = "Unsigned32"
_S5AgInfoImgDownloadPercentComplete_Object = MibScalar
s5AgInfoImgDownloadPercentComplete = _S5AgInfoImgDownloadPercentComplete_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 1, 28),
    _S5AgInfoImgDownloadPercentComplete_Type()
)
s5AgInfoImgDownloadPercentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgInfoImgDownloadPercentComplete.setStatus("current")
_S5AgMyIfTable_Object = MibTable
s5AgMyIfTable = _S5AgMyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    s5AgMyIfTable.setStatus("current")
_S5AgMyIfEntry_Object = MibTableRow
s5AgMyIfEntry = _S5AgMyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1)
)
s5AgMyIfEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgMyIfIndx"),
)
if mibBuilder.loadTexts:
    s5AgMyIfEntry.setStatus("current")
_S5AgMyIfIndx_Type = InterfaceIndex
_S5AgMyIfIndx_Object = MibTableColumn
s5AgMyIfIndx = _S5AgMyIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 1),
    _S5AgMyIfIndx_Type()
)
s5AgMyIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyIfIndx.setStatus("current")
_S5AgMyIfNxtBootIpAddr_Type = IpAddress
_S5AgMyIfNxtBootIpAddr_Object = MibTableColumn
s5AgMyIfNxtBootIpAddr = _S5AgMyIfNxtBootIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 2),
    _S5AgMyIfNxtBootIpAddr_Type()
)
s5AgMyIfNxtBootIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfNxtBootIpAddr.setStatus("current")
_S5AgMyIfNxtBootNetMask_Type = IpAddress
_S5AgMyIfNxtBootNetMask_Object = MibTableColumn
s5AgMyIfNxtBootNetMask = _S5AgMyIfNxtBootNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 3),
    _S5AgMyIfNxtBootNetMask_Type()
)
s5AgMyIfNxtBootNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfNxtBootNetMask.setStatus("current")


class _S5AgMyIfCfgFname_Type(DisplayString):
    """Custom type s5AgMyIfCfgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S5AgMyIfCfgFname_Type.__name__ = "DisplayString"
_S5AgMyIfCfgFname_Object = MibTableColumn
s5AgMyIfCfgFname = _S5AgMyIfCfgFname_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 4),
    _S5AgMyIfCfgFname_Type()
)
s5AgMyIfCfgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfCfgFname.setStatus("current")
_S5AgMyIfLdSvrAddr_Type = IpAddress
_S5AgMyIfLdSvrAddr_Object = MibTableColumn
s5AgMyIfLdSvrAddr = _S5AgMyIfLdSvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 5),
    _S5AgMyIfLdSvrAddr_Type()
)
s5AgMyIfLdSvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfLdSvrAddr.setStatus("current")


class _S5AgMyIfImgFname_Type(DisplayString):
    """Custom type s5AgMyIfImgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5AgMyIfImgFname_Type.__name__ = "DisplayString"
_S5AgMyIfImgFname_Object = MibTableColumn
s5AgMyIfImgFname = _S5AgMyIfImgFname_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 6),
    _S5AgMyIfImgFname_Type()
)
s5AgMyIfImgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfImgFname.setStatus("current")


class _S5AgMyIfValidFlag_Type(Integer32):
    """Custom type s5AgMyIfValidFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_S5AgMyIfValidFlag_Type.__name__ = "Integer32"
_S5AgMyIfValidFlag_Object = MibTableColumn
s5AgMyIfValidFlag = _S5AgMyIfValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 7),
    _S5AgMyIfValidFlag_Type()
)
s5AgMyIfValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyIfValidFlag.setStatus("current")
_S5AgMyIfNxtBootIpxAddr_Type = IpxAddress
_S5AgMyIfNxtBootIpxAddr_Object = MibTableColumn
s5AgMyIfNxtBootIpxAddr = _S5AgMyIfNxtBootIpxAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 8),
    _S5AgMyIfNxtBootIpxAddr_Type()
)
s5AgMyIfNxtBootIpxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyIfNxtBootIpxAddr.setStatus("current")
_S5AgMyIfBootRouterAddr_Type = IpAddress
_S5AgMyIfBootRouterAddr_Object = MibTableColumn
s5AgMyIfBootRouterAddr = _S5AgMyIfBootRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 9),
    _S5AgMyIfBootRouterAddr_Type()
)
s5AgMyIfBootRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgMyIfBootRouterAddr.setStatus("current")
_S5AgMyIfMacAddr_Type = MacAddress
_S5AgMyIfMacAddr_Object = MibTableColumn
s5AgMyIfMacAddr = _S5AgMyIfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 2, 1, 10),
    _S5AgMyIfMacAddr_Type()
)
s5AgMyIfMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgMyIfMacAddr.setStatus("current")
_S5AgOthIfTable_Object = MibTable
s5AgOthIfTable = _S5AgOthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3)
)
if mibBuilder.loadTexts:
    s5AgOthIfTable.setStatus("current")
_S5AgOthIfEntry_Object = MibTableRow
s5AgOthIfEntry = _S5AgOthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1)
)
s5AgOthIfEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgOthIfGrpIndx"),
    (0, "S5-AGENT-MIB", "s5AgOthIfComIndx"),
    (0, "S5-AGENT-MIB", "s5AgOthIfIndx"),
)
if mibBuilder.loadTexts:
    s5AgOthIfEntry.setStatus("current")


class _S5AgOthIfGrpIndx_Type(Integer32):
    """Custom type s5AgOthIfGrpIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5AgOthIfGrpIndx_Type.__name__ = "Integer32"
_S5AgOthIfGrpIndx_Object = MibTableColumn
s5AgOthIfGrpIndx = _S5AgOthIfGrpIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1, 1),
    _S5AgOthIfGrpIndx_Type()
)
s5AgOthIfGrpIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgOthIfGrpIndx.setStatus("current")


class _S5AgOthIfComIndx_Type(Integer32):
    """Custom type s5AgOthIfComIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_S5AgOthIfComIndx_Type.__name__ = "Integer32"
_S5AgOthIfComIndx_Object = MibTableColumn
s5AgOthIfComIndx = _S5AgOthIfComIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1, 2),
    _S5AgOthIfComIndx_Type()
)
s5AgOthIfComIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgOthIfComIndx.setStatus("current")
_S5AgOthIfIndx_Type = InterfaceIndex
_S5AgOthIfIndx_Object = MibTableColumn
s5AgOthIfIndx = _S5AgOthIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1, 3),
    _S5AgOthIfIndx_Type()
)
s5AgOthIfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgOthIfIndx.setStatus("current")
_S5AgOthIfIpAddr_Type = IpAddress
_S5AgOthIfIpAddr_Object = MibTableColumn
s5AgOthIfIpAddr = _S5AgOthIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1, 4),
    _S5AgOthIfIpAddr_Type()
)
s5AgOthIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgOthIfIpAddr.setStatus("current")
_S5AgOthIfIpxAddr_Type = IpxAddress
_S5AgOthIfIpxAddr_Object = MibTableColumn
s5AgOthIfIpxAddr = _S5AgOthIfIpxAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 3, 1, 5),
    _S5AgOthIfIpxAddr_Type()
)
s5AgOthIfIpxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgOthIfIpxAddr.setStatus("current")


class _S5AgIpRtrDefaultTimeToLive_Type(TimeIntervalSec):
    """Custom type s5AgIpRtrDefaultTimeToLive based on TimeIntervalSec"""
    defaultValue = 540

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_S5AgIpRtrDefaultTimeToLive_Type.__name__ = "TimeIntervalSec"
_S5AgIpRtrDefaultTimeToLive_Object = MibScalar
s5AgIpRtrDefaultTimeToLive = _S5AgIpRtrDefaultTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 4),
    _S5AgIpRtrDefaultTimeToLive_Type()
)
s5AgIpRtrDefaultTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgIpRtrDefaultTimeToLive.setStatus("current")


class _S5AgIpDefaultRtrSelectionMode_Type(Integer32):
    """Custom type s5AgIpDefaultRtrSelectionMode based on Integer32"""
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
        *(("config", 2),
          ("dynamic", 4),
          ("other", 1),
          ("static", 3))
    )


_S5AgIpDefaultRtrSelectionMode_Type.__name__ = "Integer32"
_S5AgIpDefaultRtrSelectionMode_Object = MibScalar
s5AgIpDefaultRtrSelectionMode = _S5AgIpDefaultRtrSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 5),
    _S5AgIpDefaultRtrSelectionMode_Type()
)
s5AgIpDefaultRtrSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgIpDefaultRtrSelectionMode.setStatus("current")


class _S5AgIpRtrDiscoverySolicitMode_Type(Integer32):
    """Custom type s5AgIpRtrDiscoverySolicitMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 1))
    )


_S5AgIpRtrDiscoverySolicitMode_Type.__name__ = "Integer32"
_S5AgIpRtrDiscoverySolicitMode_Object = MibScalar
s5AgIpRtrDiscoverySolicitMode = _S5AgIpRtrDiscoverySolicitMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 6),
    _S5AgIpRtrDiscoverySolicitMode_Type()
)
s5AgIpRtrDiscoverySolicitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgIpRtrDiscoverySolicitMode.setStatus("current")
_S5AgDataCollectTable_Object = MibTable
s5AgDataCollectTable = _S5AgDataCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 7)
)
if mibBuilder.loadTexts:
    s5AgDataCollectTable.setStatus("current")
_S5AgDataCollectEntry_Object = MibTableRow
s5AgDataCollectEntry = _S5AgDataCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 7, 1)
)
s5AgDataCollectEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgDataCollectIfIndex"),
)
if mibBuilder.loadTexts:
    s5AgDataCollectEntry.setStatus("current")


class _S5AgDataCollectIfIndex_Type(Integer32):
    """Custom type s5AgDataCollectIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgDataCollectIfIndex_Type.__name__ = "Integer32"
_S5AgDataCollectIfIndex_Object = MibTableColumn
s5AgDataCollectIfIndex = _S5AgDataCollectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 7, 1, 1),
    _S5AgDataCollectIfIndex_Type()
)
s5AgDataCollectIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgDataCollectIfIndex.setStatus("current")
_S5AgDataCollectSnTimeStamp_Type = TimeTicks
_S5AgDataCollectSnTimeStamp_Object = MibTableColumn
s5AgDataCollectSnTimeStamp = _S5AgDataCollectSnTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 7, 1, 2),
    _S5AgDataCollectSnTimeStamp_Type()
)
s5AgDataCollectSnTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgDataCollectSnTimeStamp.setStatus("current")


class _S5AgDataCollectNetworkAddrStatus_Type(Integer32):
    """Custom type s5AgDataCollectNetworkAddrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOff", 1),
          ("off", 3),
          ("on", 2))
    )


_S5AgDataCollectNetworkAddrStatus_Type.__name__ = "Integer32"
_S5AgDataCollectNetworkAddrStatus_Object = MibTableColumn
s5AgDataCollectNetworkAddrStatus = _S5AgDataCollectNetworkAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 7, 1, 3),
    _S5AgDataCollectNetworkAddrStatus_Type()
)
s5AgDataCollectNetworkAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDataCollectNetworkAddrStatus.setStatus("current")
_S5AgUnAuthIpAddr_Type = IpAddress
_S5AgUnAuthIpAddr_Object = MibScalar
s5AgUnAuthIpAddr = _S5AgUnAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 8),
    _S5AgUnAuthIpAddr_Type()
)
s5AgUnAuthIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgUnAuthIpAddr.setStatus("current")
_S5AgUnAuthIpxAddr_Type = IpxAddress
_S5AgUnAuthIpxAddr_Object = MibScalar
s5AgUnAuthIpxAddr = _S5AgUnAuthIpxAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 9),
    _S5AgUnAuthIpxAddr_Type()
)
s5AgUnAuthIpxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgUnAuthIpxAddr.setStatus("current")


class _S5AgUnAuthComm_Type(OctetString):
    """Custom type s5AgUnAuthComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_S5AgUnAuthComm_Type.__name__ = "OctetString"
_S5AgUnAuthComm_Object = MibScalar
s5AgUnAuthComm = _S5AgUnAuthComm_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 10),
    _S5AgUnAuthComm_Type()
)
s5AgUnAuthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgUnAuthComm.setStatus("current")
_S5AgTrapFilterTable_Object = MibTable
s5AgTrapFilterTable = _S5AgTrapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11)
)
if mibBuilder.loadTexts:
    s5AgTrapFilterTable.setStatus("current")
_S5AgTrapFilterEntry_Object = MibTableRow
s5AgTrapFilterEntry = _S5AgTrapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1)
)
s5AgTrapFilterEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgTrapFilterIndex"),
)
if mibBuilder.loadTexts:
    s5AgTrapFilterEntry.setStatus("current")


class _S5AgTrapFilterIndex_Type(Integer32):
    """Custom type s5AgTrapFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S5AgTrapFilterIndex_Type.__name__ = "Integer32"
_S5AgTrapFilterIndex_Object = MibTableColumn
s5AgTrapFilterIndex = _S5AgTrapFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 1),
    _S5AgTrapFilterIndex_Type()
)
s5AgTrapFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgTrapFilterIndex.setStatus("current")
_S5AgTrapFilterTrapOID_Type = ObjectIdentifier
_S5AgTrapFilterTrapOID_Object = MibTableColumn
s5AgTrapFilterTrapOID = _S5AgTrapFilterTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 2),
    _S5AgTrapFilterTrapOID_Type()
)
s5AgTrapFilterTrapOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterTrapOID.setStatus("current")
_S5AgTrapFilterTrapInitiator1_Type = Integer32
_S5AgTrapFilterTrapInitiator1_Object = MibTableColumn
s5AgTrapFilterTrapInitiator1 = _S5AgTrapFilterTrapInitiator1_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 3),
    _S5AgTrapFilterTrapInitiator1_Type()
)
s5AgTrapFilterTrapInitiator1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterTrapInitiator1.setStatus("current")
_S5AgTrapFilterTrapInitiator2_Type = Integer32
_S5AgTrapFilterTrapInitiator2_Object = MibTableColumn
s5AgTrapFilterTrapInitiator2 = _S5AgTrapFilterTrapInitiator2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 4),
    _S5AgTrapFilterTrapInitiator2_Type()
)
s5AgTrapFilterTrapInitiator2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterTrapInitiator2.setStatus("current")
_S5AgTrapFilterTrapInitiator3_Type = Integer32
_S5AgTrapFilterTrapInitiator3_Object = MibTableColumn
s5AgTrapFilterTrapInitiator3 = _S5AgTrapFilterTrapInitiator3_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 5),
    _S5AgTrapFilterTrapInitiator3_Type()
)
s5AgTrapFilterTrapInitiator3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterTrapInitiator3.setStatus("current")


class _S5AgTrapFilterStatus_Type(Integer32):
    """Custom type s5AgTrapFilterStatus based on Integer32"""
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


_S5AgTrapFilterStatus_Type.__name__ = "Integer32"
_S5AgTrapFilterStatus_Object = MibTableColumn
s5AgTrapFilterStatus = _S5AgTrapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 6),
    _S5AgTrapFilterStatus_Type()
)
s5AgTrapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterStatus.setStatus("current")
_S5AgTrapFilterDelayTime_Type = Integer32
_S5AgTrapFilterDelayTime_Object = MibTableColumn
s5AgTrapFilterDelayTime = _S5AgTrapFilterDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 7),
    _S5AgTrapFilterDelayTime_Type()
)
s5AgTrapFilterDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterDelayTime.setStatus("current")


class _S5AgTrapEntryStatus_Type(Integer32):
    """Custom type s5AgTrapEntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_S5AgTrapEntryStatus_Type.__name__ = "Integer32"
_S5AgTrapEntryStatus_Object = MibTableColumn
s5AgTrapEntryStatus = _S5AgTrapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 11, 1, 8),
    _S5AgTrapEntryStatus_Type()
)
s5AgTrapEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapEntryStatus.setStatus("current")


class _S5AgTrapFilterGlobalStatus_Type(Integer32):
    """Custom type s5AgTrapFilterGlobalStatus based on Integer32"""
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
        *(("disable-all", 2),
          ("disable-all-and-use-table", 4),
          ("enable-all", 1),
          ("enable-all-and-use-table", 3))
    )


_S5AgTrapFilterGlobalStatus_Type.__name__ = "Integer32"
_S5AgTrapFilterGlobalStatus_Object = MibScalar
s5AgTrapFilterGlobalStatus = _S5AgTrapFilterGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 12),
    _S5AgTrapFilterGlobalStatus_Type()
)
s5AgTrapFilterGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrapFilterGlobalStatus.setStatus("current")
_S5AgUnAuthInetAddressType_Type = InetAddressType
_S5AgUnAuthInetAddressType_Object = MibScalar
s5AgUnAuthInetAddressType = _S5AgUnAuthInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 13),
    _S5AgUnAuthInetAddressType_Type()
)
s5AgUnAuthInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgUnAuthInetAddressType.setStatus("current")
_S5AgUnAuthInetAddress_Type = InetAddress
_S5AgUnAuthInetAddress_Object = MibScalar
s5AgUnAuthInetAddress = _S5AgUnAuthInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 2, 14),
    _S5AgUnAuthInetAddress_Type()
)
s5AgUnAuthInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgUnAuthInetAddress.setStatus("current")
_S5AgentMgmt_ObjectIdentity = ObjectIdentity
s5AgentMgmt = _S5AgentMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3)
)


class _S5AgTrpRcvrMaxEnt_Type(Integer32):
    """Custom type s5AgTrpRcvrMaxEnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgTrpRcvrMaxEnt_Type.__name__ = "Integer32"
_S5AgTrpRcvrMaxEnt_Object = MibScalar
s5AgTrpRcvrMaxEnt = _S5AgTrpRcvrMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 1),
    _S5AgTrpRcvrMaxEnt_Type()
)
s5AgTrpRcvrMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgTrpRcvrMaxEnt.setStatus("current")


class _S5AgTrpRcvrCurEnt_Type(Integer32):
    """Custom type s5AgTrpRcvrCurEnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgTrpRcvrCurEnt_Type.__name__ = "Integer32"
_S5AgTrpRcvrCurEnt_Object = MibScalar
s5AgTrpRcvrCurEnt = _S5AgTrpRcvrCurEnt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 2),
    _S5AgTrpRcvrCurEnt_Type()
)
s5AgTrpRcvrCurEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgTrpRcvrCurEnt.setStatus("current")


class _S5AgTrpRcvrNext_Type(Integer32):
    """Custom type s5AgTrpRcvrNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgTrpRcvrNext_Type.__name__ = "Integer32"
_S5AgTrpRcvrNext_Object = MibScalar
s5AgTrpRcvrNext = _S5AgTrpRcvrNext_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 3),
    _S5AgTrpRcvrNext_Type()
)
s5AgTrpRcvrNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgTrpRcvrNext.setStatus("current")
_S5AgTrpRcvrTable_Object = MibTable
s5AgTrpRcvrTable = _S5AgTrpRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4)
)
if mibBuilder.loadTexts:
    s5AgTrpRcvrTable.setStatus("current")
_S5AgTrpRcvrEntry_Object = MibTableRow
s5AgTrpRcvrEntry = _S5AgTrpRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1)
)
s5AgTrpRcvrEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgTrpRcvrIndx"),
)
if mibBuilder.loadTexts:
    s5AgTrpRcvrEntry.setStatus("current")


class _S5AgTrpRcvrIndx_Type(Integer32):
    """Custom type s5AgTrpRcvrIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5AgTrpRcvrIndx_Type.__name__ = "Integer32"
_S5AgTrpRcvrIndx_Object = MibTableColumn
s5AgTrpRcvrIndx = _S5AgTrpRcvrIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 1),
    _S5AgTrpRcvrIndx_Type()
)
s5AgTrpRcvrIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgTrpRcvrIndx.setStatus("current")


class _S5AgTrpRcvrStatus_Type(Integer32):
    """Custom type s5AgTrpRcvrStatus based on Integer32"""
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
        *(("create", 5),
          ("delete", 4),
          ("ignore", 3),
          ("other", 1),
          ("valid", 2))
    )


_S5AgTrpRcvrStatus_Type.__name__ = "Integer32"
_S5AgTrpRcvrStatus_Object = MibTableColumn
s5AgTrpRcvrStatus = _S5AgTrpRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 2),
    _S5AgTrpRcvrStatus_Type()
)
s5AgTrpRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrpRcvrStatus.setStatus("current")


class _S5AgTrpRcvrAddrType_Type(Integer32):
    """Custom type s5AgTrpRcvrAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_S5AgTrpRcvrAddrType_Type.__name__ = "Integer32"
_S5AgTrpRcvrAddrType_Object = MibTableColumn
s5AgTrpRcvrAddrType = _S5AgTrpRcvrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 3),
    _S5AgTrpRcvrAddrType_Type()
)
s5AgTrpRcvrAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrpRcvrAddrType.setStatus("current")


class _S5AgTrpRcvrNetAddr_Type(OctetString):
    """Custom type s5AgTrpRcvrNetAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_S5AgTrpRcvrNetAddr_Type.__name__ = "OctetString"
_S5AgTrpRcvrNetAddr_Object = MibTableColumn
s5AgTrpRcvrNetAddr = _S5AgTrpRcvrNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 4),
    _S5AgTrpRcvrNetAddr_Type()
)
s5AgTrpRcvrNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrpRcvrNetAddr.setStatus("current")


class _S5AgTrpRcvrComm_Type(OctetString):
    """Custom type s5AgTrpRcvrComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5AgTrpRcvrComm_Type.__name__ = "OctetString"
_S5AgTrpRcvrComm_Object = MibTableColumn
s5AgTrpRcvrComm = _S5AgTrpRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 5),
    _S5AgTrpRcvrComm_Type()
)
s5AgTrpRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrpRcvrComm.setStatus("current")


class _S5AgTrpRcvrAgeTime_Type(TimeIntervalSec):
    """Custom type s5AgTrpRcvrAgeTime based on TimeIntervalSec"""
    defaultValue = 0


_S5AgTrpRcvrAgeTime_Object = MibTableColumn
s5AgTrpRcvrAgeTime = _S5AgTrpRcvrAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 4, 1, 6),
    _S5AgTrpRcvrAgeTime_Type()
)
s5AgTrpRcvrAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgTrpRcvrAgeTime.setStatus("current")
_S5AgRemoteLoginMgmt_ObjectIdentity = ObjectIdentity
s5AgRemoteLoginMgmt = _S5AgRemoteLoginMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 5)
)
_S5AgRemoteLoginIp_Type = IpAddress
_S5AgRemoteLoginIp_Object = MibScalar
s5AgRemoteLoginIp = _S5AgRemoteLoginIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 5, 1),
    _S5AgRemoteLoginIp_Type()
)
s5AgRemoteLoginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgRemoteLoginIp.setStatus("current")


class _S5AgRemoteLoginStatus_Type(Integer32):
    """Custom type s5AgRemoteLoginStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("accessPermissionOff", 10),
          ("excessiveLoginFail", 9),
          ("localConsoleBusy", 8),
          ("loginInactivityTimeout", 5),
          ("loginLogout", 11),
          ("loginTimeout", 4),
          ("nonAllowedIPaddr", 7),
          ("passwordFail", 3),
          ("statusUnknown", 1),
          ("successful", 2),
          ("telnetSessionExisted", 6))
    )


_S5AgRemoteLoginStatus_Type.__name__ = "Integer32"
_S5AgRemoteLoginStatus_Object = MibScalar
s5AgRemoteLoginStatus = _S5AgRemoteLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 5, 2),
    _S5AgRemoteLoginStatus_Type()
)
s5AgRemoteLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgRemoteLoginStatus.setStatus("current")
_S5AgRemoteLoginInetAddressType_Type = InetAddressType
_S5AgRemoteLoginInetAddressType_Object = MibScalar
s5AgRemoteLoginInetAddressType = _S5AgRemoteLoginInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 5, 3),
    _S5AgRemoteLoginInetAddressType_Type()
)
s5AgRemoteLoginInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgRemoteLoginInetAddressType.setStatus("current")
_S5AgRemoteLoginInetAddress_Type = InetAddress
_S5AgRemoteLoginInetAddress_Object = MibScalar
s5AgRemoteLoginInetAddress = _S5AgRemoteLoginInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 3, 5, 4),
    _S5AgRemoteLoginInetAddress_Type()
)
s5AgRemoteLoginInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgRemoteLoginInetAddress.setStatus("current")
_S5AgentSystem_ObjectIdentity = ObjectIdentity
s5AgentSystem = _S5AgentSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4)
)


class _S5AgSysAutoPvid_Type(Integer32):
    """Custom type s5AgSysAutoPvid based on Integer32"""
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


_S5AgSysAutoPvid_Type.__name__ = "Integer32"
_S5AgSysAutoPvid_Object = MibScalar
s5AgSysAutoPvid = _S5AgSysAutoPvid_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 1),
    _S5AgSysAutoPvid_Type()
)
s5AgSysAutoPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutoPvid.setStatus("current")


class _S5AgSysCurrentOperationalMode_Type(Integer32):
    """Custom type s5AgSysCurrentOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 2),
          ("pure", 1))
    )


_S5AgSysCurrentOperationalMode_Type.__name__ = "Integer32"
_S5AgSysCurrentOperationalMode_Object = MibScalar
s5AgSysCurrentOperationalMode = _S5AgSysCurrentOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 2),
    _S5AgSysCurrentOperationalMode_Type()
)
s5AgSysCurrentOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysCurrentOperationalMode.setStatus("current")


class _S5AgSysNextBootOperationalMode_Type(Integer32):
    """Custom type s5AgSysNextBootOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 2),
          ("pure", 1))
    )


_S5AgSysNextBootOperationalMode_Type.__name__ = "Integer32"
_S5AgSysNextBootOperationalMode_Object = MibScalar
s5AgSysNextBootOperationalMode = _S5AgSysNextBootOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 3),
    _S5AgSysNextBootOperationalMode_Type()
)
s5AgSysNextBootOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysNextBootOperationalMode.setStatus("current")


class _S5AgSysBinaryConfigFilename_Type(DisplayString):
    """Custom type s5AgSysBinaryConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5AgSysBinaryConfigFilename_Type.__name__ = "DisplayString"
_S5AgSysBinaryConfigFilename_Object = MibScalar
s5AgSysBinaryConfigFilename = _S5AgSysBinaryConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 4),
    _S5AgSysBinaryConfigFilename_Type()
)
s5AgSysBinaryConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysBinaryConfigFilename.setStatus("current")
_S5AgSysTftpServerAddress_Type = IpAddress
_S5AgSysTftpServerAddress_Object = MibScalar
s5AgSysTftpServerAddress = _S5AgSysTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 5),
    _S5AgSysTftpServerAddress_Type()
)
s5AgSysTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysTftpServerAddress.setStatus("current")


class _S5AgSysAsciiConfigFilename_Type(DisplayString):
    """Custom type s5AgSysAsciiConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5AgSysAsciiConfigFilename_Type.__name__ = "DisplayString"
_S5AgSysAsciiConfigFilename_Object = MibScalar
s5AgSysAsciiConfigFilename = _S5AgSysAsciiConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 6),
    _S5AgSysAsciiConfigFilename_Type()
)
s5AgSysAsciiConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigFilename.setStatus("deprecated")


class _S5AgSysAsciiConfigAutoDownload_Type(Integer32):
    """Custom type s5AgSysAsciiConfigAutoDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("useBootp", 2),
          ("useConfig", 3))
    )


_S5AgSysAsciiConfigAutoDownload_Type.__name__ = "Integer32"
_S5AgSysAsciiConfigAutoDownload_Object = MibScalar
s5AgSysAsciiConfigAutoDownload = _S5AgSysAsciiConfigAutoDownload_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 7),
    _S5AgSysAsciiConfigAutoDownload_Type()
)
s5AgSysAsciiConfigAutoDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigAutoDownload.setStatus("deprecated")


class _S5AgSysAsciiConfigAutoDldStatus_Type(Integer32):
    """Custom type s5AgSysAsciiConfigAutoDldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 2),
          ("passed", 1))
    )


_S5AgSysAsciiConfigAutoDldStatus_Type.__name__ = "Integer32"
_S5AgSysAsciiConfigAutoDldStatus_Object = MibScalar
s5AgSysAsciiConfigAutoDldStatus = _S5AgSysAsciiConfigAutoDldStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 8),
    _S5AgSysAsciiConfigAutoDldStatus_Type()
)
s5AgSysAsciiConfigAutoDldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigAutoDldStatus.setStatus("deprecated")


class _S5AgSysAsciiConfigManualDownload_Type(Integer32):
    """Custom type s5AgSysAsciiConfigManualDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("downloadFromSftp", 6),
          ("downloadFromUsb", 5),
          ("downloadNow", 4),
          ("failed", 3),
          ("inProgress", 2),
          ("passed", 1))
    )


_S5AgSysAsciiConfigManualDownload_Type.__name__ = "Integer32"
_S5AgSysAsciiConfigManualDownload_Object = MibScalar
s5AgSysAsciiConfigManualDownload = _S5AgSysAsciiConfigManualDownload_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 9),
    _S5AgSysAsciiConfigManualDownload_Type()
)
s5AgSysAsciiConfigManualDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigManualDownload.setStatus("deprecated")
_S5AgSysCpuIpAddress_Type = IpAddress
_S5AgSysCpuIpAddress_Object = MibScalar
s5AgSysCpuIpAddress = _S5AgSysCpuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 10),
    _S5AgSysCpuIpAddress_Type()
)
s5AgSysCpuIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysCpuIpAddress.setStatus("current")
_S5AgSysStackIpAddress_Type = IpAddress
_S5AgSysStackIpAddress_Object = MibScalar
s5AgSysStackIpAddress = _S5AgSysStackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 11),
    _S5AgSysStackIpAddress_Type()
)
s5AgSysStackIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackIpAddress.setStatus("current")
_S5AgSysCpuNetMask_Type = IpAddress
_S5AgSysCpuNetMask_Object = MibScalar
s5AgSysCpuNetMask = _S5AgSysCpuNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 12),
    _S5AgSysCpuNetMask_Type()
)
s5AgSysCpuNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysCpuNetMask.setStatus("current")


class _S5AgSysManagementVlanId_Type(Integer32):
    """Custom type s5AgSysManagementVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_S5AgSysManagementVlanId_Type.__name__ = "Integer32"
_S5AgSysManagementVlanId_Object = MibScalar
s5AgSysManagementVlanId = _S5AgSysManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 13),
    _S5AgSysManagementVlanId_Type()
)
s5AgSysManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysManagementVlanId.setStatus("current")


class _S5AgSysBinaryConfigUnitNumber_Type(Integer32):
    """Custom type s5AgSysBinaryConfigUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgSysBinaryConfigUnitNumber_Type.__name__ = "Integer32"
_S5AgSysBinaryConfigUnitNumber_Object = MibScalar
s5AgSysBinaryConfigUnitNumber = _S5AgSysBinaryConfigUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 14),
    _S5AgSysBinaryConfigUnitNumber_Type()
)
s5AgSysBinaryConfigUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysBinaryConfigUnitNumber.setStatus("current")


class _S5AgSysStackInsertionUnitNumber_Type(Integer32):
    """Custom type s5AgSysStackInsertionUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgSysStackInsertionUnitNumber_Type.__name__ = "Integer32"
_S5AgSysStackInsertionUnitNumber_Object = MibScalar
s5AgSysStackInsertionUnitNumber = _S5AgSysStackInsertionUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 15),
    _S5AgSysStackInsertionUnitNumber_Type()
)
s5AgSysStackInsertionUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackInsertionUnitNumber.setStatus("current")


class _S5AgSysSpanningTreeOperMode_Type(Integer32):
    """Custom type s5AgSysSpanningTreeOperMode based on Integer32"""
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
        *(("avayaStpg", 1),
          ("mstp", 4),
          ("pvst", 2),
          ("rstp", 3))
    )


_S5AgSysSpanningTreeOperMode_Type.__name__ = "Integer32"
_S5AgSysSpanningTreeOperMode_Object = MibScalar
s5AgSysSpanningTreeOperMode = _S5AgSysSpanningTreeOperMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 16),
    _S5AgSysSpanningTreeOperMode_Type()
)
s5AgSysSpanningTreeOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreeOperMode.setStatus("current")


class _S5AgSysSpanningTreeAdminMode_Type(Integer32):
    """Custom type s5AgSysSpanningTreeAdminMode based on Integer32"""
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
        *(("avayaStpg", 1),
          ("mstp", 4),
          ("pvst", 2),
          ("rstp", 3))
    )


_S5AgSysSpanningTreeAdminMode_Type.__name__ = "Integer32"
_S5AgSysSpanningTreeAdminMode_Object = MibScalar
s5AgSysSpanningTreeAdminMode = _S5AgSysSpanningTreeAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 17),
    _S5AgSysSpanningTreeAdminMode_Type()
)
s5AgSysSpanningTreeAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreeAdminMode.setStatus("current")


class _S5AgSysAutoUnitReplacementEnabled_Type(Integer32):
    """Custom type s5AgSysAutoUnitReplacementEnabled based on Integer32"""
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
        *(("false", 2),
          ("setToDefault", 3),
          ("true", 1))
    )


_S5AgSysAutoUnitReplacementEnabled_Type.__name__ = "Integer32"
_S5AgSysAutoUnitReplacementEnabled_Object = MibScalar
s5AgSysAutoUnitReplacementEnabled = _S5AgSysAutoUnitReplacementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 18),
    _S5AgSysAutoUnitReplacementEnabled_Type()
)
s5AgSysAutoUnitReplacementEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutoUnitReplacementEnabled.setStatus("current")


class _S5AgSysAsciiConfigManualUpload_Type(Integer32):
    """Custom type s5AgSysAsciiConfigManualUpload based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 2),
          ("passed", 1),
          ("uploadNow", 4),
          ("uploadToSftp", 8),
          ("uploadToUsb", 5),
          ("uploadVerboseNow", 6),
          ("uploadVerboseToSftp", 9),
          ("uploadVerboseToUsb", 7))
    )


_S5AgSysAsciiConfigManualUpload_Type.__name__ = "Integer32"
_S5AgSysAsciiConfigManualUpload_Object = MibScalar
s5AgSysAsciiConfigManualUpload = _S5AgSysAsciiConfigManualUpload_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 19),
    _S5AgSysAsciiConfigManualUpload_Type()
)
s5AgSysAsciiConfigManualUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigManualUpload.setStatus("deprecated")


class _S5AgSysSpanningTreePathCostCalculationMode_Type(Integer32):
    """Custom type s5AgSysSpanningTreePathCostCalculationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1dCompatible", 1),
          ("ieee802dot1tCompatible", 2))
    )


_S5AgSysSpanningTreePathCostCalculationMode_Type.__name__ = "Integer32"
_S5AgSysSpanningTreePathCostCalculationMode_Object = MibScalar
s5AgSysSpanningTreePathCostCalculationMode = _S5AgSysSpanningTreePathCostCalculationMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 20),
    _S5AgSysSpanningTreePathCostCalculationMode_Type()
)
s5AgSysSpanningTreePathCostCalculationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreePathCostCalculationMode.setStatus("current")


class _S5AgSysUsbTargetUnit_Type(Integer32):
    """Custom type s5AgSysUsbTargetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_S5AgSysUsbTargetUnit_Type.__name__ = "Integer32"
_S5AgSysUsbTargetUnit_Object = MibScalar
s5AgSysUsbTargetUnit = _S5AgSysUsbTargetUnit_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 21),
    _S5AgSysUsbTargetUnit_Type()
)
s5AgSysUsbTargetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysUsbTargetUnit.setStatus("current")


class _S5AgSysSpanningTreePortMode_Type(Integer32):
    """Custom type s5AgSysSpanningTreePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("normal", 1))
    )


_S5AgSysSpanningTreePortMode_Type.__name__ = "Integer32"
_S5AgSysSpanningTreePortMode_Object = MibScalar
s5AgSysSpanningTreePortMode = _S5AgSysSpanningTreePortMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 22),
    _S5AgSysSpanningTreePortMode_Type()
)
s5AgSysSpanningTreePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreePortMode.setStatus("current")


class _S5AgSysLicenseFilename_Type(DisplayString):
    """Custom type s5AgSysLicenseFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5AgSysLicenseFilename_Type.__name__ = "DisplayString"
_S5AgSysLicenseFilename_Object = MibScalar
s5AgSysLicenseFilename = _S5AgSysLicenseFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 23),
    _S5AgSysLicenseFilename_Type()
)
s5AgSysLicenseFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysLicenseFilename.setStatus("current")


class _S5AgSysSpanningTreeAdminCompatibility_Type(Bits):
    """Custom type s5AgSysSpanningTreeAdminCompatibility based on Bits"""
    namedValues = NamedValues(
        ("port802dot1dLearning", 0)
    )

_S5AgSysSpanningTreeAdminCompatibility_Type.__name__ = "Bits"
_S5AgSysSpanningTreeAdminCompatibility_Object = MibScalar
s5AgSysSpanningTreeAdminCompatibility = _S5AgSysSpanningTreeAdminCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 24),
    _S5AgSysSpanningTreeAdminCompatibility_Type()
)
s5AgSysSpanningTreeAdminCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreeAdminCompatibility.setStatus("current")


class _S5AgSysSpanningTreeOperCompatibility_Type(Bits):
    """Custom type s5AgSysSpanningTreeOperCompatibility based on Bits"""
    namedValues = NamedValues(
        ("port802dot1dLearning", 0)
    )

_S5AgSysSpanningTreeOperCompatibility_Type.__name__ = "Bits"
_S5AgSysSpanningTreeOperCompatibility_Object = MibScalar
s5AgSysSpanningTreeOperCompatibility = _S5AgSysSpanningTreeOperCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 25),
    _S5AgSysSpanningTreeOperCompatibility_Type()
)
s5AgSysSpanningTreeOperCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreeOperCompatibility.setStatus("current")
_S5AgSysGlobalFlowControlEnabled_Type = TruthValue
_S5AgSysGlobalFlowControlEnabled_Object = MibScalar
s5AgSysGlobalFlowControlEnabled = _S5AgSysGlobalFlowControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 26),
    _S5AgSysGlobalFlowControlEnabled_Type()
)
s5AgSysGlobalFlowControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysGlobalFlowControlEnabled.setStatus("current")
_S5AgSysAutosaveToNvramEnabled_Type = TruthValue
_S5AgSysAutosaveToNvramEnabled_Object = MibScalar
s5AgSysAutosaveToNvramEnabled = _S5AgSysAutosaveToNvramEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 27),
    _S5AgSysAutosaveToNvramEnabled_Type()
)
s5AgSysAutosaveToNvramEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutosaveToNvramEnabled.setStatus("current")


class _S5AgSysFlushMacAddrTableAll_Type(Integer32):
    """Custom type s5AgSysFlushMacAddrTableAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("flush", 1),
          ("static", 3))
    )


_S5AgSysFlushMacAddrTableAll_Type.__name__ = "Integer32"
_S5AgSysFlushMacAddrTableAll_Object = MibScalar
s5AgSysFlushMacAddrTableAll = _S5AgSysFlushMacAddrTableAll_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 28),
    _S5AgSysFlushMacAddrTableAll_Type()
)
s5AgSysFlushMacAddrTableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysFlushMacAddrTableAll.setStatus("current")
_S5AgSysFlushMacAddrTableByPortList_Type = PortList
_S5AgSysFlushMacAddrTableByPortList_Object = MibScalar
s5AgSysFlushMacAddrTableByPortList = _S5AgSysFlushMacAddrTableByPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 29),
    _S5AgSysFlushMacAddrTableByPortList_Type()
)
s5AgSysFlushMacAddrTableByPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysFlushMacAddrTableByPortList.setStatus("current")
_S5AgSysFlushMacAddrTableByVlan_Type = VlanId
_S5AgSysFlushMacAddrTableByVlan_Object = MibScalar
s5AgSysFlushMacAddrTableByVlan = _S5AgSysFlushMacAddrTableByVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 30),
    _S5AgSysFlushMacAddrTableByVlan_Type()
)
s5AgSysFlushMacAddrTableByVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysFlushMacAddrTableByVlan.setStatus("current")


class _S5AgSysFlushMacAddrTableByTrunk_Type(Integer32):
    """Custom type s5AgSysFlushMacAddrTableByTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_S5AgSysFlushMacAddrTableByTrunk_Type.__name__ = "Integer32"
_S5AgSysFlushMacAddrTableByTrunk_Object = MibScalar
s5AgSysFlushMacAddrTableByTrunk = _S5AgSysFlushMacAddrTableByTrunk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 31),
    _S5AgSysFlushMacAddrTableByTrunk_Type()
)
s5AgSysFlushMacAddrTableByTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysFlushMacAddrTableByTrunk.setStatus("current")
_S5AgSysFlushMacAddrTableByAddress_Type = MacAddress
_S5AgSysFlushMacAddrTableByAddress_Object = MibScalar
s5AgSysFlushMacAddrTableByAddress = _S5AgSysFlushMacAddrTableByAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 32),
    _S5AgSysFlushMacAddrTableByAddress_Type()
)
s5AgSysFlushMacAddrTableByAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysFlushMacAddrTableByAddress.setStatus("current")


class _S5AgSysVlanConfigControl_Type(Integer32):
    """Custom type s5AgSysVlanConfigControl based on Integer32"""
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
        *(("automatic", 1),
          ("autopvid", 2),
          ("flexible", 3),
          ("strict", 4))
    )


_S5AgSysVlanConfigControl_Type.__name__ = "Integer32"
_S5AgSysVlanConfigControl_Object = MibScalar
s5AgSysVlanConfigControl = _S5AgSysVlanConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 33),
    _S5AgSysVlanConfigControl_Type()
)
s5AgSysVlanConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysVlanConfigControl.setStatus("current")
_S5AgSysJumboFramesEnabled_Type = TruthValue
_S5AgSysJumboFramesEnabled_Object = MibScalar
s5AgSysJumboFramesEnabled = _S5AgSysJumboFramesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 34),
    _S5AgSysJumboFramesEnabled_Type()
)
s5AgSysJumboFramesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysJumboFramesEnabled.setStatus("current")


class _S5AgSysAutoUnitReplacementSaveEnabled_Type(TruthValue):
    """Custom type s5AgSysAutoUnitReplacementSaveEnabled based on TruthValue"""


_S5AgSysAutoUnitReplacementSaveEnabled_Object = MibScalar
s5AgSysAutoUnitReplacementSaveEnabled = _S5AgSysAutoUnitReplacementSaveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 35),
    _S5AgSysAutoUnitReplacementSaveEnabled_Type()
)
s5AgSysAutoUnitReplacementSaveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutoUnitReplacementSaveEnabled.setStatus("current")


class _S5AgSysAutoUnitReplacementRestore_Type(Integer32):
    """Custom type s5AgSysAutoUnitReplacementRestore based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_S5AgSysAutoUnitReplacementRestore_Type.__name__ = "Integer32"
_S5AgSysAutoUnitReplacementRestore_Object = MibScalar
s5AgSysAutoUnitReplacementRestore = _S5AgSysAutoUnitReplacementRestore_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 36),
    _S5AgSysAutoUnitReplacementRestore_Type()
)
s5AgSysAutoUnitReplacementRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutoUnitReplacementRestore.setStatus("current")


class _S5AgSysAutoUnitReplacementForceSave_Type(Integer32):
    """Custom type s5AgSysAutoUnitReplacementForceSave based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_S5AgSysAutoUnitReplacementForceSave_Type.__name__ = "Integer32"
_S5AgSysAutoUnitReplacementForceSave_Object = MibScalar
s5AgSysAutoUnitReplacementForceSave = _S5AgSysAutoUnitReplacementForceSave_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 37),
    _S5AgSysAutoUnitReplacementForceSave_Type()
)
s5AgSysAutoUnitReplacementForceSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAutoUnitReplacementForceSave.setStatus("current")
_S5AgSysTftpServerInetAddressType_Type = InetAddressType
_S5AgSysTftpServerInetAddressType_Object = MibScalar
s5AgSysTftpServerInetAddressType = _S5AgSysTftpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 38),
    _S5AgSysTftpServerInetAddressType_Type()
)
s5AgSysTftpServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysTftpServerInetAddressType.setStatus("current")
_S5AgSysTftpServerInetAddress_Type = InetAddress
_S5AgSysTftpServerInetAddress_Object = MibScalar
s5AgSysTftpServerInetAddress = _S5AgSysTftpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 39),
    _S5AgSysTftpServerInetAddress_Type()
)
s5AgSysTftpServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysTftpServerInetAddress.setStatus("current")


class _S5AgSysTelnetSessionLoginAuthenType_Type(Integer32):
    """Custom type s5AgSysTelnetSessionLoginAuthenType based on Integer32"""
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
        *(("local", 2),
          ("none", 1),
          ("radius", 3),
          ("tacacs", 4))
    )


_S5AgSysTelnetSessionLoginAuthenType_Type.__name__ = "Integer32"
_S5AgSysTelnetSessionLoginAuthenType_Object = MibScalar
s5AgSysTelnetSessionLoginAuthenType = _S5AgSysTelnetSessionLoginAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 40),
    _S5AgSysTelnetSessionLoginAuthenType_Type()
)
s5AgSysTelnetSessionLoginAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysTelnetSessionLoginAuthenType.setStatus("current")


class _S5AgSysSerialConsoleLoginAuthenType_Type(Integer32):
    """Custom type s5AgSysSerialConsoleLoginAuthenType based on Integer32"""
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
        *(("local", 2),
          ("none", 1),
          ("radius", 3),
          ("tacacs", 4))
    )


_S5AgSysSerialConsoleLoginAuthenType_Type.__name__ = "Integer32"
_S5AgSysSerialConsoleLoginAuthenType_Object = MibScalar
s5AgSysSerialConsoleLoginAuthenType = _S5AgSysSerialConsoleLoginAuthenType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 41),
    _S5AgSysSerialConsoleLoginAuthenType_Type()
)
s5AgSysSerialConsoleLoginAuthenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSerialConsoleLoginAuthenType.setStatus("current")


class _S5AgSysSshAuthKeyFilename_Type(DisplayString):
    """Custom type s5AgSysSshAuthKeyFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S5AgSysSshAuthKeyFilename_Type.__name__ = "DisplayString"
_S5AgSysSshAuthKeyFilename_Object = MibScalar
s5AgSysSshAuthKeyFilename = _S5AgSysSshAuthKeyFilename_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 42),
    _S5AgSysSshAuthKeyFilename_Type()
)
s5AgSysSshAuthKeyFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSshAuthKeyFilename.setStatus("current")


class _S5AgSysAsciiConfigManualUploadApplications_Type(Bits):
    """Custom type s5AgSysAsciiConfigManualUploadApplications based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 61),
          ("aaur", 1),
          ("adac", 2),
          ("arpInspection", 3),
          ("assetId", 4),
          ("aur", 5),
          ("banner", 6),
          ("brouter", 7),
          ("cfm", 53),
          ("cops", 8),
          ("core", 9),
          ("defaultCmdInterface", 10),
          ("dhcpRelay", 11),
          ("dhcpServer", 51),
          ("dhcpSnooping", 12),
          ("eap", 13),
          ("energySaver", 47),
          ("esu", 14),
          ("fabric-attach", 62),
          ("fcoe", 52),
          ("ieee802dot1ab", 0),
          ("interface", 15),
          ("ip", 16),
          ("ipSourceGuard", 17),
          ("ipfix", 18),
          ("ipmc", 19),
          ("ipmgr", 20),
          ("ipv6", 21),
          ("ipv6-fhs", 59),
          ("ipv6-mld", 58),
          ("ipv6-ripng", 63),
          ("l3", 22),
          ("l3Protocols", 23),
          ("lacp", 24),
          ("logging", 25),
          ("lst", 56),
          ("macSecurity", 26),
          ("mlt", 27),
          ("nsna", 39),
          ("pim", 28),
          ("poe", 29),
          ("portMirroring", 30),
          ("pvst", 31),
          ("qos", 32),
          ("radius", 64),
          ("rateLimit", 33),
          ("rmon", 34),
          ("rtc", 35),
          ("sflow", 57),
          ("slamon", 54),
          ("slpp", 36),
          ("smlt", 38),
          ("snmp", 37),
          ("spbm", 55),
          ("ssh", 40),
          ("sshc", 50),
          ("ssl", 41),
          ("stack", 42),
          ("stkmon", 43),
          ("stormControl", 60),
          ("stp", 44),
          ("unicastStormControl", 48),
          ("vlacp", 45),
          ("vlan", 46),
          ("wireless", 49))
    )

_S5AgSysAsciiConfigManualUploadApplications_Type.__name__ = "Bits"
_S5AgSysAsciiConfigManualUploadApplications_Object = MibScalar
s5AgSysAsciiConfigManualUploadApplications = _S5AgSysAsciiConfigManualUploadApplications_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 43),
    _S5AgSysAsciiConfigManualUploadApplications_Type()
)
s5AgSysAsciiConfigManualUploadApplications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAsciiConfigManualUploadApplications.setStatus("current")


class _S5AgSysOperationalLicense_Type(Integer32):
    """Custom type s5AgSysOperationalLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("advanced-macsec", 6),
          ("basic", 1),
          ("macsec", 5),
          ("premier", 3),
          ("stack", 4))
    )


_S5AgSysOperationalLicense_Type.__name__ = "Integer32"
_S5AgSysOperationalLicense_Object = MibScalar
s5AgSysOperationalLicense = _S5AgSysOperationalLicense_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 44),
    _S5AgSysOperationalLicense_Type()
)
s5AgSysOperationalLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysOperationalLicense.setStatus("current")


class _S5AgSysInstalledLicense_Type(Integer32):
    """Custom type s5AgSysInstalledLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("advanced-macsec", 6),
          ("basic", 1),
          ("macsec", 5),
          ("premier", 3),
          ("stack", 4))
    )


_S5AgSysInstalledLicense_Type.__name__ = "Integer32"
_S5AgSysInstalledLicense_Object = MibScalar
s5AgSysInstalledLicense = _S5AgSysInstalledLicense_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 45),
    _S5AgSysInstalledLicense_Type()
)
s5AgSysInstalledLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSysInstalledLicense.setStatus("current")
_S5AgSysCpuIpv6Address_Type = Ipv6Address
_S5AgSysCpuIpv6Address_Object = MibScalar
s5AgSysCpuIpv6Address = _S5AgSysCpuIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 46),
    _S5AgSysCpuIpv6Address_Type()
)
s5AgSysCpuIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysCpuIpv6Address.setStatus("current")
_S5AgSysStackIpv6Address_Type = Ipv6Address
_S5AgSysStackIpv6Address_Object = MibScalar
s5AgSysStackIpv6Address = _S5AgSysStackIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 47),
    _S5AgSysStackIpv6Address_Type()
)
s5AgSysStackIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackIpv6Address.setStatus("current")
_S5AgSysCpuIpv6NetMask_Type = Ipv6AddressPrefix
_S5AgSysCpuIpv6NetMask_Object = MibScalar
s5AgSysCpuIpv6NetMask = _S5AgSysCpuIpv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 48),
    _S5AgSysCpuIpv6NetMask_Type()
)
s5AgSysCpuIpv6NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysCpuIpv6NetMask.setStatus("current")
_S5AgSysStackIpv6NetMask_Type = Ipv6AddressPrefix
_S5AgSysStackIpv6NetMask_Object = MibScalar
s5AgSysStackIpv6NetMask = _S5AgSysStackIpv6NetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 49),
    _S5AgSysStackIpv6NetMask_Type()
)
s5AgSysStackIpv6NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackIpv6NetMask.setStatus("current")
_S5AgSysIpv6DefaultGateway_Type = Ipv6Address
_S5AgSysIpv6DefaultGateway_Object = MibScalar
s5AgSysIpv6DefaultGateway = _S5AgSysIpv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 50),
    _S5AgSysIpv6DefaultGateway_Type()
)
s5AgSysIpv6DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysIpv6DefaultGateway.setStatus("current")


class _S5AgSysSpanningTreeBpduFilterIgnoreSelf_Type(TruthValue):
    """Custom type s5AgSysSpanningTreeBpduFilterIgnoreSelf based on TruthValue"""


_S5AgSysSpanningTreeBpduFilterIgnoreSelf_Object = MibScalar
s5AgSysSpanningTreeBpduFilterIgnoreSelf = _S5AgSysSpanningTreeBpduFilterIgnoreSelf_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 51),
    _S5AgSysSpanningTreeBpduFilterIgnoreSelf_Type()
)
s5AgSysSpanningTreeBpduFilterIgnoreSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSpanningTreeBpduFilterIgnoreSelf.setStatus("current")


class _S5AgSysIdentifyUnits_Type(Integer32):
    """Custom type s5AgSysIdentifyUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 1),
          ("identify", 2))
    )


_S5AgSysIdentifyUnits_Type.__name__ = "Integer32"
_S5AgSysIdentifyUnits_Object = MibScalar
s5AgSysIdentifyUnits = _S5AgSysIdentifyUnits_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 52),
    _S5AgSysIdentifyUnits_Type()
)
s5AgSysIdentifyUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysIdentifyUnits.setStatus("current")
_S5AgSysMacAddrTableLearningPorts_Type = PortList
_S5AgSysMacAddrTableLearningPorts_Object = MibScalar
s5AgSysMacAddrTableLearningPorts = _S5AgSysMacAddrTableLearningPorts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 53),
    _S5AgSysMacAddrTableLearningPorts_Type()
)
s5AgSysMacAddrTableLearningPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysMacAddrTableLearningPorts.setStatus("current")
_S5AgSysSerialSecurityEnable_Type = TruthValue
_S5AgSysSerialSecurityEnable_Object = MibScalar
s5AgSysSerialSecurityEnable = _S5AgSysSerialSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 54),
    _S5AgSysSerialSecurityEnable_Type()
)
s5AgSysSerialSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSerialSecurityEnable.setStatus("current")
_S5AgSysMgmtStackIpAddress_Type = IpAddress
_S5AgSysMgmtStackIpAddress_Object = MibScalar
s5AgSysMgmtStackIpAddress = _S5AgSysMgmtStackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 55),
    _S5AgSysMgmtStackIpAddress_Type()
)
s5AgSysMgmtStackIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysMgmtStackIpAddress.setStatus("current")
_S5AgSysAuditEnable_Type = TruthValue
_S5AgSysAuditEnable_Object = MibScalar
s5AgSysAuditEnable = _S5AgSysAuditEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 56),
    _S5AgSysAuditEnable_Type()
)
s5AgSysAuditEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysAuditEnable.setStatus("current")
_S5AgSysQuickConfigEnable_Type = TruthValue
_S5AgSysQuickConfigEnable_Object = MibScalar
s5AgSysQuickConfigEnable = _S5AgSysQuickConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 57),
    _S5AgSysQuickConfigEnable_Type()
)
s5AgSysQuickConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysQuickConfigEnable.setStatus("current")
_S5AgSysStackIpv6MgmtAddress_Type = Ipv6Address
_S5AgSysStackIpv6MgmtAddress_Object = MibScalar
s5AgSysStackIpv6MgmtAddress = _S5AgSysStackIpv6MgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 58),
    _S5AgSysStackIpv6MgmtAddress_Type()
)
s5AgSysStackIpv6MgmtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackIpv6MgmtAddress.setStatus("current")
_S5AgSysStackIpv6MgmtNetMask_Type = Ipv6AddressPrefix
_S5AgSysStackIpv6MgmtNetMask_Object = MibScalar
s5AgSysStackIpv6MgmtNetMask = _S5AgSysStackIpv6MgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 59),
    _S5AgSysStackIpv6MgmtNetMask_Type()
)
s5AgSysStackIpv6MgmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysStackIpv6MgmtNetMask.setStatus("current")
_S5AgSysIpv6MgmtGateway_Type = Ipv6Address
_S5AgSysIpv6MgmtGateway_Object = MibScalar
s5AgSysIpv6MgmtGateway = _S5AgSysIpv6MgmtGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 60),
    _S5AgSysIpv6MgmtGateway_Type()
)
s5AgSysIpv6MgmtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysIpv6MgmtGateway.setStatus("current")


class _S5AgSysBlinkLeds_Type(Integer32):
    """Custom type s5AgSysBlinkLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_S5AgSysBlinkLeds_Type.__name__ = "Integer32"
_S5AgSysBlinkLeds_Object = MibScalar
s5AgSysBlinkLeds = _S5AgSysBlinkLeds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 61),
    _S5AgSysBlinkLeds_Type()
)
s5AgSysBlinkLeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysBlinkLeds.setStatus("current")


class _S5AgSysBlinkLedsUnit_Type(Integer32):
    """Custom type s5AgSysBlinkLedsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_S5AgSysBlinkLedsUnit_Type.__name__ = "Integer32"
_S5AgSysBlinkLedsUnit_Object = MibScalar
s5AgSysBlinkLedsUnit = _S5AgSysBlinkLedsUnit_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 62),
    _S5AgSysBlinkLedsUnit_Type()
)
s5AgSysBlinkLedsUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysBlinkLedsUnit.setStatus("current")


class _S5AgSysBlinkLedsTimeThreshold_Type(Integer32):
    """Custom type s5AgSysBlinkLedsTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_S5AgSysBlinkLedsTimeThreshold_Type.__name__ = "Integer32"
_S5AgSysBlinkLedsTimeThreshold_Object = MibScalar
s5AgSysBlinkLedsTimeThreshold = _S5AgSysBlinkLedsTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 63),
    _S5AgSysBlinkLedsTimeThreshold_Type()
)
s5AgSysBlinkLedsTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysBlinkLedsTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    s5AgSysBlinkLedsTimeThreshold.setUnits("Minutes")


class _S5AgSysJumboFramesSize_Type(Integer32):
    """Custom type s5AgSysJumboFramesSize based on Integer32"""
    defaultValue = 9216

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1519, 9216),
    )


_S5AgSysJumboFramesSize_Type.__name__ = "Integer32"
_S5AgSysJumboFramesSize_Object = MibScalar
s5AgSysJumboFramesSize = _S5AgSysJumboFramesSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 64),
    _S5AgSysJumboFramesSize_Type()
)
s5AgSysJumboFramesSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysJumboFramesSize.setStatus("current")
if mibBuilder.loadTexts:
    s5AgSysJumboFramesSize.setUnits("Bytes")
_S5AgSysDiagnosticsQuickModeEnabled_Type = TruthValue
_S5AgSysDiagnosticsQuickModeEnabled_Object = MibScalar
s5AgSysDiagnosticsQuickModeEnabled = _S5AgSysDiagnosticsQuickModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 65),
    _S5AgSysDiagnosticsQuickModeEnabled_Type()
)
s5AgSysDiagnosticsQuickModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysDiagnosticsQuickModeEnabled.setStatus("current")
_S5AgSysTimeStampEnabled_Type = TruthValue
_S5AgSysTimeStampEnabled_Object = MibScalar
s5AgSysTimeStampEnabled = _S5AgSysTimeStampEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 66),
    _S5AgSysTimeStampEnabled_Type()
)
s5AgSysTimeStampEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysTimeStampEnabled.setStatus("current")
_S5AgSysForcedStackModeEnabled_Type = TruthValue
_S5AgSysForcedStackModeEnabled_Object = MibScalar
s5AgSysForcedStackModeEnabled = _S5AgSysForcedStackModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 67),
    _S5AgSysForcedStackModeEnabled_Type()
)
s5AgSysForcedStackModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysForcedStackModeEnabled.setStatus("current")
_S5AgSysSflowGlobalEnable_Type = TruthValue
_S5AgSysSflowGlobalEnable_Object = MibScalar
s5AgSysSflowGlobalEnable = _S5AgSysSflowGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 4, 68),
    _S5AgSysSflowGlobalEnable_Type()
)
s5AgSysSflowGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSysSflowGlobalEnable.setStatus("current")
_S5AgentBanner_ObjectIdentity = ObjectIdentity
s5AgentBanner = _S5AgentBanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5)
)


class _S5AgBannerControl_Type(Integer32):
    """Custom type s5AgBannerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("disabled", 3),
          ("static", 1))
    )


_S5AgBannerControl_Type.__name__ = "Integer32"
_S5AgBannerControl_Object = MibScalar
s5AgBannerControl = _S5AgBannerControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 1),
    _S5AgBannerControl_Type()
)
s5AgBannerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgBannerControl.setStatus("current")
_S5AgCustomBannerTable_Object = MibTable
s5AgCustomBannerTable = _S5AgCustomBannerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 2)
)
if mibBuilder.loadTexts:
    s5AgCustomBannerTable.setStatus("current")
_S5AgCustomBannerEntry_Object = MibTableRow
s5AgCustomBannerEntry = _S5AgCustomBannerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 2, 1)
)
s5AgCustomBannerEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgCustomBannerType"),
    (0, "S5-AGENT-MIB", "s5AgCustomBannerId"),
)
if mibBuilder.loadTexts:
    s5AgCustomBannerEntry.setStatus("current")


class _S5AgCustomBannerType_Type(Integer32):
    """Custom type s5AgCustomBannerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 2),
          ("switch", 1))
    )


_S5AgCustomBannerType_Type.__name__ = "Integer32"
_S5AgCustomBannerType_Object = MibTableColumn
s5AgCustomBannerType = _S5AgCustomBannerType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 2, 1, 1),
    _S5AgCustomBannerType_Type()
)
s5AgCustomBannerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgCustomBannerType.setStatus("current")


class _S5AgCustomBannerId_Type(Integer32):
    """Custom type s5AgCustomBannerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_S5AgCustomBannerId_Type.__name__ = "Integer32"
_S5AgCustomBannerId_Object = MibTableColumn
s5AgCustomBannerId = _S5AgCustomBannerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 2, 1, 2),
    _S5AgCustomBannerId_Type()
)
s5AgCustomBannerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgCustomBannerId.setStatus("current")


class _S5AgCustomBannerLine_Type(DisplayString):
    """Custom type s5AgCustomBannerLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_S5AgCustomBannerLine_Type.__name__ = "DisplayString"
_S5AgCustomBannerLine_Object = MibTableColumn
s5AgCustomBannerLine = _S5AgCustomBannerLine_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 5, 2, 1, 3),
    _S5AgCustomBannerLine_Type()
)
s5AgCustomBannerLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgCustomBannerLine.setStatus("current")
_S5AgentSntp_ObjectIdentity = ObjectIdentity
s5AgentSntp = _S5AgentSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6)
)


class _S5AgSntpState_Type(Integer32):
    """Custom type s5AgSntpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("unicast", 2))
    )


_S5AgSntpState_Type.__name__ = "Integer32"
_S5AgSntpState_Object = MibScalar
s5AgSntpState = _S5AgSntpState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 1),
    _S5AgSntpState_Type()
)
s5AgSntpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpState.setStatus("current")
_S5AgSntpPrimaryServerAddress_Type = IpAddress
_S5AgSntpPrimaryServerAddress_Object = MibScalar
s5AgSntpPrimaryServerAddress = _S5AgSntpPrimaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 2),
    _S5AgSntpPrimaryServerAddress_Type()
)
s5AgSntpPrimaryServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpPrimaryServerAddress.setStatus("current")
_S5AgSntpSecondaryServerAddress_Type = IpAddress
_S5AgSntpSecondaryServerAddress_Object = MibScalar
s5AgSntpSecondaryServerAddress = _S5AgSntpSecondaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 3),
    _S5AgSntpSecondaryServerAddress_Type()
)
s5AgSntpSecondaryServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpSecondaryServerAddress.setStatus("current")


class _S5AgSntpSyncInterval_Type(Integer32):
    """Custom type s5AgSntpSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_S5AgSntpSyncInterval_Type.__name__ = "Integer32"
_S5AgSntpSyncInterval_Object = MibScalar
s5AgSntpSyncInterval = _S5AgSntpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 4),
    _S5AgSntpSyncInterval_Type()
)
s5AgSntpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    s5AgSntpSyncInterval.setUnits("Hours")


class _S5AgSntpManualSyncRequest_Type(Integer32):
    """Custom type s5AgSntpManualSyncRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("requestSync", 1)
    )


_S5AgSntpManualSyncRequest_Type.__name__ = "Integer32"
_S5AgSntpManualSyncRequest_Object = MibScalar
s5AgSntpManualSyncRequest = _S5AgSntpManualSyncRequest_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 5),
    _S5AgSntpManualSyncRequest_Type()
)
s5AgSntpManualSyncRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpManualSyncRequest.setStatus("current")
_S5AgSntpLastSyncTime_Type = DateAndTime
_S5AgSntpLastSyncTime_Object = MibScalar
s5AgSntpLastSyncTime = _S5AgSntpLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 6),
    _S5AgSntpLastSyncTime_Type()
)
s5AgSntpLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpLastSyncTime.setStatus("current")
_S5AgSntpLastSyncSource_Type = IpAddress
_S5AgSntpLastSyncSource_Object = MibScalar
s5AgSntpLastSyncSource = _S5AgSntpLastSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 7),
    _S5AgSntpLastSyncSource_Type()
)
s5AgSntpLastSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpLastSyncSource.setStatus("current")
_S5AgSntpNextSyncTime_Type = DateAndTime
_S5AgSntpNextSyncTime_Object = MibScalar
s5AgSntpNextSyncTime = _S5AgSntpNextSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 8),
    _S5AgSntpNextSyncTime_Type()
)
s5AgSntpNextSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpNextSyncTime.setStatus("current")
_S5AgSntpPrimaryServerSyncFailures_Type = Counter32
_S5AgSntpPrimaryServerSyncFailures_Object = MibScalar
s5AgSntpPrimaryServerSyncFailures = _S5AgSntpPrimaryServerSyncFailures_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 9),
    _S5AgSntpPrimaryServerSyncFailures_Type()
)
s5AgSntpPrimaryServerSyncFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpPrimaryServerSyncFailures.setStatus("current")
_S5AgSntpSecondaryServerSyncFailures_Type = Counter32
_S5AgSntpSecondaryServerSyncFailures_Object = MibScalar
s5AgSntpSecondaryServerSyncFailures = _S5AgSntpSecondaryServerSyncFailures_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 10),
    _S5AgSntpSecondaryServerSyncFailures_Type()
)
s5AgSntpSecondaryServerSyncFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpSecondaryServerSyncFailures.setStatus("current")
_S5AgSntpCurrentTime_Type = DateAndTime
_S5AgSntpCurrentTime_Object = MibScalar
s5AgSntpCurrentTime = _S5AgSntpCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 11),
    _S5AgSntpCurrentTime_Type()
)
s5AgSntpCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpCurrentTime.setStatus("current")


class _S5AgSntpTimeZone_Type(Integer32):
    """Custom type s5AgSntpTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-48, 52),
    )


_S5AgSntpTimeZone_Type.__name__ = "Integer32"
_S5AgSntpTimeZone_Object = MibScalar
s5AgSntpTimeZone = _S5AgSntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 12),
    _S5AgSntpTimeZone_Type()
)
s5AgSntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpTimeZone.setStatus("current")


class _S5AgSntpSyncRetryInterval_Type(Integer32):
    """Custom type s5AgSntpSyncRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_S5AgSntpSyncRetryInterval_Type.__name__ = "Integer32"
_S5AgSntpSyncRetryInterval_Object = MibScalar
s5AgSntpSyncRetryInterval = _S5AgSntpSyncRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 13),
    _S5AgSntpSyncRetryInterval_Type()
)
s5AgSntpSyncRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpSyncRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    s5AgSntpSyncRetryInterval.setUnits("Seconds")


class _S5AgSntpTimeZoneAcronym_Type(DisplayString):
    """Custom type s5AgSntpTimeZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_S5AgSntpTimeZoneAcronym_Type.__name__ = "DisplayString"
_S5AgSntpTimeZoneAcronym_Object = MibScalar
s5AgSntpTimeZoneAcronym = _S5AgSntpTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 14),
    _S5AgSntpTimeZoneAcronym_Type()
)
s5AgSntpTimeZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpTimeZoneAcronym.setStatus("current")
_S5AgSntpPrimaryServerInetAddressType_Type = InetAddressType
_S5AgSntpPrimaryServerInetAddressType_Object = MibScalar
s5AgSntpPrimaryServerInetAddressType = _S5AgSntpPrimaryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 15),
    _S5AgSntpPrimaryServerInetAddressType_Type()
)
s5AgSntpPrimaryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpPrimaryServerInetAddressType.setStatus("current")
_S5AgSntpPrimaryServerInetAddress_Type = InetAddress
_S5AgSntpPrimaryServerInetAddress_Object = MibScalar
s5AgSntpPrimaryServerInetAddress = _S5AgSntpPrimaryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 16),
    _S5AgSntpPrimaryServerInetAddress_Type()
)
s5AgSntpPrimaryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpPrimaryServerInetAddress.setStatus("current")
_S5AgSntpSecondaryServerInetAddressType_Type = InetAddressType
_S5AgSntpSecondaryServerInetAddressType_Object = MibScalar
s5AgSntpSecondaryServerInetAddressType = _S5AgSntpSecondaryServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 17),
    _S5AgSntpSecondaryServerInetAddressType_Type()
)
s5AgSntpSecondaryServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpSecondaryServerInetAddressType.setStatus("current")
_S5AgSntpSecondaryServerInetAddress_Type = InetAddress
_S5AgSntpSecondaryServerInetAddress_Object = MibScalar
s5AgSntpSecondaryServerInetAddress = _S5AgSntpSecondaryServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 18),
    _S5AgSntpSecondaryServerInetAddress_Type()
)
s5AgSntpSecondaryServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSntpSecondaryServerInetAddress.setStatus("current")
_S5AgSntpLastSyncSourceInetAddressType_Type = InetAddressType
_S5AgSntpLastSyncSourceInetAddressType_Object = MibScalar
s5AgSntpLastSyncSourceInetAddressType = _S5AgSntpLastSyncSourceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 19),
    _S5AgSntpLastSyncSourceInetAddressType_Type()
)
s5AgSntpLastSyncSourceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpLastSyncSourceInetAddressType.setStatus("current")
_S5AgSntpLastSyncSourceInetAddress_Type = InetAddress
_S5AgSntpLastSyncSourceInetAddress_Object = MibScalar
s5AgSntpLastSyncSourceInetAddress = _S5AgSntpLastSyncSourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 6, 20),
    _S5AgSntpLastSyncSourceInetAddress_Type()
)
s5AgSntpLastSyncSourceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSntpLastSyncSourceInetAddress.setStatus("current")
_S5AgentSsl_ObjectIdentity = ObjectIdentity
s5AgentSsl = _S5AgentSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7)
)
_S5AgentSslScalars_ObjectIdentity = ObjectIdentity
s5AgentSslScalars = _S5AgentSslScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1)
)
_S5AgSslEnabled_Type = TruthValue
_S5AgSslEnabled_Object = MibScalar
s5AgSslEnabled = _S5AgSslEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 1),
    _S5AgSslEnabled_Type()
)
s5AgSslEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSslEnabled.setStatus("current")


class _S5AgSslCertificateControl_Type(Integer32):
    """Custom type s5AgSslCertificateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("other", 3))
    )


_S5AgSslCertificateControl_Type.__name__ = "Integer32"
_S5AgSslCertificateControl_Object = MibScalar
s5AgSslCertificateControl = _S5AgSslCertificateControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 3),
    _S5AgSslCertificateControl_Type()
)
s5AgSslCertificateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSslCertificateControl.setStatus("current")
_S5AgSslCertificateExists_Type = TruthValue
_S5AgSslCertificateExists_Object = MibScalar
s5AgSslCertificateExists = _S5AgSslCertificateExists_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 4),
    _S5AgSslCertificateExists_Type()
)
s5AgSslCertificateExists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSslCertificateExists.setStatus("current")


class _S5AgSslCertificateData_Type(OctetString):
    """Custom type s5AgSslCertificateData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_S5AgSslCertificateData_Type.__name__ = "OctetString"
_S5AgSslCertificateData_Object = MibScalar
s5AgSslCertificateData = _S5AgSslCertificateData_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 5),
    _S5AgSslCertificateData_Type()
)
s5AgSslCertificateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSslCertificateData.setStatus("current")


class _S5AgSslCertificateControlStatus_Type(Integer32):
    """Custom type s5AgSslCertificateControlStatus based on Integer32"""
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
        *(("failure", 3),
          ("inProgress", 1),
          ("other", 4),
          ("success", 2))
    )


_S5AgSslCertificateControlStatus_Type.__name__ = "Integer32"
_S5AgSslCertificateControlStatus_Object = MibScalar
s5AgSslCertificateControlStatus = _S5AgSslCertificateControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 6),
    _S5AgSslCertificateControlStatus_Type()
)
s5AgSslCertificateControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgSslCertificateControlStatus.setStatus("current")


class _S5AgSslServerControl_Type(Integer32):
    """Custom type s5AgSslServerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("reset", 1))
    )


_S5AgSslServerControl_Type.__name__ = "Integer32"
_S5AgSslServerControl_Object = MibScalar
s5AgSslServerControl = _S5AgSslServerControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 7, 1, 7),
    _S5AgSslServerControl_Type()
)
s5AgSslServerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgSslServerControl.setStatus("current")
_S5AgentDaylightSavings_ObjectIdentity = ObjectIdentity
s5AgentDaylightSavings = _S5AgentDaylightSavings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9)
)
_S5AgDaylightSavingsEnabled_Type = TruthValue
_S5AgDaylightSavingsEnabled_Object = MibScalar
s5AgDaylightSavingsEnabled = _S5AgDaylightSavingsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 1),
    _S5AgDaylightSavingsEnabled_Type()
)
s5AgDaylightSavingsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEnabled.setStatus("current")


class _S5AgDaylightSavingsStartMonth_Type(Integer32):
    """Custom type s5AgDaylightSavingsStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_S5AgDaylightSavingsStartMonth_Type.__name__ = "Integer32"
_S5AgDaylightSavingsStartMonth_Object = MibScalar
s5AgDaylightSavingsStartMonth = _S5AgDaylightSavingsStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 2),
    _S5AgDaylightSavingsStartMonth_Type()
)
s5AgDaylightSavingsStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsStartMonth.setStatus("current")


class _S5AgDaylightSavingsStartDay_Type(Integer32):
    """Custom type s5AgDaylightSavingsStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_S5AgDaylightSavingsStartDay_Type.__name__ = "Integer32"
_S5AgDaylightSavingsStartDay_Object = MibScalar
s5AgDaylightSavingsStartDay = _S5AgDaylightSavingsStartDay_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 3),
    _S5AgDaylightSavingsStartDay_Type()
)
s5AgDaylightSavingsStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsStartDay.setStatus("current")


class _S5AgDaylightSavingsStartHour_Type(Integer32):
    """Custom type s5AgDaylightSavingsStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_S5AgDaylightSavingsStartHour_Type.__name__ = "Integer32"
_S5AgDaylightSavingsStartHour_Object = MibScalar
s5AgDaylightSavingsStartHour = _S5AgDaylightSavingsStartHour_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 4),
    _S5AgDaylightSavingsStartHour_Type()
)
s5AgDaylightSavingsStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsStartHour.setStatus("current")


class _S5AgDaylightSavingsEndMonth_Type(Integer32):
    """Custom type s5AgDaylightSavingsEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_S5AgDaylightSavingsEndMonth_Type.__name__ = "Integer32"
_S5AgDaylightSavingsEndMonth_Object = MibScalar
s5AgDaylightSavingsEndMonth = _S5AgDaylightSavingsEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 5),
    _S5AgDaylightSavingsEndMonth_Type()
)
s5AgDaylightSavingsEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEndMonth.setStatus("current")


class _S5AgDaylightSavingsEndDay_Type(Integer32):
    """Custom type s5AgDaylightSavingsEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_S5AgDaylightSavingsEndDay_Type.__name__ = "Integer32"
_S5AgDaylightSavingsEndDay_Object = MibScalar
s5AgDaylightSavingsEndDay = _S5AgDaylightSavingsEndDay_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 6),
    _S5AgDaylightSavingsEndDay_Type()
)
s5AgDaylightSavingsEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEndDay.setStatus("current")


class _S5AgDaylightSavingsEndHour_Type(Integer32):
    """Custom type s5AgDaylightSavingsEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_S5AgDaylightSavingsEndHour_Type.__name__ = "Integer32"
_S5AgDaylightSavingsEndHour_Object = MibScalar
s5AgDaylightSavingsEndHour = _S5AgDaylightSavingsEndHour_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 7),
    _S5AgDaylightSavingsEndHour_Type()
)
s5AgDaylightSavingsEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEndHour.setStatus("current")


class _S5AgDaylightSavingsOffset_Type(Integer32):
    """Custom type s5AgDaylightSavingsOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-840, 840),
    )


_S5AgDaylightSavingsOffset_Type.__name__ = "Integer32"
_S5AgDaylightSavingsOffset_Object = MibScalar
s5AgDaylightSavingsOffset = _S5AgDaylightSavingsOffset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 8),
    _S5AgDaylightSavingsOffset_Type()
)
s5AgDaylightSavingsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsOffset.setStatus("current")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsOffset.setUnits("Minutes")


class _S5AgDaylightSavingsStartMinutes_Type(Integer32):
    """Custom type s5AgDaylightSavingsStartMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_S5AgDaylightSavingsStartMinutes_Type.__name__ = "Integer32"
_S5AgDaylightSavingsStartMinutes_Object = MibScalar
s5AgDaylightSavingsStartMinutes = _S5AgDaylightSavingsStartMinutes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 9),
    _S5AgDaylightSavingsStartMinutes_Type()
)
s5AgDaylightSavingsStartMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsStartMinutes.setStatus("current")


class _S5AgDaylightSavingsEndMinutes_Type(Integer32):
    """Custom type s5AgDaylightSavingsEndMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_S5AgDaylightSavingsEndMinutes_Type.__name__ = "Integer32"
_S5AgDaylightSavingsEndMinutes_Object = MibScalar
s5AgDaylightSavingsEndMinutes = _S5AgDaylightSavingsEndMinutes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 10),
    _S5AgDaylightSavingsEndMinutes_Type()
)
s5AgDaylightSavingsEndMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEndMinutes.setStatus("current")


class _S5AgDaylightSavingsStartYear_Type(Integer32):
    """Custom type s5AgDaylightSavingsStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1990, 2099),
    )


_S5AgDaylightSavingsStartYear_Type.__name__ = "Integer32"
_S5AgDaylightSavingsStartYear_Object = MibScalar
s5AgDaylightSavingsStartYear = _S5AgDaylightSavingsStartYear_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 11),
    _S5AgDaylightSavingsStartYear_Type()
)
s5AgDaylightSavingsStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsStartYear.setStatus("current")


class _S5AgDaylightSavingsEndYear_Type(Integer32):
    """Custom type s5AgDaylightSavingsEndYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1990, 2099),
    )


_S5AgDaylightSavingsEndYear_Type.__name__ = "Integer32"
_S5AgDaylightSavingsEndYear_Object = MibScalar
s5AgDaylightSavingsEndYear = _S5AgDaylightSavingsEndYear_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 12),
    _S5AgDaylightSavingsEndYear_Type()
)
s5AgDaylightSavingsEndYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsEndYear.setStatus("current")
_S5AgDaylightSavingsRecurring_Type = TruthValue
_S5AgDaylightSavingsRecurring_Object = MibScalar
s5AgDaylightSavingsRecurring = _S5AgDaylightSavingsRecurring_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 13),
    _S5AgDaylightSavingsRecurring_Type()
)
s5AgDaylightSavingsRecurring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurring.setStatus("current")


class _S5AgDaylightSavingsTimeZoneAcronym_Type(DisplayString):
    """Custom type s5AgDaylightSavingsTimeZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_S5AgDaylightSavingsTimeZoneAcronym_Type.__name__ = "DisplayString"
_S5AgDaylightSavingsTimeZoneAcronym_Object = MibScalar
s5AgDaylightSavingsTimeZoneAcronym = _S5AgDaylightSavingsTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 14),
    _S5AgDaylightSavingsTimeZoneAcronym_Type()
)
s5AgDaylightSavingsTimeZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsTimeZoneAcronym.setStatus("current")


class _S5AgDaylightSavingsRecurringStartWeek_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringStartWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5),
    )


_S5AgDaylightSavingsRecurringStartWeek_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringStartWeek_Object = MibScalar
s5AgDaylightSavingsRecurringStartWeek = _S5AgDaylightSavingsRecurringStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 15),
    _S5AgDaylightSavingsRecurringStartWeek_Type()
)
s5AgDaylightSavingsRecurringStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringStartWeek.setStatus("current")


class _S5AgDaylightSavingsRecurringStartDay_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_S5AgDaylightSavingsRecurringStartDay_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringStartDay_Object = MibScalar
s5AgDaylightSavingsRecurringStartDay = _S5AgDaylightSavingsRecurringStartDay_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 16),
    _S5AgDaylightSavingsRecurringStartDay_Type()
)
s5AgDaylightSavingsRecurringStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringStartDay.setStatus("current")


class _S5AgDaylightSavingsRecurringStartMonth_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringStartMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_S5AgDaylightSavingsRecurringStartMonth_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringStartMonth_Object = MibScalar
s5AgDaylightSavingsRecurringStartMonth = _S5AgDaylightSavingsRecurringStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 17),
    _S5AgDaylightSavingsRecurringStartMonth_Type()
)
s5AgDaylightSavingsRecurringStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringStartMonth.setStatus("current")


class _S5AgDaylightSavingsRecurringStartHour_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_S5AgDaylightSavingsRecurringStartHour_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringStartHour_Object = MibScalar
s5AgDaylightSavingsRecurringStartHour = _S5AgDaylightSavingsRecurringStartHour_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 18),
    _S5AgDaylightSavingsRecurringStartHour_Type()
)
s5AgDaylightSavingsRecurringStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringStartHour.setStatus("current")


class _S5AgDaylightSavingsRecurringStartMinute_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_S5AgDaylightSavingsRecurringStartMinute_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringStartMinute_Object = MibScalar
s5AgDaylightSavingsRecurringStartMinute = _S5AgDaylightSavingsRecurringStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 19),
    _S5AgDaylightSavingsRecurringStartMinute_Type()
)
s5AgDaylightSavingsRecurringStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringStartMinute.setStatus("current")


class _S5AgDaylightSavingsRecurringEndWeek_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringEndWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 5),
    )


_S5AgDaylightSavingsRecurringEndWeek_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringEndWeek_Object = MibScalar
s5AgDaylightSavingsRecurringEndWeek = _S5AgDaylightSavingsRecurringEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 20),
    _S5AgDaylightSavingsRecurringEndWeek_Type()
)
s5AgDaylightSavingsRecurringEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringEndWeek.setStatus("current")


class _S5AgDaylightSavingsRecurringEndDay_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringEndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_S5AgDaylightSavingsRecurringEndDay_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringEndDay_Object = MibScalar
s5AgDaylightSavingsRecurringEndDay = _S5AgDaylightSavingsRecurringEndDay_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 21),
    _S5AgDaylightSavingsRecurringEndDay_Type()
)
s5AgDaylightSavingsRecurringEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringEndDay.setStatus("current")


class _S5AgDaylightSavingsRecurringEndMonth_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringEndMonth based on Integer32"""
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_S5AgDaylightSavingsRecurringEndMonth_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringEndMonth_Object = MibScalar
s5AgDaylightSavingsRecurringEndMonth = _S5AgDaylightSavingsRecurringEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 22),
    _S5AgDaylightSavingsRecurringEndMonth_Type()
)
s5AgDaylightSavingsRecurringEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringEndMonth.setStatus("current")


class _S5AgDaylightSavingsRecurringEndHour_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_S5AgDaylightSavingsRecurringEndHour_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringEndHour_Object = MibScalar
s5AgDaylightSavingsRecurringEndHour = _S5AgDaylightSavingsRecurringEndHour_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 23),
    _S5AgDaylightSavingsRecurringEndHour_Type()
)
s5AgDaylightSavingsRecurringEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringEndHour.setStatus("current")


class _S5AgDaylightSavingsRecurringEndMinute_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_S5AgDaylightSavingsRecurringEndMinute_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringEndMinute_Object = MibScalar
s5AgDaylightSavingsRecurringEndMinute = _S5AgDaylightSavingsRecurringEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 24),
    _S5AgDaylightSavingsRecurringEndMinute_Type()
)
s5AgDaylightSavingsRecurringEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringEndMinute.setStatus("current")


class _S5AgDaylightSavingsRecurringOffset_Type(Integer32):
    """Custom type s5AgDaylightSavingsRecurringOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_S5AgDaylightSavingsRecurringOffset_Type.__name__ = "Integer32"
_S5AgDaylightSavingsRecurringOffset_Object = MibScalar
s5AgDaylightSavingsRecurringOffset = _S5AgDaylightSavingsRecurringOffset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 9, 25),
    _S5AgDaylightSavingsRecurringOffset_Type()
)
s5AgDaylightSavingsRecurringOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgDaylightSavingsRecurringOffset.setStatus("current")
_S5AgentBootConfig_ObjectIdentity = ObjectIdentity
s5AgentBootConfig = _S5AgentBootConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10)
)
_S5AgentBootConfigScalars_ObjectIdentity = ObjectIdentity
s5AgentBootConfigScalars = _S5AgentBootConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 1)
)


class _S5AgBootCfgSaveToBlock_Type(Integer32):
    """Custom type s5AgBootCfgSaveToBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgBootCfgSaveToBlock_Type.__name__ = "Integer32"
_S5AgBootCfgSaveToBlock_Object = MibScalar
s5AgBootCfgSaveToBlock = _S5AgBootCfgSaveToBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 1, 1),
    _S5AgBootCfgSaveToBlock_Type()
)
s5AgBootCfgSaveToBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgBootCfgSaveToBlock.setStatus("current")


class _S5AgBootCfgNextBootBlock_Type(Integer32):
    """Custom type s5AgBootCfgNextBootBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5AgBootCfgNextBootBlock_Type.__name__ = "Integer32"
_S5AgBootCfgNextBootBlock_Object = MibScalar
s5AgBootCfgNextBootBlock = _S5AgBootCfgNextBootBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 1, 2),
    _S5AgBootCfgNextBootBlock_Type()
)
s5AgBootCfgNextBootBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgBootCfgNextBootBlock.setStatus("current")


class _S5AgBootCfgCurrentBootBlock_Type(Integer32):
    """Custom type s5AgBootCfgCurrentBootBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5AgBootCfgCurrentBootBlock_Type.__name__ = "Integer32"
_S5AgBootCfgCurrentBootBlock_Object = MibScalar
s5AgBootCfgCurrentBootBlock = _S5AgBootCfgCurrentBootBlock_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 1, 3),
    _S5AgBootCfgCurrentBootBlock_Type()
)
s5AgBootCfgCurrentBootBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgBootCfgCurrentBootBlock.setStatus("current")
_S5AgBootCfgBlocksTable_Object = MibTable
s5AgBootCfgBlocksTable = _S5AgBootCfgBlocksTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2)
)
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksTable.setStatus("current")
_S5AgBootCfgBlocksEntry_Object = MibTableRow
s5AgBootCfgBlocksEntry = _S5AgBootCfgBlocksEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2, 1)
)
s5AgBootCfgBlocksEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgBootCfgBlocksIndex"),
)
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksEntry.setStatus("current")


class _S5AgBootCfgBlocksIndex_Type(Integer32):
    """Custom type s5AgBootCfgBlocksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5AgBootCfgBlocksIndex_Type.__name__ = "Integer32"
_S5AgBootCfgBlocksIndex_Object = MibTableColumn
s5AgBootCfgBlocksIndex = _S5AgBootCfgBlocksIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2, 1, 1),
    _S5AgBootCfgBlocksIndex_Type()
)
s5AgBootCfgBlocksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksIndex.setStatus("current")


class _S5AgBootCfgBlocksName_Type(DisplayString):
    """Custom type s5AgBootCfgBlocksName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_S5AgBootCfgBlocksName_Type.__name__ = "DisplayString"
_S5AgBootCfgBlocksName_Object = MibTableColumn
s5AgBootCfgBlocksName = _S5AgBootCfgBlocksName_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2, 1, 2),
    _S5AgBootCfgBlocksName_Type()
)
s5AgBootCfgBlocksName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksName.setStatus("current")
_S5AgBootCfgBlocksTime_Type = DateAndTime
_S5AgBootCfgBlocksTime_Object = MibTableColumn
s5AgBootCfgBlocksTime = _S5AgBootCfgBlocksTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2, 1, 3),
    _S5AgBootCfgBlocksTime_Type()
)
s5AgBootCfgBlocksTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksTime.setStatus("current")
_S5AgBootCfgBlocksValid_Type = TruthValue
_S5AgBootCfgBlocksValid_Object = MibTableColumn
s5AgBootCfgBlocksValid = _S5AgBootCfgBlocksValid_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 10, 2, 1, 4),
    _S5AgBootCfgBlocksValid_Type()
)
s5AgBootCfgBlocksValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgBootCfgBlocksValid.setStatus("current")
_S5AgentAsciiConfig_ObjectIdentity = ObjectIdentity
s5AgentAsciiConfig = _S5AgentAsciiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11)
)
_S5AgAsciiConfigScriptTable_Object = MibTable
s5AgAsciiConfigScriptTable = _S5AgAsciiConfigScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1)
)
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptTable.setStatus("current")
_S5AgAsciiConfigScriptEntry_Object = MibTableRow
s5AgAsciiConfigScriptEntry = _S5AgAsciiConfigScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1)
)
s5AgAsciiConfigScriptEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgAsciiConfigScriptIndex"),
)
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptEntry.setStatus("current")


class _S5AgAsciiConfigScriptIndex_Type(Integer32):
    """Custom type s5AgAsciiConfigScriptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_S5AgAsciiConfigScriptIndex_Type.__name__ = "Integer32"
_S5AgAsciiConfigScriptIndex_Object = MibTableColumn
s5AgAsciiConfigScriptIndex = _S5AgAsciiConfigScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 1),
    _S5AgAsciiConfigScriptIndex_Type()
)
s5AgAsciiConfigScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptIndex.setStatus("current")


class _S5AgAsciiConfigScriptBootPriority_Type(Integer32):
    """Custom type s5AgAsciiConfigScriptBootPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_S5AgAsciiConfigScriptBootPriority_Type.__name__ = "Integer32"
_S5AgAsciiConfigScriptBootPriority_Object = MibTableColumn
s5AgAsciiConfigScriptBootPriority = _S5AgAsciiConfigScriptBootPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 2),
    _S5AgAsciiConfigScriptBootPriority_Type()
)
s5AgAsciiConfigScriptBootPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptBootPriority.setStatus("current")


class _S5AgAsciiConfigScriptSource_Type(OctetString):
    """Custom type s5AgAsciiConfigScriptSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 327),
    )


_S5AgAsciiConfigScriptSource_Type.__name__ = "OctetString"
_S5AgAsciiConfigScriptSource_Object = MibTableColumn
s5AgAsciiConfigScriptSource = _S5AgAsciiConfigScriptSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 3),
    _S5AgAsciiConfigScriptSource_Type()
)
s5AgAsciiConfigScriptSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptSource.setStatus("current")


class _S5AgAsciiConfigScriptManual_Type(Integer32):
    """Custom type s5AgAsciiConfigScriptManual based on Integer32"""
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
        *(("download", 2),
          ("other", 1),
          ("upload", 3),
          ("uploadVerbose", 4))
    )


_S5AgAsciiConfigScriptManual_Type.__name__ = "Integer32"
_S5AgAsciiConfigScriptManual_Object = MibTableColumn
s5AgAsciiConfigScriptManual = _S5AgAsciiConfigScriptManual_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 4),
    _S5AgAsciiConfigScriptManual_Type()
)
s5AgAsciiConfigScriptManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptManual.setStatus("current")


class _S5AgAsciiConfigScriptOperStatus_Type(Integer32):
    """Custom type s5AgAsciiConfigScriptOperStatus based on Integer32"""
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("autoDownloadFailed", 4),
          ("autoDownloadInProgress", 3),
          ("autoDownloadPassed", 2),
          ("manualDownloadFailed", 7),
          ("manualDownloadInProgress", 6),
          ("manualDownloadPassed", 5),
          ("manualUploadFailed", 10),
          ("manualUploadInProgress", 9),
          ("manualUploadPassed", 8),
          ("manualUploadVerboseFailed", 13),
          ("manualUploadVerboseInProgress", 12),
          ("manualUploadVerbosePassed", 11),
          ("other", 1))
    )


_S5AgAsciiConfigScriptOperStatus_Type.__name__ = "Integer32"
_S5AgAsciiConfigScriptOperStatus_Object = MibTableColumn
s5AgAsciiConfigScriptOperStatus = _S5AgAsciiConfigScriptOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 5),
    _S5AgAsciiConfigScriptOperStatus_Type()
)
s5AgAsciiConfigScriptOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptOperStatus.setStatus("current")


class _S5AgAsciiConfigScriptLastStatusChange_Type(Integer32):
    """Custom type s5AgAsciiConfigScriptLastStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5AgAsciiConfigScriptLastStatusChange_Type.__name__ = "Integer32"
_S5AgAsciiConfigScriptLastStatusChange_Object = MibTableColumn
s5AgAsciiConfigScriptLastStatusChange = _S5AgAsciiConfigScriptLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 6),
    _S5AgAsciiConfigScriptLastStatusChange_Type()
)
s5AgAsciiConfigScriptLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptLastStatusChange.setStatus("current")


class _S5AgAsciiConfigScriptUploadApplications_Type(Bits):
    """Custom type s5AgAsciiConfigScriptUploadApplications based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 61),
          ("aaur", 1),
          ("adac", 2),
          ("arpInspection", 3),
          ("assetId", 4),
          ("aur", 5),
          ("banner", 6),
          ("brouter", 7),
          ("cfm", 53),
          ("cops", 8),
          ("core", 9),
          ("defaultCmdInterface", 10),
          ("dhcpRelay", 11),
          ("dhcpServer", 51),
          ("dhcpSnooping", 12),
          ("eap", 13),
          ("energySaver", 47),
          ("esu", 14),
          ("fabric-attach", 62),
          ("fcoe", 52),
          ("ieee802dot1ab", 0),
          ("interface", 15),
          ("ip", 16),
          ("ipSourceGuard", 17),
          ("ipfix", 18),
          ("ipmc", 19),
          ("ipmgr", 20),
          ("ipv6", 21),
          ("ipv6-fhs", 59),
          ("ipv6-mld", 58),
          ("ipv6-ripng", 63),
          ("l3", 22),
          ("l3Protocols", 23),
          ("lacp", 24),
          ("logging", 25),
          ("lst", 56),
          ("macSecurity", 26),
          ("mlt", 27),
          ("nsna", 39),
          ("pim", 28),
          ("poe", 29),
          ("portMirroring", 30),
          ("pvst", 31),
          ("qos", 32),
          ("radius", 64),
          ("rateLimit", 33),
          ("rmon", 34),
          ("rtc", 35),
          ("sflow", 57),
          ("slamon", 54),
          ("slpp", 36),
          ("smlt", 38),
          ("snmp", 37),
          ("spbm", 55),
          ("ssh", 40),
          ("sshc", 50),
          ("ssl", 41),
          ("stack", 42),
          ("stkmon", 43),
          ("stormControl", 60),
          ("stp", 44),
          ("unicastStormControl", 48),
          ("vlacp", 45),
          ("vlan", 46),
          ("wireless", 49))
    )

_S5AgAsciiConfigScriptUploadApplications_Type.__name__ = "Bits"
_S5AgAsciiConfigScriptUploadApplications_Object = MibTableColumn
s5AgAsciiConfigScriptUploadApplications = _S5AgAsciiConfigScriptUploadApplications_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 11, 1, 1, 7),
    _S5AgAsciiConfigScriptUploadApplications_Type()
)
s5AgAsciiConfigScriptUploadApplications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgAsciiConfigScriptUploadApplications.setStatus("current")
_S5AgentLicense_ObjectIdentity = ObjectIdentity
s5AgentLicense = _S5AgentLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12)
)
_S5AgentLicenseTable_Object = MibTable
s5AgentLicenseTable = _S5AgentLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1)
)
if mibBuilder.loadTexts:
    s5AgentLicenseTable.setStatus("current")
_S5AgentLicenseEntry_Object = MibTableRow
s5AgentLicenseEntry = _S5AgentLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1)
)
s5AgentLicenseEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgentLicenseIndex"),
)
if mibBuilder.loadTexts:
    s5AgentLicenseEntry.setStatus("current")


class _S5AgentLicenseIndex_Type(Integer32):
    """Custom type s5AgentLicenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_S5AgentLicenseIndex_Type.__name__ = "Integer32"
_S5AgentLicenseIndex_Object = MibTableColumn
s5AgentLicenseIndex = _S5AgentLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 1),
    _S5AgentLicenseIndex_Type()
)
s5AgentLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgentLicenseIndex.setStatus("current")


class _S5AgentLicenseType_Type(Integer32):
    """Custom type s5AgentLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 2),
          ("advanced-macsec", 6),
          ("demo", 1),
          ("macsec", 5),
          ("premier", 3),
          ("stacking", 4))
    )


_S5AgentLicenseType_Type.__name__ = "Integer32"
_S5AgentLicenseType_Object = MibTableColumn
s5AgentLicenseType = _S5AgentLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 2),
    _S5AgentLicenseType_Type()
)
s5AgentLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseType.setStatus("current")


class _S5AgentLicenseVersion_Type(Integer32):
    """Custom type s5AgentLicenseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5AgentLicenseVersion_Type.__name__ = "Integer32"
_S5AgentLicenseVersion_Object = MibTableColumn
s5AgentLicenseVersion = _S5AgentLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 3),
    _S5AgentLicenseVersion_Type()
)
s5AgentLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseVersion.setStatus("current")


class _S5AgentLicenseMd5Key_Type(OctetString):
    """Custom type s5AgentLicenseMd5Key based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_S5AgentLicenseMd5Key_Type.__name__ = "OctetString"
_S5AgentLicenseMd5Key_Object = MibTableColumn
s5AgentLicenseMd5Key = _S5AgentLicenseMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 4),
    _S5AgentLicenseMd5Key_Type()
)
s5AgentLicenseMd5Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseMd5Key.setStatus("current")


class _S5AgentLicenseMd5File_Type(OctetString):
    """Custom type s5AgentLicenseMd5File based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_S5AgentLicenseMd5File_Type.__name__ = "OctetString"
_S5AgentLicenseMd5File_Object = MibTableColumn
s5AgentLicenseMd5File = _S5AgentLicenseMd5File_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 5),
    _S5AgentLicenseMd5File_Type()
)
s5AgentLicenseMd5File.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseMd5File.setStatus("current")
_S5AgentLicenseTimeBase_Type = DateAndTime
_S5AgentLicenseTimeBase_Object = MibTableColumn
s5AgentLicenseTimeBase = _S5AgentLicenseTimeBase_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 6),
    _S5AgentLicenseTimeBase_Type()
)
s5AgentLicenseTimeBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseTimeBase.setStatus("current")
_S5AgentLicenseTimeModify_Type = DateAndTime
_S5AgentLicenseTimeModify_Object = MibTableColumn
s5AgentLicenseTimeModify = _S5AgentLicenseTimeModify_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 7),
    _S5AgentLicenseTimeModify_Type()
)
s5AgentLicenseTimeModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseTimeModify.setStatus("current")
_S5AgentLicenseTimeExpiration_Type = DateAndTime
_S5AgentLicenseTimeExpiration_Object = MibTableColumn
s5AgentLicenseTimeExpiration = _S5AgentLicenseTimeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 8),
    _S5AgentLicenseTimeExpiration_Type()
)
s5AgentLicenseTimeExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseTimeExpiration.setStatus("current")


class _S5AgentLicenseNumUniqueIds_Type(Integer32):
    """Custom type s5AgentLicenseNumUniqueIds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S5AgentLicenseNumUniqueIds_Type.__name__ = "Integer32"
_S5AgentLicenseNumUniqueIds_Object = MibTableColumn
s5AgentLicenseNumUniqueIds = _S5AgentLicenseNumUniqueIds_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 9),
    _S5AgentLicenseNumUniqueIds_Type()
)
s5AgentLicenseNumUniqueIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseNumUniqueIds.setStatus("current")


class _S5AgentLicenseFlags_Type(Bits):
    """Custom type s5AgentLicenseFlags based on Bits"""
    namedValues = NamedValues(
        *(("compressed", 4),
          ("emergency", 3),
          ("expirationEnabled", 2),
          ("memoAttached", 5),
          ("singleSerial", 0),
          ("site", 1))
    )

_S5AgentLicenseFlags_Type.__name__ = "Bits"
_S5AgentLicenseFlags_Object = MibTableColumn
s5AgentLicenseFlags = _S5AgentLicenseFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 10),
    _S5AgentLicenseFlags_Type()
)
s5AgentLicenseFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseFlags.setStatus("current")
_S5AgentLicenseMemo_Type = DisplayString
_S5AgentLicenseMemo_Object = MibTableColumn
s5AgentLicenseMemo = _S5AgentLicenseMemo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 11),
    _S5AgentLicenseMemo_Type()
)
s5AgentLicenseMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentLicenseMemo.setStatus("current")


class _S5AgentLicenseStatus_Type(Integer32):
    """Custom type s5AgentLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("remove", 2))
    )


_S5AgentLicenseStatus_Type.__name__ = "Integer32"
_S5AgentLicenseStatus_Object = MibTableColumn
s5AgentLicenseStatus = _S5AgentLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 12, 1, 1, 12),
    _S5AgentLicenseStatus_Type()
)
s5AgentLicenseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgentLicenseStatus.setStatus("current")
_S5AgentScript_ObjectIdentity = ObjectIdentity
s5AgentScript = _S5AgentScript_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13)
)
_S5AgentScriptTable_Object = MibTable
s5AgentScriptTable = _S5AgentScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1)
)
if mibBuilder.loadTexts:
    s5AgentScriptTable.setStatus("current")
_S5AgentScriptEntry_Object = MibTableRow
s5AgentScriptEntry = _S5AgentScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1, 1)
)
s5AgentScriptEntry.setIndexNames(
    (0, "S5-AGENT-MIB", "s5AgentScriptIndex"),
)
if mibBuilder.loadTexts:
    s5AgentScriptEntry.setStatus("current")


class _S5AgentScriptIndex_Type(Integer32):
    """Custom type s5AgentScriptIndex based on Integer32"""
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
        *(("adac", 3),
          ("ip-office", 1),
          ("lldp", 2),
          ("voice", 4))
    )


_S5AgentScriptIndex_Type.__name__ = "Integer32"
_S5AgentScriptIndex_Object = MibTableColumn
s5AgentScriptIndex = _S5AgentScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1, 1, 1),
    _S5AgentScriptIndex_Type()
)
s5AgentScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s5AgentScriptIndex.setStatus("current")


class _S5AgentScriptParameters_Type(OctetString):
    """Custom type s5AgentScriptParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_S5AgentScriptParameters_Type.__name__ = "OctetString"
_S5AgentScriptParameters_Object = MibTableColumn
s5AgentScriptParameters = _S5AgentScriptParameters_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1, 1, 2),
    _S5AgentScriptParameters_Type()
)
s5AgentScriptParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgentScriptParameters.setStatus("current")


class _S5AgentScriptStatus_Type(Integer32):
    """Custom type s5AgentScriptStatus based on Integer32"""
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
        *(("failed", 2),
          ("inProgress", 3),
          ("passed", 1))
    )


_S5AgentScriptStatus_Type.__name__ = "Integer32"
_S5AgentScriptStatus_Object = MibTableColumn
s5AgentScriptStatus = _S5AgentScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1, 1, 3),
    _S5AgentScriptStatus_Type()
)
s5AgentScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgentScriptStatus.setStatus("current")


class _S5AgentScriptRun_Type(Integer32):
    """Custom type s5AgentScriptRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("verbose", 2))
    )


_S5AgentScriptRun_Type.__name__ = "Integer32"
_S5AgentScriptRun_Object = MibTableColumn
s5AgentScriptRun = _S5AgentScriptRun_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 13, 1, 1, 4),
    _S5AgentScriptRun_Type()
)
s5AgentScriptRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgentScriptRun.setStatus("current")
_S5AgentClock_ObjectIdentity = ObjectIdentity
s5AgentClock = _S5AgentClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14)
)
_S5AgClockSystemTime_Type = DateAndTime
_S5AgClockSystemTime_Object = MibScalar
s5AgClockSystemTime = _S5AgClockSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 1),
    _S5AgClockSystemTime_Type()
)
s5AgClockSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgClockSystemTime.setStatus("current")


class _S5AgClockRtcSyncWithNtp_Type(Integer32):
    """Custom type s5AgClockRtcSyncWithNtp based on Integer32"""
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


_S5AgClockRtcSyncWithNtp_Type.__name__ = "Integer32"
_S5AgClockRtcSyncWithNtp_Object = MibScalar
s5AgClockRtcSyncWithNtp = _S5AgClockRtcSyncWithNtp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 2),
    _S5AgClockRtcSyncWithNtp_Type()
)
s5AgClockRtcSyncWithNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgClockRtcSyncWithNtp.setStatus("current")


class _S5AgClockSource_Type(Integer32):
    """Custom type s5AgClockSource based on Integer32"""
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
        *(("ntp", 3),
          ("rtc", 1),
          ("sntp", 2),
          ("sysUpTime", 4))
    )


_S5AgClockSource_Type.__name__ = "Integer32"
_S5AgClockSource_Object = MibScalar
s5AgClockSource = _S5AgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 3),
    _S5AgClockSource_Type()
)
s5AgClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgClockSource.setStatus("current")
_S5AgClockNtpTime_Type = DateAndTime
_S5AgClockNtpTime_Object = MibScalar
s5AgClockNtpTime = _S5AgClockNtpTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 4),
    _S5AgClockNtpTime_Type()
)
s5AgClockNtpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgClockNtpTime.setStatus("current")
_S5AgClockSntpTime_Type = DateAndTime
_S5AgClockSntpTime_Object = MibScalar
s5AgClockSntpTime = _S5AgClockSntpTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 5),
    _S5AgClockSntpTime_Type()
)
s5AgClockSntpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5AgClockSntpTime.setStatus("current")
_S5AgClockRtcTime_Type = DateAndTime
_S5AgClockRtcTime_Object = MibScalar
s5AgClockRtcTime = _S5AgClockRtcTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 4, 14, 6),
    _S5AgClockRtcTime_Type()
)
s5AgClockRtcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5AgClockRtcTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-AGENT-MIB",
    **{"s5AgentHw": s5AgentHw,
       "s5AgMyGrpIndx": s5AgMyGrpIndx,
       "s5AgMyComIndx": s5AgMyComIndx,
       "s5AgentInfo": s5AgentInfo,
       "s5AgentGbl": s5AgentGbl,
       "s5AgInfoReBoot": s5AgInfoReBoot,
       "s5AgInfoWriteCfg": s5AgInfoWriteCfg,
       "s5AgInfoMgmtProtocolNxtBoot": s5AgInfoMgmtProtocolNxtBoot,
       "s5AgInfoMgmtProtocolCur": s5AgInfoMgmtProtocolCur,
       "s5AgInfoBootMode": s5AgInfoBootMode,
       "s5AgInfoCfgLoadMode": s5AgInfoCfgLoadMode,
       "s5AgInfoImgLoadMode": s5AgInfoImgLoadMode,
       "s5AgInfoImgSaveMode": s5AgInfoImgSaveMode,
       "s5AgInfoImgSaveStatus": s5AgInfoImgSaveStatus,
       "s5AgInfoVer": s5AgInfoVer,
       "s5AgInfoLocStorVer": s5AgInfoLocStorVer,
       "s5AgInfoNxtBootDfltGwAddr": s5AgInfoNxtBootDfltGwAddr,
       "s5AgInfoCurDfltGwAddr": s5AgInfoCurDfltGwAddr,
       "s5AgInfoDramUsage": s5AgInfoDramUsage,
       "s5AgInfoLoadProtocolNxtBoot": s5AgInfoLoadProtocolNxtBoot,
       "s5AgInfoLoadProtocolLast": s5AgInfoLoadProtocolLast,
       "s5AgInfoSlotScope": s5AgInfoSlotScope,
       "s5AgInfoImgType": s5AgInfoImgType,
       "s5AgInfoScheduleBootTime": s5AgInfoScheduleBootTime,
       "s5AgInfoScheduleBootCancel": s5AgInfoScheduleBootCancel,
       "s5AgInfoNumBootBanks": s5AgInfoNumBootBanks,
       "s5AgInfoNextBootBank": s5AgInfoNextBootBank,
       "s5AgInfoDstLoadBank": s5AgInfoDstLoadBank,
       "s5AgInfoFileAction": s5AgInfoFileAction,
       "s5AgInfoFileStatus": s5AgInfoFileStatus,
       "s5AgInfoStackBootpMACUsage": s5AgInfoStackBootpMACUsage,
       "s5AgInfoImgDownloadStatus": s5AgInfoImgDownloadStatus,
       "s5AgInfoImgDownloadPercentComplete": s5AgInfoImgDownloadPercentComplete,
       "s5AgMyIfTable": s5AgMyIfTable,
       "s5AgMyIfEntry": s5AgMyIfEntry,
       "s5AgMyIfIndx": s5AgMyIfIndx,
       "s5AgMyIfNxtBootIpAddr": s5AgMyIfNxtBootIpAddr,
       "s5AgMyIfNxtBootNetMask": s5AgMyIfNxtBootNetMask,
       "s5AgMyIfCfgFname": s5AgMyIfCfgFname,
       "s5AgMyIfLdSvrAddr": s5AgMyIfLdSvrAddr,
       "s5AgMyIfImgFname": s5AgMyIfImgFname,
       "s5AgMyIfValidFlag": s5AgMyIfValidFlag,
       "s5AgMyIfNxtBootIpxAddr": s5AgMyIfNxtBootIpxAddr,
       "s5AgMyIfBootRouterAddr": s5AgMyIfBootRouterAddr,
       "s5AgMyIfMacAddr": s5AgMyIfMacAddr,
       "s5AgOthIfTable": s5AgOthIfTable,
       "s5AgOthIfEntry": s5AgOthIfEntry,
       "s5AgOthIfGrpIndx": s5AgOthIfGrpIndx,
       "s5AgOthIfComIndx": s5AgOthIfComIndx,
       "s5AgOthIfIndx": s5AgOthIfIndx,
       "s5AgOthIfIpAddr": s5AgOthIfIpAddr,
       "s5AgOthIfIpxAddr": s5AgOthIfIpxAddr,
       "s5AgIpRtrDefaultTimeToLive": s5AgIpRtrDefaultTimeToLive,
       "s5AgIpDefaultRtrSelectionMode": s5AgIpDefaultRtrSelectionMode,
       "s5AgIpRtrDiscoverySolicitMode": s5AgIpRtrDiscoverySolicitMode,
       "s5AgDataCollectTable": s5AgDataCollectTable,
       "s5AgDataCollectEntry": s5AgDataCollectEntry,
       "s5AgDataCollectIfIndex": s5AgDataCollectIfIndex,
       "s5AgDataCollectSnTimeStamp": s5AgDataCollectSnTimeStamp,
       "s5AgDataCollectNetworkAddrStatus": s5AgDataCollectNetworkAddrStatus,
       "s5AgUnAuthIpAddr": s5AgUnAuthIpAddr,
       "s5AgUnAuthIpxAddr": s5AgUnAuthIpxAddr,
       "s5AgUnAuthComm": s5AgUnAuthComm,
       "s5AgTrapFilterTable": s5AgTrapFilterTable,
       "s5AgTrapFilterEntry": s5AgTrapFilterEntry,
       "s5AgTrapFilterIndex": s5AgTrapFilterIndex,
       "s5AgTrapFilterTrapOID": s5AgTrapFilterTrapOID,
       "s5AgTrapFilterTrapInitiator1": s5AgTrapFilterTrapInitiator1,
       "s5AgTrapFilterTrapInitiator2": s5AgTrapFilterTrapInitiator2,
       "s5AgTrapFilterTrapInitiator3": s5AgTrapFilterTrapInitiator3,
       "s5AgTrapFilterStatus": s5AgTrapFilterStatus,
       "s5AgTrapFilterDelayTime": s5AgTrapFilterDelayTime,
       "s5AgTrapEntryStatus": s5AgTrapEntryStatus,
       "s5AgTrapFilterGlobalStatus": s5AgTrapFilterGlobalStatus,
       "s5AgUnAuthInetAddressType": s5AgUnAuthInetAddressType,
       "s5AgUnAuthInetAddress": s5AgUnAuthInetAddress,
       "s5AgentMgmt": s5AgentMgmt,
       "s5AgTrpRcvrMaxEnt": s5AgTrpRcvrMaxEnt,
       "s5AgTrpRcvrCurEnt": s5AgTrpRcvrCurEnt,
       "s5AgTrpRcvrNext": s5AgTrpRcvrNext,
       "s5AgTrpRcvrTable": s5AgTrpRcvrTable,
       "s5AgTrpRcvrEntry": s5AgTrpRcvrEntry,
       "s5AgTrpRcvrIndx": s5AgTrpRcvrIndx,
       "s5AgTrpRcvrStatus": s5AgTrpRcvrStatus,
       "s5AgTrpRcvrAddrType": s5AgTrpRcvrAddrType,
       "s5AgTrpRcvrNetAddr": s5AgTrpRcvrNetAddr,
       "s5AgTrpRcvrComm": s5AgTrpRcvrComm,
       "s5AgTrpRcvrAgeTime": s5AgTrpRcvrAgeTime,
       "s5AgRemoteLoginMgmt": s5AgRemoteLoginMgmt,
       "s5AgRemoteLoginIp": s5AgRemoteLoginIp,
       "s5AgRemoteLoginStatus": s5AgRemoteLoginStatus,
       "s5AgRemoteLoginInetAddressType": s5AgRemoteLoginInetAddressType,
       "s5AgRemoteLoginInetAddress": s5AgRemoteLoginInetAddress,
       "s5AgentSystem": s5AgentSystem,
       "s5AgSysAutoPvid": s5AgSysAutoPvid,
       "s5AgSysCurrentOperationalMode": s5AgSysCurrentOperationalMode,
       "s5AgSysNextBootOperationalMode": s5AgSysNextBootOperationalMode,
       "s5AgSysBinaryConfigFilename": s5AgSysBinaryConfigFilename,
       "s5AgSysTftpServerAddress": s5AgSysTftpServerAddress,
       "s5AgSysAsciiConfigFilename": s5AgSysAsciiConfigFilename,
       "s5AgSysAsciiConfigAutoDownload": s5AgSysAsciiConfigAutoDownload,
       "s5AgSysAsciiConfigAutoDldStatus": s5AgSysAsciiConfigAutoDldStatus,
       "s5AgSysAsciiConfigManualDownload": s5AgSysAsciiConfigManualDownload,
       "s5AgSysCpuIpAddress": s5AgSysCpuIpAddress,
       "s5AgSysStackIpAddress": s5AgSysStackIpAddress,
       "s5AgSysCpuNetMask": s5AgSysCpuNetMask,
       "s5AgSysManagementVlanId": s5AgSysManagementVlanId,
       "s5AgSysBinaryConfigUnitNumber": s5AgSysBinaryConfigUnitNumber,
       "s5AgSysStackInsertionUnitNumber": s5AgSysStackInsertionUnitNumber,
       "s5AgSysSpanningTreeOperMode": s5AgSysSpanningTreeOperMode,
       "s5AgSysSpanningTreeAdminMode": s5AgSysSpanningTreeAdminMode,
       "s5AgSysAutoUnitReplacementEnabled": s5AgSysAutoUnitReplacementEnabled,
       "s5AgSysAsciiConfigManualUpload": s5AgSysAsciiConfigManualUpload,
       "s5AgSysSpanningTreePathCostCalculationMode": s5AgSysSpanningTreePathCostCalculationMode,
       "s5AgSysUsbTargetUnit": s5AgSysUsbTargetUnit,
       "s5AgSysSpanningTreePortMode": s5AgSysSpanningTreePortMode,
       "s5AgSysLicenseFilename": s5AgSysLicenseFilename,
       "s5AgSysSpanningTreeAdminCompatibility": s5AgSysSpanningTreeAdminCompatibility,
       "s5AgSysSpanningTreeOperCompatibility": s5AgSysSpanningTreeOperCompatibility,
       "s5AgSysGlobalFlowControlEnabled": s5AgSysGlobalFlowControlEnabled,
       "s5AgSysAutosaveToNvramEnabled": s5AgSysAutosaveToNvramEnabled,
       "s5AgSysFlushMacAddrTableAll": s5AgSysFlushMacAddrTableAll,
       "s5AgSysFlushMacAddrTableByPortList": s5AgSysFlushMacAddrTableByPortList,
       "s5AgSysFlushMacAddrTableByVlan": s5AgSysFlushMacAddrTableByVlan,
       "s5AgSysFlushMacAddrTableByTrunk": s5AgSysFlushMacAddrTableByTrunk,
       "s5AgSysFlushMacAddrTableByAddress": s5AgSysFlushMacAddrTableByAddress,
       "s5AgSysVlanConfigControl": s5AgSysVlanConfigControl,
       "s5AgSysJumboFramesEnabled": s5AgSysJumboFramesEnabled,
       "s5AgSysAutoUnitReplacementSaveEnabled": s5AgSysAutoUnitReplacementSaveEnabled,
       "s5AgSysAutoUnitReplacementRestore": s5AgSysAutoUnitReplacementRestore,
       "s5AgSysAutoUnitReplacementForceSave": s5AgSysAutoUnitReplacementForceSave,
       "s5AgSysTftpServerInetAddressType": s5AgSysTftpServerInetAddressType,
       "s5AgSysTftpServerInetAddress": s5AgSysTftpServerInetAddress,
       "s5AgSysTelnetSessionLoginAuthenType": s5AgSysTelnetSessionLoginAuthenType,
       "s5AgSysSerialConsoleLoginAuthenType": s5AgSysSerialConsoleLoginAuthenType,
       "s5AgSysSshAuthKeyFilename": s5AgSysSshAuthKeyFilename,
       "s5AgSysAsciiConfigManualUploadApplications": s5AgSysAsciiConfigManualUploadApplications,
       "s5AgSysOperationalLicense": s5AgSysOperationalLicense,
       "s5AgSysInstalledLicense": s5AgSysInstalledLicense,
       "s5AgSysCpuIpv6Address": s5AgSysCpuIpv6Address,
       "s5AgSysStackIpv6Address": s5AgSysStackIpv6Address,
       "s5AgSysCpuIpv6NetMask": s5AgSysCpuIpv6NetMask,
       "s5AgSysStackIpv6NetMask": s5AgSysStackIpv6NetMask,
       "s5AgSysIpv6DefaultGateway": s5AgSysIpv6DefaultGateway,
       "s5AgSysSpanningTreeBpduFilterIgnoreSelf": s5AgSysSpanningTreeBpduFilterIgnoreSelf,
       "s5AgSysIdentifyUnits": s5AgSysIdentifyUnits,
       "s5AgSysMacAddrTableLearningPorts": s5AgSysMacAddrTableLearningPorts,
       "s5AgSysSerialSecurityEnable": s5AgSysSerialSecurityEnable,
       "s5AgSysMgmtStackIpAddress": s5AgSysMgmtStackIpAddress,
       "s5AgSysAuditEnable": s5AgSysAuditEnable,
       "s5AgSysQuickConfigEnable": s5AgSysQuickConfigEnable,
       "s5AgSysStackIpv6MgmtAddress": s5AgSysStackIpv6MgmtAddress,
       "s5AgSysStackIpv6MgmtNetMask": s5AgSysStackIpv6MgmtNetMask,
       "s5AgSysIpv6MgmtGateway": s5AgSysIpv6MgmtGateway,
       "s5AgSysBlinkLeds": s5AgSysBlinkLeds,
       "s5AgSysBlinkLedsUnit": s5AgSysBlinkLedsUnit,
       "s5AgSysBlinkLedsTimeThreshold": s5AgSysBlinkLedsTimeThreshold,
       "s5AgSysJumboFramesSize": s5AgSysJumboFramesSize,
       "s5AgSysDiagnosticsQuickModeEnabled": s5AgSysDiagnosticsQuickModeEnabled,
       "s5AgSysTimeStampEnabled": s5AgSysTimeStampEnabled,
       "s5AgSysForcedStackModeEnabled": s5AgSysForcedStackModeEnabled,
       "s5AgSysSflowGlobalEnable": s5AgSysSflowGlobalEnable,
       "s5AgentBanner": s5AgentBanner,
       "s5AgBannerControl": s5AgBannerControl,
       "s5AgCustomBannerTable": s5AgCustomBannerTable,
       "s5AgCustomBannerEntry": s5AgCustomBannerEntry,
       "s5AgCustomBannerType": s5AgCustomBannerType,
       "s5AgCustomBannerId": s5AgCustomBannerId,
       "s5AgCustomBannerLine": s5AgCustomBannerLine,
       "s5AgentSntp": s5AgentSntp,
       "s5AgSntpState": s5AgSntpState,
       "s5AgSntpPrimaryServerAddress": s5AgSntpPrimaryServerAddress,
       "s5AgSntpSecondaryServerAddress": s5AgSntpSecondaryServerAddress,
       "s5AgSntpSyncInterval": s5AgSntpSyncInterval,
       "s5AgSntpManualSyncRequest": s5AgSntpManualSyncRequest,
       "s5AgSntpLastSyncTime": s5AgSntpLastSyncTime,
       "s5AgSntpLastSyncSource": s5AgSntpLastSyncSource,
       "s5AgSntpNextSyncTime": s5AgSntpNextSyncTime,
       "s5AgSntpPrimaryServerSyncFailures": s5AgSntpPrimaryServerSyncFailures,
       "s5AgSntpSecondaryServerSyncFailures": s5AgSntpSecondaryServerSyncFailures,
       "s5AgSntpCurrentTime": s5AgSntpCurrentTime,
       "s5AgSntpTimeZone": s5AgSntpTimeZone,
       "s5AgSntpSyncRetryInterval": s5AgSntpSyncRetryInterval,
       "s5AgSntpTimeZoneAcronym": s5AgSntpTimeZoneAcronym,
       "s5AgSntpPrimaryServerInetAddressType": s5AgSntpPrimaryServerInetAddressType,
       "s5AgSntpPrimaryServerInetAddress": s5AgSntpPrimaryServerInetAddress,
       "s5AgSntpSecondaryServerInetAddressType": s5AgSntpSecondaryServerInetAddressType,
       "s5AgSntpSecondaryServerInetAddress": s5AgSntpSecondaryServerInetAddress,
       "s5AgSntpLastSyncSourceInetAddressType": s5AgSntpLastSyncSourceInetAddressType,
       "s5AgSntpLastSyncSourceInetAddress": s5AgSntpLastSyncSourceInetAddress,
       "s5AgentSsl": s5AgentSsl,
       "s5AgentSslScalars": s5AgentSslScalars,
       "s5AgSslEnabled": s5AgSslEnabled,
       "s5AgSslCertificateControl": s5AgSslCertificateControl,
       "s5AgSslCertificateExists": s5AgSslCertificateExists,
       "s5AgSslCertificateData": s5AgSslCertificateData,
       "s5AgSslCertificateControlStatus": s5AgSslCertificateControlStatus,
       "s5AgSslServerControl": s5AgSslServerControl,
       "s5AgentMib": s5AgentMib,
       "s5AgentDaylightSavings": s5AgentDaylightSavings,
       "s5AgDaylightSavingsEnabled": s5AgDaylightSavingsEnabled,
       "s5AgDaylightSavingsStartMonth": s5AgDaylightSavingsStartMonth,
       "s5AgDaylightSavingsStartDay": s5AgDaylightSavingsStartDay,
       "s5AgDaylightSavingsStartHour": s5AgDaylightSavingsStartHour,
       "s5AgDaylightSavingsEndMonth": s5AgDaylightSavingsEndMonth,
       "s5AgDaylightSavingsEndDay": s5AgDaylightSavingsEndDay,
       "s5AgDaylightSavingsEndHour": s5AgDaylightSavingsEndHour,
       "s5AgDaylightSavingsOffset": s5AgDaylightSavingsOffset,
       "s5AgDaylightSavingsStartMinutes": s5AgDaylightSavingsStartMinutes,
       "s5AgDaylightSavingsEndMinutes": s5AgDaylightSavingsEndMinutes,
       "s5AgDaylightSavingsStartYear": s5AgDaylightSavingsStartYear,
       "s5AgDaylightSavingsEndYear": s5AgDaylightSavingsEndYear,
       "s5AgDaylightSavingsRecurring": s5AgDaylightSavingsRecurring,
       "s5AgDaylightSavingsTimeZoneAcronym": s5AgDaylightSavingsTimeZoneAcronym,
       "s5AgDaylightSavingsRecurringStartWeek": s5AgDaylightSavingsRecurringStartWeek,
       "s5AgDaylightSavingsRecurringStartDay": s5AgDaylightSavingsRecurringStartDay,
       "s5AgDaylightSavingsRecurringStartMonth": s5AgDaylightSavingsRecurringStartMonth,
       "s5AgDaylightSavingsRecurringStartHour": s5AgDaylightSavingsRecurringStartHour,
       "s5AgDaylightSavingsRecurringStartMinute": s5AgDaylightSavingsRecurringStartMinute,
       "s5AgDaylightSavingsRecurringEndWeek": s5AgDaylightSavingsRecurringEndWeek,
       "s5AgDaylightSavingsRecurringEndDay": s5AgDaylightSavingsRecurringEndDay,
       "s5AgDaylightSavingsRecurringEndMonth": s5AgDaylightSavingsRecurringEndMonth,
       "s5AgDaylightSavingsRecurringEndHour": s5AgDaylightSavingsRecurringEndHour,
       "s5AgDaylightSavingsRecurringEndMinute": s5AgDaylightSavingsRecurringEndMinute,
       "s5AgDaylightSavingsRecurringOffset": s5AgDaylightSavingsRecurringOffset,
       "s5AgentBootConfig": s5AgentBootConfig,
       "s5AgentBootConfigScalars": s5AgentBootConfigScalars,
       "s5AgBootCfgSaveToBlock": s5AgBootCfgSaveToBlock,
       "s5AgBootCfgNextBootBlock": s5AgBootCfgNextBootBlock,
       "s5AgBootCfgCurrentBootBlock": s5AgBootCfgCurrentBootBlock,
       "s5AgBootCfgBlocksTable": s5AgBootCfgBlocksTable,
       "s5AgBootCfgBlocksEntry": s5AgBootCfgBlocksEntry,
       "s5AgBootCfgBlocksIndex": s5AgBootCfgBlocksIndex,
       "s5AgBootCfgBlocksName": s5AgBootCfgBlocksName,
       "s5AgBootCfgBlocksTime": s5AgBootCfgBlocksTime,
       "s5AgBootCfgBlocksValid": s5AgBootCfgBlocksValid,
       "s5AgentAsciiConfig": s5AgentAsciiConfig,
       "s5AgAsciiConfigScriptTable": s5AgAsciiConfigScriptTable,
       "s5AgAsciiConfigScriptEntry": s5AgAsciiConfigScriptEntry,
       "s5AgAsciiConfigScriptIndex": s5AgAsciiConfigScriptIndex,
       "s5AgAsciiConfigScriptBootPriority": s5AgAsciiConfigScriptBootPriority,
       "s5AgAsciiConfigScriptSource": s5AgAsciiConfigScriptSource,
       "s5AgAsciiConfigScriptManual": s5AgAsciiConfigScriptManual,
       "s5AgAsciiConfigScriptOperStatus": s5AgAsciiConfigScriptOperStatus,
       "s5AgAsciiConfigScriptLastStatusChange": s5AgAsciiConfigScriptLastStatusChange,
       "s5AgAsciiConfigScriptUploadApplications": s5AgAsciiConfigScriptUploadApplications,
       "s5AgentLicense": s5AgentLicense,
       "s5AgentLicenseTable": s5AgentLicenseTable,
       "s5AgentLicenseEntry": s5AgentLicenseEntry,
       "s5AgentLicenseIndex": s5AgentLicenseIndex,
       "s5AgentLicenseType": s5AgentLicenseType,
       "s5AgentLicenseVersion": s5AgentLicenseVersion,
       "s5AgentLicenseMd5Key": s5AgentLicenseMd5Key,
       "s5AgentLicenseMd5File": s5AgentLicenseMd5File,
       "s5AgentLicenseTimeBase": s5AgentLicenseTimeBase,
       "s5AgentLicenseTimeModify": s5AgentLicenseTimeModify,
       "s5AgentLicenseTimeExpiration": s5AgentLicenseTimeExpiration,
       "s5AgentLicenseNumUniqueIds": s5AgentLicenseNumUniqueIds,
       "s5AgentLicenseFlags": s5AgentLicenseFlags,
       "s5AgentLicenseMemo": s5AgentLicenseMemo,
       "s5AgentLicenseStatus": s5AgentLicenseStatus,
       "s5AgentScript": s5AgentScript,
       "s5AgentScriptTable": s5AgentScriptTable,
       "s5AgentScriptEntry": s5AgentScriptEntry,
       "s5AgentScriptIndex": s5AgentScriptIndex,
       "s5AgentScriptParameters": s5AgentScriptParameters,
       "s5AgentScriptStatus": s5AgentScriptStatus,
       "s5AgentScriptRun": s5AgentScriptRun,
       "s5AgentClock": s5AgentClock,
       "s5AgClockSystemTime": s5AgClockSystemTime,
       "s5AgClockRtcSyncWithNtp": s5AgClockRtcSyncWithNtp,
       "s5AgClockSource": s5AgClockSource,
       "s5AgClockNtpTime": s5AgClockNtpTime,
       "s5AgClockSntpTime": s5AgClockSntpTime,
       "s5AgClockRtcTime": s5AgClockRtcTime}
)
