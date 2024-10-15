# SNMP MIB module (SALIX-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:35 2024
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

(platform1,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "platform1")

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

salixRtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixRtpMIBObjects_ObjectIdentity = ObjectIdentity
salixRtpMIBObjects = _SalixRtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1)
)
_SalixRtpStatsTable_Object = MibTable
salixRtpStatsTable = _SalixRtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    salixRtpStatsTable.setStatus("current")
_SalixRtpStatsEntry_Object = MibTableRow
salixRtpStatsEntry = _SalixRtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1)
)
salixRtpStatsEntry.setIndexNames(
    (0, "SALIX-RTP-MIB", "salixRtpStatsSrcIpAddress"),
    (0, "SALIX-RTP-MIB", "salixRtpStatsSrcPort"),
    (0, "SALIX-RTP-MIB", "salixRtpStatsDestIpAddress"),
    (0, "SALIX-RTP-MIB", "salixRtpStatsDestPort"),
)
if mibBuilder.loadTexts:
    salixRtpStatsEntry.setStatus("current")
_SalixRtpStatsSrcIpAddress_Type = IpAddress
_SalixRtpStatsSrcIpAddress_Object = MibTableColumn
salixRtpStatsSrcIpAddress = _SalixRtpStatsSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 1),
    _SalixRtpStatsSrcIpAddress_Type()
)
salixRtpStatsSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixRtpStatsSrcIpAddress.setStatus("current")


class _SalixRtpStatsSrcPort_Type(Integer32):
    """Custom type salixRtpStatsSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SalixRtpStatsSrcPort_Type.__name__ = "Integer32"
_SalixRtpStatsSrcPort_Object = MibTableColumn
salixRtpStatsSrcPort = _SalixRtpStatsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 2),
    _SalixRtpStatsSrcPort_Type()
)
salixRtpStatsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixRtpStatsSrcPort.setStatus("current")
_SalixRtpStatsDestIpAddress_Type = IpAddress
_SalixRtpStatsDestIpAddress_Object = MibTableColumn
salixRtpStatsDestIpAddress = _SalixRtpStatsDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 3),
    _SalixRtpStatsDestIpAddress_Type()
)
salixRtpStatsDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixRtpStatsDestIpAddress.setStatus("current")


class _SalixRtpStatsDestPort_Type(Integer32):
    """Custom type salixRtpStatsDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SalixRtpStatsDestPort_Type.__name__ = "Integer32"
_SalixRtpStatsDestPort_Object = MibTableColumn
salixRtpStatsDestPort = _SalixRtpStatsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 4),
    _SalixRtpStatsDestPort_Type()
)
salixRtpStatsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salixRtpStatsDestPort.setStatus("current")
_SalixRtpStatsPktsSent_Type = Counter32
_SalixRtpStatsPktsSent_Object = MibTableColumn
salixRtpStatsPktsSent = _SalixRtpStatsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 5),
    _SalixRtpStatsPktsSent_Type()
)
salixRtpStatsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsPktsSent.setStatus("current")
_SalixRtpStatsPktsRecv_Type = Counter32
_SalixRtpStatsPktsRecv_Object = MibTableColumn
salixRtpStatsPktsRecv = _SalixRtpStatsPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 6),
    _SalixRtpStatsPktsRecv_Type()
)
salixRtpStatsPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsPktsRecv.setStatus("current")
_SalixRtpStatsPktsDropped_Type = Counter32
_SalixRtpStatsPktsDropped_Object = MibTableColumn
salixRtpStatsPktsDropped = _SalixRtpStatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 7),
    _SalixRtpStatsPktsDropped_Type()
)
salixRtpStatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsPktsDropped.setStatus("current")
_SalixRtpStatsBytesSent_Type = Counter32
_SalixRtpStatsBytesSent_Object = MibTableColumn
salixRtpStatsBytesSent = _SalixRtpStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 8),
    _SalixRtpStatsBytesSent_Type()
)
salixRtpStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsBytesSent.setStatus("current")
_SalixRtpStatsBytesRecv_Type = Counter32
_SalixRtpStatsBytesRecv_Object = MibTableColumn
salixRtpStatsBytesRecv = _SalixRtpStatsBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 9),
    _SalixRtpStatsBytesRecv_Type()
)
salixRtpStatsBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsBytesRecv.setStatus("current")
_SalixRtpStatsBytesDropped_Type = Counter32
_SalixRtpStatsBytesDropped_Object = MibTableColumn
salixRtpStatsBytesDropped = _SalixRtpStatsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 10),
    _SalixRtpStatsBytesDropped_Type()
)
salixRtpStatsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsBytesDropped.setStatus("current")
_SalixRtpStatsSignalPktsSent_Type = Counter32
_SalixRtpStatsSignalPktsSent_Object = MibTableColumn
salixRtpStatsSignalPktsSent = _SalixRtpStatsSignalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 11),
    _SalixRtpStatsSignalPktsSent_Type()
)
salixRtpStatsSignalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsSignalPktsSent.setStatus("current")
_SalixRtpStatsSignalPktsRecv_Type = Counter32
_SalixRtpStatsSignalPktsRecv_Object = MibTableColumn
salixRtpStatsSignalPktsRecv = _SalixRtpStatsSignalPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 12),
    _SalixRtpStatsSignalPktsRecv_Type()
)
salixRtpStatsSignalPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsSignalPktsRecv.setStatus("current")
_SalixRtpStatsSignalPktsDropped_Type = Counter32
_SalixRtpStatsSignalPktsDropped_Object = MibTableColumn
salixRtpStatsSignalPktsDropped = _SalixRtpStatsSignalPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 13),
    _SalixRtpStatsSignalPktsDropped_Type()
)
salixRtpStatsSignalPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsSignalPktsDropped.setStatus("current")
_SalixRtpStatsSignalBytesRecv_Type = Counter32
_SalixRtpStatsSignalBytesRecv_Object = MibTableColumn
salixRtpStatsSignalBytesRecv = _SalixRtpStatsSignalBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 14),
    _SalixRtpStatsSignalBytesRecv_Type()
)
salixRtpStatsSignalBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsSignalBytesRecv.setStatus("current")
_SalixRtpStatsAudioPktsRecv_Type = Counter32
_SalixRtpStatsAudioPktsRecv_Object = MibTableColumn
salixRtpStatsAudioPktsRecv = _SalixRtpStatsAudioPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 15),
    _SalixRtpStatsAudioPktsRecv_Type()
)
salixRtpStatsAudioPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsAudioPktsRecv.setStatus("current")
_SalixRtpStatsAudioBytesRecv_Type = Counter32
_SalixRtpStatsAudioBytesRecv_Object = MibTableColumn
salixRtpStatsAudioBytesRecv = _SalixRtpStatsAudioBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 16),
    _SalixRtpStatsAudioBytesRecv_Type()
)
salixRtpStatsAudioBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsAudioBytesRecv.setStatus("current")
_SalixRtpStatsEstimatedAvgLatency_Type = Integer32
_SalixRtpStatsEstimatedAvgLatency_Object = MibTableColumn
salixRtpStatsEstimatedAvgLatency = _SalixRtpStatsEstimatedAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 1, 1, 1, 17),
    _SalixRtpStatsEstimatedAvgLatency_Type()
)
salixRtpStatsEstimatedAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixRtpStatsEstimatedAvgLatency.setStatus("current")
_SalixRtpMIBTraps_ObjectIdentity = ObjectIdentity
salixRtpMIBTraps = _SalixRtpMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 2)
)
_SalixRtpMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixRtpMIBTrapPrefix = _SalixRtpMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 2, 0)
)
_SalixRtpMIBCompliance_ObjectIdentity = ObjectIdentity
salixRtpMIBCompliance = _SalixRtpMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3)
)
_SalixRtpGroups_ObjectIdentity = ObjectIdentity
salixRtpGroups = _SalixRtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 1)
)
_SalixRtpCompliances_ObjectIdentity = ObjectIdentity
salixRtpCompliances = _SalixRtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 2)
)

