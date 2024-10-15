# SNMP MIB module (LIVINGSTON-PM-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIVINGSTON-PM-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:27 2024
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

(lucentPMMib,) = mibBuilder.importSymbols(
    "LIVINGSTON-ROOT-MIB",
    "lucentPMMib")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LucentPMGlobal_ObjectIdentity = ObjectIdentity
lucentPMGlobal = _LucentPMGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1)
)
_LucentPMGenGlobParams_ObjectIdentity = ObjectIdentity
lucentPMGenGlobParams = _LucentPMGenGlobParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1)
)
_LucentPMGenPriNameSrvr_Type = IpAddress
_LucentPMGenPriNameSrvr_Object = MibScalar
lucentPMGenPriNameSrvr = _LucentPMGenPriNameSrvr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 1),
    _LucentPMGenPriNameSrvr_Type()
)
lucentPMGenPriNameSrvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenPriNameSrvr.setStatus("mandatory")
_LucentPMGenAltNameSrvr_Type = IpAddress
_LucentPMGenAltNameSrvr_Object = MibScalar
lucentPMGenAltNameSrvr = _LucentPMGenAltNameSrvr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 3),
    _LucentPMGenAltNameSrvr_Type()
)
lucentPMGenAltNameSrvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenAltNameSrvr.setStatus("mandatory")
_LucentPMGenSyslogHost_Type = IpAddress
_LucentPMGenSyslogHost_Object = MibScalar
lucentPMGenSyslogHost = _LucentPMGenSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 4),
    _LucentPMGenSyslogHost_Type()
)
lucentPMGenSyslogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenSyslogHost.setStatus("mandatory")
_LucentPMGenAssignedAddr_Type = IpAddress
_LucentPMGenAssignedAddr_Object = MibScalar
lucentPMGenAssignedAddr = _LucentPMGenAssignedAddr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 5),
    _LucentPMGenAssignedAddr_Type()
)
lucentPMGenAssignedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenAssignedAddr.setStatus("mandatory")
_LucentPMGenReportedAddr_Type = IpAddress
_LucentPMGenReportedAddr_Object = MibScalar
lucentPMGenReportedAddr = _LucentPMGenReportedAddr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 6),
    _LucentPMGenReportedAddr_Type()
)
lucentPMGenReportedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenReportedAddr.setStatus("mandatory")


class _LucentPMGenNetMask_Type(Integer32):
    """Custom type lucentPMGenNetMask based on Integer32"""
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


_LucentPMGenNetMask_Type.__name__ = "Integer32"
_LucentPMGenNetMask_Object = MibScalar
lucentPMGenNetMask = _LucentPMGenNetMask_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 7),
    _LucentPMGenNetMask_Type()
)
lucentPMGenNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenNetMask.setStatus("mandatory")


