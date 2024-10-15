# SNMP MIB module (PDN-CPIWF-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-CPIWF-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:25 2024
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

(pdnCpIwfEntry,
 pdnCpIwfIndex) = mibBuilder.importSymbols(
    "PDN-CP-IWF-MIB",
    "pdnCpIwfEntry",
    "pdnCpIwfIndex")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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

pdnCpIwfIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53)
)
pdnCpIwfIpMIB.setRevisions(
        ("2005-03-24 11:00",
         "2005-01-05 11:00",
         "2004-12-03 11:00",
         "2004-10-07 11:00",
         "2004-09-30 11:00",
         "2004-08-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VoiceChannelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bearer", 1),
          ("signaling", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PdnCpIwfIpNotifications_ObjectIdentity = ObjectIdentity
pdnCpIwfIpNotifications = _PdnCpIwfIpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0)
)
_PdnCpIwfIpMIBObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfIpMIBObjects = _PdnCpIwfIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1)
)
_PdnCpIwfIpConfigObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfIpConfigObjects = _PdnCpIwfIpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1)
)
_PdnCpIwfIpTable_Object = MibTable
pdnCpIwfIpTable = _PdnCpIwfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpTable.setStatus("current")
_PdnCpIwfIpEntry_Object = MibTableRow
pdnCpIwfIpEntry = _PdnCpIwfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpEntry.setStatus("current")
_PdnCpIwfIpAddress_Type = IpAddress
_PdnCpIwfIpAddress_Object = MibTableColumn
pdnCpIwfIpAddress = _PdnCpIwfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 1),
    _PdnCpIwfIpAddress_Type()
)
pdnCpIwfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpAddress.setStatus("current")
_PdnCpIwfIpNetMask_Type = IpAddress
_PdnCpIwfIpNetMask_Object = MibTableColumn
pdnCpIwfIpNetMask = _PdnCpIwfIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 2),
    _PdnCpIwfIpNetMask_Type()
)
pdnCpIwfIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpNetMask.setStatus("current")
_PdnCpIwfIpDefGateway_Type = IpAddress
_PdnCpIwfIpDefGateway_Object = MibTableColumn
pdnCpIwfIpDefGateway = _PdnCpIwfIpDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 3),
    _PdnCpIwfIpDefGateway_Type()
)
pdnCpIwfIpDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpDefGateway.setStatus("current")


class _PdnCpIwfIpActiveSoftswitch_Type(Integer32):
    """Custom type pdnCpIwfIpActiveSoftswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_PdnCpIwfIpActiveSoftswitch_Type.__name__ = "Integer32"
_PdnCpIwfIpActiveSoftswitch_Object = MibTableColumn
pdnCpIwfIpActiveSoftswitch = _PdnCpIwfIpActiveSoftswitch_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 4),
    _PdnCpIwfIpActiveSoftswitch_Type()
)
pdnCpIwfIpActiveSoftswitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfIpActiveSoftswitch.setStatus("current")
_PdnCpIwfIpChanTable_Object = MibTable
pdnCpIwfIpChanTable = _PdnCpIwfIpChanTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpChanTable.setStatus("current")
_PdnCpIwfIpChanEntry_Object = MibTableRow
pdnCpIwfIpChanEntry = _PdnCpIwfIpChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1)
)
pdnCpIwfIpChanEntry.setIndexNames(
    (0, "PDN-CP-IWF-MIB", "pdnCpIwfIndex"),
    (0, "PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanType"),
)
if mibBuilder.loadTexts:
    pdnCpIwfIpChanEntry.setStatus("current")
_PdnCpIwfIpChanType_Type = VoiceChannelType
_PdnCpIwfIpChanType_Object = MibTableColumn
pdnCpIwfIpChanType = _PdnCpIwfIpChanType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 1),
    _PdnCpIwfIpChanType_Type()
)
pdnCpIwfIpChanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnCpIwfIpChanType.setStatus("current")


class _PdnCpIwfIpChandot1dBasePort_Type(Unsigned32):
    """Custom type pdnCpIwfIpChandot1dBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnCpIwfIpChandot1dBasePort_Type.__name__ = "Unsigned32"
