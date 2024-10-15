# SNMP MIB module (IPATM-IPMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPATM-IPMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:46 2024
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

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
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

marsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 57)
)
marsMIB.setRevisions(
        ("1998-09-01 00:00",
         "1998-04-15 01:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MarsTrapInfo_ObjectIdentity = ObjectIdentity
marsTrapInfo = _MarsTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 0)
)
_MarsClientObjects_ObjectIdentity = ObjectIdentity
marsClientObjects = _MarsClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 1)
)
_MarsClientTable_Object = MibTable
marsClientTable = _MarsClientTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1)
)
if mibBuilder.loadTexts:
    marsClientTable.setStatus("current")
_MarsClientEntry_Object = MibTableRow
marsClientEntry = _MarsClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1)
)
marsClientEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientIndex"),
)
if mibBuilder.loadTexts:
    marsClientEntry.setStatus("current")


class _MarsClientIndex_Type(Integer32):
    """Custom type marsClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsClientIndex_Type.__name__ = "Integer32"
_MarsClientIndex_Object = MibTableColumn
marsClientIndex = _MarsClientIndex_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 1),
    _MarsClientIndex_Type()
)
marsClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientIndex.setStatus("current")
_MarsClientAddr_Type = AtmAddr
_MarsClientAddr_Object = MibTableColumn
marsClientAddr = _MarsClientAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 2),
    _MarsClientAddr_Type()
)
marsClientAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientAddr.setStatus("current")
_MarsClientDefaultMarsAddr_Type = AtmAddr
_MarsClientDefaultMarsAddr_Object = MibTableColumn
marsClientDefaultMarsAddr = _MarsClientDefaultMarsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 3),
    _MarsClientDefaultMarsAddr_Type()
)
marsClientDefaultMarsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientDefaultMarsAddr.setStatus("current")
_MarsClientHsn_Type = Unsigned32
_MarsClientHsn_Object = MibTableColumn
marsClientHsn = _MarsClientHsn_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 4),
    _MarsClientHsn_Type()
)
marsClientHsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientHsn.setStatus("current")


class _MarsClientRegistration_Type(Integer32):
    """Custom type marsClientRegistration based on Integer32"""
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
        *(("notRegistered", 1),
          ("reRegisteringFault", 4),
          ("reRegisteringRedirMap", 5),
          ("registered", 3),
          ("registering", 2))
    )


_MarsClientRegistration_Type.__name__ = "Integer32"
_MarsClientRegistration_Object = MibTableColumn
marsClientRegistration = _MarsClientRegistration_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 5),
    _MarsClientRegistration_Type()
)
marsClientRegistration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRegistration.setStatus("current")


class _MarsClientCmi_Type(Integer32):
    """Custom type marsClientCmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsClientCmi_Type.__name__ = "Integer32"
_MarsClientCmi_Object = MibTableColumn
marsClientCmi = _MarsClientCmi_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 6),
    _MarsClientCmi_Type()
)
marsClientCmi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientCmi.setStatus("current")


class _MarsClientDefaultMtu_Type(Integer32):
    """Custom type marsClientDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsClientDefaultMtu_Type.__name__ = "Integer32"
_MarsClientDefaultMtu_Object = MibTableColumn
marsClientDefaultMtu = _MarsClientDefaultMtu_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 7),
    _MarsClientDefaultMtu_Type()
)
marsClientDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientDefaultMtu.setStatus("current")


class _MarsClientFailureTimer_Type(Integer32):
    """Custom type marsClientFailureTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsClientFailureTimer_Type.__name__ = "Integer32"
_MarsClientFailureTimer_Object = MibTableColumn
marsClientFailureTimer = _MarsClientFailureTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 8),
    _MarsClientFailureTimer_Type()
)
marsClientFailureTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientFailureTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientFailureTimer.setUnits("seconds")


class _MarsClientRetranDelayTimer_Type(Integer32):
    """Custom type marsClientRetranDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_MarsClientRetranDelayTimer_Type.__name__ = "Integer32"
_MarsClientRetranDelayTimer_Object = MibTableColumn
marsClientRetranDelayTimer = _MarsClientRetranDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 9),
    _MarsClientRetranDelayTimer_Type()
)
marsClientRetranDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRetranDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientRetranDelayTimer.setUnits("seconds")


class _MarsClientRdmMulReqAddRetrTimer_Type(Integer32):
    """Custom type marsClientRdmMulReqAddRetrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_MarsClientRdmMulReqAddRetrTimer_Type.__name__ = "Integer32"
_MarsClientRdmMulReqAddRetrTimer_Object = MibTableColumn
marsClientRdmMulReqAddRetrTimer = _MarsClientRdmMulReqAddRetrTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 10),
    _MarsClientRdmMulReqAddRetrTimer_Type()
)
marsClientRdmMulReqAddRetrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRdmMulReqAddRetrTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientRdmMulReqAddRetrTimer.setUnits("seconds")


class _MarsClientRdmVcRevalidateTimer_Type(Integer32):
    """Custom type marsClientRdmVcRevalidateTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MarsClientRdmVcRevalidateTimer_Type.__name__ = "Integer32"
_MarsClientRdmVcRevalidateTimer_Object = MibTableColumn
marsClientRdmVcRevalidateTimer = _MarsClientRdmVcRevalidateTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 11),
    _MarsClientRdmVcRevalidateTimer_Type()
)
marsClientRdmVcRevalidateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRdmVcRevalidateTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientRdmVcRevalidateTimer.setUnits("seconds")


class _MarsClientJoinLeaveRetrInterval_Type(Integer32):
    """Custom type marsClientJoinLeaveRetrInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_MarsClientJoinLeaveRetrInterval_Type.__name__ = "Integer32"
_MarsClientJoinLeaveRetrInterval_Object = MibTableColumn
marsClientJoinLeaveRetrInterval = _MarsClientJoinLeaveRetrInterval_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 12),
    _MarsClientJoinLeaveRetrInterval_Type()
)
marsClientJoinLeaveRetrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientJoinLeaveRetrInterval.setStatus("current")
if mibBuilder.loadTexts:
    marsClientJoinLeaveRetrInterval.setUnits("seconds")


class _MarsClientJoinLeaveRetrLimit_Type(Integer32):
    """Custom type marsClientJoinLeaveRetrLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MarsClientJoinLeaveRetrLimit_Type.__name__ = "Integer32"
_MarsClientJoinLeaveRetrLimit_Object = MibTableColumn
marsClientJoinLeaveRetrLimit = _MarsClientJoinLeaveRetrLimit_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 13),
    _MarsClientJoinLeaveRetrLimit_Type()
)
marsClientJoinLeaveRetrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientJoinLeaveRetrLimit.setStatus("current")


class _MarsClientRegWithMarsRdmTimer_Type(Integer32):
    """Custom type marsClientRegWithMarsRdmTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MarsClientRegWithMarsRdmTimer_Type.__name__ = "Integer32"
_MarsClientRegWithMarsRdmTimer_Object = MibTableColumn
marsClientRegWithMarsRdmTimer = _MarsClientRegWithMarsRdmTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 14),
    _MarsClientRegWithMarsRdmTimer_Type()
)
marsClientRegWithMarsRdmTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRegWithMarsRdmTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientRegWithMarsRdmTimer.setUnits("seconds")


class _MarsClientForceWaitTimer_Type(Integer32):
    """Custom type marsClientForceWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsClientForceWaitTimer_Type.__name__ = "Integer32"
_MarsClientForceWaitTimer_Object = MibTableColumn
marsClientForceWaitTimer = _MarsClientForceWaitTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 15),
    _MarsClientForceWaitTimer_Type()
)
marsClientForceWaitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientForceWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientForceWaitTimer.setUnits("minutes")


class _MarsClientLmtToMissRedirMapTimer_Type(Integer32):
    """Custom type marsClientLmtToMissRedirMapTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MarsClientLmtToMissRedirMapTimer_Type.__name__ = "Integer32"
_MarsClientLmtToMissRedirMapTimer_Object = MibTableColumn
marsClientLmtToMissRedirMapTimer = _MarsClientLmtToMissRedirMapTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 16),
    _MarsClientLmtToMissRedirMapTimer_Type()
)
marsClientLmtToMissRedirMapTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientLmtToMissRedirMapTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientLmtToMissRedirMapTimer.setUnits("seconds")


class _MarsClientIdleTimer_Type(Integer32):
    """Custom type marsClientIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsClientIdleTimer_Type.__name__ = "Integer32"
_MarsClientIdleTimer_Object = MibTableColumn
marsClientIdleTimer = _MarsClientIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 17),
    _MarsClientIdleTimer_Type()
)
marsClientIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientIdleTimer.setUnits("minutes")
_MarsClientRowStatus_Type = RowStatus
_MarsClientRowStatus_Object = MibTableColumn
marsClientRowStatus = _MarsClientRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 1, 1, 18),
    _MarsClientRowStatus_Type()
)
marsClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientRowStatus.setStatus("current")
_MarsClientMcGrpTable_Object = MibTable
marsClientMcGrpTable = _MarsClientMcGrpTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 2)
)
if mibBuilder.loadTexts:
    marsClientMcGrpTable.setStatus("current")
_MarsClientMcGrpEntry_Object = MibTableRow
marsClientMcGrpEntry = _MarsClientMcGrpEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 2, 1)
)
marsClientMcGrpEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientIndex"),
    (0, "IPATM-IPMC-MIB", "marsClientMcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientMcMaxGrpAddr"),
)
if mibBuilder.loadTexts:
    marsClientMcGrpEntry.setStatus("current")
_MarsClientMcMinGrpAddr_Type = IpAddress
_MarsClientMcMinGrpAddr_Object = MibTableColumn
marsClientMcMinGrpAddr = _MarsClientMcMinGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 2, 1, 1),
    _MarsClientMcMinGrpAddr_Type()
)
marsClientMcMinGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientMcMinGrpAddr.setStatus("current")
_MarsClientMcMaxGrpAddr_Type = IpAddress
_MarsClientMcMaxGrpAddr_Object = MibTableColumn
marsClientMcMaxGrpAddr = _MarsClientMcMaxGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 2, 1, 2),
    _MarsClientMcMaxGrpAddr_Type()
)
marsClientMcMaxGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientMcMaxGrpAddr.setStatus("current")
_MarsClientMcGrpRowStatus_Type = RowStatus
_MarsClientMcGrpRowStatus_Object = MibTableColumn
marsClientMcGrpRowStatus = _MarsClientMcGrpRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 2, 1, 3),
    _MarsClientMcGrpRowStatus_Type()
)
marsClientMcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientMcGrpRowStatus.setStatus("current")
_MarsClientBackupMarsTable_Object = MibTable
marsClientBackupMarsTable = _MarsClientBackupMarsTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 3)
)
if mibBuilder.loadTexts:
    marsClientBackupMarsTable.setStatus("current")
_MarsClientBackupMarsEntry_Object = MibTableRow
marsClientBackupMarsEntry = _MarsClientBackupMarsEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 3, 1)
)
marsClientBackupMarsEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientIndex"),
    (0, "IPATM-IPMC-MIB", "marsClientBackupMarsPriority"),
    (0, "IPATM-IPMC-MIB", "marsClientBackupMarsAddr"),
)
if mibBuilder.loadTexts:
    marsClientBackupMarsEntry.setStatus("current")


class _MarsClientBackupMarsPriority_Type(Unsigned32):
    """Custom type marsClientBackupMarsPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsClientBackupMarsPriority_Type.__name__ = "Unsigned32"
