# SNMP MIB module (NMS-NAT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-NAT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:02 2024
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

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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

nmsNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsNatObjects_ObjectIdentity = ObjectIdentity
nmsNatObjects = _NmsNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1)
)
_NmsNatSessionNumber_Type = Integer32
_NmsNatSessionNumber_Object = MibScalar
nmsNatSessionNumber = _NmsNatSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 1),
    _NmsNatSessionNumber_Type()
)
nmsNatSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionNumber.setStatus("mandatory")
_NmsNatSessionTableJD_Object = MibTable
nmsNatSessionTableJD = _NmsNatSessionTableJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2)
)
if mibBuilder.loadTexts:
    nmsNatSessionTableJD.setStatus("mandatory")
_NmsNatSessionEntryJD_Object = MibTableRow
nmsNatSessionEntryJD = _NmsNatSessionEntryJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1)
)
nmsNatSessionEntryJD.setIndexNames(
    (0, "NMS-NAT", "nmsNatSessionId"),
)
if mibBuilder.loadTexts:
    nmsNatSessionEntryJD.setStatus("mandatory")
_NmsNatSessionIdJD_Type = OctetString
_NmsNatSessionIdJD_Object = MibTableColumn
nmsNatSessionIdJD = _NmsNatSessionIdJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 1),
    _NmsNatSessionIdJD_Type()
)
nmsNatSessionIdJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIdJD.setStatus("current")


class _NmsNatSessionProtocolTypeJD_Type(Integer32):
    """Custom type nmsNatSessionProtocolTypeJD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("other", -1),
          ("tcp", 4),
          ("udp", 2))
    )


_NmsNatSessionProtocolTypeJD_Type.__name__ = "Integer32"
_NmsNatSessionProtocolTypeJD_Object = MibTableColumn
nmsNatSessionProtocolTypeJD = _NmsNatSessionProtocolTypeJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 2),
    _NmsNatSessionProtocolTypeJD_Type()
)
nmsNatSessionProtocolTypeJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionProtocolTypeJD.setStatus("mandatory")


class _NmsNatSessionDirectionJD_Type(Integer32):
    """Custom type nmsNatSessionDirectionJD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_NmsNatSessionDirectionJD_Type.__name__ = "Integer32"
_NmsNatSessionDirectionJD_Object = MibTableColumn
nmsNatSessionDirectionJD = _NmsNatSessionDirectionJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 3),
    _NmsNatSessionDirectionJD_Type()
)
nmsNatSessionDirectionJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionDirectionJD.setStatus("mandatory")
_NmsNatSessionIntAddrJD_Type = OctetString
_NmsNatSessionIntAddrJD_Object = MibTableColumn
nmsNatSessionIntAddrJD = _NmsNatSessionIntAddrJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 4),
    _NmsNatSessionIntAddrJD_Type()
)
nmsNatSessionIntAddrJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIntAddrJD.setStatus("mandatory")
_NmsNatSessionIntPortJD_Type = Integer32
_NmsNatSessionIntPortJD_Object = MibTableColumn
nmsNatSessionIntPortJD = _NmsNatSessionIntPortJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 5),
    _NmsNatSessionIntPortJD_Type()
)
nmsNatSessionIntPortJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIntPortJD.setStatus("mandatory")
_NmsNatSessionExtAddrJD_Type = IpAddress
_NmsNatSessionExtAddrJD_Object = MibTableColumn
nmsNatSessionExtAddrJD = _NmsNatSessionExtAddrJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 6),
    _NmsNatSessionExtAddrJD_Type()
)
nmsNatSessionExtAddrJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionExtAddrJD.setStatus("mandatory")
_NmsNatSessionExtPortJD_Type = Integer32
_NmsNatSessionExtPortJD_Object = MibTableColumn
nmsNatSessionExtPortJD = _NmsNatSessionExtPortJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 7),
    _NmsNatSessionExtPortJD_Type()
)
nmsNatSessionExtPortJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionExtPortJD.setStatus("mandatory")
_NmsNatSessionRemoteAddrJD_Type = IpAddress
_NmsNatSessionRemoteAddrJD_Object = MibTableColumn
nmsNatSessionRemoteAddrJD = _NmsNatSessionRemoteAddrJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 8),
    _NmsNatSessionRemoteAddrJD_Type()
)
nmsNatSessionRemoteAddrJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionRemoteAddrJD.setStatus("current")
_NmsNatSessionRemotePortJD_Type = Integer32
_NmsNatSessionRemotePortJD_Object = MibTableColumn
nmsNatSessionRemotePortJD = _NmsNatSessionRemotePortJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 9),
    _NmsNatSessionRemotePortJD_Type()
)
nmsNatSessionRemotePortJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionRemotePortJD.setStatus("current")
_NmsNatSessionUpTimeJD_Type = TimeTicks
_NmsNatSessionUpTimeJD_Object = MibTableColumn
nmsNatSessionUpTimeJD = _NmsNatSessionUpTimeJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 10),
    _NmsNatSessionUpTimeJD_Type()
)
nmsNatSessionUpTimeJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionUpTimeJD.setStatus("mandatory")
_NmsNatSessionIdletimeJD_Type = TimeTicks
_NmsNatSessionIdletimeJD_Object = MibTableColumn
nmsNatSessionIdletimeJD = _NmsNatSessionIdletimeJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 11),
    _NmsNatSessionIdletimeJD_Type()
)
nmsNatSessionIdletimeJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIdletimeJD.setStatus("current")