_PdnCpIwfIpChandot1dBasePort_Object = MibTableColumn
pdnCpIwfIpChandot1dBasePort = _PdnCpIwfIpChandot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 2),
    _PdnCpIwfIpChandot1dBasePort_Type()
)
pdnCpIwfIpChandot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfIpChandot1dBasePort.setStatus("current")


class _PdnCpIwfIpChanTosDSCP_Type(Integer32):
    """Custom type pdnCpIwfIpChanTosDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PdnCpIwfIpChanTosDSCP_Type.__name__ = "Integer32"
_PdnCpIwfIpChanTosDSCP_Object = MibTableColumn
pdnCpIwfIpChanTosDSCP = _PdnCpIwfIpChanTosDSCP_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 3),
    _PdnCpIwfIpChanTosDSCP_Type()
)
pdnCpIwfIpChanTosDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpChanTosDSCP.setStatus("current")
_PdnCpIwfIpTestObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfIpTestObjects = _PdnCpIwfIpTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 2)
)
_PdnCpIwfIpStatsObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfIpStatsObjects = _PdnCpIwfIpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 3)
)
_PdnCpIwfIpApplObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfIpApplObjects = _PdnCpIwfIpApplObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4)
)
_PdnCpIwfIpRtpTable_Object = MibTable
pdnCpIwfIpRtpTable = _PdnCpIwfIpRtpTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpRtpTable.setStatus("current")
_PdnCpIwfIpRtpEntry_Object = MibTableRow
pdnCpIwfIpRtpEntry = _PdnCpIwfIpRtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpRtpEntry.setStatus("current")


class _PdnCpIwfIpRtpLocalPortBase_Type(Integer32):
    """Custom type pdnCpIwfIpRtpLocalPortBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfIpRtpLocalPortBase_Type.__name__ = "Integer32"
_PdnCpIwfIpRtpLocalPortBase_Object = MibTableColumn
pdnCpIwfIpRtpLocalPortBase = _PdnCpIwfIpRtpLocalPortBase_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1, 1),
    _PdnCpIwfIpRtpLocalPortBase_Type()
)
pdnCpIwfIpRtpLocalPortBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpRtpLocalPortBase.setStatus("current")
_PdnCpIwfIpMgcpTable_Object = MibTable
pdnCpIwfIpMgcpTable = _PdnCpIwfIpMgcpTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpTable.setStatus("current")
_PdnCpIwfIpMgcpEntry_Object = MibTableRow
pdnCpIwfIpMgcpEntry = _PdnCpIwfIpMgcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpEntry.setStatus("current")


class _PdnCpIwfIpMgcpPortNumber_Type(Integer32):
    """Custom type pdnCpIwfIpMgcpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfIpMgcpPortNumber_Type.__name__ = "Integer32"
_PdnCpIwfIpMgcpPortNumber_Object = MibTableColumn
pdnCpIwfIpMgcpPortNumber = _PdnCpIwfIpMgcpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 1),
    _PdnCpIwfIpMgcpPortNumber_Type()
)
pdnCpIwfIpMgcpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpPortNumber.setStatus("current")
_PdnCpIwfIpMgcpPriAgentName_Type = DisplayString
_PdnCpIwfIpMgcpPriAgentName_Object = MibTableColumn
pdnCpIwfIpMgcpPriAgentName = _PdnCpIwfIpMgcpPriAgentName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 2),
    _PdnCpIwfIpMgcpPriAgentName_Type()
)
pdnCpIwfIpMgcpPriAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpPriAgentName.setStatus("current")
_PdnCpIwfIpMgcpPriAgentIpAddr_Type = IpAddress
_PdnCpIwfIpMgcpPriAgentIpAddr_Object = MibTableColumn
pdnCpIwfIpMgcpPriAgentIpAddr = _PdnCpIwfIpMgcpPriAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 3),
    _PdnCpIwfIpMgcpPriAgentIpAddr_Type()
)
pdnCpIwfIpMgcpPriAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpPriAgentIpAddr.setStatus("current")


class _PdnCpIwfIpMgcpPriAgentPortNum_Type(Integer32):
    """Custom type pdnCpIwfIpMgcpPriAgentPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfIpMgcpPriAgentPortNum_Type.__name__ = "Integer32"
