# SNMP MIB module (BAS-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:34 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasTcp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasTcp")

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

basAliasTcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasTcpObjects_ObjectIdentity = ObjectIdentity
basTcpObjects = _BasTcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1)
)
_BasTcpTable_Object = MibTable
basTcpTable = _BasTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basTcpTable.setStatus("current")
_BasTcpEntry_Object = MibTableRow
basTcpEntry = _BasTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1)
)
basTcpEntry.setIndexNames(
    (0, "BAS-TCP-MIB", "basTcpChassis"),
    (0, "BAS-TCP-MIB", "basTcpSlot"),
    (0, "BAS-TCP-MIB", "basTcpIf"),
    (0, "BAS-TCP-MIB", "basTcpLPort"),
)
if mibBuilder.loadTexts:
    basTcpEntry.setStatus("current")


class _BasTcpRtoAlgorithm_Type(Integer32):
    """Custom type basTcpRtoAlgorithm based on Integer32"""
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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_BasTcpRtoAlgorithm_Type.__name__ = "Integer32"
_BasTcpRtoAlgorithm_Object = MibTableColumn
basTcpRtoAlgorithm = _BasTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 1),
    _BasTcpRtoAlgorithm_Type()
)
basTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpRtoAlgorithm.setStatus("current")
_BasTcpRtoMin_Type = Integer32
_BasTcpRtoMin_Object = MibTableColumn
basTcpRtoMin = _BasTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 2),
    _BasTcpRtoMin_Type()
)
basTcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    basTcpRtoMin.setUnits("milliseconds")
_BasTcpRtoMax_Type = Integer32
_BasTcpRtoMax_Object = MibTableColumn
basTcpRtoMax = _BasTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 3),
    _BasTcpRtoMax_Type()
)
basTcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    basTcpRtoMax.setUnits("milliseconds")
_BasTcpMaxConn_Type = Integer32
_BasTcpMaxConn_Object = MibTableColumn
basTcpMaxConn = _BasTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 4),
    _BasTcpMaxConn_Type()
)
basTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpMaxConn.setStatus("current")
_BasTcpActiveOpens_Type = Counter32
_BasTcpActiveOpens_Object = MibTableColumn
basTcpActiveOpens = _BasTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 5),
    _BasTcpActiveOpens_Type()
)
basTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpActiveOpens.setStatus("current")
_BasTcpPassiveOpens_Type = Counter32
_BasTcpPassiveOpens_Object = MibTableColumn
basTcpPassiveOpens = _BasTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 6),
    _BasTcpPassiveOpens_Type()
)
basTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpPassiveOpens.setStatus("current")
_BasTcpAttemptFails_Type = Counter32
_BasTcpAttemptFails_Object = MibTableColumn
basTcpAttemptFails = _BasTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 7),
    _BasTcpAttemptFails_Type()
)
basTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpAttemptFails.setStatus("current")
_BasTcpEstabResets_Type = Counter32
_BasTcpEstabResets_Object = MibTableColumn
basTcpEstabResets = _BasTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 8),
    _BasTcpEstabResets_Type()
)
basTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpEstabResets.setStatus("current")
_BasTcpCurrEstab_Type = Gauge32
_BasTcpCurrEstab_Object = MibTableColumn
basTcpCurrEstab = _BasTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 9),
    _BasTcpCurrEstab_Type()
)
basTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpCurrEstab.setStatus("current")
_BasTcpInSegs_Type = Counter32
_BasTcpInSegs_Object = MibTableColumn
basTcpInSegs = _BasTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 10),
    _BasTcpInSegs_Type()
)
basTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpInSegs.setStatus("current")
_BasTcpOutSegs_Type = Counter32
_BasTcpOutSegs_Object = MibTableColumn
basTcpOutSegs = _BasTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 11),
    _BasTcpOutSegs_Type()
)
basTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpOutSegs.setStatus("current")
_BasTcpRetransSegs_Type = Counter32
_BasTcpRetransSegs_Object = MibTableColumn
basTcpRetransSegs = _BasTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 12),
    _BasTcpRetransSegs_Type()
)
basTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpRetransSegs.setStatus("current")
_BasTcpChassis_Type = BasChassisId
_BasTcpChassis_Object = MibTableColumn
basTcpChassis = _BasTcpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 13),
    _BasTcpChassis_Type()
)
basTcpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpChassis.setStatus("current")
_BasTcpSlot_Type = BasSlotId
_BasTcpSlot_Object = MibTableColumn
basTcpSlot = _BasTcpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 14),
    _BasTcpSlot_Type()
)
basTcpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpSlot.setStatus("current")
_BasTcpIf_Type = BasInterfaceId
_BasTcpIf_Object = MibTableColumn
basTcpIf = _BasTcpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 15),
    _BasTcpIf_Type()
)
basTcpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpIf.setStatus("current")
_BasTcpLPort_Type = BasLogicalPortId
_BasTcpLPort_Object = MibTableColumn
basTcpLPort = _BasTcpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 1, 1, 16),
    _BasTcpLPort_Type()
)
basTcpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpLPort.setStatus("current")
_BasTcpConnTable_Object = MibTable
basTcpConnTable = _BasTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basTcpConnTable.setStatus("current")
_BasTcpConnEntry_Object = MibTableRow
basTcpConnEntry = _BasTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1)
)
basTcpConnEntry.setIndexNames(
    (0, "BAS-TCP-MIB", "basTcpConnChassis"),
    (0, "BAS-TCP-MIB", "basTcpConnSlot"),
    (0, "BAS-TCP-MIB", "basTcpConnIf"),
    (0, "BAS-TCP-MIB", "basTcpConnLPort"),
    (0, "BAS-TCP-MIB", "basTcpConnLocalAddress"),
    (0, "BAS-TCP-MIB", "basTcpConnLocalPort"),
    (0, "BAS-TCP-MIB", "basTcpConnRemAddress"),
    (0, "BAS-TCP-MIB", "basTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    basTcpConnEntry.setStatus("current")


class _BasTcpConnState_Type(Integer32):
    """Custom type basTcpConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_BasTcpConnState_Type.__name__ = "Integer32"
_BasTcpConnState_Object = MibTableColumn
basTcpConnState = _BasTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 1),
    _BasTcpConnState_Type()
)
basTcpConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basTcpConnState.setStatus("current")
_BasTcpConnLocalAddress_Type = IpAddress
_BasTcpConnLocalAddress_Object = MibTableColumn
basTcpConnLocalAddress = _BasTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 2),
    _BasTcpConnLocalAddress_Type()
)
basTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpConnLocalAddress.setStatus("current")


class _BasTcpConnLocalPort_Type(Integer32):
    """Custom type basTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasTcpConnLocalPort_Type.__name__ = "Integer32"
_BasTcpConnLocalPort_Object = MibTableColumn
basTcpConnLocalPort = _BasTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 3),
    _BasTcpConnLocalPort_Type()
)
basTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpConnLocalPort.setStatus("current")
_BasTcpConnRemAddress_Type = IpAddress
_BasTcpConnRemAddress_Object = MibTableColumn
basTcpConnRemAddress = _BasTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 4),
    _BasTcpConnRemAddress_Type()
)
basTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpConnRemAddress.setStatus("current")


