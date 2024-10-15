# SNMP MIB module (ZXROS-AMAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXROS-AMAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:15 2024
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxros_ObjectIdentity = ObjectIdentity
zxros = _Zxros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 100)
)
_ZxrosAMAT_ObjectIdentity = ObjectIdentity
zxrosAMAT = _ZxrosAMAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000)
)
_ZxrosAMATconfig_ObjectIdentity = ObjectIdentity
zxrosAMATconfig = _ZxrosAMATconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1)
)
_ZxrosAMATAttackAgingTime_Type = Integer32
_ZxrosAMATAttackAgingTime_Object = MibScalar
zxrosAMATAttackAgingTime = _ZxrosAMATAttackAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 1),
    _ZxrosAMATAttackAgingTime_Type()
)
zxrosAMATAttackAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATAttackAgingTime.setStatus("current")


class _ZxrosAMATState_Type(Integer32):
    """Custom type zxrosAMATState based on Integer32"""
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


_ZxrosAMATState_Type.__name__ = "Integer32"
_ZxrosAMATState_Object = MibScalar
zxrosAMATState = _ZxrosAMATState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 2),
    _ZxrosAMATState_Type()
)
zxrosAMATState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATState.setStatus("current")
_ZxrosAMATHashOverNum_Type = Integer32
_ZxrosAMATHashOverNum_Object = MibScalar
zxrosAMATHashOverNum = _ZxrosAMATHashOverNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 3),
    _ZxrosAMATHashOverNum_Type()
)
zxrosAMATHashOverNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATHashOverNum.setStatus("current")
_ZxrosAMATHashUpdateTime_Type = Integer32
_ZxrosAMATHashUpdateTime_Object = MibScalar
zxrosAMATHashUpdateTime = _ZxrosAMATHashUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 4),
    _ZxrosAMATHashUpdateTime_Type()
)
zxrosAMATHashUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATHashUpdateTime.setStatus("current")
_ZxrosAMATIcmpConn_Type = Integer32
_ZxrosAMATIcmpConn_Object = MibScalar
zxrosAMATIcmpConn = _ZxrosAMATIcmpConn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 5),
    _ZxrosAMATIcmpConn_Type()
)
zxrosAMATIcmpConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATIcmpConn.setStatus("current")
_ZxrosAMATIcmpRate_Type = Integer32
_ZxrosAMATIcmpRate_Object = MibScalar
zxrosAMATIcmpRate = _ZxrosAMATIcmpRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 6),
    _ZxrosAMATIcmpRate_Type()
)
zxrosAMATIcmpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATIcmpRate.setStatus("current")
_ZxrosAMATIntervalSampleRate_Type = Integer32
_ZxrosAMATIntervalSampleRate_Object = MibScalar
zxrosAMATIntervalSampleRate = _ZxrosAMATIntervalSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 7),
    _ZxrosAMATIntervalSampleRate_Type()
)
zxrosAMATIntervalSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATIntervalSampleRate.setStatus("current")


