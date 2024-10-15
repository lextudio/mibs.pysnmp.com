# SNMP MIB module (RDN-PKTCABLE-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-PKTCABLE-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:06 2024
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

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rdnPacketCableGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7)
)
rdnPacketCableGroup.setRevisions(
        ("2008-10-06 00:00",
         "2008-08-08 00:00",
         "2007-10-22 00:00",
         "2006-05-24 00:00",
         "2006-05-24 00:00",
         "2006-02-15 00:00",
         "2006-01-24 00:00",
         "2003-11-05 00:00",
         "2003-10-24 00:00",
         "2003-05-12 00:00",
         "2002-09-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BcidDataArray(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )



# MIB Managed Objects in the order of their OIDs

_RdnPktDQoSConfigGroup_ObjectIdentity = ObjectIdentity
rdnPktDQoSConfigGroup = _RdnPktDQoSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1)
)
_RdnPktDQoSCOPSStatus_Type = TruthValue
_RdnPktDQoSCOPSStatus_Object = MibScalar
rdnPktDQoSCOPSStatus = _RdnPktDQoSCOPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 1),
    _RdnPktDQoSCOPSStatus_Type()
)
rdnPktDQoSCOPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSCOPSStatus.setStatus("current")
_RdnPktDQoSCMTSIp_Type = IpAddress
_RdnPktDQoSCMTSIp_Object = MibScalar
rdnPktDQoSCMTSIp = _RdnPktDQoSCMTSIp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 2),
    _RdnPktDQoSCMTSIp_Type()
)
rdnPktDQoSCMTSIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSCMTSIp.setStatus("current")


class _RdnPktDQoSPEPID_Type(DisplayString):
    """Custom type rdnPktDQoSPEPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RdnPktDQoSPEPID_Type.__name__ = "DisplayString"
_RdnPktDQoSPEPID_Object = MibScalar
rdnPktDQoSPEPID = _RdnPktDQoSPEPID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 3),
    _RdnPktDQoSPEPID_Type()
)
rdnPktDQoSPEPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSPEPID.setStatus("current")


class _RdnPktDQoSClientAccpTimer_Type(Integer32):
    """Custom type rdnPktDQoSClientAccpTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600000),
    )


_RdnPktDQoSClientAccpTimer_Type.__name__ = "Integer32"
_RdnPktDQoSClientAccpTimer_Object = MibScalar
rdnPktDQoSClientAccpTimer = _RdnPktDQoSClientAccpTimer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 4),
    _RdnPktDQoSClientAccpTimer_Type()
)
rdnPktDQoSClientAccpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSClientAccpTimer.setStatus("current")


class _RdnPktDQoST0Timer_Type(Integer32):
    """Custom type rdnPktDQoST0Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RdnPktDQoST0Timer_Type.__name__ = "Integer32"
_RdnPktDQoST0Timer_Object = MibScalar
rdnPktDQoST0Timer = _RdnPktDQoST0Timer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 5),
    _RdnPktDQoST0Timer_Type()
)
rdnPktDQoST0Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoST0Timer.setStatus("current")


class _RdnPktDQoST1Timer_Type(Integer32):
    """Custom type rdnPktDQoST1Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RdnPktDQoST1Timer_Type.__name__ = "Integer32"
_RdnPktDQoST1Timer_Object = MibScalar
rdnPktDQoST1Timer = _RdnPktDQoST1Timer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 6),
    _RdnPktDQoST1Timer_Type()
)
rdnPktDQoST1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoST1Timer.setStatus("current")
_RdnPktDQoST3Timer_Type = Integer32
_RdnPktDQoST3Timer_Object = MibScalar
rdnPktDQoST3Timer = _RdnPktDQoST3Timer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 7),
    _RdnPktDQoST3Timer_Type()
)
rdnPktDQoST3Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoST3Timer.setStatus("current")
_RdnPktDQoST6Timer_Type = Integer32
_RdnPktDQoST6Timer_Object = MibScalar
rdnPktDQoST6Timer = _RdnPktDQoST6Timer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 8),
    _RdnPktDQoST6Timer_Type()
)
rdnPktDQoST6Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoST6Timer.setStatus("current")


class _RdnPktDQoSCopsTrapEnable_Type(Integer32):
    """Custom type rdnPktDQoSCopsTrapEnable based on Integer32"""
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


_RdnPktDQoSCopsTrapEnable_Type.__name__ = "Integer32"
_RdnPktDQoSCopsTrapEnable_Object = MibScalar
rdnPktDQoSCopsTrapEnable = _RdnPktDQoSCopsTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 9),
    _RdnPktDQoSCopsTrapEnable_Type()
)
rdnPktDQoSCopsTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsTrapEnable.setStatus("current")


class _RdnPktDQoSResReqTrapEnable_Type(Integer32):
    """Custom type rdnPktDQoSResReqTrapEnable based on Integer32"""
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


_RdnPktDQoSResReqTrapEnable_Type.__name__ = "Integer32"
_RdnPktDQoSResReqTrapEnable_Object = MibScalar
rdnPktDQoSResReqTrapEnable = _RdnPktDQoSResReqTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 10),
    _RdnPktDQoSResReqTrapEnable_Type()
)
rdnPktDQoSResReqTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSResReqTrapEnable.setStatus("current")


class _RdnPktESTrapEnable_Type(Integer32):
    """Custom type rdnPktESTrapEnable based on Integer32"""
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


_RdnPktESTrapEnable_Type.__name__ = "Integer32"
_RdnPktESTrapEnable_Object = MibScalar
rdnPktESTrapEnable = _RdnPktESTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 11),
    _RdnPktESTrapEnable_Type()
)
rdnPktESTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktESTrapEnable.setStatus("current")


class _RdnPktESEnable_Type(Integer32):
    """Custom type rdnPktESEnable based on Integer32"""
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


_RdnPktESEnable_Type.__name__ = "Integer32"
_RdnPktESEnable_Object = MibScalar
rdnPktESEnable = _RdnPktESEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 12),
    _RdnPktESEnable_Type()
)
rdnPktESEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktESEnable.setStatus("current")


class _RdnPktDQoSEmergencyTrapEnable_Type(Integer32):
    """Custom type rdnPktDQoSEmergencyTrapEnable based on Integer32"""
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


_RdnPktDQoSEmergencyTrapEnable_Type.__name__ = "Integer32"
_RdnPktDQoSEmergencyTrapEnable_Object = MibScalar
rdnPktDQoSEmergencyTrapEnable = _RdnPktDQoSEmergencyTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 13),
    _RdnPktDQoSEmergencyTrapEnable_Type()
)
rdnPktDQoSEmergencyTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyTrapEnable.setStatus("current")


class _RdnPktDQoSEmergencyPreemption_Type(Integer32):
    """Custom type rdnPktDQoSEmergencyPreemption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("most-recent", 1),
          ("oldest", 2),
          ("random", 3))
    )


_RdnPktDQoSEmergencyPreemption_Type.__name__ = "Integer32"
_RdnPktDQoSEmergencyPreemption_Object = MibScalar
rdnPktDQoSEmergencyPreemption = _RdnPktDQoSEmergencyPreemption_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 14),
    _RdnPktDQoSEmergencyPreemption_Type()
)
rdnPktDQoSEmergencyPreemption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyPreemption.setStatus("current")


class _RdnPktEMRKSFailureTrapEnable_Type(Integer32):
    """Custom type rdnPktEMRKSFailureTrapEnable based on Integer32"""
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


_RdnPktEMRKSFailureTrapEnable_Type.__name__ = "Integer32"
_RdnPktEMRKSFailureTrapEnable_Object = MibScalar
rdnPktEMRKSFailureTrapEnable = _RdnPktEMRKSFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 15),
    _RdnPktEMRKSFailureTrapEnable_Type()
)
rdnPktEMRKSFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktEMRKSFailureTrapEnable.setStatus("current")


class _RdnPktDQoSDscp_Type(Integer32):
    """Custom type rdnPktDQoSDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RdnPktDQoSDscp_Type.__name__ = "Integer32"
_RdnPktDQoSDscp_Object = MibScalar
rdnPktDQoSDscp = _RdnPktDQoSDscp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 16),
    _RdnPktDQoSDscp_Type()
)
rdnPktDQoSDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktDQoSDscp.setStatus("current")


class _RdnPktMMDscp_Type(Integer32):
    """Custom type rdnPktMMDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RdnPktMMDscp_Type.__name__ = "Integer32"
_RdnPktMMDscp_Object = MibScalar
rdnPktMMDscp = _RdnPktMMDscp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 17),
    _RdnPktMMDscp_Type()
)
rdnPktMMDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktMMDscp.setStatus("current")


class _RdnPktEMDscp_Type(Integer32):
    """Custom type rdnPktEMDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RdnPktEMDscp_Type.__name__ = "Integer32"
_RdnPktEMDscp_Object = MibScalar
rdnPktEMDscp = _RdnPktEMDscp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 18),
    _RdnPktEMDscp_Type()
)
rdnPktEMDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktEMDscp.setStatus("current")