_PdnCpIwfIpMgcpPriAgentPortNum_Object = MibTableColumn
pdnCpIwfIpMgcpPriAgentPortNum = _PdnCpIwfIpMgcpPriAgentPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 4),
    _PdnCpIwfIpMgcpPriAgentPortNum_Type()
)
pdnCpIwfIpMgcpPriAgentPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpPriAgentPortNum.setStatus("current")
_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Type = IpAddress
_PdnCpIwfIpMgcpPriAgentDNSIpAddr_Object = MibTableColumn
pdnCpIwfIpMgcpPriAgentDNSIpAddr = _PdnCpIwfIpMgcpPriAgentDNSIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 5),
    _PdnCpIwfIpMgcpPriAgentDNSIpAddr_Type()
)
pdnCpIwfIpMgcpPriAgentDNSIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpPriAgentDNSIpAddr.setStatus("current")
_PdnCpIwfIpMgcpSecAgentName_Type = DisplayString
_PdnCpIwfIpMgcpSecAgentName_Object = MibTableColumn
pdnCpIwfIpMgcpSecAgentName = _PdnCpIwfIpMgcpSecAgentName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 6),
    _PdnCpIwfIpMgcpSecAgentName_Type()
)
pdnCpIwfIpMgcpSecAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpSecAgentName.setStatus("current")
_PdnCpIwfIpMgcpSecAgentIpAddr_Type = IpAddress
_PdnCpIwfIpMgcpSecAgentIpAddr_Object = MibTableColumn
pdnCpIwfIpMgcpSecAgentIpAddr = _PdnCpIwfIpMgcpSecAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 7),
    _PdnCpIwfIpMgcpSecAgentIpAddr_Type()
)
pdnCpIwfIpMgcpSecAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpSecAgentIpAddr.setStatus("current")


class _PdnCpIwfIpMgcpSecAgentPortNum_Type(Integer32):
    """Custom type pdnCpIwfIpMgcpSecAgentPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfIpMgcpSecAgentPortNum_Type.__name__ = "Integer32"
_PdnCpIwfIpMgcpSecAgentPortNum_Object = MibTableColumn
pdnCpIwfIpMgcpSecAgentPortNum = _PdnCpIwfIpMgcpSecAgentPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 8),
    _PdnCpIwfIpMgcpSecAgentPortNum_Type()
)
pdnCpIwfIpMgcpSecAgentPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpSecAgentPortNum.setStatus("current")
_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Type = IpAddress
_PdnCpIwfIpMgcpSecAgentDNSIpAddr_Object = MibTableColumn
pdnCpIwfIpMgcpSecAgentDNSIpAddr = _PdnCpIwfIpMgcpSecAgentDNSIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 9),
    _PdnCpIwfIpMgcpSecAgentDNSIpAddr_Type()
)
pdnCpIwfIpMgcpSecAgentDNSIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpSecAgentDNSIpAddr.setStatus("current")
_PdnCpIwfIpMgcpRFC2833LoopSignal_Type = SwitchState
_PdnCpIwfIpMgcpRFC2833LoopSignal_Object = MibTableColumn
pdnCpIwfIpMgcpRFC2833LoopSignal = _PdnCpIwfIpMgcpRFC2833LoopSignal_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 10),
    _PdnCpIwfIpMgcpRFC2833LoopSignal_Type()
)
pdnCpIwfIpMgcpRFC2833LoopSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpRFC2833LoopSignal.setStatus("current")
_PdnCpIwfIpMgcpIADomainName_Type = DisplayString
_PdnCpIwfIpMgcpIADomainName_Object = MibTableColumn
pdnCpIwfIpMgcpIADomainName = _PdnCpIwfIpMgcpIADomainName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 11),
    _PdnCpIwfIpMgcpIADomainName_Type()
)
pdnCpIwfIpMgcpIADomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpIADomainName.setStatus("current")


class _PdnCpIwfIpMgcpEndPtFormat_Type(Integer32):
    """Custom type pdnCpIwfIpMgcpEndPtFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bracketandipaddr", 2),
          ("domainname", 3),
          ("ipaddr", 1))
    )