_MarsClientBackupMarsPriority_Object = MibTableColumn
marsClientBackupMarsPriority = _MarsClientBackupMarsPriority_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 3, 1, 1),
    _MarsClientBackupMarsPriority_Type()
)
marsClientBackupMarsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientBackupMarsPriority.setStatus("current")
_MarsClientBackupMarsAddr_Type = AtmAddr
_MarsClientBackupMarsAddr_Object = MibTableColumn
marsClientBackupMarsAddr = _MarsClientBackupMarsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 3, 1, 2),
    _MarsClientBackupMarsAddr_Type()
)
marsClientBackupMarsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientBackupMarsAddr.setStatus("current")
_MarsClientBackupMarsRowStatus_Type = RowStatus
_MarsClientBackupMarsRowStatus_Object = MibTableColumn
marsClientBackupMarsRowStatus = _MarsClientBackupMarsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 3, 1, 3),
    _MarsClientBackupMarsRowStatus_Type()
)
marsClientBackupMarsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientBackupMarsRowStatus.setStatus("current")
_MarsClientVcTable_Object = MibTable
marsClientVcTable = _MarsClientVcTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4)
)
if mibBuilder.loadTexts:
    marsClientVcTable.setStatus("current")
_MarsClientVcEntry_Object = MibTableRow
marsClientVcEntry = _MarsClientVcEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1)
)
marsClientVcEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientIndex"),
    (0, "IPATM-IPMC-MIB", "marsClientVcVpi"),
    (0, "IPATM-IPMC-MIB", "marsClientVcVci"),
    (0, "IPATM-IPMC-MIB", "marsClientVcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientVcMaxGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientVcPartyAddr"),
)
if mibBuilder.loadTexts:
    marsClientVcEntry.setStatus("current")


class _MarsClientVcVpi_Type(Integer32):
    """Custom type marsClientVcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MarsClientVcVpi_Type.__name__ = "Integer32"
_MarsClientVcVpi_Object = MibTableColumn
marsClientVcVpi = _MarsClientVcVpi_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 1),
    _MarsClientVcVpi_Type()
)
marsClientVcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientVcVpi.setStatus("current")


class _MarsClientVcVci_Type(Integer32):
    """Custom type marsClientVcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsClientVcVci_Type.__name__ = "Integer32"
_MarsClientVcVci_Object = MibTableColumn
marsClientVcVci = _MarsClientVcVci_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 2),
    _MarsClientVcVci_Type()
)
marsClientVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientVcVci.setStatus("current")
_MarsClientVcMinGrpAddr_Type = IpAddress
_MarsClientVcMinGrpAddr_Object = MibTableColumn
marsClientVcMinGrpAddr = _MarsClientVcMinGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 3),
    _MarsClientVcMinGrpAddr_Type()
)
marsClientVcMinGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientVcMinGrpAddr.setStatus("current")
_MarsClientVcMaxGrpAddr_Type = IpAddress
_MarsClientVcMaxGrpAddr_Object = MibTableColumn
marsClientVcMaxGrpAddr = _MarsClientVcMaxGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 4),
    _MarsClientVcMaxGrpAddr_Type()
)
marsClientVcMaxGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientVcMaxGrpAddr.setStatus("current")
_MarsClientVcPartyAddr_Type = AtmAddr
_MarsClientVcPartyAddr_Object = MibTableColumn
marsClientVcPartyAddr = _MarsClientVcPartyAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 5),
    _MarsClientVcPartyAddr_Type()
)
marsClientVcPartyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsClientVcPartyAddr.setStatus("current")


class _MarsClientVcPartyAddrType_Type(Integer32):
    """Custom type marsClientVcPartyAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 2))
    )


_MarsClientVcPartyAddrType_Type.__name__ = "Integer32"
_MarsClientVcPartyAddrType_Object = MibTableColumn
marsClientVcPartyAddrType = _MarsClientVcPartyAddrType_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 6),
    _MarsClientVcPartyAddrType_Type()
)
marsClientVcPartyAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcPartyAddrType.setStatus("current")


class _MarsClientVcType_Type(Integer32):
    """Custom type marsClientVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_MarsClientVcType_Type.__name__ = "Integer32"
_MarsClientVcType_Object = MibTableColumn
marsClientVcType = _MarsClientVcType_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 7),
    _MarsClientVcType_Type()
)
marsClientVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcType.setStatus("current")


class _MarsClientVcCtrlType_Type(Integer32):
    """Custom type marsClientVcCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clusterControlVC", 2),
          ("pointToMultiPointVC", 3),
          ("pointToPointVC", 1))
    )


_MarsClientVcCtrlType_Type.__name__ = "Integer32"
_MarsClientVcCtrlType_Object = MibTableColumn
marsClientVcCtrlType = _MarsClientVcCtrlType_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 8),
    _MarsClientVcCtrlType_Type()
)
marsClientVcCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcCtrlType.setStatus("current")


class _MarsClientVcIdleTimer_Type(Integer32):
    """Custom type marsClientVcIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsClientVcIdleTimer_Type.__name__ = "Integer32"
_MarsClientVcIdleTimer_Object = MibTableColumn
marsClientVcIdleTimer = _MarsClientVcIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 9),
    _MarsClientVcIdleTimer_Type()
)
marsClientVcIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsClientVcIdleTimer.setUnits("minutes")
_MarsClientVcRevalidate_Type = TruthValue
_MarsClientVcRevalidate_Object = MibTableColumn
marsClientVcRevalidate = _MarsClientVcRevalidate_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 10),
    _MarsClientVcRevalidate_Type()
)
marsClientVcRevalidate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcRevalidate.setStatus("current")


class _MarsClientVcEncapsType_Type(Integer32):
    """Custom type marsClientVcEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llcSnap", 2),
          ("other", 1))
    )


_MarsClientVcEncapsType_Type.__name__ = "Integer32"
_MarsClientVcEncapsType_Object = MibTableColumn
marsClientVcEncapsType = _MarsClientVcEncapsType_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 11),
    _MarsClientVcEncapsType_Type()
)
marsClientVcEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcEncapsType.setStatus("current")


class _MarsClientVcNegotiatedMtu_Type(Integer32):
    """Custom type marsClientVcNegotiatedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsClientVcNegotiatedMtu_Type.__name__ = "Integer32"
_MarsClientVcNegotiatedMtu_Object = MibTableColumn
marsClientVcNegotiatedMtu = _MarsClientVcNegotiatedMtu_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 12),
    _MarsClientVcNegotiatedMtu_Type()
)
marsClientVcNegotiatedMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcNegotiatedMtu.setStatus("current")
_MarsClientVcRowStatus_Type = RowStatus
_MarsClientVcRowStatus_Object = MibTableColumn
marsClientVcRowStatus = _MarsClientVcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 4, 1, 13),
    _MarsClientVcRowStatus_Type()
)
marsClientVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsClientVcRowStatus.setStatus("current")
_MarsClientStatTable_Object = MibTable
marsClientStatTable = _MarsClientStatTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5)
)
if mibBuilder.loadTexts:
    marsClientStatTable.setStatus("current")
_MarsClientStatEntry_Object = MibTableRow
marsClientStatEntry = _MarsClientStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1)
)
marsClientStatEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
    (0, "IPATM-IPMC-MIB", "marsClientIndex"),
)
if mibBuilder.loadTexts:
    marsClientStatEntry.setStatus("current")
_MarsClientStatTxReqMsgs_Type = Counter32
_MarsClientStatTxReqMsgs_Object = MibTableColumn
marsClientStatTxReqMsgs = _MarsClientStatTxReqMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 1),
    _MarsClientStatTxReqMsgs_Type()
)
marsClientStatTxReqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatTxReqMsgs.setStatus("current")
_MarsClientStatTxJoinMsgs_Type = Counter32
_MarsClientStatTxJoinMsgs_Object = MibTableColumn
marsClientStatTxJoinMsgs = _MarsClientStatTxJoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 2),
    _MarsClientStatTxJoinMsgs_Type()
)
marsClientStatTxJoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatTxJoinMsgs.setStatus("current")
_MarsClientStatTxLeaveMsgs_Type = Counter32
_MarsClientStatTxLeaveMsgs_Object = MibTableColumn
marsClientStatTxLeaveMsgs = _MarsClientStatTxLeaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 3),
    _MarsClientStatTxLeaveMsgs_Type()
)
marsClientStatTxLeaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatTxLeaveMsgs.setStatus("current")
_MarsClientStatTxGrpLstReqMsgs_Type = Counter32
_MarsClientStatTxGrpLstReqMsgs_Object = MibTableColumn
marsClientStatTxGrpLstReqMsgs = _MarsClientStatTxGrpLstReqMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 4),
    _MarsClientStatTxGrpLstReqMsgs_Type()
)
marsClientStatTxGrpLstReqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatTxGrpLstReqMsgs.setStatus("current")
_MarsClientStatRxJoinMsgs_Type = Counter32
_MarsClientStatRxJoinMsgs_Object = MibTableColumn
marsClientStatRxJoinMsgs = _MarsClientStatRxJoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 5),
    _MarsClientStatRxJoinMsgs_Type()
)
marsClientStatRxJoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxJoinMsgs.setStatus("current")
_MarsClientStatRxLeaveMsgs_Type = Counter32
_MarsClientStatRxLeaveMsgs_Object = MibTableColumn
marsClientStatRxLeaveMsgs = _MarsClientStatRxLeaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 6),
    _MarsClientStatRxLeaveMsgs_Type()
)
marsClientStatRxLeaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxLeaveMsgs.setStatus("current")
_MarsClientStatRxMultiMsgs_Type = Counter32
_MarsClientStatRxMultiMsgs_Object = MibTableColumn
marsClientStatRxMultiMsgs = _MarsClientStatRxMultiMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 7),
    _MarsClientStatRxMultiMsgs_Type()
)
marsClientStatRxMultiMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxMultiMsgs.setStatus("current")
_MarsClientStatRxNakMsgs_Type = Counter32
_MarsClientStatRxNakMsgs_Object = MibTableColumn
marsClientStatRxNakMsgs = _MarsClientStatRxNakMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 8),
    _MarsClientStatRxNakMsgs_Type()
)
marsClientStatRxNakMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxNakMsgs.setStatus("current")
_MarsClientStatRxMigrateMsgs_Type = Counter32
_MarsClientStatRxMigrateMsgs_Object = MibTableColumn
marsClientStatRxMigrateMsgs = _MarsClientStatRxMigrateMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 9),
    _MarsClientStatRxMigrateMsgs_Type()
)
marsClientStatRxMigrateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxMigrateMsgs.setStatus("current")
_MarsClientStatRxGrpLstRplyMsgs_Type = Counter32
_MarsClientStatRxGrpLstRplyMsgs_Object = MibTableColumn
marsClientStatRxGrpLstRplyMsgs = _MarsClientStatRxGrpLstRplyMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 10),
    _MarsClientStatRxGrpLstRplyMsgs_Type()
)
marsClientStatRxGrpLstRplyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatRxGrpLstRplyMsgs.setStatus("current")
_MarsClientStatFailMultiMsgs_Type = Counter32
_MarsClientStatFailMultiMsgs_Object = MibTableColumn
marsClientStatFailMultiMsgs = _MarsClientStatFailMultiMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 1, 5, 1, 11),
    _MarsClientStatFailMultiMsgs_Type()
)
marsClientStatFailMultiMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsClientStatFailMultiMsgs.setStatus("current")
_MarsObjects_ObjectIdentity = ObjectIdentity
marsObjects = _MarsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 2)
)
_MarsTable_Object = MibTable
marsTable = _MarsTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1)
)
if mibBuilder.loadTexts:
    marsTable.setStatus("current")
_MarsEntry_Object = MibTableRow
marsEntry = _MarsEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1)
)
marsEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
)
if mibBuilder.loadTexts:
    marsEntry.setStatus("current")