class _RdnPktESCccDscp_Type(Integer32):
    """Custom type rdnPktESCccDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RdnPktESCccDscp_Type.__name__ = "Integer32"
_RdnPktESCccDscp_Object = MibScalar
rdnPktESCccDscp = _RdnPktESCccDscp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 1, 19),
    _RdnPktESCccDscp_Type()
)
rdnPktESCccDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktESCccDscp.setStatus("current")
_RdnGateStatsTable_Object = MibTable
rdnGateStatsTable = _RdnGateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2)
)
if mibBuilder.loadTexts:
    rdnGateStatsTable.setStatus("current")
_RdnGateStatsEntry_Object = MibTableRow
rdnGateStatsEntry = _RdnGateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1)
)
rdnGateStatsEntry.setIndexNames(
    (0, "RDN-PKTCABLE-GROUP-MIB", "rdnGateId"),
)
if mibBuilder.loadTexts:
    rdnGateStatsEntry.setStatus("current")
_RdnGateId_Type = Integer32
_RdnGateId_Object = MibTableColumn
rdnGateId = _RdnGateId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 1),
    _RdnGateId_Type()
)
rdnGateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnGateId.setStatus("current")


class _RdnGateStatsState_Type(Integer32):
    """Custom type rdnGateStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("allocated", 2),
          ("authorized", 3),
          ("committed", 7),
          ("committedRecovery", 8),
          ("idle", 0),
          ("numOfStates", 9),
          ("reserved", 4),
          ("start", 1))
    )


_RdnGateStatsState_Type.__name__ = "Integer32"
_RdnGateStatsState_Object = MibTableColumn
rdnGateStatsState = _RdnGateStatsState_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 2),
    _RdnGateStatsState_Type()
)
rdnGateStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsState.setStatus("current")
_RdnGateStatsSubscriberIP_Type = IpAddress
_RdnGateStatsSubscriberIP_Object = MibTableColumn
rdnGateStatsSubscriberIP = _RdnGateStatsSubscriberIP_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 3),
    _RdnGateStatsSubscriberIP_Type()
)
rdnGateStatsSubscriberIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsSubscriberIP.setStatus("current")
_RdnGateStatsRKSPrimaryAddr_Type = IpAddress
_RdnGateStatsRKSPrimaryAddr_Object = MibTableColumn
rdnGateStatsRKSPrimaryAddr = _RdnGateStatsRKSPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 4),
    _RdnGateStatsRKSPrimaryAddr_Type()
)
rdnGateStatsRKSPrimaryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsRKSPrimaryAddr.setStatus("current")
_RdnGateStatsRKSPrimaryPort_Type = Integer32
_RdnGateStatsRKSPrimaryPort_Object = MibTableColumn
rdnGateStatsRKSPrimaryPort = _RdnGateStatsRKSPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 5),
    _RdnGateStatsRKSPrimaryPort_Type()
)
rdnGateStatsRKSPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsRKSPrimaryPort.setStatus("current")
_RdnGateStatsRKSSecondaryAddr_Type = IpAddress
_RdnGateStatsRKSSecondaryAddr_Object = MibTableColumn
rdnGateStatsRKSSecondaryAddr = _RdnGateStatsRKSSecondaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 6),
    _RdnGateStatsRKSSecondaryAddr_Type()
)
rdnGateStatsRKSSecondaryAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsRKSSecondaryAddr.setStatus("current")
_RdnGateStatsRKSSecondaryPort_Type = Integer32
_RdnGateStatsRKSSecondaryPort_Object = MibTableColumn
rdnGateStatsRKSSecondaryPort = _RdnGateStatsRKSSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 7),
    _RdnGateStatsRKSSecondaryPort_Type()
)
rdnGateStatsRKSSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsRKSSecondaryPort.setStatus("current")
_RdnGateStatsEventFlag_Type = Integer32
_RdnGateStatsEventFlag_Object = MibTableColumn
rdnGateStatsEventFlag = _RdnGateStatsEventFlag_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 8),
    _RdnGateStatsEventFlag_Type()
)
rdnGateStatsEventFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsEventFlag.setStatus("current")
_RdnGateStatsBillingCorrelationID_Type = BcidDataArray
_RdnGateStatsBillingCorrelationID_Object = MibTableColumn
rdnGateStatsBillingCorrelationID = _RdnGateStatsBillingCorrelationID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 9),
    _RdnGateStatsBillingCorrelationID_Type()
)
rdnGateStatsBillingCorrelationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsBillingCorrelationID.setStatus("current")
_RdnGateStatsDurationTime_Type = DisplayString
_RdnGateStatsDurationTime_Object = MibTableColumn
rdnGateStatsDurationTime = _RdnGateStatsDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 10),
    _RdnGateStatsDurationTime_Type()
)
rdnGateStatsDurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsDurationTime.setStatus("current")
_RdnGateStatsSlotNum_Type = Integer32
_RdnGateStatsSlotNum_Object = MibTableColumn
rdnGateStatsSlotNum = _RdnGateStatsSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 11),
    _RdnGateStatsSlotNum_Type()
)
rdnGateStatsSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsSlotNum.setStatus("current")
_RdnGateStatsUpSfid_Type = Integer32
_RdnGateStatsUpSfid_Object = MibTableColumn
rdnGateStatsUpSfid = _RdnGateStatsUpSfid_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 12),
    _RdnGateStatsUpSfid_Type()
)
rdnGateStatsUpSfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsUpSfid.setStatus("current")
_RdnGateStatsDnSfid_Type = Integer32
_RdnGateStatsDnSfid_Object = MibTableColumn
rdnGateStatsDnSfid = _RdnGateStatsDnSfid_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 13),
    _RdnGateStatsDnSfid_Type()
)
rdnGateStatsDnSfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsDnSfid.setStatus("current")
_RdnGateStatsResourceID_Type = Integer32
_RdnGateStatsResourceID_Object = MibTableColumn
rdnGateStatsResourceID = _RdnGateStatsResourceID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 14),
    _RdnGateStatsResourceID_Type()
)
rdnGateStatsResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsResourceID.setStatus("current")
_RdnGateStatsESCDCAddr_Type = IpAddress
_RdnGateStatsESCDCAddr_Object = MibTableColumn
rdnGateStatsESCDCAddr = _RdnGateStatsESCDCAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 15),
    _RdnGateStatsESCDCAddr_Type()
)
rdnGateStatsESCDCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESCDCAddr.setStatus("current")
_RdnGateStatsESCDCPort_Type = Integer32
_RdnGateStatsESCDCPort_Object = MibTableColumn
rdnGateStatsESCDCPort = _RdnGateStatsESCDCPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 16),
    _RdnGateStatsESCDCPort_Type()
)
rdnGateStatsESCDCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESCDCPort.setStatus("current")
_RdnGateStatsESFlag_Type = Integer32
_RdnGateStatsESFlag_Object = MibTableColumn
rdnGateStatsESFlag = _RdnGateStatsESFlag_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 17),
    _RdnGateStatsESFlag_Type()
)
rdnGateStatsESFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESFlag.setStatus("current")
_RdnGateStatsESCCCAddr_Type = IpAddress
_RdnGateStatsESCCCAddr_Object = MibTableColumn
rdnGateStatsESCCCAddr = _RdnGateStatsESCCCAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 18),
    _RdnGateStatsESCCCAddr_Type()
)
rdnGateStatsESCCCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESCCCAddr.setStatus("current")
_RdnGateStatsESCCCPort_Type = Integer32
_RdnGateStatsESCCCPort_Object = MibTableColumn
rdnGateStatsESCCCPort = _RdnGateStatsESCCCPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 19),
    _RdnGateStatsESCCCPort_Type()
)
rdnGateStatsESCCCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESCCCPort.setStatus("current")
_RdnGateStatsESCCCId_Type = Integer32
_RdnGateStatsESCCCId_Object = MibTableColumn
rdnGateStatsESCCCId = _RdnGateStatsESCCCId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 2, 1, 20),
    _RdnGateStatsESCCCId_Type()
)
rdnGateStatsESCCCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateStatsESCCCId.setStatus("current")
_RdnGateSpecTable_Object = MibTable
rdnGateSpecTable = _RdnGateSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3)
)
if mibBuilder.loadTexts:
    rdnGateSpecTable.setStatus("current")
_RdnGateSpecEntry_Object = MibTableRow
rdnGateSpecEntry = _RdnGateSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1)
)
rdnGateSpecEntry.setIndexNames(
    (0, "RDN-PKTCABLE-GROUP-MIB", "rdnGateId"),
    (0, "RDN-PKTCABLE-GROUP-MIB", "rdnGateDirection"),
)
if mibBuilder.loadTexts:
    rdnGateSpecEntry.setStatus("current")


