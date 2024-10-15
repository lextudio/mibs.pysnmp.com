# SNMP MIB module (PROBERTTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROBERTTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:47 2024
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

(probeRttExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "probeRttExt")

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

apProbeRttExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApProbeRttEnable_Type(Integer32):
    """Custom type apProbeRttEnable based on Integer32"""
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


_ApProbeRttEnable_Type.__name__ = "Integer32"
_ApProbeRttEnable_Object = MibScalar
apProbeRttEnable = _ApProbeRttEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 2),
    _ApProbeRttEnable_Type()
)
apProbeRttEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttEnable.setStatus("current")


class _ApProbeRttMethod0_Type(Integer32):
    """Custom type apProbeRttMethod0 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 0),
          ("tcp", 1))
    )


_ApProbeRttMethod0_Type.__name__ = "Integer32"
_ApProbeRttMethod0_Object = MibScalar
apProbeRttMethod0 = _ApProbeRttMethod0_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 3),
    _ApProbeRttMethod0_Type()
)
apProbeRttMethod0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttMethod0.setStatus("current")


class _ApProbeRttMethod1_Type(Integer32):
    """Custom type apProbeRttMethod1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 0),
          ("none", 2),
          ("tcp", 1))
    )


_ApProbeRttMethod1_Type.__name__ = "Integer32"
_ApProbeRttMethod1_Object = MibScalar
apProbeRttMethod1 = _ApProbeRttMethod1_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 4),
    _ApProbeRttMethod1_Type()
)
apProbeRttMethod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttMethod1.setStatus("current")


class _ApProbeRttIcmpSamples_Type(Integer32):
    """Custom type apProbeRttIcmpSamples based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ApProbeRttIcmpSamples_Type.__name__ = "Integer32"
_ApProbeRttIcmpSamples_Object = MibScalar
apProbeRttIcmpSamples = _ApProbeRttIcmpSamples_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 5),
    _ApProbeRttIcmpSamples_Type()
)
apProbeRttIcmpSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttIcmpSamples.setStatus("current")


class _ApProbeRttIcmpInterval_Type(Integer32):
    """Custom type apProbeRttIcmpInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApProbeRttIcmpInterval_Type.__name__ = "Integer32"
_ApProbeRttIcmpInterval_Object = MibScalar
apProbeRttIcmpInterval = _ApProbeRttIcmpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 6),
    _ApProbeRttIcmpInterval_Type()
)
apProbeRttIcmpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttIcmpInterval.setStatus("current")


class _ApProbeRttTcpPort0_Type(Integer32):
    """Custom type apProbeRttTcpPort0 based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApProbeRttTcpPort0_Type.__name__ = "Integer32"
_ApProbeRttTcpPort0_Object = MibScalar
apProbeRttTcpPort0 = _ApProbeRttTcpPort0_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 7),
    _ApProbeRttTcpPort0_Type()
)
apProbeRttTcpPort0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttTcpPort0.setStatus("current")


class _ApProbeRttTcpPort1_Type(Integer32):
    """Custom type apProbeRttTcpPort1 based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApProbeRttTcpPort1_Type.__name__ = "Integer32"
_ApProbeRttTcpPort1_Object = MibScalar
apProbeRttTcpPort1 = _ApProbeRttTcpPort1_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 8),
    _ApProbeRttTcpPort1_Type()
)
apProbeRttTcpPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttTcpPort1.setStatus("current")


class _ApProbeRttTcpPort2_Type(Integer32):
    """Custom type apProbeRttTcpPort2 based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApProbeRttTcpPort2_Type.__name__ = "Integer32"
_ApProbeRttTcpPort2_Object = MibScalar
apProbeRttTcpPort2 = _ApProbeRttTcpPort2_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 9),
    _ApProbeRttTcpPort2_Type()
)
apProbeRttTcpPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttTcpPort2.setStatus("current")


class _ApProbeRttTcpPort3_Type(Integer32):
    """Custom type apProbeRttTcpPort3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApProbeRttTcpPort3_Type.__name__ = "Integer32"
_ApProbeRttTcpPort3_Object = MibScalar
apProbeRttTcpPort3 = _ApProbeRttTcpPort3_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 10),
    _ApProbeRttTcpPort3_Type()
)
apProbeRttTcpPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apProbeRttTcpPort3.setStatus("current")