class _MarsIndex_Type(Integer32):
    """Custom type marsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsIndex_Type.__name__ = "Integer32"
_MarsIndex_Object = MibTableColumn
marsIndex = _MarsIndex_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 1),
    _MarsIndex_Type()
)
marsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsIndex.setStatus("current")
_MarsIfIndex_Type = InterfaceIndex
_MarsIfIndex_Object = MibTableColumn
marsIfIndex = _MarsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 2),
    _MarsIfIndex_Type()
)
marsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsIfIndex.setStatus("current")
_MarsAddr_Type = AtmAddr
_MarsAddr_Object = MibTableColumn
marsAddr = _MarsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 3),
    _MarsAddr_Type()
)
marsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsAddr.setStatus("current")
_MarsLocal_Type = TruthValue
_MarsLocal_Object = MibTableColumn
marsLocal = _MarsLocal_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 4),
    _MarsLocal_Type()
)
marsLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsLocal.setStatus("current")


class _MarsServStatus_Type(Integer32):
    """Custom type marsServStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("faulted", 3),
          ("inactive", 2))
    )


_MarsServStatus_Type.__name__ = "Integer32"
_MarsServStatus_Object = MibTableColumn
marsServStatus = _MarsServStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 5),
    _MarsServStatus_Type()
)
marsServStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsServStatus.setStatus("current")


class _MarsServType_Type(Integer32):
    """Custom type marsServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_MarsServType_Type.__name__ = "Integer32"
_MarsServType_Object = MibTableColumn
marsServType = _MarsServType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 6),
    _MarsServType_Type()
)
marsServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsServType.setStatus("current")


class _MarsServPriority_Type(Unsigned32):
    """Custom type marsServPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsServPriority_Type.__name__ = "Unsigned32"
_MarsServPriority_Object = MibTableColumn
marsServPriority = _MarsServPriority_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 7),
    _MarsServPriority_Type()
)
marsServPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsServPriority.setStatus("current")


class _MarsRedirMapMsgTimer_Type(Integer32):
    """Custom type marsRedirMapMsgTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MarsRedirMapMsgTimer_Type.__name__ = "Integer32"
_MarsRedirMapMsgTimer_Object = MibTableColumn
marsRedirMapMsgTimer = _MarsRedirMapMsgTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 8),
    _MarsRedirMapMsgTimer_Type()
)
marsRedirMapMsgTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsRedirMapMsgTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsRedirMapMsgTimer.setUnits("minutes")
_MarsCsn_Type = Unsigned32
_MarsCsn_Object = MibTableColumn
marsCsn = _MarsCsn_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 9),
    _MarsCsn_Type()
)
marsCsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsCsn.setStatus("current")
_MarsSsn_Type = Unsigned32
_MarsSsn_Object = MibTableColumn
marsSsn = _MarsSsn_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 10),
    _MarsSsn_Type()
)
marsSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsSsn.setStatus("current")
_MarsRowStatus_Type = RowStatus
_MarsRowStatus_Object = MibTableColumn
marsRowStatus = _MarsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 1, 1, 11),
    _MarsRowStatus_Type()
)
marsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsRowStatus.setStatus("current")
_MarsMcGrpTable_Object = MibTable
marsMcGrpTable = _MarsMcGrpTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2)
)
if mibBuilder.loadTexts:
    marsMcGrpTable.setStatus("current")
_MarsMcGrpEntry_Object = MibTableRow
marsMcGrpEntry = _MarsMcGrpEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1)
)
marsMcGrpEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcMaxGrpAddr"),
)
if mibBuilder.loadTexts:
    marsMcGrpEntry.setStatus("current")
_MarsMcMinGrpAddr_Type = IpAddress
_MarsMcMinGrpAddr_Object = MibTableColumn
marsMcMinGrpAddr = _MarsMcMinGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 1),
    _MarsMcMinGrpAddr_Type()
)
marsMcMinGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcMinGrpAddr.setStatus("current")
_MarsMcMaxGrpAddr_Type = IpAddress
_MarsMcMaxGrpAddr_Object = MibTableColumn
marsMcMaxGrpAddr = _MarsMcMaxGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 2),
    _MarsMcMaxGrpAddr_Type()
)
marsMcMaxGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcMaxGrpAddr.setStatus("current")


class _MarsMcGrpAddrUsage_Type(Integer32):
    """Custom type marsMcGrpAddrUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hostMap", 1),
          ("hostServerMap", 3),
          ("serverMap", 2))
    )


_MarsMcGrpAddrUsage_Type.__name__ = "Integer32"
_MarsMcGrpAddrUsage_Object = MibTableColumn
marsMcGrpAddrUsage = _MarsMcGrpAddrUsage_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 3),
    _MarsMcGrpAddrUsage_Type()
)
marsMcGrpAddrUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcGrpAddrUsage.setStatus("current")
_MarsMcGrpRxLayer3GrpSets_Type = Counter32
_MarsMcGrpRxLayer3GrpSets_Object = MibTableColumn
marsMcGrpRxLayer3GrpSets = _MarsMcGrpRxLayer3GrpSets_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 4),
    _MarsMcGrpRxLayer3GrpSets_Type()
)
marsMcGrpRxLayer3GrpSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcGrpRxLayer3GrpSets.setStatus("current")
_MarsMcGrpRxLayer3GrpResets_Type = Counter32
_MarsMcGrpRxLayer3GrpResets_Object = MibTableColumn
marsMcGrpRxLayer3GrpResets = _MarsMcGrpRxLayer3GrpResets_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 5),
    _MarsMcGrpRxLayer3GrpResets_Type()
)
marsMcGrpRxLayer3GrpResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcGrpRxLayer3GrpResets.setStatus("current")
_MarsMcGrpRowStatus_Type = RowStatus
_MarsMcGrpRowStatus_Object = MibTableColumn
marsMcGrpRowStatus = _MarsMcGrpRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 2, 1, 6),
    _MarsMcGrpRowStatus_Type()
)
marsMcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcGrpRowStatus.setStatus("current")
_MarsHostMapTable_Object = MibTable
marsHostMapTable = _MarsHostMapTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 3)
)
if mibBuilder.loadTexts:
    marsHostMapTable.setStatus("current")
_MarsHostMapEntry_Object = MibTableRow
marsHostMapEntry = _MarsHostMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 3, 1)
)
marsHostMapEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcMaxGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsHostMapAtmAddr"),
)
if mibBuilder.loadTexts:
    marsHostMapEntry.setStatus("current")
_MarsHostMapAtmAddr_Type = AtmAddr
_MarsHostMapAtmAddr_Object = MibTableColumn
marsHostMapAtmAddr = _MarsHostMapAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 3, 1, 1),
    _MarsHostMapAtmAddr_Type()
)
marsHostMapAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsHostMapAtmAddr.setStatus("current")


class _MarsHostMapRowType_Type(Integer32):
    """Custom type marsHostMapRowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MarsHostMapRowType_Type.__name__ = "Integer32"
_MarsHostMapRowType_Object = MibTableColumn
marsHostMapRowType = _MarsHostMapRowType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 3, 1, 2),
    _MarsHostMapRowType_Type()
)
marsHostMapRowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsHostMapRowType.setStatus("current")
_MarsHostMapRowStatus_Type = RowStatus
_MarsHostMapRowStatus_Object = MibTableColumn
marsHostMapRowStatus = _MarsHostMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 3, 1, 3),
    _MarsHostMapRowStatus_Type()
)
marsHostMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsHostMapRowStatus.setStatus("current")
_MarsServerMapTable_Object = MibTable
marsServerMapTable = _MarsServerMapTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 4)
)
if mibBuilder.loadTexts:
    marsServerMapTable.setStatus("current")
_MarsServerMapEntry_Object = MibTableRow
marsServerMapEntry = _MarsServerMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 4, 1)
)
marsServerMapEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcMaxGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsServerMapAtmAddr"),
)
if mibBuilder.loadTexts:
    marsServerMapEntry.setStatus("current")
_MarsServerMapAtmAddr_Type = AtmAddr
_MarsServerMapAtmAddr_Object = MibTableColumn
marsServerMapAtmAddr = _MarsServerMapAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 4, 1, 1),
    _MarsServerMapAtmAddr_Type()
)
marsServerMapAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsServerMapAtmAddr.setStatus("current")


class _MarsServerMapRowType_Type(Integer32):
    """Custom type marsServerMapRowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MarsServerMapRowType_Type.__name__ = "Integer32"
_MarsServerMapRowType_Object = MibTableColumn
marsServerMapRowType = _MarsServerMapRowType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 4, 1, 2),
    _MarsServerMapRowType_Type()
)
marsServerMapRowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsServerMapRowType.setStatus("current")
_MarsServerMapRowStatus_Type = RowStatus
_MarsServerMapRowStatus_Object = MibTableColumn
marsServerMapRowStatus = _MarsServerMapRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 4, 1, 3),
    _MarsServerMapRowStatus_Type()
)
marsServerMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsServerMapRowStatus.setStatus("current")
_MarsVcTable_Object = MibTable
marsVcTable = _MarsVcTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5)
)
if mibBuilder.loadTexts:
    marsVcTable.setStatus("current")
_MarsVcEntry_Object = MibTableRow
marsVcEntry = _MarsVcEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1)
)
marsVcEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsVcVpi"),
    (0, "IPATM-IPMC-MIB", "marsVcVci"),
    (0, "IPATM-IPMC-MIB", "marsVcPartyAddr"),
)
if mibBuilder.loadTexts:
    marsVcEntry.setStatus("current")


class _MarsVcVpi_Type(Integer32):
    """Custom type marsVcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MarsVcVpi_Type.__name__ = "Integer32"
_MarsVcVpi_Object = MibTableColumn
marsVcVpi = _MarsVcVpi_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 1),
    _MarsVcVpi_Type()
)
marsVcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsVcVpi.setStatus("current")


class _MarsVcVci_Type(Integer32):
    """Custom type marsVcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsVcVci_Type.__name__ = "Integer32"
_MarsVcVci_Object = MibTableColumn
marsVcVci = _MarsVcVci_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 2),
    _MarsVcVci_Type()
)
marsVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsVcVci.setStatus("current")
_MarsVcPartyAddr_Type = AtmAddr
_MarsVcPartyAddr_Object = MibTableColumn
marsVcPartyAddr = _MarsVcPartyAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 5),
    _MarsVcPartyAddr_Type()
)
marsVcPartyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsVcPartyAddr.setStatus("current")


class _MarsVcPartyAddrType_Type(Integer32):
    """Custom type marsVcPartyAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 2))
    )


_MarsVcPartyAddrType_Type.__name__ = "Integer32"
_MarsVcPartyAddrType_Object = MibTableColumn
marsVcPartyAddrType = _MarsVcPartyAddrType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 6),
    _MarsVcPartyAddrType_Type()
)
marsVcPartyAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcPartyAddrType.setStatus("current")


class _MarsVcType_Type(Integer32):
    """Custom type marsVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_MarsVcType_Type.__name__ = "Integer32"
_MarsVcType_Object = MibTableColumn
marsVcType = _MarsVcType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 7),
    _MarsVcType_Type()
)
marsVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcType.setStatus("current")


class _MarsVcCtrlType_Type(Integer32):
    """Custom type marsVcCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clusterControlVC", 2),
          ("pointToPointVC", 1),
          ("serverControlVC", 3))
    )


_MarsVcCtrlType_Type.__name__ = "Integer32"
_MarsVcCtrlType_Object = MibTableColumn
marsVcCtrlType = _MarsVcCtrlType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 8),
    _MarsVcCtrlType_Type()
)
marsVcCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcCtrlType.setStatus("current")


class _MarsVcIdleTimer_Type(Integer32):
    """Custom type marsVcIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsVcIdleTimer_Type.__name__ = "Integer32"