class _RdnGateDirection_Type(Integer32):
    """Custom type rdnGateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("upstream", 1))
    )


_RdnGateDirection_Type.__name__ = "Integer32"
_RdnGateDirection_Object = MibTableColumn
rdnGateDirection = _RdnGateDirection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 2),
    _RdnGateDirection_Type()
)
rdnGateDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnGateDirection.setStatus("current")
_RdnGateSpecProtocol_Type = Integer32
_RdnGateSpecProtocol_Object = MibTableColumn
rdnGateSpecProtocol = _RdnGateSpecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 3),
    _RdnGateSpecProtocol_Type()
)
rdnGateSpecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecProtocol.setStatus("current")
_RdnGateSpecSourceIP_Type = IpAddress
_RdnGateSpecSourceIP_Object = MibTableColumn
rdnGateSpecSourceIP = _RdnGateSpecSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 4),
    _RdnGateSpecSourceIP_Type()
)
rdnGateSpecSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecSourceIP.setStatus("current")
_RdnGateSpecSourcePort_Type = Integer32
_RdnGateSpecSourcePort_Object = MibTableColumn
rdnGateSpecSourcePort = _RdnGateSpecSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 5),
    _RdnGateSpecSourcePort_Type()
)
rdnGateSpecSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecSourcePort.setStatus("current")
_RdnGateSpecDestIP_Type = IpAddress
_RdnGateSpecDestIP_Object = MibTableColumn
rdnGateSpecDestIP = _RdnGateSpecDestIP_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 6),
    _RdnGateSpecDestIP_Type()
)
rdnGateSpecDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecDestIP.setStatus("current")
_RdnGateSpecDestPort_Type = Integer32
_RdnGateSpecDestPort_Object = MibTableColumn
rdnGateSpecDestPort = _RdnGateSpecDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 7),
    _RdnGateSpecDestPort_Type()
)
rdnGateSpecDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecDestPort.setStatus("current")
_RdnGateSpecServiceFlowID_Type = Integer32
_RdnGateSpecServiceFlowID_Object = MibTableColumn
rdnGateSpecServiceFlowID = _RdnGateSpecServiceFlowID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 8),
    _RdnGateSpecServiceFlowID_Type()
)
rdnGateSpecServiceFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecServiceFlowID.setStatus("current")


class _RdnGateSpecFlags_Type(Integer32):
    """Custom type rdnGateSpecFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoCommit", 1),
          ("commitNotAllowed", 2))
    )


_RdnGateSpecFlags_Type.__name__ = "Integer32"
_RdnGateSpecFlags_Object = MibTableColumn
rdnGateSpecFlags = _RdnGateSpecFlags_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 9),
    _RdnGateSpecFlags_Type()
)
rdnGateSpecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecFlags.setStatus("current")


class _RdnGateSpecSessionClass_Type(Integer32):
    """Custom type rdnGateSpecSessionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 2),
          ("normalPriority", 1),
          ("unspecified", 255))
    )


_RdnGateSpecSessionClass_Type.__name__ = "Integer32"
_RdnGateSpecSessionClass_Object = MibTableColumn
rdnGateSpecSessionClass = _RdnGateSpecSessionClass_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 10),
    _RdnGateSpecSessionClass_Type()
)
rdnGateSpecSessionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecSessionClass.setStatus("current")
_RdnGateSpecDiffServCode_Type = Integer32
_RdnGateSpecDiffServCode_Object = MibTableColumn
rdnGateSpecDiffServCode = _RdnGateSpecDiffServCode_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 11),
    _RdnGateSpecDiffServCode_Type()
)
rdnGateSpecDiffServCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecDiffServCode.setStatus("current")
_RdnGateSpecT1Timer_Type = Integer32
_RdnGateSpecT1Timer_Object = MibTableColumn
rdnGateSpecT1Timer = _RdnGateSpecT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 12),
    _RdnGateSpecT1Timer_Type()
)
rdnGateSpecT1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecT1Timer.setStatus("current")
_RdnGateSpecTokenBuckRate_Type = Integer32
_RdnGateSpecTokenBuckRate_Object = MibTableColumn
rdnGateSpecTokenBuckRate = _RdnGateSpecTokenBuckRate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 13),
    _RdnGateSpecTokenBuckRate_Type()
)
rdnGateSpecTokenBuckRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecTokenBuckRate.setStatus("current")
_RdnGateSpecBuckSize_Type = Integer32
_RdnGateSpecBuckSize_Object = MibTableColumn
rdnGateSpecBuckSize = _RdnGateSpecBuckSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 14),
    _RdnGateSpecBuckSize_Type()
)
rdnGateSpecBuckSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecBuckSize.setStatus("current")
_RdnGateSpecPeakDataRate_Type = Integer32
_RdnGateSpecPeakDataRate_Object = MibTableColumn
rdnGateSpecPeakDataRate = _RdnGateSpecPeakDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 15),
    _RdnGateSpecPeakDataRate_Type()
)
rdnGateSpecPeakDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecPeakDataRate.setStatus("current")
_RdnGateSpecMinPoliceUnit_Type = Integer32
_RdnGateSpecMinPoliceUnit_Object = MibTableColumn
rdnGateSpecMinPoliceUnit = _RdnGateSpecMinPoliceUnit_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 16),
    _RdnGateSpecMinPoliceUnit_Type()
)
rdnGateSpecMinPoliceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecMinPoliceUnit.setStatus("current")
_RdnGateSpecMaxPacketSize_Type = Integer32
_RdnGateSpecMaxPacketSize_Object = MibTableColumn
rdnGateSpecMaxPacketSize = _RdnGateSpecMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 17),
    _RdnGateSpecMaxPacketSize_Type()
)
rdnGateSpecMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecMaxPacketSize.setStatus("current")
_RdnGateSpecReserveRate_Type = Integer32
_RdnGateSpecReserveRate_Object = MibTableColumn
rdnGateSpecReserveRate = _RdnGateSpecReserveRate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 18),
    _RdnGateSpecReserveRate_Type()
)
rdnGateSpecReserveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSpecReserveRate.setStatus("current")
_RdnGateSlackTerm_Type = Integer32
_RdnGateSlackTerm_Object = MibTableColumn
rdnGateSlackTerm = _RdnGateSlackTerm_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 3, 1, 19),
    _RdnGateSlackTerm_Type()
)
rdnGateSlackTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnGateSlackTerm.setStatus("current")
_RdnPktCMSIpConfigTable_Object = MibTable
rdnPktCMSIpConfigTable = _RdnPktCMSIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 4)
)
if mibBuilder.loadTexts:
    rdnPktCMSIpConfigTable.setStatus("current")
_RdnPktCMSIpConfigEntry_Object = MibTableRow
rdnPktCMSIpConfigEntry = _RdnPktCMSIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 4, 1)
)
rdnPktCMSIpConfigEntry.setIndexNames(
    (0, "RDN-PKTCABLE-GROUP-MIB", "rdnPktCMSIpAddressIndex"),
)
if mibBuilder.loadTexts:
    rdnPktCMSIpConfigEntry.setStatus("current")
_RdnPktCMSIpAddressIndex_Type = Integer32
_RdnPktCMSIpAddressIndex_Object = MibTableColumn
rdnPktCMSIpAddressIndex = _RdnPktCMSIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 4, 1, 1),
    _RdnPktCMSIpAddressIndex_Type()
)
rdnPktCMSIpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnPktCMSIpAddressIndex.setStatus("current")
_RdnPktCMSIpAddress_Type = IpAddress
_RdnPktCMSIpAddress_Object = MibTableColumn
rdnPktCMSIpAddress = _RdnPktCMSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 4, 1, 2),
    _RdnPktCMSIpAddress_Type()
)
rdnPktCMSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnPktCMSIpAddress.setStatus("current")
_RdnPktDQoSStatsTable_Object = MibTable
rdnPktDQoSStatsTable = _RdnPktDQoSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6)
)
if mibBuilder.loadTexts:
    rdnPktDQoSStatsTable.setStatus("current")
_RdnPktDQoSStatsEntry_Object = MibTableRow
rdnPktDQoSStatsEntry = _RdnPktDQoSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1)
)
rdnPktDQoSStatsEntry.setIndexNames(
    (0, "RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCopsHandle"),
)
if mibBuilder.loadTexts:
    rdnPktDQoSStatsEntry.setStatus("current")
_RdnPktDQoSIpAddress_Type = IpAddress
_RdnPktDQoSIpAddress_Object = MibTableColumn
rdnPktDQoSIpAddress = _RdnPktDQoSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 1),
    _RdnPktDQoSIpAddress_Type()
)
rdnPktDQoSIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSIpAddress.setStatus("current")
_RdnPktDQoSCopsHandle_Type = Integer32
_RdnPktDQoSCopsHandle_Object = MibTableColumn
rdnPktDQoSCopsHandle = _RdnPktDQoSCopsHandle_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 2),
    _RdnPktDQoSCopsHandle_Type()
)
rdnPktDQoSCopsHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsHandle.setStatus("current")


class _RdnPktDQoSCopsStatus_Type(Integer32):
    """Custom type rdnPktDQoSCopsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 2),
          ("opening", 1))
    )


