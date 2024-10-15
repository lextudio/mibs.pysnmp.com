# SNMP MIB module (VERTICAL16-IPTEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL16-IPTEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:26 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_Iptel_ObjectIdentity = ObjectIdentity
iptel = _Iptel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 16)
)
_IptelTrunkSize_Type = Integer32
_IptelTrunkSize_Object = MibScalar
iptelTrunkSize = _IptelTrunkSize_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 1),
    _IptelTrunkSize_Type()
)
iptelTrunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iptelTrunkSize.setStatus("mandatory")
_IpTelTrunkSummary_Object = MibTable
ipTelTrunkSummary = _IpTelTrunkSummary_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2)
)
if mibBuilder.loadTexts:
    ipTelTrunkSummary.setStatus("mandatory")
_IpTelTrunkInfo_Object = MibTableRow
ipTelTrunkInfo = _IpTelTrunkInfo_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1)
)
ipTelTrunkInfo.setIndexNames(
    (0, "VERTICAL16-IPTEL-MIB", "TrunkIndex"),
)
if mibBuilder.loadTexts:
    ipTelTrunkInfo.setStatus("mandatory")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("mandatory")


class _TrunkState_Type(Integer32):
    """Custom type trunkState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("connected", 6),
          ("disconnecting", 7),
          ("idle", 3),
          ("incoming", 5),
          ("initializing", 2),
          ("not-configured", 0),
          ("out-of-service", 1),
          ("outgoing", 4))
    )


_TrunkState_Type.__name__ = "Integer32"
_TrunkState_Object = MibTableColumn
trunkState = _TrunkState_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 2),
    _TrunkState_Type()
)
trunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkState.setStatus("mandatory")
_CalledParty_Type = DisplayString
_CalledParty_Object = MibTableColumn
calledParty = _CalledParty_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 3),
    _CalledParty_Type()
)
calledParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calledParty.setStatus("mandatory")
_CallingParty_Type = DisplayString
_CallingParty_Object = MibTableColumn
callingParty = _CallingParty_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 4),
    _CallingParty_Type()
)
callingParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callingParty.setStatus("mandatory")
_RemoteGateway_Type = DisplayString
_RemoteGateway_Object = MibTableColumn
remoteGateway = _RemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 5),
    _RemoteGateway_Type()
)
remoteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteGateway.setStatus("mandatory")
_LocalAlarmThreshold_Type = Integer32
_LocalAlarmThreshold_Object = MibTableColumn
localAlarmThreshold = _LocalAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 6),
    _LocalAlarmThreshold_Type()
)
localAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localAlarmThreshold.setStatus("mandatory")
_RemoteAlarmThreshold_Type = Integer32
_RemoteAlarmThreshold_Object = MibTableColumn
remoteAlarmThreshold = _RemoteAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2338, 16, 2, 1, 7),
    _RemoteAlarmThreshold_Type()
)
remoteAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlarmThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ipTelReconfigComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 64)
)
ipTelReconfigComplete.setObjects(
    ("VERTICAL16-IPTEL-MIB", "iptelTrunkSize")
)
if mibBuilder.loadTexts:
    ipTelReconfigComplete.setStatus(
        ""
    )

ipTelTrunkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 65)
)
ipTelTrunkFailure.setObjects(
    ("VERTICAL16-IPTEL-MIB", "trunkIndex")
)
if mibBuilder.loadTexts:
    ipTelTrunkFailure.setStatus(
        ""
    )

ipTelTrunkAlarmInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 66)
)
ipTelTrunkAlarmInfo.setObjects(
      *(("VERTICAL16-IPTEL-MIB", "trunkIndex"),
        ("VERTICAL16-IPTEL-MIB", "localAlarmThreshold"),
        ("VERTICAL16-IPTEL-MIB", "remoteAlarmThreshold"))
)
if mibBuilder.loadTexts:
    ipTelTrunkAlarmInfo.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL16-IPTEL-MIB",
    **{"vertical": vertical,
       "ipTelReconfigComplete": ipTelReconfigComplete,
       "ipTelTrunkFailure": ipTelTrunkFailure,
       "ipTelTrunkAlarmInfo": ipTelTrunkAlarmInfo,
       "iptel": iptel,
       "iptelTrunkSize": iptelTrunkSize,
       "ipTelTrunkSummary": ipTelTrunkSummary,
       "ipTelTrunkInfo": ipTelTrunkInfo,
       "trunkIndex": trunkIndex,
       "trunkState": trunkState,
       "calledParty": calledParty,
       "callingParty": callingParty,
       "remoteGateway": remoteGateway,
       "localAlarmThreshold": localAlarmThreshold,
       "remoteAlarmThreshold": remoteAlarmThreshold}
)