class _ApProbeRttLastReset_Type(DisplayString):
    """Custom type apProbeRttLastReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ApProbeRttLastReset_Type.__name__ = "DisplayString"
_ApProbeRttLastReset_Object = MibScalar
apProbeRttLastReset = _ApProbeRttLastReset_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 11),
    _ApProbeRttLastReset_Type()
)
apProbeRttLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttLastReset.setStatus("current")
_ApProbeRttTtlProbes_Type = Integer32
_ApProbeRttTtlProbes_Object = MibScalar
apProbeRttTtlProbes = _ApProbeRttTtlProbes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 12),
    _ApProbeRttTtlProbes_Type()
)
apProbeRttTtlProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTtlProbes.setStatus("current")
_ApProbeRttAvgProbes_Type = Integer32
_ApProbeRttAvgProbes_Object = MibScalar
apProbeRttAvgProbes = _ApProbeRttAvgProbes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 13),
    _ApProbeRttAvgProbes_Type()
)
apProbeRttAvgProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttAvgProbes.setStatus("current")
_ApProbeRttICMPReqSent_Type = Integer32
_ApProbeRttICMPReqSent_Object = MibScalar
apProbeRttICMPReqSent = _ApProbeRttICMPReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 14),
    _ApProbeRttICMPReqSent_Type()
)
apProbeRttICMPReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttICMPReqSent.setStatus("current")
_ApProbeRttICMPResp_Type = Integer32
_ApProbeRttICMPResp_Object = MibScalar
apProbeRttICMPResp = _ApProbeRttICMPResp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 15),
    _ApProbeRttICMPResp_Type()
)
apProbeRttICMPResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttICMPResp.setStatus("current")
_ApProbeRttICMPNoResp_Type = Integer32
_ApProbeRttICMPNoResp_Object = MibScalar
apProbeRttICMPNoResp = _ApProbeRttICMPNoResp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 16),
    _ApProbeRttICMPNoResp_Type()
)
apProbeRttICMPNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttICMPNoResp.setStatus("current")
_ApProbeRttICMPAvgReq_Type = Integer32
_ApProbeRttICMPAvgReq_Object = MibScalar
apProbeRttICMPAvgReq = _ApProbeRttICMPAvgReq_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 17),
    _ApProbeRttICMPAvgReq_Type()
)
apProbeRttICMPAvgReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttICMPAvgReq.setStatus("current")
_ApProbeRttICMPSendFail_Type = Integer32
_ApProbeRttICMPSendFail_Object = MibScalar
apProbeRttICMPSendFail = _ApProbeRttICMPSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 18),
    _ApProbeRttICMPSendFail_Type()
)
apProbeRttICMPSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttICMPSendFail.setStatus("current")
_ApProbeRttTCPReqSent_Type = Integer32
_ApProbeRttTCPReqSent_Object = MibScalar
apProbeRttTCPReqSent = _ApProbeRttTCPReqSent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 19),
    _ApProbeRttTCPReqSent_Type()
)
apProbeRttTCPReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTCPReqSent.setStatus("current")
_ApProbeRttTCPResp_Type = Integer32
_ApProbeRttTCPResp_Object = MibScalar
apProbeRttTCPResp = _ApProbeRttTCPResp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 20),
    _ApProbeRttTCPResp_Type()
)
apProbeRttTCPResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTCPResp.setStatus("current")
_ApProbeRttTCPNoResp_Type = Integer32
_ApProbeRttTCPNoResp_Object = MibScalar
apProbeRttTCPNoResp = _ApProbeRttTCPNoResp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 21),
    _ApProbeRttTCPNoResp_Type()
)
apProbeRttTCPNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTCPNoResp.setStatus("current")
_ApProbeRttTCPAvgReq_Type = Integer32
_ApProbeRttTCPAvgReq_Object = MibScalar
apProbeRttTCPAvgReq = _ApProbeRttTCPAvgReq_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 22),
    _ApProbeRttTCPAvgReq_Type()
)
apProbeRttTCPAvgReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTCPAvgReq.setStatus("current")
_ApProbeRttTCPSendFail_Type = Integer32
_ApProbeRttTCPSendFail_Object = MibScalar
apProbeRttTCPSendFail = _ApProbeRttTCPSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 23),
    _ApProbeRttTCPSendFail_Type()
)
apProbeRttTCPSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttTCPSendFail.setStatus("current")
_ApProbeRttPortTable_Object = MibTable
apProbeRttPortTable = _ApProbeRttPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24)
)
if mibBuilder.loadTexts:
    apProbeRttPortTable.setStatus("current")
_ApProbeRttPortEntry_Object = MibTableRow
apProbeRttPortEntry = _ApProbeRttPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1)
)
apProbeRttPortEntry.setIndexNames(
    (0, "PROBERTTEXT-MIB", "apProbeRttPortIndex"),
)
if mibBuilder.loadTexts:
    apProbeRttPortEntry.setStatus("current")


class _ApProbeRttPortIndex_Type(Integer32):
    """Custom type apProbeRttPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ApProbeRttPortIndex_Type.__name__ = "Integer32"