_RdnPktDQoSCopsStatus_Type.__name__ = "Integer32"
_RdnPktDQoSCopsStatus_Object = MibTableColumn
rdnPktDQoSCopsStatus = _RdnPktDQoSCopsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 3),
    _RdnPktDQoSCopsStatus_Type()
)
rdnPktDQoSCopsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsStatus.setStatus("current")
_RdnPktDQoSCopsConnected_Type = Integer32
_RdnPktDQoSCopsConnected_Object = MibTableColumn
rdnPktDQoSCopsConnected = _RdnPktDQoSCopsConnected_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 4),
    _RdnPktDQoSCopsConnected_Type()
)
rdnPktDQoSCopsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsConnected.setStatus("current")
_RdnPktDQoSCopsTerminated_Type = Integer32
_RdnPktDQoSCopsTerminated_Object = MibTableColumn
rdnPktDQoSCopsTerminated = _RdnPktDQoSCopsTerminated_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 5),
    _RdnPktDQoSCopsTerminated_Type()
)
rdnPktDQoSCopsTerminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsTerminated.setStatus("current")
_RdnPktDQoSCopsKASent_Type = Integer32
_RdnPktDQoSCopsKASent_Object = MibTableColumn
rdnPktDQoSCopsKASent = _RdnPktDQoSCopsKASent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 6),
    _RdnPktDQoSCopsKASent_Type()
)
rdnPktDQoSCopsKASent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsKASent.setStatus("current")
_RdnPktDQoSCopsKARcvd_Type = Integer32
_RdnPktDQoSCopsKARcvd_Object = MibTableColumn
rdnPktDQoSCopsKARcvd = _RdnPktDQoSCopsKARcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 7),
    _RdnPktDQoSCopsKARcvd_Type()
)
rdnPktDQoSCopsKARcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsKARcvd.setStatus("current")
_RdnPktDQoSKATimeout_Type = Integer32
_RdnPktDQoSKATimeout_Object = MibTableColumn
rdnPktDQoSKATimeout = _RdnPktDQoSKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 8),
    _RdnPktDQoSKATimeout_Type()
)
rdnPktDQoSKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSKATimeout.setStatus("current")
_RdnPktDQoST0Timeout_Type = Integer32
_RdnPktDQoST0Timeout_Object = MibTableColumn
rdnPktDQoST0Timeout = _RdnPktDQoST0Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 9),
    _RdnPktDQoST0Timeout_Type()
)
rdnPktDQoST0Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoST0Timeout.setStatus("current")
_RdnPktDQoST1Timeout_Type = Integer32
_RdnPktDQoST1Timeout_Object = MibTableColumn
rdnPktDQoST1Timeout = _RdnPktDQoST1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 10),
    _RdnPktDQoST1Timeout_Type()
)
rdnPktDQoST1Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoST1Timeout.setStatus("current")
_RdnPktDQoSGateAllocCount_Type = Integer32
_RdnPktDQoSGateAllocCount_Object = MibTableColumn
rdnPktDQoSGateAllocCount = _RdnPktDQoSGateAllocCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 11),
    _RdnPktDQoSGateAllocCount_Type()
)
rdnPktDQoSGateAllocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateAllocCount.setStatus("current")
_RdnPktDQoSGateAllocAckCount_Type = Integer32
_RdnPktDQoSGateAllocAckCount_Object = MibTableColumn
rdnPktDQoSGateAllocAckCount = _RdnPktDQoSGateAllocAckCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 12),
    _RdnPktDQoSGateAllocAckCount_Type()
)
rdnPktDQoSGateAllocAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateAllocAckCount.setStatus("current")
_RdnPktDQoSGateAllocErrCount_Type = Integer32
_RdnPktDQoSGateAllocErrCount_Object = MibTableColumn
rdnPktDQoSGateAllocErrCount = _RdnPktDQoSGateAllocErrCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 13),
    _RdnPktDQoSGateAllocErrCount_Type()
)
rdnPktDQoSGateAllocErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateAllocErrCount.setStatus("current")
_RdnPktDQoSGateSetCount_Type = Integer32
_RdnPktDQoSGateSetCount_Object = MibTableColumn
rdnPktDQoSGateSetCount = _RdnPktDQoSGateSetCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 14),
    _RdnPktDQoSGateSetCount_Type()
)
rdnPktDQoSGateSetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateSetCount.setStatus("current")
_RdnPktDQoSGateSetAckCount_Type = Integer32
_RdnPktDQoSGateSetAckCount_Object = MibTableColumn
rdnPktDQoSGateSetAckCount = _RdnPktDQoSGateSetAckCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 15),
    _RdnPktDQoSGateSetAckCount_Type()
)
rdnPktDQoSGateSetAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateSetAckCount.setStatus("current")
_RdnPktDQoSGateSetErrCount_Type = Integer32
_RdnPktDQoSGateSetErrCount_Object = MibTableColumn
rdnPktDQoSGateSetErrCount = _RdnPktDQoSGateSetErrCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 16),
    _RdnPktDQoSGateSetErrCount_Type()
)
rdnPktDQoSGateSetErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateSetErrCount.setStatus("current")
_RdnPktDQoSGateDeleteCount_Type = Integer32
_RdnPktDQoSGateDeleteCount_Object = MibTableColumn
rdnPktDQoSGateDeleteCount = _RdnPktDQoSGateDeleteCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 17),
    _RdnPktDQoSGateDeleteCount_Type()
)
rdnPktDQoSGateDeleteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateDeleteCount.setStatus("current")
_RdnPktDQoSGateDeleteAckCount_Type = Integer32
_RdnPktDQoSGateDeleteAckCount_Object = MibTableColumn
rdnPktDQoSGateDeleteAckCount = _RdnPktDQoSGateDeleteAckCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 18),
    _RdnPktDQoSGateDeleteAckCount_Type()
)
rdnPktDQoSGateDeleteAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateDeleteAckCount.setStatus("current")
_RdnPktDQoSGateDeleteErrCount_Type = Integer32
_RdnPktDQoSGateDeleteErrCount_Object = MibTableColumn
rdnPktDQoSGateDeleteErrCount = _RdnPktDQoSGateDeleteErrCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 19),
    _RdnPktDQoSGateDeleteErrCount_Type()
)
rdnPktDQoSGateDeleteErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateDeleteErrCount.setStatus("current")
_RdnPktDQoSGateInfoCount_Type = Integer32
_RdnPktDQoSGateInfoCount_Object = MibTableColumn
rdnPktDQoSGateInfoCount = _RdnPktDQoSGateInfoCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 20),
    _RdnPktDQoSGateInfoCount_Type()
)
rdnPktDQoSGateInfoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateInfoCount.setStatus("current")
_RdnPktDQoSGateInfoAckCount_Type = Integer32
_RdnPktDQoSGateInfoAckCount_Object = MibTableColumn
rdnPktDQoSGateInfoAckCount = _RdnPktDQoSGateInfoAckCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 21),
    _RdnPktDQoSGateInfoAckCount_Type()
)
rdnPktDQoSGateInfoAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateInfoAckCount.setStatus("current")
_RdnPktDQoSGateInfoErrCount_Type = Integer32
_RdnPktDQoSGateInfoErrCount_Object = MibTableColumn
rdnPktDQoSGateInfoErrCount = _RdnPktDQoSGateInfoErrCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 22),
    _RdnPktDQoSGateInfoErrCount_Type()
)
rdnPktDQoSGateInfoErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateInfoErrCount.setStatus("current")
_RdnPktDQoSGateOpenRcvd_Type = Integer32
_RdnPktDQoSGateOpenRcvd_Object = MibTableColumn
rdnPktDQoSGateOpenRcvd = _RdnPktDQoSGateOpenRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 23),
    _RdnPktDQoSGateOpenRcvd_Type()
)
rdnPktDQoSGateOpenRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenRcvd.setStatus("obsolete")
_RdnPktDQoSGateOpenAckSent_Type = Integer32
_RdnPktDQoSGateOpenAckSent_Object = MibTableColumn
rdnPktDQoSGateOpenAckSent = _RdnPktDQoSGateOpenAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 24),
    _RdnPktDQoSGateOpenAckSent_Type()
)
rdnPktDQoSGateOpenAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenAckSent.setStatus("obsolete")
_RdnPktDQoSGateOpenErrSent_Type = Integer32
_RdnPktDQoSGateOpenErrSent_Object = MibTableColumn
rdnPktDQoSGateOpenErrSent = _RdnPktDQoSGateOpenErrSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 25),
    _RdnPktDQoSGateOpenErrSent_Type()
)
rdnPktDQoSGateOpenErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenErrSent.setStatus("obsolete")
_RdnPktDQoSGateCloseRcvd_Type = Integer32
_RdnPktDQoSGateCloseRcvd_Object = MibTableColumn
rdnPktDQoSGateCloseRcvd = _RdnPktDQoSGateCloseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 26),
    _RdnPktDQoSGateCloseRcvd_Type()
)
rdnPktDQoSGateCloseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseRcvd.setStatus("obsolete")
_RdnPktDQoSGateCloseAckSent_Type = Integer32
_RdnPktDQoSGateCloseAckSent_Object = MibTableColumn
rdnPktDQoSGateCloseAckSent = _RdnPktDQoSGateCloseAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 27),
    _RdnPktDQoSGateCloseAckSent_Type()
)
rdnPktDQoSGateCloseAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseAckSent.setStatus("obsolete")
_RdnPktDQoSGateCloseErrSent_Type = Integer32
_RdnPktDQoSGateCloseErrSent_Object = MibTableColumn
rdnPktDQoSGateCloseErrSent = _RdnPktDQoSGateCloseErrSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 28),
    _RdnPktDQoSGateCloseErrSent_Type()
)
rdnPktDQoSGateCloseErrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseErrSent.setStatus("obsolete")
_RdnPktDQoSGateOpenSent_Type = Integer32
_RdnPktDQoSGateOpenSent_Object = MibTableColumn
rdnPktDQoSGateOpenSent = _RdnPktDQoSGateOpenSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 29),
    _RdnPktDQoSGateOpenSent_Type()
)
rdnPktDQoSGateOpenSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenSent.setStatus("current")
_RdnPktDQoSGateOpenAckRcvd_Type = Integer32
_RdnPktDQoSGateOpenAckRcvd_Object = MibTableColumn
rdnPktDQoSGateOpenAckRcvd = _RdnPktDQoSGateOpenAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 30),
    _RdnPktDQoSGateOpenAckRcvd_Type()
)
rdnPktDQoSGateOpenAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenAckRcvd.setStatus("obsolete")
_RdnPktDQoSGateOpenErrRcvd_Type = Integer32
_RdnPktDQoSGateOpenErrRcvd_Object = MibTableColumn
rdnPktDQoSGateOpenErrRcvd = _RdnPktDQoSGateOpenErrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 31),
    _RdnPktDQoSGateOpenErrRcvd_Type()
)
rdnPktDQoSGateOpenErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenErrRcvd.setStatus("obsolete")
_RdnPktDQoSGateCloseSent_Type = Integer32
_RdnPktDQoSGateCloseSent_Object = MibTableColumn
rdnPktDQoSGateCloseSent = _RdnPktDQoSGateCloseSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 32),
    _RdnPktDQoSGateCloseSent_Type()
)
rdnPktDQoSGateCloseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseSent.setStatus("current")
_RdnPktDQoSGateCloseAckRcvd_Type = Integer32
_RdnPktDQoSGateCloseAckRcvd_Object = MibTableColumn
rdnPktDQoSGateCloseAckRcvd = _RdnPktDQoSGateCloseAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 33),
    _RdnPktDQoSGateCloseAckRcvd_Type()
)
rdnPktDQoSGateCloseAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseAckRcvd.setStatus("obsolete")
_RdnPktDQoSGateCloseErrRcvd_Type = Integer32
_RdnPktDQoSGateCloseErrRcvd_Object = MibTableColumn
rdnPktDQoSGateCloseErrRcvd = _RdnPktDQoSGateCloseErrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 34),
    _RdnPktDQoSGateCloseErrRcvd_Type()
)
rdnPktDQoSGateCloseErrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseErrRcvd.setStatus("obsolete")
_RdnPktDQoSGateOpenRetries_Type = Integer32
_RdnPktDQoSGateOpenRetries_Object = MibTableColumn
rdnPktDQoSGateOpenRetries = _RdnPktDQoSGateOpenRetries_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 35),
    _RdnPktDQoSGateOpenRetries_Type()
)
rdnPktDQoSGateOpenRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenRetries.setStatus("obsolete")
_RdnPktDQoSGateCloseRetries_Type = Integer32
_RdnPktDQoSGateCloseRetries_Object = MibTableColumn
rdnPktDQoSGateCloseRetries = _RdnPktDQoSGateCloseRetries_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 36),
    _RdnPktDQoSGateCloseRetries_Type()
)
rdnPktDQoSGateCloseRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseRetries.setStatus("obsolete")
_RdnPktDQoSGateOpenExhausted_Type = Integer32
_RdnPktDQoSGateOpenExhausted_Object = MibTableColumn
rdnPktDQoSGateOpenExhausted = _RdnPktDQoSGateOpenExhausted_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 37),
    _RdnPktDQoSGateOpenExhausted_Type()
)
rdnPktDQoSGateOpenExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateOpenExhausted.setStatus("obsolete")
_RdnPktDQoSGateCloseExhausted_Type = Integer32
_RdnPktDQoSGateCloseExhausted_Object = MibTableColumn
rdnPktDQoSGateCloseExhausted = _RdnPktDQoSGateCloseExhausted_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 38),
    _RdnPktDQoSGateCloseExhausted_Type()
)
rdnPktDQoSGateCloseExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCloseExhausted.setStatus("obsolete")
_RdnPktDQoSCliOpenSent_Type = Integer32
_RdnPktDQoSCliOpenSent_Object = MibTableColumn
rdnPktDQoSCliOpenSent = _RdnPktDQoSCliOpenSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 39),
    _RdnPktDQoSCliOpenSent_Type()
)
rdnPktDQoSCliOpenSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCliOpenSent.setStatus("current")
_RdnPktDQoSCliAcceptReceived_Type = Integer32
_RdnPktDQoSCliAcceptReceived_Object = MibTableColumn
rdnPktDQoSCliAcceptReceived = _RdnPktDQoSCliAcceptReceived_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 40),
    _RdnPktDQoSCliAcceptReceived_Type()
)
rdnPktDQoSCliAcceptReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCliAcceptReceived.setStatus("current")
_RdnPktDQoSRequestSent_Type = Integer32
_RdnPktDQoSRequestSent_Object = MibTableColumn
rdnPktDQoSRequestSent = _RdnPktDQoSRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 41),
    _RdnPktDQoSRequestSent_Type()
)
rdnPktDQoSRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSRequestSent.setStatus("current")
_RdnPktDQoSCliCloseReceived_Type = Integer32
_RdnPktDQoSCliCloseReceived_Object = MibTableColumn
rdnPktDQoSCliCloseReceived = _RdnPktDQoSCliCloseReceived_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 42),
    _RdnPktDQoSCliCloseReceived_Type()
)
rdnPktDQoSCliCloseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCliCloseReceived.setStatus("current")
_RdnPktDQoSCliCloseSent_Type = Integer32
_RdnPktDQoSCliCloseSent_Object = MibTableColumn
rdnPktDQoSCliCloseSent = _RdnPktDQoSCliCloseSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 43),
    _RdnPktDQoSCliCloseSent_Type()
)
rdnPktDQoSCliCloseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSCliCloseSent.setStatus("current")
_RdnPktDQoSSsqReceived_Type = Integer32
_RdnPktDQoSSsqReceived_Object = MibTableColumn
rdnPktDQoSSsqReceived = _RdnPktDQoSSsqReceived_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 44),
    _RdnPktDQoSSsqReceived_Type()
)
rdnPktDQoSSsqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSSsqReceived.setStatus("current")
_RdnPktDQoSSscSent_Type = Integer32
_RdnPktDQoSSscSent_Object = MibTableColumn
rdnPktDQoSSscSent = _RdnPktDQoSSscSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 45),
    _RdnPktDQoSSscSent_Type()
)
rdnPktDQoSSscSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSSscSent.setStatus("current")
_RdnPktDQoSDrqSent_Type = Integer32
_RdnPktDQoSDrqSent_Object = MibTableColumn
rdnPktDQoSDrqSent = _RdnPktDQoSDrqSent_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 46),
    _RdnPktDQoSDrqSent_Type()
)
rdnPktDQoSDrqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSDrqSent.setStatus("current")
_RdnPktDQoST7Timeout_Type = Integer32
_RdnPktDQoST7Timeout_Object = MibTableColumn
rdnPktDQoST7Timeout = _RdnPktDQoST7Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 47),
    _RdnPktDQoST7Timeout_Type()
)
rdnPktDQoST7Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoST7Timeout.setStatus("current")
_RdnPktDQoST8Timeout_Type = Integer32
_RdnPktDQoST8Timeout_Object = MibTableColumn
rdnPktDQoST8Timeout = _RdnPktDQoST8Timeout_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 48),
    _RdnPktDQoST8Timeout_Type()
)
rdnPktDQoST8Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoST8Timeout.setStatus("current")
_RdnPktDQoSGateCmDel_Type = Integer32
_RdnPktDQoSGateCmDel_Object = MibTableColumn
rdnPktDQoSGateCmDel = _RdnPktDQoSGateCmDel_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 49),
    _RdnPktDQoSGateCmDel_Type()
)
rdnPktDQoSGateCmDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCmDel.setStatus("current")
_RdnPktDQoSGateCmDereg_Type = Integer32
_RdnPktDQoSGateCmDereg_Object = MibTableColumn
rdnPktDQoSGateCmDereg = _RdnPktDQoSGateCmDereg_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 50),
    _RdnPktDQoSGateCmDereg_Type()
)
rdnPktDQoSGateCmDereg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateCmDereg.setStatus("current")
_RdnPktDQoSGateAdminDel_Type = Integer32
_RdnPktDQoSGateAdminDel_Object = MibTableColumn
rdnPktDQoSGateAdminDel = _RdnPktDQoSGateAdminDel_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 51),
    _RdnPktDQoSGateAdminDel_Type()
)
rdnPktDQoSGateAdminDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateAdminDel.setStatus("current")
_RdnPktDQoSGateResReassign_Type = Integer32
_RdnPktDQoSGateResReassign_Object = MibTableColumn
rdnPktDQoSGateResReassign = _RdnPktDQoSGateResReassign_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 6, 1, 52),
    _RdnPktDQoSGateResReassign_Type()
)
rdnPktDQoSGateResReassign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnPktDQoSGateResReassign.setStatus("current")
_RdnPktDQoSNotificationObject_ObjectIdentity = ObjectIdentity
rdnPktDQoSNotificationObject = _RdnPktDQoSNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7)
)