class _ZxrosAMATLogging_Type(Integer32):
    """Custom type zxrosAMATLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ZxrosAMATLogging_Type.__name__ = "Integer32"
_ZxrosAMATLogging_Object = MibScalar
zxrosAMATLogging = _ZxrosAMATLogging_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 8),
    _ZxrosAMATLogging_Type()
)
zxrosAMATLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATLogging.setStatus("current")
_ZxrosAMATRateLimit_Type = Integer32
_ZxrosAMATRateLimit_Object = MibScalar
zxrosAMATRateLimit = _ZxrosAMATRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 9),
    _ZxrosAMATRateLimit_Type()
)
zxrosAMATRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATRateLimit.setStatus("current")
_ZxrosAMATRuleUpdateTime_Type = Integer32
_ZxrosAMATRuleUpdateTime_Object = MibScalar
zxrosAMATRuleUpdateTime = _ZxrosAMATRuleUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 10),
    _ZxrosAMATRuleUpdateTime_Type()
)
zxrosAMATRuleUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATRuleUpdateTime.setStatus("current")
_ZxrosAMATSampleCode_Type = Integer32
_ZxrosAMATSampleCode_Object = MibScalar
zxrosAMATSampleCode = _ZxrosAMATSampleCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 11),
    _ZxrosAMATSampleCode_Type()
)
zxrosAMATSampleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATSampleCode.setStatus("current")
_ZxrosAMATSampleMatchCode_Type = Integer32
_ZxrosAMATSampleMatchCode_Object = MibScalar
zxrosAMATSampleMatchCode = _ZxrosAMATSampleMatchCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 12),
    _ZxrosAMATSampleMatchCode_Type()
)
zxrosAMATSampleMatchCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATSampleMatchCode.setStatus("current")
_ZxrosAMATTcpConn_Type = Integer32
_ZxrosAMATTcpConn_Object = MibScalar
zxrosAMATTcpConn = _ZxrosAMATTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 13),
    _ZxrosAMATTcpConn_Type()
)
zxrosAMATTcpConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATTcpConn.setStatus("current")
_ZxrosAMATTcpProportion_Type = Integer32
_ZxrosAMATTcpProportion_Object = MibScalar
zxrosAMATTcpProportion = _ZxrosAMATTcpProportion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 14),
    _ZxrosAMATTcpProportion_Type()
)
zxrosAMATTcpProportion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATTcpProportion.setStatus("current")
_ZxrosAMATTcpRate_Type = Integer32
_ZxrosAMATTcpRate_Object = MibScalar
zxrosAMATTcpRate = _ZxrosAMATTcpRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 15),
    _ZxrosAMATTcpRate_Type()
)
zxrosAMATTcpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATTcpRate.setStatus("current")
_ZxrosAMATUdpConn_Type = Integer32
_ZxrosAMATUdpConn_Object = MibScalar
zxrosAMATUdpConn = _ZxrosAMATUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 16),
    _ZxrosAMATUdpConn_Type()
)
zxrosAMATUdpConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATUdpConn.setStatus("current")
_ZxrosAMATUdpRate_Type = Integer32
_ZxrosAMATUdpRate_Object = MibScalar
zxrosAMATUdpRate = _ZxrosAMATUdpRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 1, 17),
    _ZxrosAMATUdpRate_Type()
)
zxrosAMATUdpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATUdpRate.setStatus("current")
_ZxrosAMATIgnoreIpAddressTable_Object = MibTable
zxrosAMATIgnoreIpAddressTable = _ZxrosAMATIgnoreIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 2)
)
if mibBuilder.loadTexts:
    zxrosAMATIgnoreIpAddressTable.setStatus("current")
_ZxrosAMATIgnoreIpAddressEntry_Object = MibTableRow
zxrosAMATIgnoreIpAddressEntry = _ZxrosAMATIgnoreIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 2, 1)
)
zxrosAMATIgnoreIpAddressEntry.setIndexNames(
    (0, "ZXROS-AMAT-MIB", "zxrosAMATIgnoreIpAddressIpAddress"),
    (0, "ZXROS-AMAT-MIB", "zxrosAMATIgnoreIpAddressVpnName"),
)
if mibBuilder.loadTexts:
    zxrosAMATIgnoreIpAddressEntry.setStatus("current")
_ZxrosAMATIgnoreIpAddressIpAddress_Type = IpAddress
_ZxrosAMATIgnoreIpAddressIpAddress_Object = MibTableColumn
zxrosAMATIgnoreIpAddressIpAddress = _ZxrosAMATIgnoreIpAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 2, 1, 1),
    _ZxrosAMATIgnoreIpAddressIpAddress_Type()
)
zxrosAMATIgnoreIpAddressIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIgnoreIpAddressIpAddress.setStatus("current")
_ZxrosAMATIgnoreIpAddressVpnName_Type = DisplayString
_ZxrosAMATIgnoreIpAddressVpnName_Object = MibTableColumn
zxrosAMATIgnoreIpAddressVpnName = _ZxrosAMATIgnoreIpAddressVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 2, 1, 2),
    _ZxrosAMATIgnoreIpAddressVpnName_Type()
)
zxrosAMATIgnoreIpAddressVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIgnoreIpAddressVpnName.setStatus("current")
_ZxrosAMATIgnoreIpAddressRowStatus_Type = RowStatus
_ZxrosAMATIgnoreIpAddressRowStatus_Object = MibTableColumn
zxrosAMATIgnoreIpAddressRowStatus = _ZxrosAMATIgnoreIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 2, 1, 3),
    _ZxrosAMATIgnoreIpAddressRowStatus_Type()
)
zxrosAMATIgnoreIpAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATIgnoreIpAddressRowStatus.setStatus("current")
_ZxrosAMATAttackLoggingTable_Object = MibTable
zxrosAMATAttackLoggingTable = _ZxrosAMATAttackLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3)
)
if mibBuilder.loadTexts:
    zxrosAMATAttackLoggingTable.setStatus("current")
_ZxrosAMATAttackLoggingEntry_Object = MibTableRow
zxrosAMATAttackLoggingEntry = _ZxrosAMATAttackLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1)
)
zxrosAMATAttackLoggingEntry.setIndexNames(
    (0, "ZXROS-AMAT-MIB", "zxrosAMATAttackLoggingNo"),
)
if mibBuilder.loadTexts:
    zxrosAMATAttackLoggingEntry.setStatus("current")
_ZxrosAMATAttackLoggingNo_Type = Integer32
_ZxrosAMATAttackLoggingNo_Object = MibTableColumn
zxrosAMATAttackLoggingNo = _ZxrosAMATAttackLoggingNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 1),
    _ZxrosAMATAttackLoggingNo_Type()
)
zxrosAMATAttackLoggingNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATAttackLoggingNo.setStatus("current")
_ZxrosAMATAttackDetectedTime_Type = TimeTicks
_ZxrosAMATAttackDetectedTime_Object = MibTableColumn
zxrosAMATAttackDetectedTime = _ZxrosAMATAttackDetectedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 2),
    _ZxrosAMATAttackDetectedTime_Type()
)
zxrosAMATAttackDetectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATAttackDetectedTime.setStatus("current")
_ZxrosAMATAttackOverTime_Type = TimeTicks
_ZxrosAMATAttackOverTime_Object = MibTableColumn
zxrosAMATAttackOverTime = _ZxrosAMATAttackOverTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 3),
    _ZxrosAMATAttackOverTime_Type()
)
zxrosAMATAttackOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATAttackOverTime.setStatus("current")
_ZxrosAMATVpnName_Type = DisplayString
_ZxrosAMATVpnName_Object = MibTableColumn
zxrosAMATVpnName = _ZxrosAMATVpnName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 4),
    _ZxrosAMATVpnName_Type()
)
zxrosAMATVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATVpnName.setStatus("current")
_ZxrosAMATIpAddress_Type = IpAddress
_ZxrosAMATIpAddress_Object = MibTableColumn
zxrosAMATIpAddress = _ZxrosAMATIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 5),
    _ZxrosAMATIpAddress_Type()
)
zxrosAMATIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIpAddress.setStatus("current")
_ZxrosAMATAttackMode_Type = DisplayString
_ZxrosAMATAttackMode_Object = MibTableColumn
zxrosAMATAttackMode = _ZxrosAMATAttackMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 6),
    _ZxrosAMATAttackMode_Type()
)
zxrosAMATAttackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATAttackMode.setStatus("current")
_ZxrosAMATTcpPassPacket_Type = Integer32
_ZxrosAMATTcpPassPacket_Object = MibTableColumn
zxrosAMATTcpPassPacket = _ZxrosAMATTcpPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 7),
    _ZxrosAMATTcpPassPacket_Type()
)
zxrosAMATTcpPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTcpPassPacket.setStatus("current")
_ZxrosAMATTcpFilterPacket_Type = Integer32
_ZxrosAMATTcpFilterPacket_Object = MibTableColumn
zxrosAMATTcpFilterPacket = _ZxrosAMATTcpFilterPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 8),
    _ZxrosAMATTcpFilterPacket_Type()
)
zxrosAMATTcpFilterPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTcpFilterPacket.setStatus("current")
_ZxrosAMATUdpPassPacket_Type = Integer32
_ZxrosAMATUdpPassPacket_Object = MibTableColumn
zxrosAMATUdpPassPacket = _ZxrosAMATUdpPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 9),
    _ZxrosAMATUdpPassPacket_Type()
)
zxrosAMATUdpPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATUdpPassPacket.setStatus("current")
_ZxrosAMATUdpFilterPacket_Type = Integer32
_ZxrosAMATUdpFilterPacket_Object = MibTableColumn
zxrosAMATUdpFilterPacket = _ZxrosAMATUdpFilterPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 10),
    _ZxrosAMATUdpFilterPacket_Type()
)
zxrosAMATUdpFilterPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATUdpFilterPacket.setStatus("current")
_ZxrosAMATIcmpPassPacket_Type = Integer32
_ZxrosAMATIcmpPassPacket_Object = MibTableColumn
zxrosAMATIcmpPassPacket = _ZxrosAMATIcmpPassPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 11),
    _ZxrosAMATIcmpPassPacket_Type()
)
zxrosAMATIcmpPassPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIcmpPassPacket.setStatus("current")
_ZxrosAMATIcmpFilterPacket_Type = Integer32
_ZxrosAMATIcmpFilterPacket_Object = MibTableColumn
zxrosAMATIcmpFilterPacket = _ZxrosAMATIcmpFilterPacket_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 12),
    _ZxrosAMATIcmpFilterPacket_Type()
)
zxrosAMATIcmpFilterPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIcmpFilterPacket.setStatus("current")
_ZxrosAMATTcpAttackOverValue_Type = Integer32
_ZxrosAMATTcpAttackOverValue_Object = MibTableColumn
zxrosAMATTcpAttackOverValue = _ZxrosAMATTcpAttackOverValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 13),
    _ZxrosAMATTcpAttackOverValue_Type()
)
zxrosAMATTcpAttackOverValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTcpAttackOverValue.setStatus("current")
_ZxrosAMATUdpAttackOverValue_Type = Integer32
_ZxrosAMATUdpAttackOverValue_Object = MibTableColumn
zxrosAMATUdpAttackOverValue = _ZxrosAMATUdpAttackOverValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 14),
    _ZxrosAMATUdpAttackOverValue_Type()
)
zxrosAMATUdpAttackOverValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATUdpAttackOverValue.setStatus("current")
_ZxrosAMATIcmpAttackOverValue_Type = Integer32
_ZxrosAMATIcmpAttackOverValue_Object = MibTableColumn
zxrosAMATIcmpAttackOverValue = _ZxrosAMATIcmpAttackOverValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 15),
    _ZxrosAMATIcmpAttackOverValue_Type()
)
zxrosAMATIcmpAttackOverValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIcmpAttackOverValue.setStatus("current")
_ZxrosAMATPassPacketsBeforeRuleCreated_Type = Integer32
_ZxrosAMATPassPacketsBeforeRuleCreated_Object = MibTableColumn
zxrosAMATPassPacketsBeforeRuleCreated = _ZxrosAMATPassPacketsBeforeRuleCreated_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 3, 1, 16),
    _ZxrosAMATPassPacketsBeforeRuleCreated_Type()
)
zxrosAMATPassPacketsBeforeRuleCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATPassPacketsBeforeRuleCreated.setStatus("current")
_ZxrosAMATShutDownLoggingTable_Object = MibTable
zxrosAMATShutDownLoggingTable = _ZxrosAMATShutDownLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4)
)
if mibBuilder.loadTexts:
    zxrosAMATShutDownLoggingTable.setStatus("current")
_ZxrosAMATShutDownLoggingEntry_Object = MibTableRow
zxrosAMATShutDownLoggingEntry = _ZxrosAMATShutDownLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1)
)
zxrosAMATShutDownLoggingEntry.setIndexNames(
    (0, "ZXROS-AMAT-MIB", "zxrosAMATShutDownLoggingNo"),
)
if mibBuilder.loadTexts:
    zxrosAMATShutDownLoggingEntry.setStatus("current")
_ZxrosAMATShutDownLoggingNo_Type = Integer32
_ZxrosAMATShutDownLoggingNo_Object = MibTableColumn
zxrosAMATShutDownLoggingNo = _ZxrosAMATShutDownLoggingNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 1),
    _ZxrosAMATShutDownLoggingNo_Type()
)
zxrosAMATShutDownLoggingNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATShutDownLoggingNo.setStatus("current")
_ZxrosAMATStartUpTime_Type = TimeTicks
_ZxrosAMATStartUpTime_Object = MibTableColumn
zxrosAMATStartUpTime = _ZxrosAMATStartUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 2),
    _ZxrosAMATStartUpTime_Type()
)
zxrosAMATStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATStartUpTime.setStatus("current")
_ZxrosAMATShutDownTime_Type = TimeTicks
_ZxrosAMATShutDownTime_Object = MibTableColumn
zxrosAMATShutDownTime = _ZxrosAMATShutDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 3),
    _ZxrosAMATShutDownTime_Type()
)
zxrosAMATShutDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATShutDownTime.setStatus("current")
_ZxrosAMATNoAmatPackets_Type = Integer32
_ZxrosAMATNoAmatPackets_Object = MibTableColumn
zxrosAMATNoAmatPackets = _ZxrosAMATNoAmatPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 4),
    _ZxrosAMATNoAmatPackets_Type()
)
zxrosAMATNoAmatPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATNoAmatPackets.setStatus("current")
_ZxrosAMATTotalPassPackets_Type = Integer32
_ZxrosAMATTotalPassPackets_Object = MibTableColumn
zxrosAMATTotalPassPackets = _ZxrosAMATTotalPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 5),
    _ZxrosAMATTotalPassPackets_Type()
)
zxrosAMATTotalPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTotalPassPackets.setStatus("current")
_ZxrosAMATTotalFilterPackets_Type = Integer32
_ZxrosAMATTotalFilterPackets_Object = MibTableColumn
zxrosAMATTotalFilterPackets = _ZxrosAMATTotalFilterPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 6),
    _ZxrosAMATTotalFilterPackets_Type()
)
zxrosAMATTotalFilterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTotalFilterPackets.setStatus("current")
_ZxrosAMATTcpPassPackets_Type = Integer32
_ZxrosAMATTcpPassPackets_Object = MibTableColumn
zxrosAMATTcpPassPackets = _ZxrosAMATTcpPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 7),
    _ZxrosAMATTcpPassPackets_Type()
)
zxrosAMATTcpPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTcpPassPackets.setStatus("current")
_ZxrosAMATTcpFilterPackets_Type = Integer32
_ZxrosAMATTcpFilterPackets_Object = MibTableColumn
zxrosAMATTcpFilterPackets = _ZxrosAMATTcpFilterPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 8),
    _ZxrosAMATTcpFilterPackets_Type()
)
zxrosAMATTcpFilterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATTcpFilterPackets.setStatus("current")
_ZxrosAMATUdpPassPackets_Type = Integer32
_ZxrosAMATUdpPassPackets_Object = MibTableColumn
zxrosAMATUdpPassPackets = _ZxrosAMATUdpPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 9),
    _ZxrosAMATUdpPassPackets_Type()
)
zxrosAMATUdpPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATUdpPassPackets.setStatus("current")
_ZxrosAMATUdpFilterPackets_Type = Integer32
_ZxrosAMATUdpFilterPackets_Object = MibTableColumn
zxrosAMATUdpFilterPackets = _ZxrosAMATUdpFilterPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 10),
    _ZxrosAMATUdpFilterPackets_Type()
)
zxrosAMATUdpFilterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATUdpFilterPackets.setStatus("current")
_ZxrosAMATIcmpPassPackets_Type = Integer32
_ZxrosAMATIcmpPassPackets_Object = MibTableColumn
zxrosAMATIcmpPassPackets = _ZxrosAMATIcmpPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 11),
    _ZxrosAMATIcmpPassPackets_Type()
)
zxrosAMATIcmpPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIcmpPassPackets.setStatus("current")
_ZxrosAMATIcmpFilterPackets_Type = Integer32
_ZxrosAMATIcmpFilterPackets_Object = MibTableColumn
zxrosAMATIcmpFilterPackets = _ZxrosAMATIcmpFilterPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1000, 4, 1, 12),
    _ZxrosAMATIcmpFilterPackets_Type()
)
zxrosAMATIcmpFilterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATIcmpFilterPackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXROS-AMAT-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxros": zxros,
       "zxrosAMAT": zxrosAMAT,
       "zxrosAMATconfig": zxrosAMATconfig,
       "zxrosAMATAttackAgingTime": zxrosAMATAttackAgingTime,
       "zxrosAMATState": zxrosAMATState,
       "zxrosAMATHashOverNum": zxrosAMATHashOverNum,
       "zxrosAMATHashUpdateTime": zxrosAMATHashUpdateTime,
       "zxrosAMATIcmpConn": zxrosAMATIcmpConn,
       "zxrosAMATIcmpRate": zxrosAMATIcmpRate,
       "zxrosAMATIntervalSampleRate": zxrosAMATIntervalSampleRate,
       "zxrosAMATLogging": zxrosAMATLogging,
       "zxrosAMATRateLimit": zxrosAMATRateLimit,
       "zxrosAMATRuleUpdateTime": zxrosAMATRuleUpdateTime,
       "zxrosAMATSampleCode": zxrosAMATSampleCode,
       "zxrosAMATSampleMatchCode": zxrosAMATSampleMatchCode,
       "zxrosAMATTcpConn": zxrosAMATTcpConn,
       "zxrosAMATTcpProportion": zxrosAMATTcpProportion,
       "zxrosAMATTcpRate": zxrosAMATTcpRate,
       "zxrosAMATUdpConn": zxrosAMATUdpConn,
       "zxrosAMATUdpRate": zxrosAMATUdpRate,
       "zxrosAMATIgnoreIpAddressTable": zxrosAMATIgnoreIpAddressTable,
       "zxrosAMATIgnoreIpAddressEntry": zxrosAMATIgnoreIpAddressEntry,
       "zxrosAMATIgnoreIpAddressIpAddress": zxrosAMATIgnoreIpAddressIpAddress,
       "zxrosAMATIgnoreIpAddressVpnName": zxrosAMATIgnoreIpAddressVpnName,
       "zxrosAMATIgnoreIpAddressRowStatus": zxrosAMATIgnoreIpAddressRowStatus,
       "zxrosAMATAttackLoggingTable": zxrosAMATAttackLoggingTable,
       "zxrosAMATAttackLoggingEntry": zxrosAMATAttackLoggingEntry,
       "zxrosAMATAttackLoggingNo": zxrosAMATAttackLoggingNo,
       "zxrosAMATAttackDetectedTime": zxrosAMATAttackDetectedTime,
       "zxrosAMATAttackOverTime": zxrosAMATAttackOverTime,
       "zxrosAMATVpnName": zxrosAMATVpnName,
       "zxrosAMATIpAddress": zxrosAMATIpAddress,
       "zxrosAMATAttackMode": zxrosAMATAttackMode,
       "zxrosAMATTcpPassPacket": zxrosAMATTcpPassPacket,
       "zxrosAMATTcpFilterPacket": zxrosAMATTcpFilterPacket,
       "zxrosAMATUdpPassPacket": zxrosAMATUdpPassPacket,
       "zxrosAMATUdpFilterPacket": zxrosAMATUdpFilterPacket,
       "zxrosAMATIcmpPassPacket": zxrosAMATIcmpPassPacket,
       "zxrosAMATIcmpFilterPacket": zxrosAMATIcmpFilterPacket,
       "zxrosAMATTcpAttackOverValue": zxrosAMATTcpAttackOverValue,
       "zxrosAMATUdpAttackOverValue": zxrosAMATUdpAttackOverValue,
       "zxrosAMATIcmpAttackOverValue": zxrosAMATIcmpAttackOverValue,
       "zxrosAMATPassPacketsBeforeRuleCreated": zxrosAMATPassPacketsBeforeRuleCreated,
       "zxrosAMATShutDownLoggingTable": zxrosAMATShutDownLoggingTable,
       "zxrosAMATShutDownLoggingEntry": zxrosAMATShutDownLoggingEntry,
       "zxrosAMATShutDownLoggingNo": zxrosAMATShutDownLoggingNo,
       "zxrosAMATStartUpTime": zxrosAMATStartUpTime,
       "zxrosAMATShutDownTime": zxrosAMATShutDownTime,
       "zxrosAMATNoAmatPackets": zxrosAMATNoAmatPackets,
       "zxrosAMATTotalPassPackets": zxrosAMATTotalPassPackets,
       "zxrosAMATTotalFilterPackets": zxrosAMATTotalFilterPackets,
       "zxrosAMATTcpPassPackets": zxrosAMATTcpPassPackets,
       "zxrosAMATTcpFilterPackets": zxrosAMATTcpFilterPackets,
       "zxrosAMATUdpPassPackets": zxrosAMATUdpPassPackets,
       "zxrosAMATUdpFilterPackets": zxrosAMATUdpFilterPackets,
       "zxrosAMATIcmpPassPackets": zxrosAMATIcmpPassPackets,
       "zxrosAMATIcmpFilterPackets": zxrosAMATIcmpFilterPackets}
)