_MarsVcIdleTimer_Object = MibTableColumn
marsVcIdleTimer = _MarsVcIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 9),
    _MarsVcIdleTimer_Type()
)
marsVcIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsVcIdleTimer.setUnits("minutes")


class _MarsVcCmi_Type(Integer32):
    """Custom type marsVcCmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsVcCmi_Type.__name__ = "Integer32"
_MarsVcCmi_Object = MibTableColumn
marsVcCmi = _MarsVcCmi_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 10),
    _MarsVcCmi_Type()
)
marsVcCmi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcCmi.setStatus("current")


class _MarsVcEncapsType_Type(Integer32):
    """Custom type marsVcEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llcSnap", 2),
          ("other", 1))
    )


_MarsVcEncapsType_Type.__name__ = "Integer32"
_MarsVcEncapsType_Object = MibTableColumn
marsVcEncapsType = _MarsVcEncapsType_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 11),
    _MarsVcEncapsType_Type()
)
marsVcEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcEncapsType.setStatus("current")


class _MarsVcNegotiatedMtu_Type(Integer32):
    """Custom type marsVcNegotiatedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsVcNegotiatedMtu_Type.__name__ = "Integer32"
_MarsVcNegotiatedMtu_Object = MibTableColumn
marsVcNegotiatedMtu = _MarsVcNegotiatedMtu_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 12),
    _MarsVcNegotiatedMtu_Type()
)
marsVcNegotiatedMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcNegotiatedMtu.setStatus("current")
_MarsVcRowStatus_Type = RowStatus
_MarsVcRowStatus_Object = MibTableColumn
marsVcRowStatus = _MarsVcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 5, 1, 13),
    _MarsVcRowStatus_Type()
)
marsVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsVcRowStatus.setStatus("current")
_MarsRegClientTable_Object = MibTable
marsRegClientTable = _MarsRegClientTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 6)
)
if mibBuilder.loadTexts:
    marsRegClientTable.setStatus("current")
_MarsRegClientEntry_Object = MibTableRow
marsRegClientEntry = _MarsRegClientEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 6, 1)
)
marsRegClientEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsRegClientCmi"),
)
if mibBuilder.loadTexts:
    marsRegClientEntry.setStatus("current")


class _MarsRegClientCmi_Type(Integer32):
    """Custom type marsRegClientCmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsRegClientCmi_Type.__name__ = "Integer32"
_MarsRegClientCmi_Object = MibTableColumn
marsRegClientCmi = _MarsRegClientCmi_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 6, 1, 1),
    _MarsRegClientCmi_Type()
)
marsRegClientCmi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsRegClientCmi.setStatus("current")
_MarsRegClientAtmAddr_Type = AtmAddr
_MarsRegClientAtmAddr_Object = MibTableColumn
marsRegClientAtmAddr = _MarsRegClientAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 6, 1, 2),
    _MarsRegClientAtmAddr_Type()
)
marsRegClientAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsRegClientAtmAddr.setStatus("current")
_MarsRegMcsTable_Object = MibTable
marsRegMcsTable = _MarsRegMcsTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 7)
)
if mibBuilder.loadTexts:
    marsRegMcsTable.setStatus("current")
_MarsRegMcsEntry_Object = MibTableRow
marsRegMcsEntry = _MarsRegMcsEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 7, 1)
)
marsRegMcsEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsRegMcsAtmAddr"),
)
if mibBuilder.loadTexts:
    marsRegMcsEntry.setStatus("current")
_MarsRegMcsAtmAddr_Type = AtmAddr
_MarsRegMcsAtmAddr_Object = MibTableColumn
marsRegMcsAtmAddr = _MarsRegMcsAtmAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 7, 1, 1),
    _MarsRegMcsAtmAddr_Type()
)
marsRegMcsAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsRegMcsAtmAddr.setStatus("current")
_MarsStatTable_Object = MibTable
marsStatTable = _MarsStatTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8)
)
if mibBuilder.loadTexts:
    marsStatTable.setStatus("current")
_MarsStatEntry_Object = MibTableRow
marsStatEntry = _MarsStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1)
)
marsStatEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsIndex"),
    (0, "IPATM-IPMC-MIB", "marsIfIndex"),
)
if mibBuilder.loadTexts:
    marsStatEntry.setStatus("current")
_MarsStatTxMultiMsgs_Type = Counter32
_MarsStatTxMultiMsgs_Object = MibTableColumn
marsStatTxMultiMsgs = _MarsStatTxMultiMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 1),
    _MarsStatTxMultiMsgs_Type()
)
marsStatTxMultiMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxMultiMsgs.setStatus("current")
_MarsStatTxGrpLstRplyMsgs_Type = Counter32
_MarsStatTxGrpLstRplyMsgs_Object = MibTableColumn
marsStatTxGrpLstRplyMsgs = _MarsStatTxGrpLstRplyMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 2),
    _MarsStatTxGrpLstRplyMsgs_Type()
)
marsStatTxGrpLstRplyMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxGrpLstRplyMsgs.setStatus("current")
_MarsStatTxRedirectMapMsgs_Type = Counter32
_MarsStatTxRedirectMapMsgs_Object = MibTableColumn
marsStatTxRedirectMapMsgs = _MarsStatTxRedirectMapMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 3),
    _MarsStatTxRedirectMapMsgs_Type()
)
marsStatTxRedirectMapMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxRedirectMapMsgs.setStatus("current")
_MarsStatTxMigrateMsgs_Type = Counter32
_MarsStatTxMigrateMsgs_Object = MibTableColumn
marsStatTxMigrateMsgs = _MarsStatTxMigrateMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 4),
    _MarsStatTxMigrateMsgs_Type()
)
marsStatTxMigrateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxMigrateMsgs.setStatus("current")
_MarsStatTxNakMsgs_Type = Counter32
_MarsStatTxNakMsgs_Object = MibTableColumn
marsStatTxNakMsgs = _MarsStatTxNakMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 5),
    _MarsStatTxNakMsgs_Type()
)
marsStatTxNakMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxNakMsgs.setStatus("current")
_MarsStatTxJoinMsgs_Type = Counter32
_MarsStatTxJoinMsgs_Object = MibTableColumn
marsStatTxJoinMsgs = _MarsStatTxJoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 6),
    _MarsStatTxJoinMsgs_Type()
)
marsStatTxJoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxJoinMsgs.setStatus("current")
_MarsStatTxLeaveMsgs_Type = Counter32
_MarsStatTxLeaveMsgs_Object = MibTableColumn
marsStatTxLeaveMsgs = _MarsStatTxLeaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 7),
    _MarsStatTxLeaveMsgs_Type()
)
marsStatTxLeaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxLeaveMsgs.setStatus("current")
_MarsStatTxSjoinMsgs_Type = Counter32
_MarsStatTxSjoinMsgs_Object = MibTableColumn
marsStatTxSjoinMsgs = _MarsStatTxSjoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 8),
    _MarsStatTxSjoinMsgs_Type()
)
marsStatTxSjoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxSjoinMsgs.setStatus("current")
_MarsStatTxSleaveMsgs_Type = Counter32
_MarsStatTxSleaveMsgs_Object = MibTableColumn
marsStatTxSleaveMsgs = _MarsStatTxSleaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 9),
    _MarsStatTxSleaveMsgs_Type()
)
marsStatTxSleaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxSleaveMsgs.setStatus("current")
_MarsStatTxMservMsgs_Type = Counter32
_MarsStatTxMservMsgs_Object = MibTableColumn
marsStatTxMservMsgs = _MarsStatTxMservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 10),
    _MarsStatTxMservMsgs_Type()
)
marsStatTxMservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxMservMsgs.setStatus("current")
_MarsStatTxUnservMsgs_Type = Counter32
_MarsStatTxUnservMsgs_Object = MibTableColumn
marsStatTxUnservMsgs = _MarsStatTxUnservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 11),
    _MarsStatTxUnservMsgs_Type()
)
marsStatTxUnservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatTxUnservMsgs.setStatus("current")
_MarsStatRxReqMsgs_Type = Counter32
_MarsStatRxReqMsgs_Object = MibTableColumn
marsStatRxReqMsgs = _MarsStatRxReqMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 12),
    _MarsStatRxReqMsgs_Type()
)
marsStatRxReqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxReqMsgs.setStatus("current")
_MarsStatRxGrpLstReqMsgs_Type = Counter32
_MarsStatRxGrpLstReqMsgs_Object = MibTableColumn
marsStatRxGrpLstReqMsgs = _MarsStatRxGrpLstReqMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 13),
    _MarsStatRxGrpLstReqMsgs_Type()
)
marsStatRxGrpLstReqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxGrpLstReqMsgs.setStatus("current")
_MarsStatRxJoinMsgs_Type = Counter32
_MarsStatRxJoinMsgs_Object = MibTableColumn
marsStatRxJoinMsgs = _MarsStatRxJoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 14),
    _MarsStatRxJoinMsgs_Type()
)
marsStatRxJoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxJoinMsgs.setStatus("current")
_MarsStatRxLeaveMsgs_Type = Counter32
_MarsStatRxLeaveMsgs_Object = MibTableColumn
marsStatRxLeaveMsgs = _MarsStatRxLeaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 15),
    _MarsStatRxLeaveMsgs_Type()
)
marsStatRxLeaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxLeaveMsgs.setStatus("current")
_MarsStatRxMservMsgs_Type = Counter32
_MarsStatRxMservMsgs_Object = MibTableColumn
marsStatRxMservMsgs = _MarsStatRxMservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 16),
    _MarsStatRxMservMsgs_Type()
)
marsStatRxMservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxMservMsgs.setStatus("current")
_MarsStatRxUnservMsgs_Type = Counter32
_MarsStatRxUnservMsgs_Object = MibTableColumn
marsStatRxUnservMsgs = _MarsStatRxUnservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 17),
    _MarsStatRxUnservMsgs_Type()
)
marsStatRxUnservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxUnservMsgs.setStatus("current")
_MarsStatRxBlkJoinMsgs_Type = Counter32
_MarsStatRxBlkJoinMsgs_Object = MibTableColumn
marsStatRxBlkJoinMsgs = _MarsStatRxBlkJoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 18),
    _MarsStatRxBlkJoinMsgs_Type()
)
marsStatRxBlkJoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRxBlkJoinMsgs.setStatus("current")
_MarsStatRegMemGroups_Type = Counter32
_MarsStatRegMemGroups_Object = MibTableColumn
marsStatRegMemGroups = _MarsStatRegMemGroups_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 19),
    _MarsStatRegMemGroups_Type()
)
marsStatRegMemGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRegMemGroups.setStatus("current")
_MarsStatRegMcsGroups_Type = Counter32
_MarsStatRegMcsGroups_Object = MibTableColumn
marsStatRegMcsGroups = _MarsStatRegMcsGroups_Object(
    (1, 3, 6, 1, 2, 1, 57, 2, 8, 1, 20),
    _MarsStatRegMcsGroups_Type()
)
marsStatRegMcsGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsStatRegMcsGroups.setStatus("current")
_MarsMcsObjects_ObjectIdentity = ObjectIdentity
marsMcsObjects = _MarsMcsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 3)
)
_MarsMcsTable_Object = MibTable
marsMcsTable = _MarsMcsTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1)
)
if mibBuilder.loadTexts:
    marsMcsTable.setStatus("current")
_MarsMcsEntry_Object = MibTableRow
marsMcsEntry = _MarsMcsEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1)
)
marsMcsEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsMcsIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsIfIndex"),
)
if mibBuilder.loadTexts:
    marsMcsEntry.setStatus("current")