class _RdnPktDQoSCopsReason_Type(Integer32):
    """Custom type rdnPktDQoSCopsReason based on Integer32"""
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
        *(("cantEstablishCopsConnection", 2),
          ("copsConnectionClosed", 4),
          ("copsConnectionDisconnected", 5),
          ("copsConnectionEstablished", 1),
          ("keepAliveFailure", 6),
          ("unauthorizedCms", 3))
    )


_RdnPktDQoSCopsReason_Type.__name__ = "Integer32"
_RdnPktDQoSCopsReason_Object = MibScalar
rdnPktDQoSCopsReason = _RdnPktDQoSCopsReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 1),
    _RdnPktDQoSCopsReason_Type()
)
rdnPktDQoSCopsReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsReason.setStatus("current")
_RdnPktDQoSCopsCmsIpAddr_Type = IpAddress
_RdnPktDQoSCopsCmsIpAddr_Object = MibScalar
rdnPktDQoSCopsCmsIpAddr = _RdnPktDQoSCopsCmsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 2),
    _RdnPktDQoSCopsCmsIpAddr_Type()
)
rdnPktDQoSCopsCmsIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsCmsIpAddr.setStatus("current")
_RdnPktDQoSCopsCmsPortNum_Type = Integer32
_RdnPktDQoSCopsCmsPortNum_Object = MibScalar
rdnPktDQoSCopsCmsPortNum = _RdnPktDQoSCopsCmsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 3),
    _RdnPktDQoSCopsCmsPortNum_Type()
)
rdnPktDQoSCopsCmsPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsCmsPortNum.setStatus("current")
_RdnPktDQoSCopsCmsHandleId_Type = Integer32
_RdnPktDQoSCopsCmsHandleId_Object = MibScalar
rdnPktDQoSCopsCmsHandleId = _RdnPktDQoSCopsCmsHandleId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 4),
    _RdnPktDQoSCopsCmsHandleId_Type()
)
rdnPktDQoSCopsCmsHandleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSCopsCmsHandleId.setStatus("current")