class _BasTcpConnRemPort_Type(Integer32):
    """Custom type basTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasTcpConnRemPort_Type.__name__ = "Integer32"
_BasTcpConnRemPort_Object = MibTableColumn
basTcpConnRemPort = _BasTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 5),
    _BasTcpConnRemPort_Type()
)
basTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpConnRemPort.setStatus("current")
_BasTcpConnChassis_Type = BasChassisId
_BasTcpConnChassis_Object = MibTableColumn
basTcpConnChassis = _BasTcpConnChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 6),
    _BasTcpConnChassis_Type()
)
basTcpConnChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpConnChassis.setStatus("current")
_BasTcpConnSlot_Type = BasSlotId
_BasTcpConnSlot_Object = MibTableColumn
basTcpConnSlot = _BasTcpConnSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 7),
    _BasTcpConnSlot_Type()
)
basTcpConnSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpConnSlot.setStatus("current")
_BasTcpConnIf_Type = BasInterfaceId
_BasTcpConnIf_Object = MibTableColumn
basTcpConnIf = _BasTcpConnIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 8),
    _BasTcpConnIf_Type()
)
basTcpConnIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpConnIf.setStatus("current")
_BasTcpConnLPort_Type = BasLogicalPortId
_BasTcpConnLPort_Object = MibTableColumn
basTcpConnLPort = _BasTcpConnLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 2, 1, 9),
    _BasTcpConnLPort_Type()
)
basTcpConnLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpConnLPort.setStatus("current")
_BasTcpStatsTable_Object = MibTable
basTcpStatsTable = _BasTcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    basTcpStatsTable.setStatus("current")
_BasTcpStatsEntry_Object = MibTableRow
basTcpStatsEntry = _BasTcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1)
)
basTcpStatsEntry.setIndexNames(
    (0, "BAS-TCP-MIB", "basTcpStatsChassis"),
    (0, "BAS-TCP-MIB", "basTcpStatsSlot"),
    (0, "BAS-TCP-MIB", "basTcpStatsIf"),
    (0, "BAS-TCP-MIB", "basTcpStatsLPort"),
)
if mibBuilder.loadTexts:
    basTcpStatsEntry.setStatus("current")
_BasTcpInErrs_Type = Counter32
_BasTcpInErrs_Object = MibTableColumn
basTcpInErrs = _BasTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 1),
    _BasTcpInErrs_Type()
)
basTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpInErrs.setStatus("current")
_BasTcpOutRsts_Type = Counter32
_BasTcpOutRsts_Object = MibTableColumn
basTcpOutRsts = _BasTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 2),
    _BasTcpOutRsts_Type()
)
basTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basTcpOutRsts.setStatus("current")
_BasTcpStatsChassis_Type = BasChassisId
_BasTcpStatsChassis_Object = MibTableColumn
basTcpStatsChassis = _BasTcpStatsChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 3),
    _BasTcpStatsChassis_Type()
)
basTcpStatsChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpStatsChassis.setStatus("current")
_BasTcpStatsSlot_Type = BasSlotId
_BasTcpStatsSlot_Object = MibTableColumn
basTcpStatsSlot = _BasTcpStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 4),
    _BasTcpStatsSlot_Type()
)
basTcpStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpStatsSlot.setStatus("current")
_BasTcpStatsIf_Type = BasInterfaceId
_BasTcpStatsIf_Object = MibTableColumn
basTcpStatsIf = _BasTcpStatsIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 5),
    _BasTcpStatsIf_Type()
)
basTcpStatsIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpStatsIf.setStatus("current")
_BasTcpStatsLPort_Type = BasLogicalPortId
_BasTcpStatsLPort_Object = MibTableColumn
basTcpStatsLPort = _BasTcpStatsLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 3, 1, 1, 3, 1, 6),
    _BasTcpStatsLPort_Type()
)
basTcpStatsLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basTcpStatsLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-TCP-MIB",
    **{"basAliasTcpMib": basAliasTcpMib,
       "basTcpObjects": basTcpObjects,
       "basTcpTable": basTcpTable,
       "basTcpEntry": basTcpEntry,
       "basTcpRtoAlgorithm": basTcpRtoAlgorithm,
       "basTcpRtoMin": basTcpRtoMin,
       "basTcpRtoMax": basTcpRtoMax,
       "basTcpMaxConn": basTcpMaxConn,
       "basTcpActiveOpens": basTcpActiveOpens,
       "basTcpPassiveOpens": basTcpPassiveOpens,
       "basTcpAttemptFails": basTcpAttemptFails,
       "basTcpEstabResets": basTcpEstabResets,
       "basTcpCurrEstab": basTcpCurrEstab,
       "basTcpInSegs": basTcpInSegs,
       "basTcpOutSegs": basTcpOutSegs,
       "basTcpRetransSegs": basTcpRetransSegs,
       "basTcpChassis": basTcpChassis,
       "basTcpSlot": basTcpSlot,
       "basTcpIf": basTcpIf,
       "basTcpLPort": basTcpLPort,
       "basTcpConnTable": basTcpConnTable,
       "basTcpConnEntry": basTcpConnEntry,
       "basTcpConnState": basTcpConnState,
       "basTcpConnLocalAddress": basTcpConnLocalAddress,
       "basTcpConnLocalPort": basTcpConnLocalPort,
       "basTcpConnRemAddress": basTcpConnRemAddress,
       "basTcpConnRemPort": basTcpConnRemPort,
       "basTcpConnChassis": basTcpConnChassis,
       "basTcpConnSlot": basTcpConnSlot,
       "basTcpConnIf": basTcpConnIf,
       "basTcpConnLPort": basTcpConnLPort,
       "basTcpStatsTable": basTcpStatsTable,
       "basTcpStatsEntry": basTcpStatsEntry,
       "basTcpInErrs": basTcpInErrs,
       "basTcpOutRsts": basTcpOutRsts,
       "basTcpStatsChassis": basTcpStatsChassis,
       "basTcpStatsSlot": basTcpStatsSlot,
       "basTcpStatsIf": basTcpStatsIf,
       "basTcpStatsLPort": basTcpStatsLPort}
)