class _MarsMcsIndex_Type(Integer32):
    """Custom type marsMcsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsMcsIndex_Type.__name__ = "Integer32"
_MarsMcsIndex_Object = MibTableColumn
marsMcsIndex = _MarsMcsIndex_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 1),
    _MarsMcsIndex_Type()
)
marsMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsIndex.setStatus("current")
_MarsMcsIfIndex_Type = InterfaceIndex
_MarsMcsIfIndex_Object = MibTableColumn
marsMcsIfIndex = _MarsMcsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 2),
    _MarsMcsIfIndex_Type()
)
marsMcsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsIfIndex.setStatus("current")
_MarsMcsAddr_Type = AtmAddr
_MarsMcsAddr_Object = MibTableColumn
marsMcsAddr = _MarsMcsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 3),
    _MarsMcsAddr_Type()
)
marsMcsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsAddr.setStatus("current")
_MarsMcsDefaultMarsAddr_Type = AtmAddr
_MarsMcsDefaultMarsAddr_Object = MibTableColumn
marsMcsDefaultMarsAddr = _MarsMcsDefaultMarsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 4),
    _MarsMcsDefaultMarsAddr_Type()
)
marsMcsDefaultMarsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsDefaultMarsAddr.setStatus("current")


class _MarsMcsRegistration_Type(Integer32):
    """Custom type marsMcsRegistration based on Integer32"""
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
        *(("notRegistered", 1),
          ("reRegisteringFault", 4),
          ("reRegisteringRedirMap", 5),
          ("registered", 3),
          ("registering", 2))
    )


_MarsMcsRegistration_Type.__name__ = "Integer32"
_MarsMcsRegistration_Object = MibTableColumn
marsMcsRegistration = _MarsMcsRegistration_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 5),
    _MarsMcsRegistration_Type()
)
marsMcsRegistration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRegistration.setStatus("current")
_MarsMcsSsn_Type = Unsigned32
_MarsMcsSsn_Object = MibTableColumn
marsMcsSsn = _MarsMcsSsn_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 6),
    _MarsMcsSsn_Type()
)
marsMcsSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsSsn.setStatus("current")


class _MarsMcsDefaultMtu_Type(Integer32):
    """Custom type marsMcsDefaultMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsMcsDefaultMtu_Type.__name__ = "Integer32"
_MarsMcsDefaultMtu_Object = MibTableColumn
marsMcsDefaultMtu = _MarsMcsDefaultMtu_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 7),
    _MarsMcsDefaultMtu_Type()
)
marsMcsDefaultMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsDefaultMtu.setStatus("current")


class _MarsMcsFailureTimer_Type(Integer32):
    """Custom type marsMcsFailureTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsMcsFailureTimer_Type.__name__ = "Integer32"
_MarsMcsFailureTimer_Object = MibTableColumn
marsMcsFailureTimer = _MarsMcsFailureTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 8),
    _MarsMcsFailureTimer_Type()
)
marsMcsFailureTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsFailureTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsFailureTimer.setUnits("seconds")


class _MarsMcsRetranDelayTimer_Type(Integer32):
    """Custom type marsMcsRetranDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_MarsMcsRetranDelayTimer_Type.__name__ = "Integer32"
_MarsMcsRetranDelayTimer_Object = MibTableColumn
marsMcsRetranDelayTimer = _MarsMcsRetranDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 9),
    _MarsMcsRetranDelayTimer_Type()
)
marsMcsRetranDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRetranDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsRetranDelayTimer.setUnits("seconds")


class _MarsMcsRdmMulReqAddRetrTimer_Type(Integer32):
    """Custom type marsMcsRdmMulReqAddRetrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_MarsMcsRdmMulReqAddRetrTimer_Type.__name__ = "Integer32"
_MarsMcsRdmMulReqAddRetrTimer_Object = MibTableColumn
marsMcsRdmMulReqAddRetrTimer = _MarsMcsRdmMulReqAddRetrTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 10),
    _MarsMcsRdmMulReqAddRetrTimer_Type()
)
marsMcsRdmMulReqAddRetrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRdmMulReqAddRetrTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsRdmMulReqAddRetrTimer.setUnits("seconds")


class _MarsMcsRdmVcRevalidateTimer_Type(Integer32):
    """Custom type marsMcsRdmVcRevalidateTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MarsMcsRdmVcRevalidateTimer_Type.__name__ = "Integer32"
_MarsMcsRdmVcRevalidateTimer_Object = MibTableColumn
marsMcsRdmVcRevalidateTimer = _MarsMcsRdmVcRevalidateTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 11),
    _MarsMcsRdmVcRevalidateTimer_Type()
)
marsMcsRdmVcRevalidateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRdmVcRevalidateTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsRdmVcRevalidateTimer.setUnits("seconds")


class _MarsMcsRegisterRetrInterval_Type(Integer32):
    """Custom type marsMcsRegisterRetrInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_MarsMcsRegisterRetrInterval_Type.__name__ = "Integer32"
_MarsMcsRegisterRetrInterval_Object = MibTableColumn
marsMcsRegisterRetrInterval = _MarsMcsRegisterRetrInterval_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 12),
    _MarsMcsRegisterRetrInterval_Type()
)
marsMcsRegisterRetrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRegisterRetrInterval.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsRegisterRetrInterval.setUnits("seconds")


class _MarsMcsRegisterRetrLimit_Type(Integer32):
    """Custom type marsMcsRegisterRetrLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MarsMcsRegisterRetrLimit_Type.__name__ = "Integer32"
_MarsMcsRegisterRetrLimit_Object = MibTableColumn
marsMcsRegisterRetrLimit = _MarsMcsRegisterRetrLimit_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 13),
    _MarsMcsRegisterRetrLimit_Type()
)
marsMcsRegisterRetrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRegisterRetrLimit.setStatus("current")


class _MarsMcsRegWithMarsRdmTimer_Type(Integer32):
    """Custom type marsMcsRegWithMarsRdmTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MarsMcsRegWithMarsRdmTimer_Type.__name__ = "Integer32"
_MarsMcsRegWithMarsRdmTimer_Object = MibTableColumn
marsMcsRegWithMarsRdmTimer = _MarsMcsRegWithMarsRdmTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 14),
    _MarsMcsRegWithMarsRdmTimer_Type()
)
marsMcsRegWithMarsRdmTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRegWithMarsRdmTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsRegWithMarsRdmTimer.setUnits("seconds")


class _MarsMcsForceWaitTimer_Type(Integer32):
    """Custom type marsMcsForceWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsMcsForceWaitTimer_Type.__name__ = "Integer32"
_MarsMcsForceWaitTimer_Object = MibTableColumn
marsMcsForceWaitTimer = _MarsMcsForceWaitTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 15),
    _MarsMcsForceWaitTimer_Type()
)
marsMcsForceWaitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsForceWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsForceWaitTimer.setUnits("minutes")


class _MarsMcsLmtToMissRedirMapTimer_Type(Integer32):
    """Custom type marsMcsLmtToMissRedirMapTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MarsMcsLmtToMissRedirMapTimer_Type.__name__ = "Integer32"
_MarsMcsLmtToMissRedirMapTimer_Object = MibTableColumn
marsMcsLmtToMissRedirMapTimer = _MarsMcsLmtToMissRedirMapTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 16),
    _MarsMcsLmtToMissRedirMapTimer_Type()
)
marsMcsLmtToMissRedirMapTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsLmtToMissRedirMapTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsLmtToMissRedirMapTimer.setUnits("seconds")


class _MarsMcsIdleTimer_Type(Integer32):
    """Custom type marsMcsIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsMcsIdleTimer_Type.__name__ = "Integer32"
_MarsMcsIdleTimer_Object = MibTableColumn
marsMcsIdleTimer = _MarsMcsIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 17),
    _MarsMcsIdleTimer_Type()
)
marsMcsIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsIdleTimer.setUnits("minutes")
_MarsMcsRowStatus_Type = RowStatus
_MarsMcsRowStatus_Object = MibTableColumn
marsMcsRowStatus = _MarsMcsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 1, 1, 18),
    _MarsMcsRowStatus_Type()
)
marsMcsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsRowStatus.setStatus("current")
_MarsMcsMcGrpTable_Object = MibTable
marsMcsMcGrpTable = _MarsMcsMcGrpTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 2)
)
if mibBuilder.loadTexts:
    marsMcsMcGrpTable.setStatus("current")
_MarsMcsMcGrpEntry_Object = MibTableRow
marsMcsMcGrpEntry = _MarsMcsMcGrpEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 2, 1)
)
marsMcsMcGrpEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsMcsIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsMcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcsMcMaxGrpAddr"),
)
if mibBuilder.loadTexts:
    marsMcsMcGrpEntry.setStatus("current")
_MarsMcsMcMinGrpAddr_Type = IpAddress
_MarsMcsMcMinGrpAddr_Object = MibTableColumn
marsMcsMcMinGrpAddr = _MarsMcsMcMinGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 2, 1, 1),
    _MarsMcsMcMinGrpAddr_Type()
)
marsMcsMcMinGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsMcMinGrpAddr.setStatus("current")
_MarsMcsMcMaxGrpAddr_Type = IpAddress
_MarsMcsMcMaxGrpAddr_Object = MibTableColumn
marsMcsMcMaxGrpAddr = _MarsMcsMcMaxGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 2, 1, 2),
    _MarsMcsMcMaxGrpAddr_Type()
)
marsMcsMcMaxGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsMcMaxGrpAddr.setStatus("current")
_MarsMcsMcGrpRowStatus_Type = RowStatus
_MarsMcsMcGrpRowStatus_Object = MibTableColumn
marsMcsMcGrpRowStatus = _MarsMcsMcGrpRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 2, 1, 3),
    _MarsMcsMcGrpRowStatus_Type()
)
marsMcsMcGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsMcGrpRowStatus.setStatus("current")
_MarsMcsBackupMarsTable_Object = MibTable
marsMcsBackupMarsTable = _MarsMcsBackupMarsTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 3)
)
if mibBuilder.loadTexts:
    marsMcsBackupMarsTable.setStatus("current")
_MarsMcsBackupMarsEntry_Object = MibTableRow
marsMcsBackupMarsEntry = _MarsMcsBackupMarsEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 3, 1)
)
marsMcsBackupMarsEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsMcsIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsBackupMarsPriority"),
    (0, "IPATM-IPMC-MIB", "marsMcsBackupMarsAddr"),
)
if mibBuilder.loadTexts:
    marsMcsBackupMarsEntry.setStatus("current")


class _MarsMcsBackupMarsPriority_Type(Unsigned32):
    """Custom type marsMcsBackupMarsPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsMcsBackupMarsPriority_Type.__name__ = "Unsigned32"
_MarsMcsBackupMarsPriority_Object = MibTableColumn
marsMcsBackupMarsPriority = _MarsMcsBackupMarsPriority_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 3, 1, 1),
    _MarsMcsBackupMarsPriority_Type()
)
marsMcsBackupMarsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsBackupMarsPriority.setStatus("current")
_MarsMcsBackupMarsAddr_Type = AtmAddr
_MarsMcsBackupMarsAddr_Object = MibTableColumn
marsMcsBackupMarsAddr = _MarsMcsBackupMarsAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 3, 1, 2),
    _MarsMcsBackupMarsAddr_Type()
)
marsMcsBackupMarsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsBackupMarsAddr.setStatus("current")
_MarsMcsBackupMarsRowStatus_Type = RowStatus
_MarsMcsBackupMarsRowStatus_Object = MibTableColumn
marsMcsBackupMarsRowStatus = _MarsMcsBackupMarsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 3, 1, 3),
    _MarsMcsBackupMarsRowStatus_Type()
)
marsMcsBackupMarsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsBackupMarsRowStatus.setStatus("current")
_MarsMcsVcTable_Object = MibTable
marsMcsVcTable = _MarsMcsVcTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4)
)
if mibBuilder.loadTexts:
    marsMcsVcTable.setStatus("current")
_MarsMcsVcEntry_Object = MibTableRow
marsMcsVcEntry = _MarsMcsVcEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1)
)
marsMcsVcEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsMcsIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsIfIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsVcVpi"),
    (0, "IPATM-IPMC-MIB", "marsMcsVcVci"),
    (0, "IPATM-IPMC-MIB", "marsMcsVcMinGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcsVcMaxGrpAddr"),
    (0, "IPATM-IPMC-MIB", "marsMcsVcPartyAddr"),
)
if mibBuilder.loadTexts:
    marsMcsVcEntry.setStatus("current")


class _MarsMcsVcVpi_Type(Integer32):
    """Custom type marsMcsVcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MarsMcsVcVpi_Type.__name__ = "Integer32"