class _RdnPktDQoSResReqReason_Type(Integer32):
    """Custom type rdnPktDQoSResReqReason based on Integer32"""
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
        *(("dsaReqResourceGreaterThanAuth", 1),
          ("dsaResReqWithInvalidGateId", 3),
          ("dsaResReqWithoutGateId", 2),
          ("dscReqResourceGreaterThanAuth", 4),
          ("dscResReqWithInvalidGateId", 6),
          ("dscResReqWithoutGateId", 5))
    )


_RdnPktDQoSResReqReason_Type.__name__ = "Integer32"
_RdnPktDQoSResReqReason_Object = MibScalar
rdnPktDQoSResReqReason = _RdnPktDQoSResReqReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 5),
    _RdnPktDQoSResReqReason_Type()
)
rdnPktDQoSResReqReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSResReqReason.setStatus("current")
_RdnPktDQoSCmMacAddr_Type = MacAddress
_RdnPktDQoSCmMacAddr_Object = MibScalar
rdnPktDQoSCmMacAddr = _RdnPktDQoSCmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 6),
    _RdnPktDQoSCmMacAddr_Type()
)
rdnPktDQoSCmMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSCmMacAddr.setStatus("current")


class _RdnPktDQoSEmergencyReason_Type(Integer32):
    """Custom type rdnPktDQoSEmergencyReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("emergencyCallBeingRejected", 1)
    )


_RdnPktDQoSEmergencyReason_Type.__name__ = "Integer32"
_RdnPktDQoSEmergencyReason_Object = MibScalar
rdnPktDQoSEmergencyReason = _RdnPktDQoSEmergencyReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 7),
    _RdnPktDQoSEmergencyReason_Type()
)
rdnPktDQoSEmergencyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyReason.setStatus("current")


class _RdnPktDQoSClassName_Type(DisplayString):
    """Custom type rdnPktDQoSClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RdnPktDQoSClassName_Type.__name__ = "DisplayString"
_RdnPktDQoSClassName_Object = MibScalar
rdnPktDQoSClassName = _RdnPktDQoSClassName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 8),
    _RdnPktDQoSClassName_Type()
)
rdnPktDQoSClassName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSClassName.setStatus("current")
_RdnPktDQoSGateId_Type = Integer32
_RdnPktDQoSGateId_Object = MibScalar
rdnPktDQoSGateId = _RdnPktDQoSGateId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 9),
    _RdnPktDQoSGateId_Type()
)
rdnPktDQoSGateId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSGateId.setStatus("current")


class _RdnPktDQoSEmergencyPreemptReason_Type(Integer32):
    """Custom type rdnPktDQoSEmergencyPreemptReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("emergencyPreemptedMostRecentCall", 1),
          ("emergencyPreemptedOldestCall", 2),
          ("emergencyPreemptedRandomCall", 3))
    )


_RdnPktDQoSEmergencyPreemptReason_Type.__name__ = "Integer32"
_RdnPktDQoSEmergencyPreemptReason_Object = MibScalar
rdnPktDQoSEmergencyPreemptReason = _RdnPktDQoSEmergencyPreemptReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 7, 10),
    _RdnPktDQoSEmergencyPreemptReason_Type()
)
rdnPktDQoSEmergencyPreemptReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyPreemptReason.setStatus("current")
_RdnPktDQoSNotificationTraps_ObjectIdentity = ObjectIdentity
rdnPktDQoSNotificationTraps = _RdnPktDQoSNotificationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8)
)
_RdnPktDQoSNotificationTrapsPrefix_ObjectIdentity = ObjectIdentity
rdnPktDQoSNotificationTrapsPrefix = _RdnPktDQoSNotificationTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8, 0)
)
_RdnPktESNotificationObject_ObjectIdentity = ObjectIdentity
rdnPktESNotificationObject = _RdnPktESNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 9)
)


class _RdnPktESReason_Type(Integer32):
    """Custom type rdnPktESReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cdcFailure", 1)
    )


_RdnPktESReason_Type.__name__ = "Integer32"
_RdnPktESReason_Object = MibScalar
rdnPktESReason = _RdnPktESReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 9, 1),
    _RdnPktESReason_Type()
)
rdnPktESReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktESReason.setStatus("current")
_RdnPktESDFIpAddr_Type = IpAddress
_RdnPktESDFIpAddr_Object = MibScalar
rdnPktESDFIpAddr = _RdnPktESDFIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 9, 2),
    _RdnPktESDFIpAddr_Type()
)
rdnPktESDFIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktESDFIpAddr.setStatus("current")
_RdnPktESDFPortNum_Type = Integer32
_RdnPktESDFPortNum_Object = MibScalar
rdnPktESDFPortNum = _RdnPktESDFPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 9, 3),
    _RdnPktESDFPortNum_Type()
)
rdnPktESDFPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktESDFPortNum.setStatus("current")
_RdnPktESNotificationTraps_ObjectIdentity = ObjectIdentity
rdnPktESNotificationTraps = _RdnPktESNotificationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 10)
)
_RdnPktESNotificationTrapsPrefix_ObjectIdentity = ObjectIdentity
rdnPktESNotificationTrapsPrefix = _RdnPktESNotificationTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 10, 0)
)
_RdnPktRKSNotificationObject_ObjectIdentity = ObjectIdentity
rdnPktRKSNotificationObject = _RdnPktRKSNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11)
)