_PdnCpIwfIpMgcpEndPtFormat_Type.__name__ = "Integer32"
_PdnCpIwfIpMgcpEndPtFormat_Object = MibTableColumn
pdnCpIwfIpMgcpEndPtFormat = _PdnCpIwfIpMgcpEndPtFormat_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 12),
    _PdnCpIwfIpMgcpEndPtFormat_Type()
)
pdnCpIwfIpMgcpEndPtFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpEndPtFormat.setStatus("current")


class _PdnCpIwfIpMgcpRSIPKeepAlive_Type(Integer32):
    """Custom type pdnCpIwfIpMgcpRSIPKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PdnCpIwfIpMgcpRSIPKeepAlive_Type.__name__ = "Integer32"
_PdnCpIwfIpMgcpRSIPKeepAlive_Object = MibTableColumn
pdnCpIwfIpMgcpRSIPKeepAlive = _PdnCpIwfIpMgcpRSIPKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 13),
    _PdnCpIwfIpMgcpRSIPKeepAlive_Type()
)
pdnCpIwfIpMgcpRSIPKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfIpMgcpRSIPKeepAlive.setStatus("current")
_PdnCpIwfIpMIBConformance_ObjectIdentity = ObjectIdentity
pdnCpIwfIpMIBConformance = _PdnCpIwfIpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2)
)
_PdnCpIwfIpMIBCompliances_ObjectIdentity = ObjectIdentity
pdnCpIwfIpMIBCompliances = _PdnCpIwfIpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1)
)
_PdnCpIwfIpMIBGroups_ObjectIdentity = ObjectIdentity
pdnCpIwfIpMIBGroups = _PdnCpIwfIpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2)
)
_PdnCpIwfIpNtfyGroups_ObjectIdentity = ObjectIdentity
pdnCpIwfIpNtfyGroups = _PdnCpIwfIpNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3)
)
pdnCpIwfEntry.registerAugmentions(
    ("PDN-CPIWF-IP-MIB",
     "pdnCpIwfIpEntry")
)
pdnCpIwfIpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
pdnCpIwfEntry.registerAugmentions(
    ("PDN-CPIWF-IP-MIB",
     "pdnCpIwfIpRtpEntry")
)
pdnCpIwfIpRtpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
pdnCpIwfEntry.registerAugmentions(
    ("PDN-CPIWF-IP-MIB",
     "pdnCpIwfIpMgcpEntry")
)
pdnCpIwfIpMgcpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())

# Managed Objects groups

pdnCpIwfIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 1)
)
pdnCpIwfIpConfigGroup.setObjects(
      *(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChandot1dBasePort"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanTosDSCP"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpAddress"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpNetMask"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpDefGateway"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftswitch"))
)
if mibBuilder.loadTexts:
    pdnCpIwfIpConfigGroup.setStatus("current")

pdnCpIwfIpApplConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 2)
)
pdnCpIwfIpApplConfigGroup.setObjects(
      *(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpRtpLocalPortBase"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPortNumber"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentName"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentIpAddr"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentPortNum"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentDNSIpAddr"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentName"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentIpAddr"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentPortNum"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentDNSIpAddr"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRFC2833LoopSignal"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpIADomainName"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpEndPtFormat"),
        ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRSIPKeepAlive"))
)
if mibBuilder.loadTexts:
    pdnCpIwfIpApplConfigGroup.setStatus("current")


# Notification objects

pdnCpIwfIpActiveSoftSwitchChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpActiveSoftSwitchChanged.setStatus(
        "current"
    )


# Notifications groups

pdnCpIwfIpNtfyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3, 1)
)
pdnCpIwfIpNtfyGroup.setObjects(
    ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftSwitchChanged")
)
if mibBuilder.loadTexts:
    pdnCpIwfIpNtfyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnCpIwfIpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfIpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-CPIWF-IP-MIB",
    **{"VoiceChannelType": VoiceChannelType,
       "pdnCpIwfIpMIB": pdnCpIwfIpMIB,
       "pdnCpIwfIpNotifications": pdnCpIwfIpNotifications,
       "pdnCpIwfIpActiveSoftSwitchChanged": pdnCpIwfIpActiveSoftSwitchChanged,
       "pdnCpIwfIpMIBObjects": pdnCpIwfIpMIBObjects,
       "pdnCpIwfIpConfigObjects": pdnCpIwfIpConfigObjects,
       "pdnCpIwfIpTable": pdnCpIwfIpTable,
       "pdnCpIwfIpEntry": pdnCpIwfIpEntry,
       "pdnCpIwfIpAddress": pdnCpIwfIpAddress,
       "pdnCpIwfIpNetMask": pdnCpIwfIpNetMask,
       "pdnCpIwfIpDefGateway": pdnCpIwfIpDefGateway,
       "pdnCpIwfIpActiveSoftswitch": pdnCpIwfIpActiveSoftswitch,
       "pdnCpIwfIpChanTable": pdnCpIwfIpChanTable,
       "pdnCpIwfIpChanEntry": pdnCpIwfIpChanEntry,
       "pdnCpIwfIpChanType": pdnCpIwfIpChanType,
       "pdnCpIwfIpChandot1dBasePort": pdnCpIwfIpChandot1dBasePort,
       "pdnCpIwfIpChanTosDSCP": pdnCpIwfIpChanTosDSCP,
       "pdnCpIwfIpTestObjects": pdnCpIwfIpTestObjects,
       "pdnCpIwfIpStatsObjects": pdnCpIwfIpStatsObjects,
       "pdnCpIwfIpApplObjects": pdnCpIwfIpApplObjects,
       "pdnCpIwfIpRtpTable": pdnCpIwfIpRtpTable,
       "pdnCpIwfIpRtpEntry": pdnCpIwfIpRtpEntry,
       "pdnCpIwfIpRtpLocalPortBase": pdnCpIwfIpRtpLocalPortBase,
       "pdnCpIwfIpMgcpTable": pdnCpIwfIpMgcpTable,
       "pdnCpIwfIpMgcpEntry": pdnCpIwfIpMgcpEntry,
       "pdnCpIwfIpMgcpPortNumber": pdnCpIwfIpMgcpPortNumber,
       "pdnCpIwfIpMgcpPriAgentName": pdnCpIwfIpMgcpPriAgentName,
       "pdnCpIwfIpMgcpPriAgentIpAddr": pdnCpIwfIpMgcpPriAgentIpAddr,
       "pdnCpIwfIpMgcpPriAgentPortNum": pdnCpIwfIpMgcpPriAgentPortNum,
       "pdnCpIwfIpMgcpPriAgentDNSIpAddr": pdnCpIwfIpMgcpPriAgentDNSIpAddr,
       "pdnCpIwfIpMgcpSecAgentName": pdnCpIwfIpMgcpSecAgentName,
       "pdnCpIwfIpMgcpSecAgentIpAddr": pdnCpIwfIpMgcpSecAgentIpAddr,
       "pdnCpIwfIpMgcpSecAgentPortNum": pdnCpIwfIpMgcpSecAgentPortNum,
       "pdnCpIwfIpMgcpSecAgentDNSIpAddr": pdnCpIwfIpMgcpSecAgentDNSIpAddr,
       "pdnCpIwfIpMgcpRFC2833LoopSignal": pdnCpIwfIpMgcpRFC2833LoopSignal,
       "pdnCpIwfIpMgcpIADomainName": pdnCpIwfIpMgcpIADomainName,
       "pdnCpIwfIpMgcpEndPtFormat": pdnCpIwfIpMgcpEndPtFormat,
       "pdnCpIwfIpMgcpRSIPKeepAlive": pdnCpIwfIpMgcpRSIPKeepAlive,
       "pdnCpIwfIpMIBConformance": pdnCpIwfIpMIBConformance,
       "pdnCpIwfIpMIBCompliances": pdnCpIwfIpMIBCompliances,
       "pdnCpIwfIpMIBCompliance": pdnCpIwfIpMIBCompliance,
       "pdnCpIwfIpMIBGroups": pdnCpIwfIpMIBGroups,
       "pdnCpIwfIpConfigGroup": pdnCpIwfIpConfigGroup,
       "pdnCpIwfIpApplConfigGroup": pdnCpIwfIpApplConfigGroup,
       "pdnCpIwfIpNtfyGroups": pdnCpIwfIpNtfyGroups,
       "pdnCpIwfIpNtfyGroup": pdnCpIwfIpNtfyGroup}
)