_MarsMcsVcVpi_Object = MibTableColumn
marsMcsVcVpi = _MarsMcsVcVpi_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 1),
    _MarsMcsVcVpi_Type()
)
marsMcsVcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsVcVpi.setStatus("current")


class _MarsMcsVcVci_Type(Integer32):
    """Custom type marsMcsVcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MarsMcsVcVci_Type.__name__ = "Integer32"
_MarsMcsVcVci_Object = MibTableColumn
marsMcsVcVci = _MarsMcsVcVci_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 2),
    _MarsMcsVcVci_Type()
)
marsMcsVcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsVcVci.setStatus("current")
_MarsMcsVcMinGrpAddr_Type = IpAddress
_MarsMcsVcMinGrpAddr_Object = MibTableColumn
marsMcsVcMinGrpAddr = _MarsMcsVcMinGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 3),
    _MarsMcsVcMinGrpAddr_Type()
)
marsMcsVcMinGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsVcMinGrpAddr.setStatus("current")
_MarsMcsVcMaxGrpAddr_Type = IpAddress
_MarsMcsVcMaxGrpAddr_Object = MibTableColumn
marsMcsVcMaxGrpAddr = _MarsMcsVcMaxGrpAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 4),
    _MarsMcsVcMaxGrpAddr_Type()
)
marsMcsVcMaxGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsVcMaxGrpAddr.setStatus("current")
_MarsMcsVcPartyAddr_Type = AtmAddr
_MarsMcsVcPartyAddr_Object = MibTableColumn
marsMcsVcPartyAddr = _MarsMcsVcPartyAddr_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 5),
    _MarsMcsVcPartyAddr_Type()
)
marsMcsVcPartyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    marsMcsVcPartyAddr.setStatus("current")


class _MarsMcsVcPartyAddrType_Type(Integer32):
    """Custom type marsMcsVcPartyAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 2))
    )


_MarsMcsVcPartyAddrType_Type.__name__ = "Integer32"
_MarsMcsVcPartyAddrType_Object = MibTableColumn
marsMcsVcPartyAddrType = _MarsMcsVcPartyAddrType_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 6),
    _MarsMcsVcPartyAddrType_Type()
)
marsMcsVcPartyAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcPartyAddrType.setStatus("current")


class _MarsMcsVcType_Type(Integer32):
    """Custom type marsMcsVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_MarsMcsVcType_Type.__name__ = "Integer32"
_MarsMcsVcType_Object = MibTableColumn
marsMcsVcType = _MarsMcsVcType_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 7),
    _MarsMcsVcType_Type()
)
marsMcsVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcType.setStatus("current")


class _MarsMcsVcCtrlType_Type(Integer32):
    """Custom type marsMcsVcCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultiPointVC", 3),
          ("pointToPointVC", 1),
          ("serverControlVC", 2))
    )


_MarsMcsVcCtrlType_Type.__name__ = "Integer32"
_MarsMcsVcCtrlType_Object = MibTableColumn
marsMcsVcCtrlType = _MarsMcsVcCtrlType_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 8),
    _MarsMcsVcCtrlType_Type()
)
marsMcsVcCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcCtrlType.setStatus("current")


class _MarsMcsVcIdleTimer_Type(Integer32):
    """Custom type marsMcsVcIdleTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MarsMcsVcIdleTimer_Type.__name__ = "Integer32"
_MarsMcsVcIdleTimer_Object = MibTableColumn
marsMcsVcIdleTimer = _MarsMcsVcIdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 9),
    _MarsMcsVcIdleTimer_Type()
)
marsMcsVcIdleTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcIdleTimer.setStatus("current")
if mibBuilder.loadTexts:
    marsMcsVcIdleTimer.setUnits("minutes")
_MarsMcsVcRevalidate_Type = TruthValue
_MarsMcsVcRevalidate_Object = MibTableColumn
marsMcsVcRevalidate = _MarsMcsVcRevalidate_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 10),
    _MarsMcsVcRevalidate_Type()
)
marsMcsVcRevalidate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcRevalidate.setStatus("current")


class _MarsMcsVcEncapsType_Type(Integer32):
    """Custom type marsMcsVcEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llcSnap", 2),
          ("other", 1))
    )


_MarsMcsVcEncapsType_Type.__name__ = "Integer32"
_MarsMcsVcEncapsType_Object = MibTableColumn
marsMcsVcEncapsType = _MarsMcsVcEncapsType_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 11),
    _MarsMcsVcEncapsType_Type()
)
marsMcsVcEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcEncapsType.setStatus("current")