# Managed Objects groups

salixRtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 1, 3)
)
salixRtpGroup.setObjects(
      *(("SALIX-RTP-MIB", "salixRtpStatsPktsSent"),
        ("SALIX-RTP-MIB", "salixRtpStatsPktsRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsPktsDropped"),
        ("SALIX-RTP-MIB", "salixRtpStatsBytesSent"),
        ("SALIX-RTP-MIB", "salixRtpStatsBytesRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsBytesDropped"),
        ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsSent"),
        ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsSignalPktsDropped"),
        ("SALIX-RTP-MIB", "salixRtpStatsSignalBytesRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsAudioPktsRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsAudioBytesRecv"),
        ("SALIX-RTP-MIB", "salixRtpStatsEstimatedAvgLatency"))
)
if mibBuilder.loadTexts:
    salixRtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixRtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixRtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-RTP-MIB",
    **{"salixRtpMIB": salixRtpMIB,
       "salixRtpMIBObjects": salixRtpMIBObjects,
       "salixRtpStatsTable": salixRtpStatsTable,
       "salixRtpStatsEntry": salixRtpStatsEntry,
       "salixRtpStatsSrcIpAddress": salixRtpStatsSrcIpAddress,
       "salixRtpStatsSrcPort": salixRtpStatsSrcPort,
       "salixRtpStatsDestIpAddress": salixRtpStatsDestIpAddress,
       "salixRtpStatsDestPort": salixRtpStatsDestPort,
       "salixRtpStatsPktsSent": salixRtpStatsPktsSent,
       "salixRtpStatsPktsRecv": salixRtpStatsPktsRecv,
       "salixRtpStatsPktsDropped": salixRtpStatsPktsDropped,
       "salixRtpStatsBytesSent": salixRtpStatsBytesSent,
       "salixRtpStatsBytesRecv": salixRtpStatsBytesRecv,
       "salixRtpStatsBytesDropped": salixRtpStatsBytesDropped,
       "salixRtpStatsSignalPktsSent": salixRtpStatsSignalPktsSent,
       "salixRtpStatsSignalPktsRecv": salixRtpStatsSignalPktsRecv,
       "salixRtpStatsSignalPktsDropped": salixRtpStatsSignalPktsDropped,
       "salixRtpStatsSignalBytesRecv": salixRtpStatsSignalBytesRecv,
       "salixRtpStatsAudioPktsRecv": salixRtpStatsAudioPktsRecv,
       "salixRtpStatsAudioBytesRecv": salixRtpStatsAudioBytesRecv,
       "salixRtpStatsEstimatedAvgLatency": salixRtpStatsEstimatedAvgLatency,
       "salixRtpMIBTraps": salixRtpMIBTraps,
       "salixRtpMIBTrapPrefix": salixRtpMIBTrapPrefix,
       "salixRtpMIBCompliance": salixRtpMIBCompliance,
       "salixRtpGroups": salixRtpGroups,
       "salixRtpGroup": salixRtpGroup,
       "salixRtpCompliances": salixRtpCompliances,
       "salixRtpCompliance": salixRtpCompliance}
)