class _LucentPMGenNameSvc_Type(Integer32):
    """Custom type lucentPMGenNameSvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dns", 2),
          ("nis", 3),
          ("none", 1))
    )


_LucentPMGenNameSvc_Type.__name__ = "Integer32"
_LucentPMGenNameSvc_Object = MibScalar
lucentPMGenNameSvc = _LucentPMGenNameSvc_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 8),
    _LucentPMGenNameSvc_Type()
)
lucentPMGenNameSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenNameSvc.setStatus("mandatory")
_LucentPMGenDomainName_Type = DisplayString
_LucentPMGenDomainName_Object = MibScalar
lucentPMGenDomainName = _LucentPMGenDomainName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 9),
    _LucentPMGenDomainName_Type()
)
lucentPMGenDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenDomainName.setStatus("mandatory")
_LucentPMGenTelnetPortNum_Type = Integer32
_LucentPMGenTelnetPortNum_Object = MibScalar
lucentPMGenTelnetPortNum = _LucentPMGenTelnetPortNum_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 10),
    _LucentPMGenTelnetPortNum_Type()
)
lucentPMGenTelnetPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenTelnetPortNum.setStatus("mandatory")
_LucentPMGenMaxConsConn_Type = Integer32
_LucentPMGenMaxConsConn_Object = MibScalar
lucentPMGenMaxConsConn = _LucentPMGenMaxConsConn_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 11),
    _LucentPMGenMaxConsConn_Type()
)
lucentPMGenMaxConsConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenMaxConsConn.setStatus("mandatory")


class _LucentPMGenOSPF_Type(Integer32):
    """Custom type lucentPMGenOSPF based on Integer32"""
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


_LucentPMGenOSPF_Type.__name__ = "Integer32"
_LucentPMGenOSPF_Object = MibScalar
lucentPMGenOSPF = _LucentPMGenOSPF_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 12),
    _LucentPMGenOSPF_Type()
)
lucentPMGenOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenOSPF.setStatus("mandatory")


class _LucentPMGenBGP_Type(Integer32):
    """Custom type lucentPMGenBGP based on Integer32"""
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


_LucentPMGenBGP_Type.__name__ = "Integer32"
_LucentPMGenBGP_Object = MibScalar
lucentPMGenBGP = _LucentPMGenBGP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 13),
    _LucentPMGenBGP_Type()
)
lucentPMGenBGP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenBGP.setStatus("mandatory")


class _LucentPMGenIPX_Type(Integer32):
    """Custom type lucentPMGenIPX based on Integer32"""
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


_LucentPMGenIPX_Type.__name__ = "Integer32"
_LucentPMGenIPX_Object = MibScalar
lucentPMGenIPX = _LucentPMGenIPX_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 14),
    _LucentPMGenIPX_Type()
)
lucentPMGenIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenIPX.setStatus("mandatory")


class _LucentPMGenNetBIOS_Type(Integer32):
    """Custom type lucentPMGenNetBIOS based on Integer32"""
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


_LucentPMGenNetBIOS_Type.__name__ = "Integer32"
_LucentPMGenNetBIOS_Object = MibScalar
lucentPMGenNetBIOS = _LucentPMGenNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 15),
    _LucentPMGenNetBIOS_Type()
)
lucentPMGenNetBIOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenNetBIOS.setStatus("mandatory")


class _LucentPMGenCallCheck_Type(Integer32):
    """Custom type lucentPMGenCallCheck based on Integer32"""
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


_LucentPMGenCallCheck_Type.__name__ = "Integer32"
_LucentPMGenCallCheck_Object = MibScalar
lucentPMGenCallCheck = _LucentPMGenCallCheck_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 1, 16),
    _LucentPMGenCallCheck_Type()
)
lucentPMGenCallCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMGenCallCheck.setStatus("mandatory")
_LucentPMRadiusMgmt_ObjectIdentity = ObjectIdentity
lucentPMRadiusMgmt = _LucentPMRadiusMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2)
)
_LucentPMRadiusPriIP_Type = IpAddress
_LucentPMRadiusPriIP_Object = MibScalar
lucentPMRadiusPriIP = _LucentPMRadiusPriIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 1),
    _LucentPMRadiusPriIP_Type()
)
lucentPMRadiusPriIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusPriIP.setStatus("mandatory")
_LucentPMRadiusAltIP_Type = IpAddress
_LucentPMRadiusAltIP_Object = MibScalar
lucentPMRadiusAltIP = _LucentPMRadiusAltIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 2),
    _LucentPMRadiusAltIP_Type()
)
lucentPMRadiusAltIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusAltIP.setStatus("mandatory")
_LucentPMRadiusPriAcctIP_Type = IpAddress
_LucentPMRadiusPriAcctIP_Object = MibScalar
lucentPMRadiusPriAcctIP = _LucentPMRadiusPriAcctIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 3),
    _LucentPMRadiusPriAcctIP_Type()
)
lucentPMRadiusPriAcctIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusPriAcctIP.setStatus("mandatory")
_LucentPMRadiusAltAcctIP_Type = IpAddress
_LucentPMRadiusAltAcctIP_Object = MibScalar
lucentPMRadiusAltAcctIP = _LucentPMRadiusAltAcctIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 4),
    _LucentPMRadiusAltAcctIP_Type()
)
lucentPMRadiusAltAcctIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusAltAcctIP.setStatus("mandatory")
_LucentPMRadiusPriPort_Type = Integer32
_LucentPMRadiusPriPort_Object = MibScalar
lucentPMRadiusPriPort = _LucentPMRadiusPriPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 5),
    _LucentPMRadiusPriPort_Type()
)
lucentPMRadiusPriPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusPriPort.setStatus("mandatory")
_LucentPMRadiusAltPort_Type = Integer32
_LucentPMRadiusAltPort_Object = MibScalar
lucentPMRadiusAltPort = _LucentPMRadiusAltPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 6),
    _LucentPMRadiusAltPort_Type()
)
lucentPMRadiusAltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusAltPort.setStatus("mandatory")
_LucentPMRadiusPriAcctPort_Type = Integer32
_LucentPMRadiusPriAcctPort_Object = MibScalar
lucentPMRadiusPriAcctPort = _LucentPMRadiusPriAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 7),
    _LucentPMRadiusPriAcctPort_Type()
)
lucentPMRadiusPriAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusPriAcctPort.setStatus("mandatory")
_LucentPMRadiusAltAcctPort_Type = IpAddress
_LucentPMRadiusAltAcctPort_Object = MibScalar
lucentPMRadiusAltAcctPort = _LucentPMRadiusAltAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 8),
    _LucentPMRadiusAltAcctPort_Type()
)
lucentPMRadiusAltAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusAltAcctPort.setStatus("mandatory")
_LucentPMRadiusAuthFails_Type = Counter32
_LucentPMRadiusAuthFails_Object = MibScalar
lucentPMRadiusAuthFails = _LucentPMRadiusAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 9),
    _LucentPMRadiusAuthFails_Type()
)
lucentPMRadiusAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPMRadiusAuthFails.setStatus("mandatory")
_LucentPMRadiusRetrans_Type = Integer32
_LucentPMRadiusRetrans_Object = MibScalar
lucentPMRadiusRetrans = _LucentPMRadiusRetrans_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 10),
    _LucentPMRadiusRetrans_Type()
)
lucentPMRadiusRetrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusRetrans.setStatus("mandatory")
_LucentPMRadiusTimeout_Type = Integer32
_LucentPMRadiusTimeout_Object = MibScalar
lucentPMRadiusTimeout = _LucentPMRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 11),
    _LucentPMRadiusTimeout_Type()
)
lucentPMRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusTimeout.setStatus("mandatory")


class _LucentPMRadiusAuth_Type(Integer32):
    """Custom type lucentPMRadiusAuth based on Integer32"""
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


_LucentPMRadiusAuth_Type.__name__ = "Integer32"
_LucentPMRadiusAuth_Object = MibScalar
lucentPMRadiusAuth = _LucentPMRadiusAuth_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 12),
    _LucentPMRadiusAuth_Type()
)
lucentPMRadiusAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMRadiusAuth.setStatus("mandatory")


class _LucentPMRadiusSecret_Type(OctetString):
    """Custom type lucentPMRadiusSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_LucentPMRadiusSecret_Type.__name__ = "OctetString"