class _RdnPktRKSReason_Type(Integer32):
    """Custom type rdnPktRKSReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("retriesExhausted", 1)
    )


_RdnPktRKSReason_Type.__name__ = "Integer32"
_RdnPktRKSReason_Object = MibScalar
rdnPktRKSReason = _RdnPktRKSReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 1),
    _RdnPktRKSReason_Type()
)
rdnPktRKSReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSReason.setStatus("current")
_RdnPktRKSTransID_Type = Integer32
_RdnPktRKSTransID_Object = MibScalar
rdnPktRKSTransID = _RdnPktRKSTransID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 2),
    _RdnPktRKSTransID_Type()
)
rdnPktRKSTransID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSTransID.setStatus("current")
_RdnPktRKSIPPrimary_Type = IpAddress
_RdnPktRKSIPPrimary_Object = MibScalar
rdnPktRKSIPPrimary = _RdnPktRKSIPPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 3),
    _RdnPktRKSIPPrimary_Type()
)
rdnPktRKSIPPrimary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSIPPrimary.setStatus("current")
_RdnPktRKSPortPrimary_Type = Integer32
_RdnPktRKSPortPrimary_Object = MibScalar
rdnPktRKSPortPrimary = _RdnPktRKSPortPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 4),
    _RdnPktRKSPortPrimary_Type()
)
rdnPktRKSPortPrimary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSPortPrimary.setStatus("current")
_RdnPktRKSIPSecondary_Type = IpAddress
_RdnPktRKSIPSecondary_Object = MibScalar
rdnPktRKSIPSecondary = _RdnPktRKSIPSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 5),
    _RdnPktRKSIPSecondary_Type()
)
rdnPktRKSIPSecondary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSIPSecondary.setStatus("current")
_RdnPktRKSPortSecondary_Type = Integer32
_RdnPktRKSPortSecondary_Object = MibScalar
rdnPktRKSPortSecondary = _RdnPktRKSPortSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 6),
    _RdnPktRKSPortSecondary_Type()
)
rdnPktRKSPortSecondary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSPortSecondary.setStatus("current")


class _RdnPktRKSVersionID_Type(Integer32):
    """Custom type rdnPktRKSVersionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("packetCable10", 1),
          ("packetCable11", 2),
          ("packetCableMultiMedia", 3))
    )


_RdnPktRKSVersionID_Type.__name__ = "Integer32"
_RdnPktRKSVersionID_Object = MibScalar
rdnPktRKSVersionID = _RdnPktRKSVersionID_Object(
    (1, 3, 6, 1, 4, 1, 4981, 7, 11, 7),
    _RdnPktRKSVersionID_Type()
)
rdnPktRKSVersionID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktRKSVersionID.setStatus("current")
_RdnPktRKSNotificationTraps_ObjectIdentity = ObjectIdentity
rdnPktRKSNotificationTraps = _RdnPktRKSNotificationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 12)
)
_RdnPktRKSNotificationTrapsPrefix_ObjectIdentity = ObjectIdentity
rdnPktRKSNotificationTrapsPrefix = _RdnPktRKSNotificationTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 7, 12, 0)
)

# Managed Objects groups


# Notification objects

rdnPktDQoSCopsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8, 0, 1)
)
rdnPktDQoSCopsTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCopsReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCopsCmsIpAddr"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSCopsTrap.setStatus(
        "current"
    )

rdnPktDQoSResReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8, 0, 2)
)
rdnPktDQoSResReqTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSResReqReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCmMacAddr"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSResReqTrap.setStatus(
        "current"
    )

rdnPktDQoSEmergencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8, 0, 3)
)
rdnPktDQoSEmergencyTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSEmergencyReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCmMacAddr"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSClassName"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSGateId"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyTrap.setStatus(
        "current"
    )

rdnPktDQoSEmergencyPreemptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 8, 0, 4)
)
rdnPktDQoSEmergencyPreemptTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSEmergencyPreemptReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSCmMacAddr"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSClassName"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSGateId"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSEmergencyPreemptTrap.setStatus(
        "current"
    )

rdnPktESTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 10, 0, 1)
)
rdnPktESTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktESReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktESDFIpAddr"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktESDFPortNum"))
)
if mibBuilder.loadTexts:
    rdnPktESTrap.setStatus(
        "current"
    )

rdnPktDQoSRKSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 7, 12, 0, 1)
)
rdnPktDQoSRKSTrap.setObjects(
      *(("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSTransID"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSIPPrimary"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSPortPrimary"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSIPSecondary"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSPortSecondary"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktRKSVersionID"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSRKSTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-PKTCABLE-GROUP-MIB",
    **{"BcidDataArray": BcidDataArray,
       "rdnPacketCableGroup": rdnPacketCableGroup,
       "rdnPktDQoSConfigGroup": rdnPktDQoSConfigGroup,
       "rdnPktDQoSCOPSStatus": rdnPktDQoSCOPSStatus,
       "rdnPktDQoSCMTSIp": rdnPktDQoSCMTSIp,
       "rdnPktDQoSPEPID": rdnPktDQoSPEPID,
       "rdnPktDQoSClientAccpTimer": rdnPktDQoSClientAccpTimer,
       "rdnPktDQoST0Timer": rdnPktDQoST0Timer,
       "rdnPktDQoST1Timer": rdnPktDQoST1Timer,
       "rdnPktDQoST3Timer": rdnPktDQoST3Timer,
       "rdnPktDQoST6Timer": rdnPktDQoST6Timer,
       "rdnPktDQoSCopsTrapEnable": rdnPktDQoSCopsTrapEnable,
       "rdnPktDQoSResReqTrapEnable": rdnPktDQoSResReqTrapEnable,
       "rdnPktESTrapEnable": rdnPktESTrapEnable,
       "rdnPktESEnable": rdnPktESEnable,
       "rdnPktDQoSEmergencyTrapEnable": rdnPktDQoSEmergencyTrapEnable,
       "rdnPktDQoSEmergencyPreemption": rdnPktDQoSEmergencyPreemption,
       "rdnPktEMRKSFailureTrapEnable": rdnPktEMRKSFailureTrapEnable,
       "rdnPktDQoSDscp": rdnPktDQoSDscp,
       "rdnPktMMDscp": rdnPktMMDscp,
       "rdnPktEMDscp": rdnPktEMDscp,
       "rdnPktESCccDscp": rdnPktESCccDscp,
       "rdnGateStatsTable": rdnGateStatsTable,
       "rdnGateStatsEntry": rdnGateStatsEntry,
       "rdnGateId": rdnGateId,
       "rdnGateStatsState": rdnGateStatsState,
       "rdnGateStatsSubscriberIP": rdnGateStatsSubscriberIP,
       "rdnGateStatsRKSPrimaryAddr": rdnGateStatsRKSPrimaryAddr,
       "rdnGateStatsRKSPrimaryPort": rdnGateStatsRKSPrimaryPort,
       "rdnGateStatsRKSSecondaryAddr": rdnGateStatsRKSSecondaryAddr,
       "rdnGateStatsRKSSecondaryPort": rdnGateStatsRKSSecondaryPort,
       "rdnGateStatsEventFlag": rdnGateStatsEventFlag,
       "rdnGateStatsBillingCorrelationID": rdnGateStatsBillingCorrelationID,
       "rdnGateStatsDurationTime": rdnGateStatsDurationTime,
       "rdnGateStatsSlotNum": rdnGateStatsSlotNum,
       "rdnGateStatsUpSfid": rdnGateStatsUpSfid,
       "rdnGateStatsDnSfid": rdnGateStatsDnSfid,
       "rdnGateStatsResourceID": rdnGateStatsResourceID,
       "rdnGateStatsESCDCAddr": rdnGateStatsESCDCAddr,
       "rdnGateStatsESCDCPort": rdnGateStatsESCDCPort,
       "rdnGateStatsESFlag": rdnGateStatsESFlag,
       "rdnGateStatsESCCCAddr": rdnGateStatsESCCCAddr,
       "rdnGateStatsESCCCPort": rdnGateStatsESCCCPort,
       "rdnGateStatsESCCCId": rdnGateStatsESCCCId,
       "rdnGateSpecTable": rdnGateSpecTable,
       "rdnGateSpecEntry": rdnGateSpecEntry,
       "rdnGateDirection": rdnGateDirection,
       "rdnGateSpecProtocol": rdnGateSpecProtocol,
       "rdnGateSpecSourceIP": rdnGateSpecSourceIP,
       "rdnGateSpecSourcePort": rdnGateSpecSourcePort,
       "rdnGateSpecDestIP": rdnGateSpecDestIP,
       "rdnGateSpecDestPort": rdnGateSpecDestPort,
       "rdnGateSpecServiceFlowID": rdnGateSpecServiceFlowID,
       "rdnGateSpecFlags": rdnGateSpecFlags,
       "rdnGateSpecSessionClass": rdnGateSpecSessionClass,
       "rdnGateSpecDiffServCode": rdnGateSpecDiffServCode,
       "rdnGateSpecT1Timer": rdnGateSpecT1Timer,
       "rdnGateSpecTokenBuckRate": rdnGateSpecTokenBuckRate,
       "rdnGateSpecBuckSize": rdnGateSpecBuckSize,
       "rdnGateSpecPeakDataRate": rdnGateSpecPeakDataRate,
       "rdnGateSpecMinPoliceUnit": rdnGateSpecMinPoliceUnit,
       "rdnGateSpecMaxPacketSize": rdnGateSpecMaxPacketSize,
       "rdnGateSpecReserveRate": rdnGateSpecReserveRate,
       "rdnGateSlackTerm": rdnGateSlackTerm,
       "rdnPktCMSIpConfigTable": rdnPktCMSIpConfigTable,
       "rdnPktCMSIpConfigEntry": rdnPktCMSIpConfigEntry,
       "rdnPktCMSIpAddressIndex": rdnPktCMSIpAddressIndex,
       "rdnPktCMSIpAddress": rdnPktCMSIpAddress,
       "rdnPktDQoSStatsTable": rdnPktDQoSStatsTable,
       "rdnPktDQoSStatsEntry": rdnPktDQoSStatsEntry,
       "rdnPktDQoSIpAddress": rdnPktDQoSIpAddress,
       "rdnPktDQoSCopsHandle": rdnPktDQoSCopsHandle,
       "rdnPktDQoSCopsStatus": rdnPktDQoSCopsStatus,
       "rdnPktDQoSCopsConnected": rdnPktDQoSCopsConnected,
       "rdnPktDQoSCopsTerminated": rdnPktDQoSCopsTerminated,
       "rdnPktDQoSCopsKASent": rdnPktDQoSCopsKASent,
       "rdnPktDQoSCopsKARcvd": rdnPktDQoSCopsKARcvd,
       "rdnPktDQoSKATimeout": rdnPktDQoSKATimeout,
       "rdnPktDQoST0Timeout": rdnPktDQoST0Timeout,
       "rdnPktDQoST1Timeout": rdnPktDQoST1Timeout,
       "rdnPktDQoSGateAllocCount": rdnPktDQoSGateAllocCount,
       "rdnPktDQoSGateAllocAckCount": rdnPktDQoSGateAllocAckCount,
       "rdnPktDQoSGateAllocErrCount": rdnPktDQoSGateAllocErrCount,
       "rdnPktDQoSGateSetCount": rdnPktDQoSGateSetCount,
       "rdnPktDQoSGateSetAckCount": rdnPktDQoSGateSetAckCount,
       "rdnPktDQoSGateSetErrCount": rdnPktDQoSGateSetErrCount,
       "rdnPktDQoSGateDeleteCount": rdnPktDQoSGateDeleteCount,
       "rdnPktDQoSGateDeleteAckCount": rdnPktDQoSGateDeleteAckCount,
       "rdnPktDQoSGateDeleteErrCount": rdnPktDQoSGateDeleteErrCount,
       "rdnPktDQoSGateInfoCount": rdnPktDQoSGateInfoCount,
       "rdnPktDQoSGateInfoAckCount": rdnPktDQoSGateInfoAckCount,
       "rdnPktDQoSGateInfoErrCount": rdnPktDQoSGateInfoErrCount,
       "rdnPktDQoSGateOpenRcvd": rdnPktDQoSGateOpenRcvd,
       "rdnPktDQoSGateOpenAckSent": rdnPktDQoSGateOpenAckSent,
       "rdnPktDQoSGateOpenErrSent": rdnPktDQoSGateOpenErrSent,
       "rdnPktDQoSGateCloseRcvd": rdnPktDQoSGateCloseRcvd,
       "rdnPktDQoSGateCloseAckSent": rdnPktDQoSGateCloseAckSent,
       "rdnPktDQoSGateCloseErrSent": rdnPktDQoSGateCloseErrSent,
       "rdnPktDQoSGateOpenSent": rdnPktDQoSGateOpenSent,
       "rdnPktDQoSGateOpenAckRcvd": rdnPktDQoSGateOpenAckRcvd,
       "rdnPktDQoSGateOpenErrRcvd": rdnPktDQoSGateOpenErrRcvd,
       "rdnPktDQoSGateCloseSent": rdnPktDQoSGateCloseSent,
       "rdnPktDQoSGateCloseAckRcvd": rdnPktDQoSGateCloseAckRcvd,
       "rdnPktDQoSGateCloseErrRcvd": rdnPktDQoSGateCloseErrRcvd,
       "rdnPktDQoSGateOpenRetries": rdnPktDQoSGateOpenRetries,
       "rdnPktDQoSGateCloseRetries": rdnPktDQoSGateCloseRetries,
       "rdnPktDQoSGateOpenExhausted": rdnPktDQoSGateOpenExhausted,
       "rdnPktDQoSGateCloseExhausted": rdnPktDQoSGateCloseExhausted,
       "rdnPktDQoSCliOpenSent": rdnPktDQoSCliOpenSent,
       "rdnPktDQoSCliAcceptReceived": rdnPktDQoSCliAcceptReceived,
       "rdnPktDQoSRequestSent": rdnPktDQoSRequestSent,
       "rdnPktDQoSCliCloseReceived": rdnPktDQoSCliCloseReceived,
       "rdnPktDQoSCliCloseSent": rdnPktDQoSCliCloseSent,
       "rdnPktDQoSSsqReceived": rdnPktDQoSSsqReceived,
       "rdnPktDQoSSscSent": rdnPktDQoSSscSent,
       "rdnPktDQoSDrqSent": rdnPktDQoSDrqSent,
       "rdnPktDQoST7Timeout": rdnPktDQoST7Timeout,
       "rdnPktDQoST8Timeout": rdnPktDQoST8Timeout,
       "rdnPktDQoSGateCmDel": rdnPktDQoSGateCmDel,
       "rdnPktDQoSGateCmDereg": rdnPktDQoSGateCmDereg,
       "rdnPktDQoSGateAdminDel": rdnPktDQoSGateAdminDel,
       "rdnPktDQoSGateResReassign": rdnPktDQoSGateResReassign,
       "rdnPktDQoSNotificationObject": rdnPktDQoSNotificationObject,
       "rdnPktDQoSCopsReason": rdnPktDQoSCopsReason,
       "rdnPktDQoSCopsCmsIpAddr": rdnPktDQoSCopsCmsIpAddr,
       "rdnPktDQoSCopsCmsPortNum": rdnPktDQoSCopsCmsPortNum,
       "rdnPktDQoSCopsCmsHandleId": rdnPktDQoSCopsCmsHandleId,
       "rdnPktDQoSResReqReason": rdnPktDQoSResReqReason,
       "rdnPktDQoSCmMacAddr": rdnPktDQoSCmMacAddr,
       "rdnPktDQoSEmergencyReason": rdnPktDQoSEmergencyReason,
       "rdnPktDQoSClassName": rdnPktDQoSClassName,
       "rdnPktDQoSGateId": rdnPktDQoSGateId,
       "rdnPktDQoSEmergencyPreemptReason": rdnPktDQoSEmergencyPreemptReason,
       "rdnPktDQoSNotificationTraps": rdnPktDQoSNotificationTraps,
       "rdnPktDQoSNotificationTrapsPrefix": rdnPktDQoSNotificationTrapsPrefix,
       "rdnPktDQoSCopsTrap": rdnPktDQoSCopsTrap,
       "rdnPktDQoSResReqTrap": rdnPktDQoSResReqTrap,
       "rdnPktDQoSEmergencyTrap": rdnPktDQoSEmergencyTrap,
       "rdnPktDQoSEmergencyPreemptTrap": rdnPktDQoSEmergencyPreemptTrap,
       "rdnPktESNotificationObject": rdnPktESNotificationObject,
       "rdnPktESReason": rdnPktESReason,
       "rdnPktESDFIpAddr": rdnPktESDFIpAddr,
       "rdnPktESDFPortNum": rdnPktESDFPortNum,
       "rdnPktESNotificationTraps": rdnPktESNotificationTraps,
       "rdnPktESNotificationTrapsPrefix": rdnPktESNotificationTrapsPrefix,
       "rdnPktESTrap": rdnPktESTrap,
       "rdnPktRKSNotificationObject": rdnPktRKSNotificationObject,
       "rdnPktRKSReason": rdnPktRKSReason,
       "rdnPktRKSTransID": rdnPktRKSTransID,
       "rdnPktRKSIPPrimary": rdnPktRKSIPPrimary,
       "rdnPktRKSPortPrimary": rdnPktRKSPortPrimary,
       "rdnPktRKSIPSecondary": rdnPktRKSIPSecondary,
       "rdnPktRKSPortSecondary": rdnPktRKSPortSecondary,
       "rdnPktRKSVersionID": rdnPktRKSVersionID,
       "rdnPktRKSNotificationTraps": rdnPktRKSNotificationTraps,
       "rdnPktRKSNotificationTrapsPrefix": rdnPktRKSNotificationTrapsPrefix,
       "rdnPktDQoSRKSTrap": rdnPktDQoSRKSTrap}
)