_ApProbeRttPortIndex_Object = MibTableColumn
apProbeRttPortIndex = _ApProbeRttPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 1),
    _ApProbeRttPortIndex_Type()
)
apProbeRttPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttPortIndex.setStatus("current")
_ApProbeRttPortNumber_Type = Integer32
_ApProbeRttPortNumber_Object = MibTableColumn
apProbeRttPortNumber = _ApProbeRttPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 2),
    _ApProbeRttPortNumber_Type()
)
apProbeRttPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttPortNumber.setStatus("current")
_ApProbeRttPortRequests_Type = Integer32
_ApProbeRttPortRequests_Object = MibTableColumn
apProbeRttPortRequests = _ApProbeRttPortRequests_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 3),
    _ApProbeRttPortRequests_Type()
)
apProbeRttPortRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttPortRequests.setStatus("current")
_ApProbeRttPortResponses_Type = Integer32
_ApProbeRttPortResponses_Object = MibTableColumn
apProbeRttPortResponses = _ApProbeRttPortResponses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 4),
    _ApProbeRttPortResponses_Type()
)
apProbeRttPortResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttPortResponses.setStatus("current")
_ApProbeRttPortFailures_Type = Integer32
_ApProbeRttPortFailures_Object = MibTableColumn
apProbeRttPortFailures = _ApProbeRttPortFailures_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 5),
    _ApProbeRttPortFailures_Type()
)
apProbeRttPortFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apProbeRttPortFailures.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROBERTTEXT-MIB",
    **{"apProbeRttExtMib": apProbeRttExtMib,
       "apProbeRttEnable": apProbeRttEnable,
       "apProbeRttMethod0": apProbeRttMethod0,
       "apProbeRttMethod1": apProbeRttMethod1,
       "apProbeRttIcmpSamples": apProbeRttIcmpSamples,
       "apProbeRttIcmpInterval": apProbeRttIcmpInterval,
       "apProbeRttTcpPort0": apProbeRttTcpPort0,
       "apProbeRttTcpPort1": apProbeRttTcpPort1,
       "apProbeRttTcpPort2": apProbeRttTcpPort2,
       "apProbeRttTcpPort3": apProbeRttTcpPort3,
       "apProbeRttLastReset": apProbeRttLastReset,
       "apProbeRttTtlProbes": apProbeRttTtlProbes,
       "apProbeRttAvgProbes": apProbeRttAvgProbes,
       "apProbeRttICMPReqSent": apProbeRttICMPReqSent,
       "apProbeRttICMPResp": apProbeRttICMPResp,
       "apProbeRttICMPNoResp": apProbeRttICMPNoResp,
       "apProbeRttICMPAvgReq": apProbeRttICMPAvgReq,
       "apProbeRttICMPSendFail": apProbeRttICMPSendFail,
       "apProbeRttTCPReqSent": apProbeRttTCPReqSent,
       "apProbeRttTCPResp": apProbeRttTCPResp,
       "apProbeRttTCPNoResp": apProbeRttTCPNoResp,
       "apProbeRttTCPAvgReq": apProbeRttTCPAvgReq,
       "apProbeRttTCPSendFail": apProbeRttTCPSendFail,
       "apProbeRttPortTable": apProbeRttPortTable,
       "apProbeRttPortEntry": apProbeRttPortEntry,
       "apProbeRttPortIndex": apProbeRttPortIndex,
       "apProbeRttPortNumber": apProbeRttPortNumber,
       "apProbeRttPortRequests": apProbeRttPortRequests,
       "apProbeRttPortResponses": apProbeRttPortResponses,
       "apProbeRttPortFailures": apProbeRttPortFailures}
)