class _NmsNatSessionContextJD_Type(DisplayString):
    """Custom type nmsNatSessionContextJD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmsNatSessionContextJD_Type.__name__ = "DisplayString"
_NmsNatSessionContextJD_Object = MibTableColumn
nmsNatSessionContextJD = _NmsNatSessionContextJD_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 2, 1, 12),
    _NmsNatSessionContextJD_Type()
)
nmsNatSessionContextJD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionContextJD.setStatus("mandatory")
_NmsNATLimitedTotalSessions_Type = Integer32
_NmsNATLimitedTotalSessions_Object = MibScalar
nmsNATLimitedTotalSessions = _NmsNATLimitedTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 3),
    _NmsNATLimitedTotalSessions_Type()
)
nmsNATLimitedTotalSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsNATLimitedTotalSessions.setStatus("mandatory")
_NmsNatSessionTable_Object = MibTable
nmsNatSessionTable = _NmsNatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4)
)
if mibBuilder.loadTexts:
    nmsNatSessionTable.setStatus("mandatory")
_NmsNatSessionEntry_Object = MibTableRow
nmsNatSessionEntry = _NmsNatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1)
)
nmsNatSessionEntry.setIndexNames(
    (0, "NMS-NAT", "nmsNatSessionId"),
)
if mibBuilder.loadTexts:
    nmsNatSessionEntry.setStatus("mandatory")
_NmsNatSessionId_Type = OctetString
_NmsNatSessionId_Object = MibTableColumn
nmsNatSessionId = _NmsNatSessionId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 1),
    _NmsNatSessionId_Type()
)
nmsNatSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionId.setStatus("current")
_NmsNatSessionProtocolType_Type = OctetString
_NmsNatSessionProtocolType_Object = MibTableColumn
nmsNatSessionProtocolType = _NmsNatSessionProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 2),
    _NmsNatSessionProtocolType_Type()
)
nmsNatSessionProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionProtocolType.setStatus("mandatory")
_NmsNatSessionDirection_Type = OctetString
_NmsNatSessionDirection_Object = MibTableColumn
nmsNatSessionDirection = _NmsNatSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 3),
    _NmsNatSessionDirection_Type()
)
nmsNatSessionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionDirection.setStatus("mandatory")
_NmsNatSessionIntAddr_Type = OctetString
_NmsNatSessionIntAddr_Object = MibTableColumn
nmsNatSessionIntAddr = _NmsNatSessionIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 4),
    _NmsNatSessionIntAddr_Type()
)
nmsNatSessionIntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIntAddr.setStatus("mandatory")
_NmsNatSessionIntPort_Type = OctetString
_NmsNatSessionIntPort_Object = MibTableColumn
nmsNatSessionIntPort = _NmsNatSessionIntPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 5),
    _NmsNatSessionIntPort_Type()
)
nmsNatSessionIntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIntPort.setStatus("mandatory")
_NmsNatSessionExtAddr_Type = OctetString
_NmsNatSessionExtAddr_Object = MibTableColumn
nmsNatSessionExtAddr = _NmsNatSessionExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 6),
    _NmsNatSessionExtAddr_Type()
)
nmsNatSessionExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionExtAddr.setStatus("mandatory")
_NmsNatSessionExtPort_Type = OctetString
_NmsNatSessionExtPort_Object = MibTableColumn
nmsNatSessionExtPort = _NmsNatSessionExtPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 7),
    _NmsNatSessionExtPort_Type()
)
nmsNatSessionExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionExtPort.setStatus("mandatory")
_NmsNatSessionRemoteAddr_Type = OctetString
_NmsNatSessionRemoteAddr_Object = MibTableColumn
nmsNatSessionRemoteAddr = _NmsNatSessionRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 8),
    _NmsNatSessionRemoteAddr_Type()
)
nmsNatSessionRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionRemoteAddr.setStatus("current")
_NmsNatSessionRemotePort_Type = OctetString
_NmsNatSessionRemotePort_Object = MibTableColumn
nmsNatSessionRemotePort = _NmsNatSessionRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 9),
    _NmsNatSessionRemotePort_Type()
)
nmsNatSessionRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionRemotePort.setStatus("current")
_NmsNatSessionUpTime_Type = OctetString
_NmsNatSessionUpTime_Object = MibTableColumn
nmsNatSessionUpTime = _NmsNatSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 10),
    _NmsNatSessionUpTime_Type()
)
nmsNatSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionUpTime.setStatus("mandatory")
_NmsNatSessionIdletime_Type = OctetString
_NmsNatSessionIdletime_Object = MibTableColumn
nmsNatSessionIdletime = _NmsNatSessionIdletime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 11),
    _NmsNatSessionIdletime_Type()
)
nmsNatSessionIdletime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionIdletime.setStatus("current")
_NmsNatSessionContext_Type = OctetString
_NmsNatSessionContext_Object = MibTableColumn
nmsNatSessionContext = _NmsNatSessionContext_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 12),
    _NmsNatSessionContext_Type()
)
nmsNatSessionContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatSessionContext.setStatus("mandatory")
_NmsNATLimitedHostSessions_Type = OctetString
_NmsNATLimitedHostSessions_Object = MibTableColumn
nmsNATLimitedHostSessions = _NmsNATLimitedHostSessions_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 13),
    _NmsNATLimitedHostSessions_Type()
)
nmsNATLimitedHostSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsNATLimitedHostSessions.setStatus("mandatory")
_NmsNATHostFlows_Type = OctetString
_NmsNATHostFlows_Object = MibTableColumn
nmsNATHostFlows = _NmsNATHostFlows_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 4, 1, 14),
    _NmsNATHostFlows_Type()
)
nmsNATHostFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNATHostFlows.setStatus("mandatory")
_NmsNatCpuPercent_Type = Integer32
_NmsNatCpuPercent_Object = MibScalar
nmsNatCpuPercent = _NmsNatCpuPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 5),
    _NmsNatCpuPercent_Type()
)
nmsNatCpuPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatCpuPercent.setStatus("mandatory")
_NmsNatHeapPercent_Type = Integer32
_NmsNatHeapPercent_Object = MibScalar
nmsNatHeapPercent = _NmsNatHeapPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 6),
    _NmsNatHeapPercent_Type()
)
nmsNatHeapPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatHeapPercent.setStatus("mandatory")
_NmsNatMblkPercent_Type = Integer32
_NmsNatMblkPercent_Object = MibScalar
nmsNatMblkPercent = _NmsNatMblkPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 7),
    _NmsNatMblkPercent_Type()
)
nmsNatMblkPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatMblkPercent.setStatus("mandatory")
_NmsNathostlimitset_Type = Integer32
_NmsNathostlimitset_Object = MibScalar
nmsNathostlimitset = _NmsNathostlimitset_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 8),
    _NmsNathostlimitset_Type()
)
nmsNathostlimitset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsNathostlimitset.setStatus("mandatory")
_NmsNathostlimitcurrent_Type = Integer32
_NmsNathostlimitcurrent_Object = MibScalar
nmsNathostlimitcurrent = _NmsNathostlimitcurrent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 9),
    _NmsNathostlimitcurrent_Type()
)
nmsNathostlimitcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNathostlimitcurrent.setStatus("mandatory")
_NmsNathostlimitenable_Type = Integer32
_NmsNathostlimitenable_Object = MibScalar
nmsNathostlimitenable = _NmsNathostlimitenable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 10),
    _NmsNathostlimitenable_Type()
)
nmsNathostlimitenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsNathostlimitenable.setStatus("mandatory")
_NmsNatIf_Type = OctetString
_NmsNatIf_Object = MibScalar
nmsNatIf = _NmsNatIf_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 100, 1, 11),
    _NmsNatIf_Type()
)
nmsNatIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsNatIf.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-NAT",
    **{"nmsNatMIB": nmsNatMIB,
       "nmsNatObjects": nmsNatObjects,
       "nmsNatSessionNumber": nmsNatSessionNumber,
       "nmsNatSessionTableJD": nmsNatSessionTableJD,
       "nmsNatSessionEntryJD": nmsNatSessionEntryJD,
       "nmsNatSessionIdJD": nmsNatSessionIdJD,
       "nmsNatSessionProtocolTypeJD": nmsNatSessionProtocolTypeJD,
       "nmsNatSessionDirectionJD": nmsNatSessionDirectionJD,
       "nmsNatSessionIntAddrJD": nmsNatSessionIntAddrJD,
       "nmsNatSessionIntPortJD": nmsNatSessionIntPortJD,
       "nmsNatSessionExtAddrJD": nmsNatSessionExtAddrJD,
       "nmsNatSessionExtPortJD": nmsNatSessionExtPortJD,
       "nmsNatSessionRemoteAddrJD": nmsNatSessionRemoteAddrJD,
       "nmsNatSessionRemotePortJD": nmsNatSessionRemotePortJD,
       "nmsNatSessionUpTimeJD": nmsNatSessionUpTimeJD,
       "nmsNatSessionIdletimeJD": nmsNatSessionIdletimeJD,
       "nmsNatSessionContextJD": nmsNatSessionContextJD,
       "nmsNATLimitedTotalSessions": nmsNATLimitedTotalSessions,
       "nmsNatSessionTable": nmsNatSessionTable,
       "nmsNatSessionEntry": nmsNatSessionEntry,
       "nmsNatSessionId": nmsNatSessionId,
       "nmsNatSessionProtocolType": nmsNatSessionProtocolType,
       "nmsNatSessionDirection": nmsNatSessionDirection,
       "nmsNatSessionIntAddr": nmsNatSessionIntAddr,
       "nmsNatSessionIntPort": nmsNatSessionIntPort,
       "nmsNatSessionExtAddr": nmsNatSessionExtAddr,
       "nmsNatSessionExtPort": nmsNatSessionExtPort,
       "nmsNatSessionRemoteAddr": nmsNatSessionRemoteAddr,
       "nmsNatSessionRemotePort": nmsNatSessionRemotePort,
       "nmsNatSessionUpTime": nmsNatSessionUpTime,
       "nmsNatSessionIdletime": nmsNatSessionIdletime,
       "nmsNatSessionContext": nmsNatSessionContext,
       "nmsNATLimitedHostSessions": nmsNATLimitedHostSessions,
       "nmsNATHostFlows": nmsNATHostFlows,
       "nmsNatCpuPercent": nmsNatCpuPercent,
       "nmsNatHeapPercent": nmsNatHeapPercent,
       "nmsNatMblkPercent": nmsNatMblkPercent,
       "nmsNathostlimitset": nmsNathostlimitset,
       "nmsNathostlimitcurrent": nmsNathostlimitcurrent,
       "nmsNathostlimitenable": nmsNathostlimitenable,
       "nmsNatIf": nmsNatIf}
)