_LucentPMRadiusSecret_Object = MibScalar
lucentPMRadiusSecret = _LucentPMRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 2, 13),
    _LucentPMRadiusSecret_Type()
)
lucentPMRadiusSecret.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lucentPMRadiusSecret.setStatus("mandatory")
_LucentPMChoiceNetMgmt_ObjectIdentity = ObjectIdentity
lucentPMChoiceNetMgmt = _LucentPMChoiceNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3)
)
_LucentPMChoiceNetPriIP_Type = IpAddress
_LucentPMChoiceNetPriIP_Object = MibScalar
lucentPMChoiceNetPriIP = _LucentPMChoiceNetPriIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3, 1),
    _LucentPMChoiceNetPriIP_Type()
)
lucentPMChoiceNetPriIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMChoiceNetPriIP.setStatus("mandatory")
_LucentPMChoiceNetAltIP_Type = IpAddress
_LucentPMChoiceNetAltIP_Object = MibScalar
lucentPMChoiceNetAltIP = _LucentPMChoiceNetAltIP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3, 2),
    _LucentPMChoiceNetAltIP_Type()
)
lucentPMChoiceNetAltIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMChoiceNetAltIP.setStatus("mandatory")
_LucentPMChoiceNetPriPort_Type = Integer32
_LucentPMChoiceNetPriPort_Object = MibScalar
lucentPMChoiceNetPriPort = _LucentPMChoiceNetPriPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3, 3),
    _LucentPMChoiceNetPriPort_Type()
)
lucentPMChoiceNetPriPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMChoiceNetPriPort.setStatus("mandatory")
_LucentPMChoiceNetAltPort_Type = Integer32
_LucentPMChoiceNetAltPort_Object = MibScalar
lucentPMChoiceNetAltPort = _LucentPMChoiceNetAltPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3, 4),
    _LucentPMChoiceNetAltPort_Type()
)
lucentPMChoiceNetAltPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPMChoiceNetAltPort.setStatus("mandatory")