class _MarsMcsVcNegotiatedMtu_Type(Integer32):
    """Custom type marsMcsVcNegotiatedMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MarsMcsVcNegotiatedMtu_Type.__name__ = "Integer32"
_MarsMcsVcNegotiatedMtu_Object = MibTableColumn
marsMcsVcNegotiatedMtu = _MarsMcsVcNegotiatedMtu_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 12),
    _MarsMcsVcNegotiatedMtu_Type()
)
marsMcsVcNegotiatedMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcNegotiatedMtu.setStatus("current")
_MarsMcsVcRowStatus_Type = RowStatus
_MarsMcsVcRowStatus_Object = MibTableColumn
marsMcsVcRowStatus = _MarsMcsVcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 4, 1, 13),
    _MarsMcsVcRowStatus_Type()
)
marsMcsVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    marsMcsVcRowStatus.setStatus("current")
_MarsMcsStatTable_Object = MibTable
marsMcsStatTable = _MarsMcsStatTable_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5)
)
if mibBuilder.loadTexts:
    marsMcsStatTable.setStatus("current")
_MarsMcsStatEntry_Object = MibTableRow
marsMcsStatEntry = _MarsMcsStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1)
)
marsMcsStatEntry.setIndexNames(
    (0, "IPATM-IPMC-MIB", "marsMcsIndex"),
    (0, "IPATM-IPMC-MIB", "marsMcsIfIndex"),
)
if mibBuilder.loadTexts:
    marsMcsStatEntry.setStatus("current")
_MarsMcsStatTxReqMsgs_Type = Counter32
_MarsMcsStatTxReqMsgs_Object = MibTableColumn
marsMcsStatTxReqMsgs = _MarsMcsStatTxReqMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 1),
    _MarsMcsStatTxReqMsgs_Type()
)
marsMcsStatTxReqMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatTxReqMsgs.setStatus("current")
_MarsMcsStatTxMservMsgs_Type = Counter32
_MarsMcsStatTxMservMsgs_Object = MibTableColumn
marsMcsStatTxMservMsgs = _MarsMcsStatTxMservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 2),
    _MarsMcsStatTxMservMsgs_Type()
)
marsMcsStatTxMservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatTxMservMsgs.setStatus("current")
_MarsMcsStatTxUnservMsgs_Type = Counter32
_MarsMcsStatTxUnservMsgs_Object = MibTableColumn
marsMcsStatTxUnservMsgs = _MarsMcsStatTxUnservMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 3),
    _MarsMcsStatTxUnservMsgs_Type()
)
marsMcsStatTxUnservMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatTxUnservMsgs.setStatus("current")
_MarsMcsStatRxMultiMsgs_Type = Counter32
_MarsMcsStatRxMultiMsgs_Object = MibTableColumn
marsMcsStatRxMultiMsgs = _MarsMcsStatRxMultiMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 4),
    _MarsMcsStatRxMultiMsgs_Type()
)
marsMcsStatRxMultiMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatRxMultiMsgs.setStatus("current")
_MarsMcsStatRxSjoinMsgs_Type = Counter32
_MarsMcsStatRxSjoinMsgs_Object = MibTableColumn
marsMcsStatRxSjoinMsgs = _MarsMcsStatRxSjoinMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 5),
    _MarsMcsStatRxSjoinMsgs_Type()
)
marsMcsStatRxSjoinMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatRxSjoinMsgs.setStatus("current")
_MarsMcsStatRxSleaveMsgs_Type = Counter32
_MarsMcsStatRxSleaveMsgs_Object = MibTableColumn
marsMcsStatRxSleaveMsgs = _MarsMcsStatRxSleaveMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 6),
    _MarsMcsStatRxSleaveMsgs_Type()
)
marsMcsStatRxSleaveMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatRxSleaveMsgs.setStatus("current")
_MarsMcsStatRxNakMsgs_Type = Counter32
_MarsMcsStatRxNakMsgs_Object = MibTableColumn
marsMcsStatRxNakMsgs = _MarsMcsStatRxNakMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 7),
    _MarsMcsStatRxNakMsgs_Type()
)
marsMcsStatRxNakMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatRxNakMsgs.setStatus("current")
_MarsMcsStatRxMigrateMsgs_Type = Counter32
_MarsMcsStatRxMigrateMsgs_Object = MibTableColumn
marsMcsStatRxMigrateMsgs = _MarsMcsStatRxMigrateMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 8),
    _MarsMcsStatRxMigrateMsgs_Type()
)
marsMcsStatRxMigrateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatRxMigrateMsgs.setStatus("current")
_MarsMcsStatFailMultiMsgs_Type = Counter32
_MarsMcsStatFailMultiMsgs_Object = MibTableColumn
marsMcsStatFailMultiMsgs = _MarsMcsStatFailMultiMsgs_Object(
    (1, 3, 6, 1, 2, 1, 57, 3, 5, 1, 9),
    _MarsMcsStatFailMultiMsgs_Type()
)
marsMcsStatFailMultiMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    marsMcsStatFailMultiMsgs.setStatus("current")
_MarsConformance_ObjectIdentity = ObjectIdentity
marsConformance = _MarsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4)
)
_MarsClientConformance_ObjectIdentity = ObjectIdentity
marsClientConformance = _MarsClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 1)
)
_MarsClientCompliances_ObjectIdentity = ObjectIdentity
marsClientCompliances = _MarsClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 1, 1)
)
_MarsClientGroups_ObjectIdentity = ObjectIdentity
marsClientGroups = _MarsClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 1, 2)
)
_MarsServerConformance_ObjectIdentity = ObjectIdentity
marsServerConformance = _MarsServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 2)
)
_MarsServerCompliances_ObjectIdentity = ObjectIdentity
marsServerCompliances = _MarsServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 2, 1)
)
_MarsServerGroups_ObjectIdentity = ObjectIdentity
marsServerGroups = _MarsServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 2, 2)
)
_MarsMcsConformance_ObjectIdentity = ObjectIdentity
marsMcsConformance = _MarsMcsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 3)
)
_MarsMcsCompliances_ObjectIdentity = ObjectIdentity
marsMcsCompliances = _MarsMcsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 3, 1)
)
_MarsMcsGroups_ObjectIdentity = ObjectIdentity
marsMcsGroups = _MarsMcsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 57, 4, 3, 2)
)

# Managed Objects groups

marsClientGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 57, 4, 1, 2, 1)
)
marsClientGroup.setObjects(
      *(("IPATM-IPMC-MIB", "marsClientAddr"),
        ("IPATM-IPMC-MIB", "marsClientDefaultMarsAddr"),
        ("IPATM-IPMC-MIB", "marsClientHsn"),
        ("IPATM-IPMC-MIB", "marsClientRegistration"),
        ("IPATM-IPMC-MIB", "marsClientCmi"),
        ("IPATM-IPMC-MIB", "marsClientDefaultMtu"),
        ("IPATM-IPMC-MIB", "marsClientFailureTimer"),
        ("IPATM-IPMC-MIB", "marsClientRetranDelayTimer"),
        ("IPATM-IPMC-MIB", "marsClientRdmMulReqAddRetrTimer"),
        ("IPATM-IPMC-MIB", "marsClientRdmVcRevalidateTimer"),
        ("IPATM-IPMC-MIB", "marsClientJoinLeaveRetrInterval"),
        ("IPATM-IPMC-MIB", "marsClientJoinLeaveRetrLimit"),
        ("IPATM-IPMC-MIB", "marsClientRegWithMarsRdmTimer"),
        ("IPATM-IPMC-MIB", "marsClientForceWaitTimer"),
        ("IPATM-IPMC-MIB", "marsClientIdleTimer"),
        ("IPATM-IPMC-MIB", "marsClientLmtToMissRedirMapTimer"),
        ("IPATM-IPMC-MIB", "marsClientRowStatus"),
        ("IPATM-IPMC-MIB", "marsClientMcGrpRowStatus"),
        ("IPATM-IPMC-MIB", "marsClientBackupMarsRowStatus"),
        ("IPATM-IPMC-MIB", "marsClientVcPartyAddrType"),
        ("IPATM-IPMC-MIB", "marsClientVcType"),
        ("IPATM-IPMC-MIB", "marsClientVcCtrlType"),
        ("IPATM-IPMC-MIB", "marsClientVcIdleTimer"),
        ("IPATM-IPMC-MIB", "marsClientVcRevalidate"),
        ("IPATM-IPMC-MIB", "marsClientVcEncapsType"),
        ("IPATM-IPMC-MIB", "marsClientVcNegotiatedMtu"),
        ("IPATM-IPMC-MIB", "marsClientVcRowStatus"),
        ("IPATM-IPMC-MIB", "marsClientStatTxReqMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatTxJoinMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatTxLeaveMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatTxGrpLstReqMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxJoinMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxLeaveMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxMultiMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxNakMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxGrpLstRplyMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatRxMigrateMsgs"),
        ("IPATM-IPMC-MIB", "marsClientStatFailMultiMsgs"))
)
if mibBuilder.loadTexts:
    marsClientGroup.setStatus("current")

marsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 57, 4, 2, 2, 1)
)
marsServerGroup.setObjects(
      *(("IPATM-IPMC-MIB", "marsAddr"),
        ("IPATM-IPMC-MIB", "marsLocal"),
        ("IPATM-IPMC-MIB", "marsServStatus"),
        ("IPATM-IPMC-MIB", "marsServType"),
        ("IPATM-IPMC-MIB", "marsServPriority"),
        ("IPATM-IPMC-MIB", "marsRedirMapMsgTimer"),
        ("IPATM-IPMC-MIB", "marsCsn"),
        ("IPATM-IPMC-MIB", "marsSsn"),
        ("IPATM-IPMC-MIB", "marsRowStatus"),
        ("IPATM-IPMC-MIB", "marsMcGrpAddrUsage"),
        ("IPATM-IPMC-MIB", "marsMcGrpRxLayer3GrpSets"),
        ("IPATM-IPMC-MIB", "marsMcGrpRxLayer3GrpResets"),
        ("IPATM-IPMC-MIB", "marsMcGrpRowStatus"),
        ("IPATM-IPMC-MIB", "marsHostMapRowType"),
        ("IPATM-IPMC-MIB", "marsHostMapRowStatus"),
        ("IPATM-IPMC-MIB", "marsServerMapRowType"),
        ("IPATM-IPMC-MIB", "marsServerMapRowStatus"),
        ("IPATM-IPMC-MIB", "marsVcPartyAddrType"),
        ("IPATM-IPMC-MIB", "marsVcType"),
        ("IPATM-IPMC-MIB", "marsVcCtrlType"),
        ("IPATM-IPMC-MIB", "marsVcIdleTimer"),
        ("IPATM-IPMC-MIB", "marsVcCmi"),
        ("IPATM-IPMC-MIB", "marsVcEncapsType"),
        ("IPATM-IPMC-MIB", "marsVcNegotiatedMtu"),
        ("IPATM-IPMC-MIB", "marsVcRowStatus"),
        ("IPATM-IPMC-MIB", "marsRegClientAtmAddr"),
        ("IPATM-IPMC-MIB", "marsRegMcsAtmAddr"),
        ("IPATM-IPMC-MIB", "marsStatTxMultiMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxGrpLstRplyMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxRedirectMapMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxMigrateMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxNakMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxJoinMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxLeaveMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxSjoinMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxSleaveMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxMservMsgs"),
        ("IPATM-IPMC-MIB", "marsStatTxUnservMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxReqMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxGrpLstReqMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxJoinMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxLeaveMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxMservMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxUnservMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRxBlkJoinMsgs"),
        ("IPATM-IPMC-MIB", "marsStatRegMemGroups"),
        ("IPATM-IPMC-MIB", "marsStatRegMcsGroups"))
)
if mibBuilder.loadTexts:
    marsServerGroup.setStatus("current")

marsMcsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 57, 4, 3, 2, 1)
)
marsMcsGroup.setObjects(
      *(("IPATM-IPMC-MIB", "marsMcsAddr"),
        ("IPATM-IPMC-MIB", "marsMcsDefaultMarsAddr"),
        ("IPATM-IPMC-MIB", "marsMcsRegistration"),
        ("IPATM-IPMC-MIB", "marsMcsSsn"),
        ("IPATM-IPMC-MIB", "marsMcsDefaultMtu"),
        ("IPATM-IPMC-MIB", "marsMcsFailureTimer"),
        ("IPATM-IPMC-MIB", "marsMcsRetranDelayTimer"),
        ("IPATM-IPMC-MIB", "marsMcsRdmMulReqAddRetrTimer"),
        ("IPATM-IPMC-MIB", "marsMcsRdmVcRevalidateTimer"),
        ("IPATM-IPMC-MIB", "marsMcsRegisterRetrInterval"),
        ("IPATM-IPMC-MIB", "marsMcsRegisterRetrLimit"),
        ("IPATM-IPMC-MIB", "marsMcsRegWithMarsRdmTimer"),
        ("IPATM-IPMC-MIB", "marsMcsForceWaitTimer"),
        ("IPATM-IPMC-MIB", "marsMcsIdleTimer"),
        ("IPATM-IPMC-MIB", "marsMcsLmtToMissRedirMapTimer"),
        ("IPATM-IPMC-MIB", "marsMcsRowStatus"),
        ("IPATM-IPMC-MIB", "marsMcsMcGrpRowStatus"),
        ("IPATM-IPMC-MIB", "marsMcsVcPartyAddrType"),
        ("IPATM-IPMC-MIB", "marsMcsBackupMarsRowStatus"),
        ("IPATM-IPMC-MIB", "marsMcsVcType"),
        ("IPATM-IPMC-MIB", "marsMcsVcCtrlType"),
        ("IPATM-IPMC-MIB", "marsMcsVcIdleTimer"),
        ("IPATM-IPMC-MIB", "marsMcsVcRevalidate"),
        ("IPATM-IPMC-MIB", "marsMcsVcEncapsType"),
        ("IPATM-IPMC-MIB", "marsMcsVcNegotiatedMtu"),
        ("IPATM-IPMC-MIB", "marsMcsVcRowStatus"),
        ("IPATM-IPMC-MIB", "marsMcsStatTxReqMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatTxMservMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatTxUnservMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatRxMultiMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatRxSjoinMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatRxSleaveMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatRxNakMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatRxMigrateMsgs"),
        ("IPATM-IPMC-MIB", "marsMcsStatFailMultiMsgs"))
)
if mibBuilder.loadTexts:
    marsMcsGroup.setStatus("current")


# Notification objects

marsFaultTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 57, 0, 1)
)
marsFaultTrap.setObjects(
      *(("IPATM-IPMC-MIB", "marsAddr"),
        ("IPATM-IPMC-MIB", "marsServStatus"))
)
if mibBuilder.loadTexts:
    marsFaultTrap.setStatus(
        "current"
    )


# Notifications groups

marsServerEventGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 57, 4, 2, 2, 2)
)
marsServerEventGroup.setObjects(
    ("IPATM-IPMC-MIB", "marsFaultTrap")
)
if mibBuilder.loadTexts:
    marsServerEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

marsClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 57, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    marsClientCompliance.setStatus(
        "current"
    )

marsServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 57, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    marsServerCompliance.setStatus(
        "current"
    )

marsMcsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 57, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    marsMcsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPATM-IPMC-MIB",
    **{"marsMIB": marsMIB,
       "marsTrapInfo": marsTrapInfo,
       "marsFaultTrap": marsFaultTrap,
       "marsClientObjects": marsClientObjects,
       "marsClientTable": marsClientTable,
       "marsClientEntry": marsClientEntry,
       "marsClientIndex": marsClientIndex,
       "marsClientAddr": marsClientAddr,
       "marsClientDefaultMarsAddr": marsClientDefaultMarsAddr,
       "marsClientHsn": marsClientHsn,
       "marsClientRegistration": marsClientRegistration,
       "marsClientCmi": marsClientCmi,
       "marsClientDefaultMtu": marsClientDefaultMtu,
       "marsClientFailureTimer": marsClientFailureTimer,
       "marsClientRetranDelayTimer": marsClientRetranDelayTimer,
       "marsClientRdmMulReqAddRetrTimer": marsClientRdmMulReqAddRetrTimer,
       "marsClientRdmVcRevalidateTimer": marsClientRdmVcRevalidateTimer,
       "marsClientJoinLeaveRetrInterval": marsClientJoinLeaveRetrInterval,
       "marsClientJoinLeaveRetrLimit": marsClientJoinLeaveRetrLimit,
       "marsClientRegWithMarsRdmTimer": marsClientRegWithMarsRdmTimer,
       "marsClientForceWaitTimer": marsClientForceWaitTimer,
       "marsClientLmtToMissRedirMapTimer": marsClientLmtToMissRedirMapTimer,
       "marsClientIdleTimer": marsClientIdleTimer,
       "marsClientRowStatus": marsClientRowStatus,
       "marsClientMcGrpTable": marsClientMcGrpTable,
       "marsClientMcGrpEntry": marsClientMcGrpEntry,
       "marsClientMcMinGrpAddr": marsClientMcMinGrpAddr,
       "marsClientMcMaxGrpAddr": marsClientMcMaxGrpAddr,
       "marsClientMcGrpRowStatus": marsClientMcGrpRowStatus,
       "marsClientBackupMarsTable": marsClientBackupMarsTable,
       "marsClientBackupMarsEntry": marsClientBackupMarsEntry,
       "marsClientBackupMarsPriority": marsClientBackupMarsPriority,
       "marsClientBackupMarsAddr": marsClientBackupMarsAddr,
       "marsClientBackupMarsRowStatus": marsClientBackupMarsRowStatus,
       "marsClientVcTable": marsClientVcTable,
       "marsClientVcEntry": marsClientVcEntry,
       "marsClientVcVpi": marsClientVcVpi,
       "marsClientVcVci": marsClientVcVci,
       "marsClientVcMinGrpAddr": marsClientVcMinGrpAddr,
       "marsClientVcMaxGrpAddr": marsClientVcMaxGrpAddr,
       "marsClientVcPartyAddr": marsClientVcPartyAddr,
       "marsClientVcPartyAddrType": marsClientVcPartyAddrType,
       "marsClientVcType": marsClientVcType,
       "marsClientVcCtrlType": marsClientVcCtrlType,
       "marsClientVcIdleTimer": marsClientVcIdleTimer,
       "marsClientVcRevalidate": marsClientVcRevalidate,
       "marsClientVcEncapsType": marsClientVcEncapsType,
       "marsClientVcNegotiatedMtu": marsClientVcNegotiatedMtu,
       "marsClientVcRowStatus": marsClientVcRowStatus,
       "marsClientStatTable": marsClientStatTable,
       "marsClientStatEntry": marsClientStatEntry,
       "marsClientStatTxReqMsgs": marsClientStatTxReqMsgs,
       "marsClientStatTxJoinMsgs": marsClientStatTxJoinMsgs,
       "marsClientStatTxLeaveMsgs": marsClientStatTxLeaveMsgs,
       "marsClientStatTxGrpLstReqMsgs": marsClientStatTxGrpLstReqMsgs,
       "marsClientStatRxJoinMsgs": marsClientStatRxJoinMsgs,
       "marsClientStatRxLeaveMsgs": marsClientStatRxLeaveMsgs,
       "marsClientStatRxMultiMsgs": marsClientStatRxMultiMsgs,
       "marsClientStatRxNakMsgs": marsClientStatRxNakMsgs,
       "marsClientStatRxMigrateMsgs": marsClientStatRxMigrateMsgs,
       "marsClientStatRxGrpLstRplyMsgs": marsClientStatRxGrpLstRplyMsgs,
       "marsClientStatFailMultiMsgs": marsClientStatFailMultiMsgs,
       "marsObjects": marsObjects,
       "marsTable": marsTable,
       "marsEntry": marsEntry,
       "marsIndex": marsIndex,
       "marsIfIndex": marsIfIndex,
       "marsAddr": marsAddr,
       "marsLocal": marsLocal,
       "marsServStatus": marsServStatus,
       "marsServType": marsServType,
       "marsServPriority": marsServPriority,
       "marsRedirMapMsgTimer": marsRedirMapMsgTimer,
       "marsCsn": marsCsn,
       "marsSsn": marsSsn,
       "marsRowStatus": marsRowStatus,
       "marsMcGrpTable": marsMcGrpTable,
       "marsMcGrpEntry": marsMcGrpEntry,
       "marsMcMinGrpAddr": marsMcMinGrpAddr,
       "marsMcMaxGrpAddr": marsMcMaxGrpAddr,
       "marsMcGrpAddrUsage": marsMcGrpAddrUsage,
       "marsMcGrpRxLayer3GrpSets": marsMcGrpRxLayer3GrpSets,
       "marsMcGrpRxLayer3GrpResets": marsMcGrpRxLayer3GrpResets,
       "marsMcGrpRowStatus": marsMcGrpRowStatus,
       "marsHostMapTable": marsHostMapTable,
       "marsHostMapEntry": marsHostMapEntry,
       "marsHostMapAtmAddr": marsHostMapAtmAddr,
       "marsHostMapRowType": marsHostMapRowType,
       "marsHostMapRowStatus": marsHostMapRowStatus,
       "marsServerMapTable": marsServerMapTable,
       "marsServerMapEntry": marsServerMapEntry,
       "marsServerMapAtmAddr": marsServerMapAtmAddr,
       "marsServerMapRowType": marsServerMapRowType,
       "marsServerMapRowStatus": marsServerMapRowStatus,
       "marsVcTable": marsVcTable,
       "marsVcEntry": marsVcEntry,
       "marsVcVpi": marsVcVpi,
       "marsVcVci": marsVcVci,
       "marsVcPartyAddr": marsVcPartyAddr,
       "marsVcPartyAddrType": marsVcPartyAddrType,
       "marsVcType": marsVcType,
       "marsVcCtrlType": marsVcCtrlType,
       "marsVcIdleTimer": marsVcIdleTimer,
       "marsVcCmi": marsVcCmi,
       "marsVcEncapsType": marsVcEncapsType,
       "marsVcNegotiatedMtu": marsVcNegotiatedMtu,
       "marsVcRowStatus": marsVcRowStatus,
       "marsRegClientTable": marsRegClientTable,
       "marsRegClientEntry": marsRegClientEntry,
       "marsRegClientCmi": marsRegClientCmi,
       "marsRegClientAtmAddr": marsRegClientAtmAddr,
       "marsRegMcsTable": marsRegMcsTable,
       "marsRegMcsEntry": marsRegMcsEntry,
       "marsRegMcsAtmAddr": marsRegMcsAtmAddr,
       "marsStatTable": marsStatTable,
       "marsStatEntry": marsStatEntry,
       "marsStatTxMultiMsgs": marsStatTxMultiMsgs,
       "marsStatTxGrpLstRplyMsgs": marsStatTxGrpLstRplyMsgs,
       "marsStatTxRedirectMapMsgs": marsStatTxRedirectMapMsgs,
       "marsStatTxMigrateMsgs": marsStatTxMigrateMsgs,
       "marsStatTxNakMsgs": marsStatTxNakMsgs,
       "marsStatTxJoinMsgs": marsStatTxJoinMsgs,
       "marsStatTxLeaveMsgs": marsStatTxLeaveMsgs,
       "marsStatTxSjoinMsgs": marsStatTxSjoinMsgs,
       "marsStatTxSleaveMsgs": marsStatTxSleaveMsgs,
       "marsStatTxMservMsgs": marsStatTxMservMsgs,
       "marsStatTxUnservMsgs": marsStatTxUnservMsgs,
       "marsStatRxReqMsgs": marsStatRxReqMsgs,
       "marsStatRxGrpLstReqMsgs": marsStatRxGrpLstReqMsgs,
       "marsStatRxJoinMsgs": marsStatRxJoinMsgs,
       "marsStatRxLeaveMsgs": marsStatRxLeaveMsgs,
       "marsStatRxMservMsgs": marsStatRxMservMsgs,
       "marsStatRxUnservMsgs": marsStatRxUnservMsgs,
       "marsStatRxBlkJoinMsgs": marsStatRxBlkJoinMsgs,
       "marsStatRegMemGroups": marsStatRegMemGroups,
       "marsStatRegMcsGroups": marsStatRegMcsGroups,
       "marsMcsObjects": marsMcsObjects,
       "marsMcsTable": marsMcsTable,
       "marsMcsEntry": marsMcsEntry,
       "marsMcsIndex": marsMcsIndex,
       "marsMcsIfIndex": marsMcsIfIndex,
       "marsMcsAddr": marsMcsAddr,
       "marsMcsDefaultMarsAddr": marsMcsDefaultMarsAddr,
       "marsMcsRegistration": marsMcsRegistration,
       "marsMcsSsn": marsMcsSsn,
       "marsMcsDefaultMtu": marsMcsDefaultMtu,
       "marsMcsFailureTimer": marsMcsFailureTimer,
       "marsMcsRetranDelayTimer": marsMcsRetranDelayTimer,
       "marsMcsRdmMulReqAddRetrTimer": marsMcsRdmMulReqAddRetrTimer,
       "marsMcsRdmVcRevalidateTimer": marsMcsRdmVcRevalidateTimer,
       "marsMcsRegisterRetrInterval": marsMcsRegisterRetrInterval,
       "marsMcsRegisterRetrLimit": marsMcsRegisterRetrLimit,
       "marsMcsRegWithMarsRdmTimer": marsMcsRegWithMarsRdmTimer,
       "marsMcsForceWaitTimer": marsMcsForceWaitTimer,
       "marsMcsLmtToMissRedirMapTimer": marsMcsLmtToMissRedirMapTimer,
       "marsMcsIdleTimer": marsMcsIdleTimer,
       "marsMcsRowStatus": marsMcsRowStatus,
       "marsMcsMcGrpTable": marsMcsMcGrpTable,
       "marsMcsMcGrpEntry": marsMcsMcGrpEntry,
       "marsMcsMcMinGrpAddr": marsMcsMcMinGrpAddr,
       "marsMcsMcMaxGrpAddr": marsMcsMcMaxGrpAddr,
       "marsMcsMcGrpRowStatus": marsMcsMcGrpRowStatus,
       "marsMcsBackupMarsTable": marsMcsBackupMarsTable,
       "marsMcsBackupMarsEntry": marsMcsBackupMarsEntry,
       "marsMcsBackupMarsPriority": marsMcsBackupMarsPriority,
       "marsMcsBackupMarsAddr": marsMcsBackupMarsAddr,
       "marsMcsBackupMarsRowStatus": marsMcsBackupMarsRowStatus,
       "marsMcsVcTable": marsMcsVcTable,
       "marsMcsVcEntry": marsMcsVcEntry,
       "marsMcsVcVpi": marsMcsVcVpi,
       "marsMcsVcVci": marsMcsVcVci,
       "marsMcsVcMinGrpAddr": marsMcsVcMinGrpAddr,
       "marsMcsVcMaxGrpAddr": marsMcsVcMaxGrpAddr,
       "marsMcsVcPartyAddr": marsMcsVcPartyAddr,
       "marsMcsVcPartyAddrType": marsMcsVcPartyAddrType,
       "marsMcsVcType": marsMcsVcType,
       "marsMcsVcCtrlType": marsMcsVcCtrlType,
       "marsMcsVcIdleTimer": marsMcsVcIdleTimer,
       "marsMcsVcRevalidate": marsMcsVcRevalidate,
       "marsMcsVcEncapsType": marsMcsVcEncapsType,
       "marsMcsVcNegotiatedMtu": marsMcsVcNegotiatedMtu,
       "marsMcsVcRowStatus": marsMcsVcRowStatus,
       "marsMcsStatTable": marsMcsStatTable,
       "marsMcsStatEntry": marsMcsStatEntry,
       "marsMcsStatTxReqMsgs": marsMcsStatTxReqMsgs,
       "marsMcsStatTxMservMsgs": marsMcsStatTxMservMsgs,
       "marsMcsStatTxUnservMsgs": marsMcsStatTxUnservMsgs,
       "marsMcsStatRxMultiMsgs": marsMcsStatRxMultiMsgs,
       "marsMcsStatRxSjoinMsgs": marsMcsStatRxSjoinMsgs,
       "marsMcsStatRxSleaveMsgs": marsMcsStatRxSleaveMsgs,
       "marsMcsStatRxNakMsgs": marsMcsStatRxNakMsgs,
       "marsMcsStatRxMigrateMsgs": marsMcsStatRxMigrateMsgs,
       "marsMcsStatFailMultiMsgs": marsMcsStatFailMultiMsgs,
       "marsConformance": marsConformance,
       "marsClientConformance": marsClientConformance,
       "marsClientCompliances": marsClientCompliances,
       "marsClientCompliance": marsClientCompliance,
       "marsClientGroups": marsClientGroups,
       "marsClientGroup": marsClientGroup,
       "marsServerConformance": marsServerConformance,
       "marsServerCompliances": marsServerCompliances,
       "marsServerCompliance": marsServerCompliance,
       "marsServerGroups": marsServerGroups,
       "marsServerGroup": marsServerGroup,
       "marsServerEventGroup": marsServerEventGroup,
       "marsMcsConformance": marsMcsConformance,
       "marsMcsCompliances": marsMcsCompliances,
       "marsMcsCompliance": marsMcsCompliance,
       "marsMcsGroups": marsMcsGroups,
       "marsMcsGroup": marsMcsGroup}
)
