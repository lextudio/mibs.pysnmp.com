# SNMP MIB module (CISCO-DMN-DSG-PROTOCOLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-PROTOCOLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:30 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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


# MODULE-IDENTITY

ciscoDSGProtocols = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39)
)
ciscoDSGProtocols.setRevisions(
        ("2013-07-10 19:03",
         "2012-03-07 07:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ProtocolsCtrlTelnet_Type(Integer32):
    """Custom type protocolsCtrlTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ProtocolsCtrlTelnet_Type.__name__ = "Integer32"
_ProtocolsCtrlTelnet_Object = MibScalar
protocolsCtrlTelnet = _ProtocolsCtrlTelnet_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 1),
    _ProtocolsCtrlTelnet_Type()
)
protocolsCtrlTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlTelnet.setStatus("current")


class _ProtocolsCtrlSSH_Type(Integer32):
    """Custom type protocolsCtrlSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ProtocolsCtrlSSH_Type.__name__ = "Integer32"
_ProtocolsCtrlSSH_Object = MibScalar
protocolsCtrlSSH = _ProtocolsCtrlSSH_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 2),
    _ProtocolsCtrlSSH_Type()
)
protocolsCtrlSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlSSH.setStatus("current")


class _ProtocolsCtrlHTTP_Type(Integer32):
    """Custom type protocolsCtrlHTTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("secure", 3))
    )


_ProtocolsCtrlHTTP_Type.__name__ = "Integer32"
_ProtocolsCtrlHTTP_Object = MibScalar
protocolsCtrlHTTP = _ProtocolsCtrlHTTP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 3),
    _ProtocolsCtrlHTTP_Type()
)
protocolsCtrlHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlHTTP.setStatus("current")


class _ProtocolsCtrlSNMP_Type(Integer32):
    """Custom type protocolsCtrlSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ProtocolsCtrlSNMP_Type.__name__ = "Integer32"
_ProtocolsCtrlSNMP_Object = MibScalar
protocolsCtrlSNMP = _ProtocolsCtrlSNMP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 5),
    _ProtocolsCtrlSNMP_Type()
)
protocolsCtrlSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlSNMP.setStatus("current")


class _ProtocolsCtrlRIP_Type(Integer32):
    """Custom type protocolsCtrlRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ProtocolsCtrlRIP_Type.__name__ = "Integer32"
_ProtocolsCtrlRIP_Object = MibScalar
protocolsCtrlRIP = _ProtocolsCtrlRIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 6),
    _ProtocolsCtrlRIP_Type()
)
protocolsCtrlRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlRIP.setStatus("current")


class _ProtocolsCtrlMPE_Type(Integer32):
    """Custom type protocolsCtrlMPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fwdAll", 2),
          ("fwdFiltered", 3),
          ("fwdNone", 1))
    )


_ProtocolsCtrlMPE_Type.__name__ = "Integer32"
_ProtocolsCtrlMPE_Object = MibScalar
protocolsCtrlMPE = _ProtocolsCtrlMPE_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 7),
    _ProtocolsCtrlMPE_Type()
)
protocolsCtrlMPE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlMPE.setStatus("current")


class _ProtocolsCtrlIGMP_Type(Integer32):
    """Custom type protocolsCtrlIGMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("v2", 3),
          ("v3", 2))
    )


_ProtocolsCtrlIGMP_Type.__name__ = "Integer32"
_ProtocolsCtrlIGMP_Object = MibScalar
protocolsCtrlIGMP = _ProtocolsCtrlIGMP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 8),
    _ProtocolsCtrlIGMP_Type()
)
protocolsCtrlIGMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlIGMP.setStatus("current")


class _ProtocolslTimeoutsIdleSessonGlobal_Type(Integer32):
    """Custom type protocolslTimeoutsIdleSessonGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209600),
    )


_ProtocolslTimeoutsIdleSessonGlobal_Type.__name__ = "Integer32"
_ProtocolslTimeoutsIdleSessonGlobal_Object = MibScalar
protocolslTimeoutsIdleSessonGlobal = _ProtocolslTimeoutsIdleSessonGlobal_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 9),
    _ProtocolslTimeoutsIdleSessonGlobal_Type()
)
protocolslTimeoutsIdleSessonGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolslTimeoutsIdleSessonGlobal.setStatus("current")


class _ProtocolsCtrlSyslog_Type(Integer32):
    """Custom type protocolsCtrlSyslog based on Integer32"""
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
        *(("disable", 1),
          ("legacy", 2),
          ("syslogTcp", 3),
          ("syslogUdp", 4))
    )


_ProtocolsCtrlSyslog_Type.__name__ = "Integer32"
_ProtocolsCtrlSyslog_Object = MibScalar
protocolsCtrlSyslog = _ProtocolsCtrlSyslog_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 10),
    _ProtocolsCtrlSyslog_Type()
)
protocolsCtrlSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlSyslog.setStatus("current")
_ProtocolsCtrlSyslogCfgIpAddr_Type = IpAddress
_ProtocolsCtrlSyslogCfgIpAddr_Object = MibScalar
protocolsCtrlSyslogCfgIpAddr = _ProtocolsCtrlSyslogCfgIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 11),
    _ProtocolsCtrlSyslogCfgIpAddr_Type()
)
protocolsCtrlSyslogCfgIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlSyslogCfgIpAddr.setStatus("current")


class _ProtocolsCtrlSyslogCfgPort_Type(Integer32):
    """Custom type protocolsCtrlSyslogCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtocolsCtrlSyslogCfgPort_Type.__name__ = "Integer32"
_ProtocolsCtrlSyslogCfgPort_Object = MibScalar
protocolsCtrlSyslogCfgPort = _ProtocolsCtrlSyslogCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 39, 12),
    _ProtocolsCtrlSyslogCfgPort_Type()
)
protocolsCtrlSyslogCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolsCtrlSyslogCfgPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-PROTOCOLS-MIB",
    **{"ciscoDSGProtocols": ciscoDSGProtocols,
       "protocolsCtrlTelnet": protocolsCtrlTelnet,
       "protocolsCtrlSSH": protocolsCtrlSSH,
       "protocolsCtrlHTTP": protocolsCtrlHTTP,
       "protocolsCtrlSNMP": protocolsCtrlSNMP,
       "protocolsCtrlRIP": protocolsCtrlRIP,
       "protocolsCtrlMPE": protocolsCtrlMPE,
       "protocolsCtrlIGMP": protocolsCtrlIGMP,
       "protocolslTimeoutsIdleSessonGlobal": protocolslTimeoutsIdleSessonGlobal,
       "protocolsCtrlSyslog": protocolsCtrlSyslog,
       "protocolsCtrlSyslogCfgIpAddr": protocolsCtrlSyslogCfgIpAddr,
       "protocolsCtrlSyslogCfgPort": protocolsCtrlSyslogCfgPort}
)