class _LucentPMChoiceNetSecret_Type(OctetString):
    """Custom type lucentPMChoiceNetSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_LucentPMChoiceNetSecret_Type.__name__ = "OctetString"
_LucentPMChoiceNetSecret_Object = MibScalar
lucentPMChoiceNetSecret = _LucentPMChoiceNetSecret_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 2, 1, 3, 5),
    _LucentPMChoiceNetSecret_Type()
)
lucentPMChoiceNetSecret.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lucentPMChoiceNetSecret.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIVINGSTON-PM-GLOBAL-MIB",
    **{"lucentPMGlobal": lucentPMGlobal,
       "lucentPMGenGlobParams": lucentPMGenGlobParams,
       "lucentPMGenPriNameSrvr": lucentPMGenPriNameSrvr,
       "lucentPMGenAltNameSrvr": lucentPMGenAltNameSrvr,
       "lucentPMGenSyslogHost": lucentPMGenSyslogHost,
       "lucentPMGenAssignedAddr": lucentPMGenAssignedAddr,
       "lucentPMGenReportedAddr": lucentPMGenReportedAddr,
       "lucentPMGenNetMask": lucentPMGenNetMask,
       "lucentPMGenNameSvc": lucentPMGenNameSvc,
       "lucentPMGenDomainName": lucentPMGenDomainName,
       "lucentPMGenTelnetPortNum": lucentPMGenTelnetPortNum,
       "lucentPMGenMaxConsConn": lucentPMGenMaxConsConn,
       "lucentPMGenOSPF": lucentPMGenOSPF,
       "lucentPMGenBGP": lucentPMGenBGP,
       "lucentPMGenIPX": lucentPMGenIPX,
       "lucentPMGenNetBIOS": lucentPMGenNetBIOS,
       "lucentPMGenCallCheck": lucentPMGenCallCheck,
       "lucentPMRadiusMgmt": lucentPMRadiusMgmt,
       "lucentPMRadiusPriIP": lucentPMRadiusPriIP,
       "lucentPMRadiusAltIP": lucentPMRadiusAltIP,
       "lucentPMRadiusPriAcctIP": lucentPMRadiusPriAcctIP,
       "lucentPMRadiusAltAcctIP": lucentPMRadiusAltAcctIP,
       "lucentPMRadiusPriPort": lucentPMRadiusPriPort,
       "lucentPMRadiusAltPort": lucentPMRadiusAltPort,
       "lucentPMRadiusPriAcctPort": lucentPMRadiusPriAcctPort,
       "lucentPMRadiusAltAcctPort": lucentPMRadiusAltAcctPort,
       "lucentPMRadiusAuthFails": lucentPMRadiusAuthFails,
       "lucentPMRadiusRetrans": lucentPMRadiusRetrans,
       "lucentPMRadiusTimeout": lucentPMRadiusTimeout,
       "lucentPMRadiusAuth": lucentPMRadiusAuth,
       "lucentPMRadiusSecret": lucentPMRadiusSecret,
       "lucentPMChoiceNetMgmt": lucentPMChoiceNetMgmt,
       "lucentPMChoiceNetPriIP": lucentPMChoiceNetPriIP,
       "lucentPMChoiceNetAltIP": lucentPMChoiceNetAltIP,
       "lucentPMChoiceNetPriPort": lucentPMChoiceNetPriPort,
       "lucentPMChoiceNetAltPort": lucentPMChoiceNetAltPort,
       "lucentPMChoiceNetSecret": lucentPMChoiceNetSecret}
)
