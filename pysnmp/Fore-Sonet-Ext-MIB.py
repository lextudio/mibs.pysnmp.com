# SNMP MIB module (Fore-Sonet-Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Sonet-Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:16 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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

(sonetFarEndLineIntervalNumber,
 sonetFarEndPathIntervalNumber,
 sonetFarEndVTIntervalNumber,
 sonetLineIntervalNumber,
 sonetPathIntervalNumber,
 sonetSectionIntervalNumber,
 sonetVTIntervalNumber) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetFarEndLineIntervalNumber",
    "sonetFarEndPathIntervalNumber",
    "sonetFarEndVTIntervalNumber",
    "sonetLineIntervalNumber",
    "sonetPathIntervalNumber",
    "sonetSectionIntervalNumber",
    "sonetVTIntervalNumber")


# MODULE-IDENTITY

foreSonetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForeSonetMedium_ObjectIdentity = ObjectIdentity
foreSonetMedium = _ForeSonetMedium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 1)
)
_ForeSonetMediumConfigTable_Object = MibTable
foreSonetMediumConfigTable = _ForeSonetMediumConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    foreSonetMediumConfigTable.setStatus("current")
_ForeSonetMediumConfigEntry_Object = MibTableRow
foreSonetMediumConfigEntry = _ForeSonetMediumConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 1, 1, 1)
)
foreSonetMediumConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetMediumConfigEntry.setStatus("current")


class _ForeSonetMediumConfigLoopbackMode_Type(Integer32):
    """Custom type foreSonetMediumConfigLoopbackMode based on Integer32"""
    defaultValue = 1

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
        *(("sonetDiagLoop", 3),
          ("sonetLineLoop", 2),
          ("sonetNoLoop", 1),
          ("sonetOtherLoop", 4))
    )


_ForeSonetMediumConfigLoopbackMode_Type.__name__ = "Integer32"
_ForeSonetMediumConfigLoopbackMode_Object = MibTableColumn
foreSonetMediumConfigLoopbackMode = _ForeSonetMediumConfigLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 1, 1, 1, 1),
    _ForeSonetMediumConfigLoopbackMode_Type()
)
foreSonetMediumConfigLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetMediumConfigLoopbackMode.setStatus("current")


class _ForeSonetMediumConfigTxClockSource_Type(Integer32):
    """Custom type foreSonetMediumConfigTxClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("rxTiming", 1))
    )


_ForeSonetMediumConfigTxClockSource_Type.__name__ = "Integer32"
_ForeSonetMediumConfigTxClockSource_Object = MibTableColumn
foreSonetMediumConfigTxClockSource = _ForeSonetMediumConfigTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 1, 1, 1, 2),
    _ForeSonetMediumConfigTxClockSource_Type()
)
foreSonetMediumConfigTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetMediumConfigTxClockSource.setStatus("current")
_ForeSonetSection_ObjectIdentity = ObjectIdentity
foreSonetSection = _ForeSonetSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2)
)
_ForeSonetSectionTotalTable_Object = MibTable
foreSonetSectionTotalTable = _ForeSonetSectionTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    foreSonetSectionTotalTable.setStatus("current")
_ForeSonetSectionTotalEntry_Object = MibTableRow
foreSonetSectionTotalEntry = _ForeSonetSectionTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 2, 1)
)
foreSonetSectionTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetSectionTotalEntry.setStatus("current")
_ForeSonetSectionTotalBIPs_Type = Counter32
_ForeSonetSectionTotalBIPs_Object = MibTableColumn
foreSonetSectionTotalBIPs = _ForeSonetSectionTotalBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 2, 1, 1),
    _ForeSonetSectionTotalBIPs_Type()
)
foreSonetSectionTotalBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionTotalBIPs.setStatus("current")
_ForeSonetSectionTotalLOSs_Type = Counter32
_ForeSonetSectionTotalLOSs_Object = MibTableColumn
foreSonetSectionTotalLOSs = _ForeSonetSectionTotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 2, 1, 2),
    _ForeSonetSectionTotalLOSs_Type()
)
foreSonetSectionTotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionTotalLOSs.setStatus("current")
_ForeSonetSectionTotalLOFs_Type = Counter32
_ForeSonetSectionTotalLOFs_Object = MibTableColumn
foreSonetSectionTotalLOFs = _ForeSonetSectionTotalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 2, 1, 3),
    _ForeSonetSectionTotalLOFs_Type()
)
foreSonetSectionTotalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionTotalLOFs.setStatus("current")
_ForeSonetSectionDiagnosticsTable_Object = MibTable
foreSonetSectionDiagnosticsTable = _ForeSonetSectionDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3)
)
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsTable.setStatus("current")
_ForeSonetSectionDiagnosticsEntry_Object = MibTableRow
foreSonetSectionDiagnosticsEntry = _ForeSonetSectionDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1)
)
foreSonetSectionDiagnosticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsEntry.setStatus("current")


class _ForeSonetSectionDiagnosticsFraming_Type(Integer32):
    """Custom type foreSonetSectionDiagnosticsFraming based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetSectionDiagnosticsFraming_Type.__name__ = "Integer32"
_ForeSonetSectionDiagnosticsFraming_Object = MibTableColumn
foreSonetSectionDiagnosticsFraming = _ForeSonetSectionDiagnosticsFraming_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1, 1),
    _ForeSonetSectionDiagnosticsFraming_Type()
)
foreSonetSectionDiagnosticsFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsFraming.setStatus("current")


class _ForeSonetSectionDiagnosticsB1_Type(Integer32):
    """Custom type foreSonetSectionDiagnosticsB1 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetSectionDiagnosticsB1_Type.__name__ = "Integer32"
_ForeSonetSectionDiagnosticsB1_Object = MibTableColumn
foreSonetSectionDiagnosticsB1 = _ForeSonetSectionDiagnosticsB1_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1, 2),
    _ForeSonetSectionDiagnosticsB1_Type()
)
foreSonetSectionDiagnosticsB1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsB1.setStatus("current")


class _ForeSonetSectionDiagnosticsDisableTxScrambling_Type(Integer32):
    """Custom type foreSonetSectionDiagnosticsDisableTxScrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetSectionDiagnosticsDisableTxScrambling_Type.__name__ = "Integer32"
_ForeSonetSectionDiagnosticsDisableTxScrambling_Object = MibTableColumn
foreSonetSectionDiagnosticsDisableTxScrambling = _ForeSonetSectionDiagnosticsDisableTxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1, 3),
    _ForeSonetSectionDiagnosticsDisableTxScrambling_Type()
)
foreSonetSectionDiagnosticsDisableTxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsDisableTxScrambling.setStatus("current")


class _ForeSonetSectionDiagnosticsDisableRxDescrambling_Type(Integer32):
    """Custom type foreSonetSectionDiagnosticsDisableRxDescrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetSectionDiagnosticsDisableRxDescrambling_Type.__name__ = "Integer32"
_ForeSonetSectionDiagnosticsDisableRxDescrambling_Object = MibTableColumn
foreSonetSectionDiagnosticsDisableRxDescrambling = _ForeSonetSectionDiagnosticsDisableRxDescrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1, 4),
    _ForeSonetSectionDiagnosticsDisableRxDescrambling_Type()
)
foreSonetSectionDiagnosticsDisableRxDescrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsDisableRxDescrambling.setStatus("current")


class _ForeSonetSectionDiagnosticsLOS_Type(Integer32):
    """Custom type foreSonetSectionDiagnosticsLOS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetSectionDiagnosticsLOS_Type.__name__ = "Integer32"
_ForeSonetSectionDiagnosticsLOS_Object = MibTableColumn
foreSonetSectionDiagnosticsLOS = _ForeSonetSectionDiagnosticsLOS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 3, 1, 5),
    _ForeSonetSectionDiagnosticsLOS_Type()
)
foreSonetSectionDiagnosticsLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetSectionDiagnosticsLOS.setStatus("current")
_ForeSonetSectionCurrentTable_Object = MibTable
foreSonetSectionCurrentTable = _ForeSonetSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 4)
)
if mibBuilder.loadTexts:
    foreSonetSectionCurrentTable.setStatus("current")
_ForeSonetSectionCurrentEntry_Object = MibTableRow
foreSonetSectionCurrentEntry = _ForeSonetSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 4, 1)
)
foreSonetSectionCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetSectionCurrentEntry.setStatus("current")
_ForeSonetSectionCurrentBBEs_Type = Integer32
_ForeSonetSectionCurrentBBEs_Object = MibTableColumn
foreSonetSectionCurrentBBEs = _ForeSonetSectionCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 4, 1, 1),
    _ForeSonetSectionCurrentBBEs_Type()
)
foreSonetSectionCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionCurrentBBEs.setStatus("current")
_ForeSonetSectionIntervalTable_Object = MibTable
foreSonetSectionIntervalTable = _ForeSonetSectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5)
)
if mibBuilder.loadTexts:
    foreSonetSectionIntervalTable.setStatus("current")
_ForeSonetSectionIntervalEntry_Object = MibTableRow
foreSonetSectionIntervalEntry = _ForeSonetSectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5, 1)
)
foreSonetSectionIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetSectionIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetSectionIntervalEntry.setStatus("current")
_ForeSonetSectionIntervalBBEs_Type = Integer32
_ForeSonetSectionIntervalBBEs_Object = MibTableColumn
foreSonetSectionIntervalBBEs = _ForeSonetSectionIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5, 1, 1),
    _ForeSonetSectionIntervalBBEs_Type()
)
foreSonetSectionIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionIntervalBBEs.setStatus("current")
_ForeSonetSectionIntervalESR_Type = Integer32
_ForeSonetSectionIntervalESR_Object = MibTableColumn
foreSonetSectionIntervalESR = _ForeSonetSectionIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5, 1, 2),
    _ForeSonetSectionIntervalESR_Type()
)
foreSonetSectionIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionIntervalESR.setStatus("current")
_ForeSonetSectionIntervalSESR_Type = Integer32
_ForeSonetSectionIntervalSESR_Object = MibTableColumn
foreSonetSectionIntervalSESR = _ForeSonetSectionIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5, 1, 3),
    _ForeSonetSectionIntervalSESR_Type()
)
foreSonetSectionIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionIntervalSESR.setStatus("current")
_ForeSonetSectionIntervalBBER_Type = Integer32
_ForeSonetSectionIntervalBBER_Object = MibTableColumn
foreSonetSectionIntervalBBER = _ForeSonetSectionIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 2, 5, 1, 4),
    _ForeSonetSectionIntervalBBER_Type()
)
foreSonetSectionIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetSectionIntervalBBER.setStatus("current")
_ForeSonetLine_ObjectIdentity = ObjectIdentity
foreSonetLine = _ForeSonetLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3)
)
_ForeSonetLineConfigTable_Object = MibTable
foreSonetLineConfigTable = _ForeSonetLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    foreSonetLineConfigTable.setStatus("current")
_ForeSonetLineConfigEntry_Object = MibTableRow
foreSonetLineConfigEntry = _ForeSonetLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1)
)
foreSonetLineConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetLineConfigEntry.setStatus("current")


class _ForeSonetLineBipThrSeconds_Type(Integer32):
    """Custom type foreSonetLineBipThrSeconds based on Integer32"""
    defaultValue = 10


_ForeSonetLineBipThrSeconds_Object = MibTableColumn
foreSonetLineBipThrSeconds = _ForeSonetLineBipThrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 2),
    _ForeSonetLineBipThrSeconds_Type()
)
foreSonetLineBipThrSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineBipThrSeconds.setStatus("current")


class _ForeSonetLineBipThrErrors_Type(Integer32):
    """Custom type foreSonetLineBipThrErrors based on Integer32"""
    defaultValue = 1


_ForeSonetLineBipThrErrors_Object = MibTableColumn
foreSonetLineBipThrErrors = _ForeSonetLineBipThrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 3),
    _ForeSonetLineBipThrErrors_Type()
)
foreSonetLineBipThrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineBipThrErrors.setStatus("current")


class _ForeSonetLineBipFailEnable_Type(Integer32):
    """Custom type foreSonetLineBipFailEnable based on Integer32"""
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


_ForeSonetLineBipFailEnable_Type.__name__ = "Integer32"
_ForeSonetLineBipFailEnable_Object = MibTableColumn
foreSonetLineBipFailEnable = _ForeSonetLineBipFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 4),
    _ForeSonetLineBipFailEnable_Type()
)
foreSonetLineBipFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineBipFailEnable.setStatus("current")
_ForeSonetLineSignalDegradeBer_Type = Integer32
_ForeSonetLineSignalDegradeBer_Object = MibTableColumn
foreSonetLineSignalDegradeBer = _ForeSonetLineSignalDegradeBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 5),
    _ForeSonetLineSignalDegradeBer_Type()
)
foreSonetLineSignalDegradeBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineSignalDegradeBer.setStatus("current")
_ForeSonetLineSignalFailBer_Type = Integer32
_ForeSonetLineSignalFailBer_Object = MibTableColumn
foreSonetLineSignalFailBer = _ForeSonetLineSignalFailBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 6),
    _ForeSonetLineSignalFailBer_Type()
)
foreSonetLineSignalFailBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineSignalFailBer.setStatus("current")


class _ForeSonetLineBerErrorModel_Type(Integer32):
    """Custom type foreSonetLineBerErrorModel based on Integer32"""
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
        *(("errorModelBurst", 2),
          ("errorModelNone", 0),
          ("errorModelRandom", 1))
    )


_ForeSonetLineBerErrorModel_Type.__name__ = "Integer32"
_ForeSonetLineBerErrorModel_Object = MibTableColumn
foreSonetLineBerErrorModel = _ForeSonetLineBerErrorModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 7),
    _ForeSonetLineBerErrorModel_Type()
)
foreSonetLineBerErrorModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineBerErrorModel.setStatus("current")


class _ForeSonetLineBerState_Type(Integer32):
    """Custom type foreSonetLineBerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("berStateOk", 0),
          ("berStateSigDegrade", 1),
          ("berStateSigFail", 2))
    )


_ForeSonetLineBerState_Type.__name__ = "Integer32"
_ForeSonetLineBerState_Object = MibTableColumn
foreSonetLineBerState = _ForeSonetLineBerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 1, 1, 8),
    _ForeSonetLineBerState_Type()
)
foreSonetLineBerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineBerState.setStatus("current")
_ForeSonetLineTotalTable_Object = MibTable
foreSonetLineTotalTable = _ForeSonetLineTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2)
)
if mibBuilder.loadTexts:
    foreSonetLineTotalTable.setStatus("current")
_ForeSonetLineTotalEntry_Object = MibTableRow
foreSonetLineTotalEntry = _ForeSonetLineTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2, 1)
)
foreSonetLineTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetLineTotalEntry.setStatus("current")
_ForeSonetLineTotalBIPs_Type = Counter32
_ForeSonetLineTotalBIPs_Object = MibTableColumn
foreSonetLineTotalBIPs = _ForeSonetLineTotalBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2, 1, 1),
    _ForeSonetLineTotalBIPs_Type()
)
foreSonetLineTotalBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineTotalBIPs.setStatus("current")
_ForeSonetLineTotalFEBEs_Type = Counter32
_ForeSonetLineTotalFEBEs_Object = MibTableColumn
foreSonetLineTotalFEBEs = _ForeSonetLineTotalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2, 1, 2),
    _ForeSonetLineTotalFEBEs_Type()
)
foreSonetLineTotalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineTotalFEBEs.setStatus("current")
_ForeSonetLineTotalAISs_Type = Counter32
_ForeSonetLineTotalAISs_Object = MibTableColumn
foreSonetLineTotalAISs = _ForeSonetLineTotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2, 1, 3),
    _ForeSonetLineTotalAISs_Type()
)
foreSonetLineTotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineTotalAISs.setStatus("current")
_ForeSonetLineTotalRDIs_Type = Counter32
_ForeSonetLineTotalRDIs_Object = MibTableColumn
foreSonetLineTotalRDIs = _ForeSonetLineTotalRDIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 2, 1, 4),
    _ForeSonetLineTotalRDIs_Type()
)
foreSonetLineTotalRDIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineTotalRDIs.setStatus("current")
_ForeSonetLineDiagnosticsTable_Object = MibTable
foreSonetLineDiagnosticsTable = _ForeSonetLineDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3)
)
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsTable.setStatus("current")
_ForeSonetLineDiagnosticsEntry_Object = MibTableRow
foreSonetLineDiagnosticsEntry = _ForeSonetLineDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1)
)
foreSonetLineDiagnosticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsEntry.setStatus("current")


class _ForeSonetLineDiagnosticsLAIS_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsLAIS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetLineDiagnosticsLAIS_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsLAIS_Object = MibTableColumn
foreSonetLineDiagnosticsLAIS = _ForeSonetLineDiagnosticsLAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 1),
    _ForeSonetLineDiagnosticsLAIS_Type()
)
foreSonetLineDiagnosticsLAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsLAIS.setStatus("current")


class _ForeSonetLineDiagnosticsB2_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsB2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetLineDiagnosticsB2_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsB2_Object = MibTableColumn
foreSonetLineDiagnosticsB2 = _ForeSonetLineDiagnosticsB2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 2),
    _ForeSonetLineDiagnosticsB2_Type()
)
foreSonetLineDiagnosticsB2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsB2.setStatus("current")


class _ForeSonetLineDiagnosticsAPS_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsAPS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetLineDiagnosticsAPS_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsAPS_Object = MibTableColumn
foreSonetLineDiagnosticsAPS = _ForeSonetLineDiagnosticsAPS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 3),
    _ForeSonetLineDiagnosticsAPS_Type()
)
foreSonetLineDiagnosticsAPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsAPS.setStatus("current")


class _ForeSonetLineDiagnosticsK1channel_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsK1channel based on Integer32"""
    defaultValue = 0

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("extraTraffic", 15),
          ("null", 0),
          ("working1", 1),
          ("working10", 10),
          ("working11", 11),
          ("working12", 12),
          ("working13", 13),
          ("working14", 14),
          ("working2", 2),
          ("working3", 3),
          ("working4", 4),
          ("working5", 5),
          ("working6", 6),
          ("working7", 7),
          ("working8", 8),
          ("working9", 9))
    )


_ForeSonetLineDiagnosticsK1channel_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsK1channel_Object = MibTableColumn
foreSonetLineDiagnosticsK1channel = _ForeSonetLineDiagnosticsK1channel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 4),
    _ForeSonetLineDiagnosticsK1channel_Type()
)
foreSonetLineDiagnosticsK1channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsK1channel.setStatus("current")


class _ForeSonetLineDiagnosticsK1request_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsK1request based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("donotrevert", 1),
          ("exercise", 4),
          ("forcedsw", 14),
          ("lockout", 15),
          ("manualsw", 8),
          ("noreq", 0),
          ("rr", 2),
          ("sdhp", 11),
          ("sdlp", 10),
          ("sfhp", 13),
          ("sflp", 12),
          ("wtr", 6))
    )


_ForeSonetLineDiagnosticsK1request_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsK1request_Object = MibTableColumn
foreSonetLineDiagnosticsK1request = _ForeSonetLineDiagnosticsK1request_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 5),
    _ForeSonetLineDiagnosticsK1request_Type()
)
foreSonetLineDiagnosticsK1request.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsK1request.setStatus("current")


class _ForeSonetLineDiagnosticsK2channel_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsK2channel based on Integer32"""
    defaultValue = 0

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("extraTraffic", 15),
          ("null", 0),
          ("working1", 1),
          ("working10", 10),
          ("working11", 11),
          ("working12", 12),
          ("working13", 13),
          ("working14", 14),
          ("working2", 2),
          ("working3", 3),
          ("working4", 4),
          ("working5", 5),
          ("working6", 6),
          ("working7", 7),
          ("working8", 8),
          ("working9", 9))
    )


_ForeSonetLineDiagnosticsK2channel_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsK2channel_Object = MibTableColumn
foreSonetLineDiagnosticsK2channel = _ForeSonetLineDiagnosticsK2channel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 6),
    _ForeSonetLineDiagnosticsK2channel_Type()
)
foreSonetLineDiagnosticsK2channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsK2channel.setStatus("current")


class _ForeSonetLineDiagnosticsK2Architecture_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsK2Architecture based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onen", 1),
          ("oneplusone", 0))
    )


_ForeSonetLineDiagnosticsK2Architecture_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsK2Architecture_Object = MibTableColumn
foreSonetLineDiagnosticsK2Architecture = _ForeSonetLineDiagnosticsK2Architecture_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 7),
    _ForeSonetLineDiagnosticsK2Architecture_Type()
)
foreSonetLineDiagnosticsK2Architecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsK2Architecture.setStatus("current")


class _ForeSonetLineDiagnosticsK2Mode_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsK2Mode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 5),
          ("unidirectional", 4))
    )


_ForeSonetLineDiagnosticsK2Mode_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsK2Mode_Object = MibTableColumn
foreSonetLineDiagnosticsK2Mode = _ForeSonetLineDiagnosticsK2Mode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 8),
    _ForeSonetLineDiagnosticsK2Mode_Type()
)
foreSonetLineDiagnosticsK2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsK2Mode.setStatus("current")


class _ForeSonetLineDiagnosticsLRDI_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsLRDI based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetLineDiagnosticsLRDI_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsLRDI_Object = MibTableColumn
foreSonetLineDiagnosticsLRDI = _ForeSonetLineDiagnosticsLRDI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 9),
    _ForeSonetLineDiagnosticsLRDI_Type()
)
foreSonetLineDiagnosticsLRDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsLRDI.setStatus("current")


class _ForeSonetLineDiagnosticsLREI_Type(Integer32):
    """Custom type foreSonetLineDiagnosticsLREI based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetLineDiagnosticsLREI_Type.__name__ = "Integer32"
_ForeSonetLineDiagnosticsLREI_Object = MibTableColumn
foreSonetLineDiagnosticsLREI = _ForeSonetLineDiagnosticsLREI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 3, 1, 10),
    _ForeSonetLineDiagnosticsLREI_Type()
)
foreSonetLineDiagnosticsLREI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetLineDiagnosticsLREI.setStatus("current")
_ForeSonetLineCurrentTable_Object = MibTable
foreSonetLineCurrentTable = _ForeSonetLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    foreSonetLineCurrentTable.setStatus("current")
_ForeSonetLineCurrentEntry_Object = MibTableRow
foreSonetLineCurrentEntry = _ForeSonetLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 4, 1)
)
foreSonetLineCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetLineCurrentEntry.setStatus("current")
_ForeSonetLineCurrentBBEs_Type = Integer32
_ForeSonetLineCurrentBBEs_Object = MibTableColumn
foreSonetLineCurrentBBEs = _ForeSonetLineCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 4, 1, 1),
    _ForeSonetLineCurrentBBEs_Type()
)
foreSonetLineCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineCurrentBBEs.setStatus("current")
_ForeSonetLineIntervalTable_Object = MibTable
foreSonetLineIntervalTable = _ForeSonetLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5)
)
if mibBuilder.loadTexts:
    foreSonetLineIntervalTable.setStatus("current")
_ForeSonetLineIntervalEntry_Object = MibTableRow
foreSonetLineIntervalEntry = _ForeSonetLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5, 1)
)
foreSonetLineIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetLineIntervalEntry.setStatus("current")
_ForeSonetLineIntervalBBEs_Type = Integer32
_ForeSonetLineIntervalBBEs_Object = MibTableColumn
foreSonetLineIntervalBBEs = _ForeSonetLineIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5, 1, 1),
    _ForeSonetLineIntervalBBEs_Type()
)
foreSonetLineIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineIntervalBBEs.setStatus("current")
_ForeSonetLineIntervalESR_Type = Integer32
_ForeSonetLineIntervalESR_Object = MibTableColumn
foreSonetLineIntervalESR = _ForeSonetLineIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5, 1, 2),
    _ForeSonetLineIntervalESR_Type()
)
foreSonetLineIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineIntervalESR.setStatus("current")
_ForeSonetLineIntervalSESR_Type = Integer32
_ForeSonetLineIntervalSESR_Object = MibTableColumn
foreSonetLineIntervalSESR = _ForeSonetLineIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5, 1, 3),
    _ForeSonetLineIntervalSESR_Type()
)
foreSonetLineIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineIntervalSESR.setStatus("current")
_ForeSonetLineIntervalBBER_Type = Integer32
_ForeSonetLineIntervalBBER_Object = MibTableColumn
foreSonetLineIntervalBBER = _ForeSonetLineIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 3, 5, 1, 4),
    _ForeSonetLineIntervalBBER_Type()
)
foreSonetLineIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetLineIntervalBBER.setStatus("current")
_ForeSonetPath_ObjectIdentity = ObjectIdentity
foreSonetPath = _ForeSonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4)
)
_ForeSonetPathConfigTable_Object = MibTable
foreSonetPathConfigTable = _ForeSonetPathConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    foreSonetPathConfigTable.setStatus("current")
_ForeSonetPathConfigEntry_Object = MibTableRow
foreSonetPathConfigEntry = _ForeSonetPathConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 1, 1)
)
foreSonetPathConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetPathConfigEntry.setStatus("current")


class _ForeSonetPathRxSignalLabel_Type(Integer32):
    """Custom type foreSonetPathRxSignalLabel based on Integer32"""
    defaultValue = 19


_ForeSonetPathRxSignalLabel_Object = MibTableColumn
foreSonetPathRxSignalLabel = _ForeSonetPathRxSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 1, 1, 2),
    _ForeSonetPathRxSignalLabel_Type()
)
foreSonetPathRxSignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathRxSignalLabel.setStatus("current")


class _ForeSonetPathTxSignalLabel_Type(Integer32):
    """Custom type foreSonetPathTxSignalLabel based on Integer32"""
    defaultValue = 19


_ForeSonetPathTxSignalLabel_Object = MibTableColumn
foreSonetPathTxSignalLabel = _ForeSonetPathTxSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 1, 1, 3),
    _ForeSonetPathTxSignalLabel_Type()
)
foreSonetPathTxSignalLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathTxSignalLabel.setStatus("current")


class _ForeSonetPathLoopbackMode_Type(Integer32):
    """Custom type foreSonetPathLoopbackMode based on Integer32"""
    defaultValue = 1

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
        *(("sonetPathDiagLoop", 3),
          ("sonetPathLineLoop", 2),
          ("sonetPathNoLoop", 1),
          ("sonetPathOtherLoop", 4))
    )


_ForeSonetPathLoopbackMode_Type.__name__ = "Integer32"
_ForeSonetPathLoopbackMode_Object = MibTableColumn
foreSonetPathLoopbackMode = _ForeSonetPathLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 1, 1, 5),
    _ForeSonetPathLoopbackMode_Type()
)
foreSonetPathLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathLoopbackMode.setStatus("current")
_ForeSonetPathTotalTable_Object = MibTable
foreSonetPathTotalTable = _ForeSonetPathTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2)
)
if mibBuilder.loadTexts:
    foreSonetPathTotalTable.setStatus("current")
_ForeSonetPathTotalEntry_Object = MibTableRow
foreSonetPathTotalEntry = _ForeSonetPathTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1)
)
foreSonetPathTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetPathTotalEntry.setStatus("current")
_ForeSonetPathTotalBIPs_Type = Counter32
_ForeSonetPathTotalBIPs_Object = MibTableColumn
foreSonetPathTotalBIPs = _ForeSonetPathTotalBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 1),
    _ForeSonetPathTotalBIPs_Type()
)
foreSonetPathTotalBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalBIPs.setStatus("current")
_ForeSonetPathTotalLOPs_Type = Counter32
_ForeSonetPathTotalLOPs_Object = MibTableColumn
foreSonetPathTotalLOPs = _ForeSonetPathTotalLOPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 2),
    _ForeSonetPathTotalLOPs_Type()
)
foreSonetPathTotalLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalLOPs.setStatus("current")
_ForeSonetPathTotalAISs_Type = Counter32
_ForeSonetPathTotalAISs_Object = MibTableColumn
foreSonetPathTotalAISs = _ForeSonetPathTotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 3),
    _ForeSonetPathTotalAISs_Type()
)
foreSonetPathTotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalAISs.setStatus("current")
_ForeSonetPathTotalRDIs_Type = Counter32
_ForeSonetPathTotalRDIs_Object = MibTableColumn
foreSonetPathTotalRDIs = _ForeSonetPathTotalRDIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 4),
    _ForeSonetPathTotalRDIs_Type()
)
foreSonetPathTotalRDIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalRDIs.setStatus("current")
_ForeSonetPathTotalUNEQs_Type = Counter32
_ForeSonetPathTotalUNEQs_Object = MibTableColumn
foreSonetPathTotalUNEQs = _ForeSonetPathTotalUNEQs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 5),
    _ForeSonetPathTotalUNEQs_Type()
)
foreSonetPathTotalUNEQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalUNEQs.setStatus("current")
_ForeSonetPathTotalPLMs_Type = Counter32
_ForeSonetPathTotalPLMs_Object = MibTableColumn
foreSonetPathTotalPLMs = _ForeSonetPathTotalPLMs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 6),
    _ForeSonetPathTotalPLMs_Type()
)
foreSonetPathTotalPLMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalPLMs.setStatus("current")
_ForeSonetPathTotalFEBEs_Type = Counter32
_ForeSonetPathTotalFEBEs_Object = MibTableColumn
foreSonetPathTotalFEBEs = _ForeSonetPathTotalFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 2, 1, 7),
    _ForeSonetPathTotalFEBEs_Type()
)
foreSonetPathTotalFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathTotalFEBEs.setStatus("current")
_ForeSonetPathCurrentTable_Object = MibTable
foreSonetPathCurrentTable = _ForeSonetPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    foreSonetPathCurrentTable.setStatus("current")
_ForeSonetPathCurrentEntry_Object = MibTableRow
foreSonetPathCurrentEntry = _ForeSonetPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 3, 1)
)
foreSonetPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetPathCurrentEntry.setStatus("current")
_ForeSonetPathCurrentStatus_Type = Integer32
_ForeSonetPathCurrentStatus_Object = MibTableColumn
foreSonetPathCurrentStatus = _ForeSonetPathCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 3, 1, 1),
    _ForeSonetPathCurrentStatus_Type()
)
foreSonetPathCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathCurrentStatus.setStatus("current")
_ForeSonetPathCurrentBBEs_Type = Integer32
_ForeSonetPathCurrentBBEs_Object = MibTableColumn
foreSonetPathCurrentBBEs = _ForeSonetPathCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 3, 1, 2),
    _ForeSonetPathCurrentBBEs_Type()
)
foreSonetPathCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathCurrentBBEs.setStatus("current")
_ForeSonetPathDiagnosticsTable_Object = MibTable
foreSonetPathDiagnosticsTable = _ForeSonetPathDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4)
)
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsTable.setStatus("current")
_ForeSonetPathDiagnosticsEntry_Object = MibTableRow
foreSonetPathDiagnosticsEntry = _ForeSonetPathDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1)
)
foreSonetPathDiagnosticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsEntry.setStatus("current")


class _ForeSonetPathDiagnosticsC2_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsC2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsC2_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsC2_Object = MibTableColumn
foreSonetPathDiagnosticsC2 = _ForeSonetPathDiagnosticsC2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 1),
    _ForeSonetPathDiagnosticsC2_Type()
)
foreSonetPathDiagnosticsC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsC2.setStatus("current")


class _ForeSonetPathDiagnosticsC2Value_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsC2Value based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              18,
              19,
              20,
              21,
              22,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252)
        )
    )
    namedValues = NamedValues(
        *(("asyncDS3mapping", 4),
          ("asyncDS4na", 18),
          ("asyncfddimapping", 21),
          ("atmmapping", 19),
          ("dqdbmapping", 20),
          ("equippednonspecPL", 1),
          ("hdlcwithscrambling", 22),
          ("lockedVTmode", 3),
          ("payloaddefect", 252),
          ("sts1with10vtxPD", 234),
          ("sts1with11vtxPD", 235),
          ("sts1with12vtxPD", 236),
          ("sts1with13vtxPD", 237),
          ("sts1with14vtxPD", 238),
          ("sts1with15vtxPD", 239),
          ("sts1with16vtxPD", 240),
          ("sts1with17vtxPD", 241),
          ("sts1with18vtxPD", 242),
          ("sts1with19vtxPD", 243),
          ("sts1with1vtxPD", 225),
          ("sts1with20vtxPD", 244),
          ("sts1with21vtxPD", 245),
          ("sts1with22vtxPD", 246),
          ("sts1with23vtxPD", 247),
          ("sts1with24vtxPD", 248),
          ("sts1with25vtxPD", 249),
          ("sts1with26vtxPD", 250),
          ("sts1with27vtxPD", 251),
          ("sts1with2vtxPD", 226),
          ("sts1with3vtxPD", 227),
          ("sts1with4vtxPD", 228),
          ("sts1with5vtxPD", 229),
          ("sts1with6vtxPD", 230),
          ("sts1with7vtxPD", 231),
          ("sts1with8vtxPD", 232),
          ("sts1with9vtxPD", 233),
          ("unequipped", 0),
          ("vtstructSTSSPE", 2))
    )


_ForeSonetPathDiagnosticsC2Value_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsC2Value_Object = MibTableColumn
foreSonetPathDiagnosticsC2Value = _ForeSonetPathDiagnosticsC2Value_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 2),
    _ForeSonetPathDiagnosticsC2Value_Type()
)
foreSonetPathDiagnosticsC2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsC2Value.setStatus("current")


class _ForeSonetPathDiagnosticsB3_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsB3 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsB3_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsB3_Object = MibTableColumn
foreSonetPathDiagnosticsB3 = _ForeSonetPathDiagnosticsB3_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 3),
    _ForeSonetPathDiagnosticsB3_Type()
)
foreSonetPathDiagnosticsB3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsB3.setStatus("current")


class _ForeSonetPathDiagnosticsPREI_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsPREI based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsPREI_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsPREI_Object = MibTableColumn
foreSonetPathDiagnosticsPREI = _ForeSonetPathDiagnosticsPREI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 4),
    _ForeSonetPathDiagnosticsPREI_Type()
)
foreSonetPathDiagnosticsPREI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsPREI.setStatus("current")


class _ForeSonetPathDiagnosticsPAIS_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsPAIS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsPAIS_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsPAIS_Object = MibTableColumn
foreSonetPathDiagnosticsPAIS = _ForeSonetPathDiagnosticsPAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 5),
    _ForeSonetPathDiagnosticsPAIS_Type()
)
foreSonetPathDiagnosticsPAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsPAIS.setStatus("current")


class _ForeSonetPathDiagnosticsPERDI_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsPERDI based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsPERDI_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsPERDI_Object = MibTableColumn
foreSonetPathDiagnosticsPERDI = _ForeSonetPathDiagnosticsPERDI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 6),
    _ForeSonetPathDiagnosticsPERDI_Type()
)
foreSonetPathDiagnosticsPERDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsPERDI.setStatus("current")


class _ForeSonetPathDiagnosticsERDIValue_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsERDIValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sonetPathERDIOnebitRDI", 4),
          ("sonetPathERDIconnDefect", 6),
          ("sonetPathERDInoDefect", 1),
          ("sonetPathERDInoPrionoDefect", 0),
          ("sonetPathERDIpayloadDefect", 2),
          ("sonetPathERDIserverDefect", 5))
    )


_ForeSonetPathDiagnosticsERDIValue_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsERDIValue_Object = MibTableColumn
foreSonetPathDiagnosticsERDIValue = _ForeSonetPathDiagnosticsERDIValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 7),
    _ForeSonetPathDiagnosticsERDIValue_Type()
)
foreSonetPathDiagnosticsERDIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsERDIValue.setStatus("current")


class _ForeSonetPathDiagnosticsLOP_Type(Integer32):
    """Custom type foreSonetPathDiagnosticsLOP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetPathDiagnosticsLOP_Type.__name__ = "Integer32"
_ForeSonetPathDiagnosticsLOP_Object = MibTableColumn
foreSonetPathDiagnosticsLOP = _ForeSonetPathDiagnosticsLOP_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 4, 1, 8),
    _ForeSonetPathDiagnosticsLOP_Type()
)
foreSonetPathDiagnosticsLOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetPathDiagnosticsLOP.setStatus("current")
_ForeSonetPathGroupConfigTable_Object = MibTable
foreSonetPathGroupConfigTable = _ForeSonetPathGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 5)
)
if mibBuilder.loadTexts:
    foreSonetPathGroupConfigTable.setStatus("current")
_ForeSonetPathGroupConfigEntry_Object = MibTableRow
foreSonetPathGroupConfigEntry = _ForeSonetPathGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 5, 1)
)
foreSonetPathGroupConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Fore-Sonet-Ext-MIB", "foreVTGroup"),
)
if mibBuilder.loadTexts:
    foreSonetPathGroupConfigEntry.setStatus("current")
_ForeVTGroup_Type = Integer32
_ForeVTGroup_Object = MibTableColumn
foreVTGroup = _ForeVTGroup_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 5, 1, 1),
    _ForeVTGroup_Type()
)
foreVTGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreVTGroup.setStatus("current")


class _ForeVTWidth_Type(Integer32):
    """Custom type foreVTWidth based on Integer32"""
    defaultValue = 1

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
        *(("vtWidth15VC11", 1),
          ("vtWidth2VC12", 2),
          ("vtWidth3", 3),
          ("vtWidth6VC2", 4),
          ("vtWidth6c", 5))
    )


_ForeVTWidth_Type.__name__ = "Integer32"
_ForeVTWidth_Object = MibTableColumn
foreVTWidth = _ForeVTWidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 5, 1, 2),
    _ForeVTWidth_Type()
)
foreVTWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreVTWidth.setStatus("current")
_ForeSonetPathIntervalTable_Object = MibTable
foreSonetPathIntervalTable = _ForeSonetPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6)
)
if mibBuilder.loadTexts:
    foreSonetPathIntervalTable.setStatus("current")
_ForeSonetPathIntervalEntry_Object = MibTableRow
foreSonetPathIntervalEntry = _ForeSonetPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6, 1)
)
foreSonetPathIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetPathIntervalEntry.setStatus("current")
_ForeSonetPathIntervalBBEs_Type = Integer32
_ForeSonetPathIntervalBBEs_Object = MibTableColumn
foreSonetPathIntervalBBEs = _ForeSonetPathIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6, 1, 1),
    _ForeSonetPathIntervalBBEs_Type()
)
foreSonetPathIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathIntervalBBEs.setStatus("current")
_ForeSonetPathIntervalESR_Type = Integer32
_ForeSonetPathIntervalESR_Object = MibTableColumn
foreSonetPathIntervalESR = _ForeSonetPathIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6, 1, 2),
    _ForeSonetPathIntervalESR_Type()
)
foreSonetPathIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathIntervalESR.setStatus("current")
_ForeSonetPathIntervalSESR_Type = Integer32
_ForeSonetPathIntervalSESR_Object = MibTableColumn
foreSonetPathIntervalSESR = _ForeSonetPathIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6, 1, 3),
    _ForeSonetPathIntervalSESR_Type()
)
foreSonetPathIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathIntervalSESR.setStatus("current")
_ForeSonetPathIntervalBBER_Type = Integer32
_ForeSonetPathIntervalBBER_Object = MibTableColumn
foreSonetPathIntervalBBER = _ForeSonetPathIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 4, 6, 1, 4),
    _ForeSonetPathIntervalBBER_Type()
)
foreSonetPathIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetPathIntervalBBER.setStatus("current")
_ForeSonetVT_ObjectIdentity = ObjectIdentity
foreSonetVT = _ForeSonetVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5)
)
_ForeSonetVTConfigTable_Object = MibTable
foreSonetVTConfigTable = _ForeSonetVTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 1)
)
if mibBuilder.loadTexts:
    foreSonetVTConfigTable.setStatus("current")
_ForeSonetVTConfigEntry_Object = MibTableRow
foreSonetVTConfigEntry = _ForeSonetVTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 1, 1)
)
foreSonetVTConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetVTConfigEntry.setStatus("current")


class _ForeSonetVTLoopbackMode_Type(Integer32):
    """Custom type foreSonetVTLoopbackMode based on Integer32"""
    defaultValue = 1

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
        *(("sonetVTDiagLoop", 3),
          ("sonetVTLineLoop", 2),
          ("sonetVTNoLoop", 1),
          ("sonetVTOtherLoop", 4))
    )


_ForeSonetVTLoopbackMode_Type.__name__ = "Integer32"
_ForeSonetVTLoopbackMode_Object = MibTableColumn
foreSonetVTLoopbackMode = _ForeSonetVTLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 1, 1, 1),
    _ForeSonetVTLoopbackMode_Type()
)
foreSonetVTLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVTLoopbackMode.setStatus("current")
_ForeSonetVTTotalTable_Object = MibTable
foreSonetVTTotalTable = _ForeSonetVTTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2)
)
if mibBuilder.loadTexts:
    foreSonetVTTotalTable.setStatus("current")
_ForeSonetVTTotalEntry_Object = MibTableRow
foreSonetVTTotalEntry = _ForeSonetVTTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1)
)
foreSonetVTTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetVTTotalEntry.setStatus("current")
_ForeSonetVTTotalBIPs_Type = Counter32
_ForeSonetVTTotalBIPs_Object = MibTableColumn
foreSonetVTTotalBIPs = _ForeSonetVTTotalBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 1),
    _ForeSonetVTTotalBIPs_Type()
)
foreSonetVTTotalBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalBIPs.setStatus("current")
_ForeSonetVTTotalREIs_Type = Counter32
_ForeSonetVTTotalREIs_Object = MibTableColumn
foreSonetVTTotalREIs = _ForeSonetVTTotalREIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 2),
    _ForeSonetVTTotalREIs_Type()
)
foreSonetVTTotalREIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalREIs.setStatus("current")
_ForeSonetVTTotalLOPs_Type = Counter32
_ForeSonetVTTotalLOPs_Object = MibTableColumn
foreSonetVTTotalLOPs = _ForeSonetVTTotalLOPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 3),
    _ForeSonetVTTotalLOPs_Type()
)
foreSonetVTTotalLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalLOPs.setStatus("current")
_ForeSonetVTTotalAISs_Type = Counter32
_ForeSonetVTTotalAISs_Object = MibTableColumn
foreSonetVTTotalAISs = _ForeSonetVTTotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 4),
    _ForeSonetVTTotalAISs_Type()
)
foreSonetVTTotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalAISs.setStatus("current")
_ForeSonetVTTotalRDIs_Type = Counter32
_ForeSonetVTTotalRDIs_Object = MibTableColumn
foreSonetVTTotalRDIs = _ForeSonetVTTotalRDIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 5),
    _ForeSonetVTTotalRDIs_Type()
)
foreSonetVTTotalRDIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalRDIs.setStatus("current")
_ForeSonetVTTotalUNEQs_Type = Counter32
_ForeSonetVTTotalUNEQs_Object = MibTableColumn
foreSonetVTTotalUNEQs = _ForeSonetVTTotalUNEQs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 6),
    _ForeSonetVTTotalUNEQs_Type()
)
foreSonetVTTotalUNEQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalUNEQs.setStatus("current")
_ForeSonetVTTotalPLMs_Type = Counter32
_ForeSonetVTTotalPLMs_Object = MibTableColumn
foreSonetVTTotalPLMs = _ForeSonetVTTotalPLMs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 2, 1, 7),
    _ForeSonetVTTotalPLMs_Type()
)
foreSonetVTTotalPLMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTTotalPLMs.setStatus("current")
_ForeSonetVTDiagnosticsTable_Object = MibTable
foreSonetVTDiagnosticsTable = _ForeSonetVTDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3)
)
if mibBuilder.loadTexts:
    foreSonetVTDiagnosticsTable.setStatus("current")
_ForeSonetVTDiagnosticsEntry_Object = MibTableRow
foreSonetVTDiagnosticsEntry = _ForeSonetVTDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1)
)
foreSonetVTDiagnosticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetVTDiagnosticsEntry.setStatus("current")


class _ForeSonetVtDiagnosticsBIP_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsBIP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsBIP_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsBIP_Object = MibTableColumn
foreSonetVtDiagnosticsBIP = _ForeSonetVtDiagnosticsBIP_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 1),
    _ForeSonetVtDiagnosticsBIP_Type()
)
foreSonetVtDiagnosticsBIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsBIP.setStatus("current")


class _ForeSonetVtDiagnosticsRDI_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsRDI based on Integer32"""
    defaultValue = 4

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
        *(("auto", 4),
          ("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsRDI_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsRDI_Object = MibTableColumn
foreSonetVtDiagnosticsRDI = _ForeSonetVtDiagnosticsRDI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 2),
    _ForeSonetVtDiagnosticsRDI_Type()
)
foreSonetVtDiagnosticsRDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsRDI.setStatus("current")


class _ForeSonetVtDiagnosticsRFI_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsRFI based on Integer32"""
    defaultValue = 4

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
        *(("auto", 4),
          ("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsRFI_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsRFI_Object = MibTableColumn
foreSonetVtDiagnosticsRFI = _ForeSonetVtDiagnosticsRFI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 3),
    _ForeSonetVtDiagnosticsRFI_Type()
)
foreSonetVtDiagnosticsRFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsRFI.setStatus("current")


class _ForeSonetVtDiagnosticsAIS_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsAIS based on Integer32"""
    defaultValue = 4

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
        *(("auto", 4),
          ("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsAIS_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsAIS_Object = MibTableColumn
foreSonetVtDiagnosticsAIS = _ForeSonetVtDiagnosticsAIS_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 4),
    _ForeSonetVtDiagnosticsAIS_Type()
)
foreSonetVtDiagnosticsAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsAIS.setStatus("current")


class _ForeSonetVtDiagnosticsLOP_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsLOP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("momentary", 3),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsLOP_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsLOP_Object = MibTableColumn
foreSonetVtDiagnosticsLOP = _ForeSonetVtDiagnosticsLOP_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 5),
    _ForeSonetVtDiagnosticsLOP_Type()
)
foreSonetVtDiagnosticsLOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsLOP.setStatus("current")


class _ForeSonetVtDiagnosticsLabel_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsLabel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsLabel_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsLabel_Object = MibTableColumn
foreSonetVtDiagnosticsLabel = _ForeSonetVtDiagnosticsLabel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 6),
    _ForeSonetVtDiagnosticsLabel_Type()
)
foreSonetVtDiagnosticsLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsLabel.setStatus("current")


class _ForeSonetVtDiagnosticsLabelValue_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsLabelValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 2),
          ("bitsynchronous", 3),
          ("bytesynchronous", 4),
          ("equippednonspec", 1),
          ("unequipped", 0))
    )


_ForeSonetVtDiagnosticsLabelValue_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsLabelValue_Object = MibTableColumn
foreSonetVtDiagnosticsLabelValue = _ForeSonetVtDiagnosticsLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 7),
    _ForeSonetVtDiagnosticsLabelValue_Type()
)
foreSonetVtDiagnosticsLabelValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsLabelValue.setStatus("current")


class _ForeSonetVtDiagnosticsREI_Type(Integer32):
    """Custom type foreSonetVtDiagnosticsREI based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("off", 2),
          ("on", 1))
    )


_ForeSonetVtDiagnosticsREI_Type.__name__ = "Integer32"
_ForeSonetVtDiagnosticsREI_Object = MibTableColumn
foreSonetVtDiagnosticsREI = _ForeSonetVtDiagnosticsREI_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 3, 1, 8),
    _ForeSonetVtDiagnosticsREI_Type()
)
foreSonetVtDiagnosticsREI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSonetVtDiagnosticsREI.setStatus("current")
_ForeSonetVTCurrentTable_Object = MibTable
foreSonetVTCurrentTable = _ForeSonetVTCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 4)
)
if mibBuilder.loadTexts:
    foreSonetVTCurrentTable.setStatus("current")
_ForeSonetVTCurrentEntry_Object = MibTableRow
foreSonetVTCurrentEntry = _ForeSonetVTCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 4, 1)
)
foreSonetVTCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetVTCurrentEntry.setStatus("current")
_ForeSonetVTCurrentBBEs_Type = Integer32
_ForeSonetVTCurrentBBEs_Object = MibTableColumn
foreSonetVTCurrentBBEs = _ForeSonetVTCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 4, 1, 1),
    _ForeSonetVTCurrentBBEs_Type()
)
foreSonetVTCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTCurrentBBEs.setStatus("current")
_ForeSonetVTIntervalTable_Object = MibTable
foreSonetVTIntervalTable = _ForeSonetVTIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5)
)
if mibBuilder.loadTexts:
    foreSonetVTIntervalTable.setStatus("current")
_ForeSonetVTIntervalEntry_Object = MibTableRow
foreSonetVTIntervalEntry = _ForeSonetVTIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5, 1)
)
foreSonetVTIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetVTIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetVTIntervalEntry.setStatus("current")
_ForeSonetVTIntervalBBEs_Type = Integer32
_ForeSonetVTIntervalBBEs_Object = MibTableColumn
foreSonetVTIntervalBBEs = _ForeSonetVTIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5, 1, 1),
    _ForeSonetVTIntervalBBEs_Type()
)
foreSonetVTIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTIntervalBBEs.setStatus("current")
_ForeSonetVTIntervalESR_Type = Integer32
_ForeSonetVTIntervalESR_Object = MibTableColumn
foreSonetVTIntervalESR = _ForeSonetVTIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5, 1, 2),
    _ForeSonetVTIntervalESR_Type()
)
foreSonetVTIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTIntervalESR.setStatus("current")
_ForeSonetVTIntervalSESR_Type = Integer32
_ForeSonetVTIntervalSESR_Object = MibTableColumn
foreSonetVTIntervalSESR = _ForeSonetVTIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5, 1, 3),
    _ForeSonetVTIntervalSESR_Type()
)
foreSonetVTIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTIntervalSESR.setStatus("current")
_ForeSonetVTIntervalBBER_Type = Integer32
_ForeSonetVTIntervalBBER_Object = MibTableColumn
foreSonetVTIntervalBBER = _ForeSonetVTIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 5, 5, 1, 4),
    _ForeSonetVTIntervalBBER_Type()
)
foreSonetVTIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetVTIntervalBBER.setStatus("current")
_ForeSonetSPE_ObjectIdentity = ObjectIdentity
foreSonetSPE = _ForeSonetSPE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 6)
)
_ForeSonetFarEndLine_ObjectIdentity = ObjectIdentity
foreSonetFarEndLine = _ForeSonetFarEndLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7)
)
_ForeSonetFarEndLineCurrentTable_Object = MibTable
foreSonetFarEndLineCurrentTable = _ForeSonetFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 1)
)
if mibBuilder.loadTexts:
    foreSonetFarEndLineCurrentTable.setStatus("current")
_ForeSonetFarEndLineCurrentEntry_Object = MibTableRow
foreSonetFarEndLineCurrentEntry = _ForeSonetFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 1, 1)
)
foreSonetFarEndLineCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndLineCurrentEntry.setStatus("current")
_ForeSonetFarEndLineCurrentBBEs_Type = Integer32
_ForeSonetFarEndLineCurrentBBEs_Object = MibTableColumn
foreSonetFarEndLineCurrentBBEs = _ForeSonetFarEndLineCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 1, 1, 1),
    _ForeSonetFarEndLineCurrentBBEs_Type()
)
foreSonetFarEndLineCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndLineCurrentBBEs.setStatus("current")
_ForeSonetFarEndLineIntervalTable_Object = MibTable
foreSonetFarEndLineIntervalTable = _ForeSonetFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2)
)
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalTable.setStatus("current")
_ForeSonetFarEndLineIntervalEntry_Object = MibTableRow
foreSonetFarEndLineIntervalEntry = _ForeSonetFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2, 1)
)
foreSonetFarEndLineIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndLineIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalEntry.setStatus("current")
_ForeSonetFarEndLineIntervalBBEs_Type = Integer32
_ForeSonetFarEndLineIntervalBBEs_Object = MibTableColumn
foreSonetFarEndLineIntervalBBEs = _ForeSonetFarEndLineIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2, 1, 1),
    _ForeSonetFarEndLineIntervalBBEs_Type()
)
foreSonetFarEndLineIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalBBEs.setStatus("current")
_ForeSonetFarEndLineIntervalESR_Type = Integer32
_ForeSonetFarEndLineIntervalESR_Object = MibTableColumn
foreSonetFarEndLineIntervalESR = _ForeSonetFarEndLineIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2, 1, 2),
    _ForeSonetFarEndLineIntervalESR_Type()
)
foreSonetFarEndLineIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalESR.setStatus("current")
_ForeSonetFarEndLineIntervalSESR_Type = Integer32
_ForeSonetFarEndLineIntervalSESR_Object = MibTableColumn
foreSonetFarEndLineIntervalSESR = _ForeSonetFarEndLineIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2, 1, 3),
    _ForeSonetFarEndLineIntervalSESR_Type()
)
foreSonetFarEndLineIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalSESR.setStatus("current")
_ForeSonetFarEndLineIntervalBBER_Type = Integer32
_ForeSonetFarEndLineIntervalBBER_Object = MibTableColumn
foreSonetFarEndLineIntervalBBER = _ForeSonetFarEndLineIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 7, 2, 1, 4),
    _ForeSonetFarEndLineIntervalBBER_Type()
)
foreSonetFarEndLineIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndLineIntervalBBER.setStatus("current")
_ForeSonetFarEndPath_ObjectIdentity = ObjectIdentity
foreSonetFarEndPath = _ForeSonetFarEndPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8)
)
_ForeSonetFarEndPathCurrentTable_Object = MibTable
foreSonetFarEndPathCurrentTable = _ForeSonetFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 1)
)
if mibBuilder.loadTexts:
    foreSonetFarEndPathCurrentTable.setStatus("current")
_ForeSonetFarEndPathCurrentEntry_Object = MibTableRow
foreSonetFarEndPathCurrentEntry = _ForeSonetFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 1, 1)
)
foreSonetFarEndPathCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndPathCurrentEntry.setStatus("current")
_ForeSonetFarEndPathCurrentBBEs_Type = Integer32
_ForeSonetFarEndPathCurrentBBEs_Object = MibTableColumn
foreSonetFarEndPathCurrentBBEs = _ForeSonetFarEndPathCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 1, 1, 1),
    _ForeSonetFarEndPathCurrentBBEs_Type()
)
foreSonetFarEndPathCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndPathCurrentBBEs.setStatus("current")
_ForeSonetFarEndPathIntervalTable_Object = MibTable
foreSonetFarEndPathIntervalTable = _ForeSonetFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2)
)
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalTable.setStatus("current")
_ForeSonetFarEndPathIntervalEntry_Object = MibTableRow
foreSonetFarEndPathIntervalEntry = _ForeSonetFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2, 1)
)
foreSonetFarEndPathIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndPathIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalEntry.setStatus("current")
_ForeSonetFarEndPathIntervalBBEs_Type = Integer32
_ForeSonetFarEndPathIntervalBBEs_Object = MibTableColumn
foreSonetFarEndPathIntervalBBEs = _ForeSonetFarEndPathIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2, 1, 1),
    _ForeSonetFarEndPathIntervalBBEs_Type()
)
foreSonetFarEndPathIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalBBEs.setStatus("current")
_ForeSonetFarEndPathIntervalESR_Type = Integer32
_ForeSonetFarEndPathIntervalESR_Object = MibTableColumn
foreSonetFarEndPathIntervalESR = _ForeSonetFarEndPathIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2, 1, 2),
    _ForeSonetFarEndPathIntervalESR_Type()
)
foreSonetFarEndPathIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalESR.setStatus("current")
_ForeSonetFarEndPathIntervalSESR_Type = Integer32
_ForeSonetFarEndPathIntervalSESR_Object = MibTableColumn
foreSonetFarEndPathIntervalSESR = _ForeSonetFarEndPathIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2, 1, 3),
    _ForeSonetFarEndPathIntervalSESR_Type()
)
foreSonetFarEndPathIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalSESR.setStatus("current")
_ForeSonetFarEndPathIntervalBBER_Type = Integer32
_ForeSonetFarEndPathIntervalBBER_Object = MibTableColumn
foreSonetFarEndPathIntervalBBER = _ForeSonetFarEndPathIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 8, 2, 1, 4),
    _ForeSonetFarEndPathIntervalBBER_Type()
)
foreSonetFarEndPathIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndPathIntervalBBER.setStatus("current")
_ForeSonetFarEndVT_ObjectIdentity = ObjectIdentity
foreSonetFarEndVT = _ForeSonetFarEndVT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9)
)
_ForeSonetFarEndVTCurrentTable_Object = MibTable
foreSonetFarEndVTCurrentTable = _ForeSonetFarEndVTCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 1)
)
if mibBuilder.loadTexts:
    foreSonetFarEndVTCurrentTable.setStatus("current")
_ForeSonetFarEndVTCurrentEntry_Object = MibTableRow
foreSonetFarEndVTCurrentEntry = _ForeSonetFarEndVTCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 1, 1)
)
foreSonetFarEndVTCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndVTCurrentEntry.setStatus("current")
_ForeSonetFarEndVTCurrentBBEs_Type = Integer32
_ForeSonetFarEndVTCurrentBBEs_Object = MibTableColumn
foreSonetFarEndVTCurrentBBEs = _ForeSonetFarEndVTCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 1, 1, 1),
    _ForeSonetFarEndVTCurrentBBEs_Type()
)
foreSonetFarEndVTCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndVTCurrentBBEs.setStatus("current")
_ForeSonetFarEndVTIntervalTable_Object = MibTable
foreSonetFarEndVTIntervalTable = _ForeSonetFarEndVTIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2)
)
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalTable.setStatus("current")
_ForeSonetFarEndVTIntervalEntry_Object = MibTableRow
foreSonetFarEndVTIntervalEntry = _ForeSonetFarEndVTIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2, 1)
)
foreSonetFarEndVTIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SONET-MIB", "sonetFarEndVTIntervalNumber"),
)
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalEntry.setStatus("current")
_ForeSonetFarEndVTIntervalBBEs_Type = Integer32
_ForeSonetFarEndVTIntervalBBEs_Object = MibTableColumn
foreSonetFarEndVTIntervalBBEs = _ForeSonetFarEndVTIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2, 1, 1),
    _ForeSonetFarEndVTIntervalBBEs_Type()
)
foreSonetFarEndVTIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalBBEs.setStatus("current")
_ForeSonetFarEndVTIntervalESR_Type = Integer32
_ForeSonetFarEndVTIntervalESR_Object = MibTableColumn
foreSonetFarEndVTIntervalESR = _ForeSonetFarEndVTIntervalESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2, 1, 2),
    _ForeSonetFarEndVTIntervalESR_Type()
)
foreSonetFarEndVTIntervalESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalESR.setStatus("current")
_ForeSonetFarEndVTIntervalSESR_Type = Integer32
_ForeSonetFarEndVTIntervalSESR_Object = MibTableColumn
foreSonetFarEndVTIntervalSESR = _ForeSonetFarEndVTIntervalSESR_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2, 1, 3),
    _ForeSonetFarEndVTIntervalSESR_Type()
)
foreSonetFarEndVTIntervalSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalSESR.setStatus("current")
_ForeSonetFarEndVTIntervalBBER_Type = Integer32
_ForeSonetFarEndVTIntervalBBER_Object = MibTableColumn
foreSonetFarEndVTIntervalBBER = _ForeSonetFarEndVTIntervalBBER_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 9, 2, 1, 4),
    _ForeSonetFarEndVTIntervalBBER_Type()
)
foreSonetFarEndVTIntervalBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    foreSonetFarEndVTIntervalBBER.setStatus("current")

# Managed Objects groups


# Notification objects

foreSonetLOSDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 1)
)
foreSonetLOSDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLOSDetected.setStatus(
        "current"
    )

foreSonetLOSCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 2)
)
foreSonetLOSCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLOSCleared.setStatus(
        "current"
    )

foreSonetPathLabelDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 3)
)
foreSonetPathLabelDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathLabelDetected.setStatus(
        "current"
    )

foreSonetPathLabelCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 4)
)
foreSonetPathLabelCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathLabelCleared.setStatus(
        "current"
    )

foreSonetLineAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 5)
)
foreSonetLineAISDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineAISDetected.setStatus(
        "current"
    )

foreSonetLineAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 6)
)
foreSonetLineAISCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineAISCleared.setStatus(
        "current"
    )

foreSonetLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 7)
)
foreSonetLOFDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLOFDetected.setStatus(
        "current"
    )

foreSonetLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 8)
)
foreSonetLOFCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLOFCleared.setStatus(
        "current"
    )

foreSonetLineRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 9)
)
foreSonetLineRDIDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineRDIDetected.setStatus(
        "current"
    )

foreSonetLineRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 10)
)
foreSonetLineRDICleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineRDICleared.setStatus(
        "current"
    )

foreSonetPathAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 11)
)
foreSonetPathAISDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathAISDetected.setStatus(
        "current"
    )

foreSonetPathAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 12)
)
foreSonetPathAISCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathAISCleared.setStatus(
        "current"
    )

foreSonetPathLOPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 13)
)
foreSonetPathLOPDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathLOPDetected.setStatus(
        "current"
    )

foreSonetPathLOPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 14)
)
foreSonetPathLOPCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathLOPCleared.setStatus(
        "current"
    )

foreSonetPathUNEQDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 15)
)
foreSonetPathUNEQDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathUNEQDetected.setStatus(
        "current"
    )

foreSonetPathUNEQCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 16)
)
foreSonetPathUNEQCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathUNEQCleared.setStatus(
        "current"
    )

foreSonetPathRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 17)
)
foreSonetPathRDIDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathRDIDetected.setStatus(
        "current"
    )

foreSonetPathRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 18)
)
foreSonetPathRDICleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathRDICleared.setStatus(
        "current"
    )

foreSonetPathPDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 19)
)
foreSonetPathPDIDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathPDIDetected.setStatus(
        "current"
    )

foreSonetPathPDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 20)
)
foreSonetPathPDICleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetPathPDICleared.setStatus(
        "current"
    )

foreSonetLineBIPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 21)
)
foreSonetLineBIPDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineBIPDetected.setStatus(
        "current"
    )

foreSonetLineBIPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 22)
)
foreSonetLineBIPCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetLineBIPCleared.setStatus(
        "current"
    )

foreSonetVtAISDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 23)
)
foreSonetVtAISDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtAISDetected.setStatus(
        "current"
    )

foreSonetVtAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 24)
)
foreSonetVtAISCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtAISCleared.setStatus(
        "current"
    )

foreSonetVtLOPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 25)
)
foreSonetVtLOPDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtLOPDetected.setStatus(
        "current"
    )

foreSonetVtLOPCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 26)
)
foreSonetVtLOPCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtLOPCleared.setStatus(
        "current"
    )

foreSonetVtUNEQDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 27)
)
foreSonetVtUNEQDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtUNEQDetected.setStatus(
        "current"
    )

foreSonetVtUNEQCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 28)
)
foreSonetVtUNEQCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtUNEQCleared.setStatus(
        "current"
    )

foreSonetVtVILMDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 29)
)
foreSonetVtVILMDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtVILMDetected.setStatus(
        "current"
    )

foreSonetVtVILMCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 30)
)
foreSonetVtVILMCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtVILMCleared.setStatus(
        "current"
    )

foreSonetVtRDIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 31)
)
foreSonetVtRDIDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtRDIDetected.setStatus(
        "current"
    )

foreSonetVtRDICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 32)
)
foreSonetVtRDICleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtRDICleared.setStatus(
        "current"
    )

foreSonetVtRFIDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 33)
)
foreSonetVtRFIDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtRFIDetected.setStatus(
        "current"
    )

foreSonetVtRFICleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 14, 0, 34)
)
foreSonetVtRFICleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    foreSonetVtRFICleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Sonet-Ext-MIB",
    **{"foreSonetMib": foreSonetMib,
       "foreSonetLOSDetected": foreSonetLOSDetected,
       "foreSonetLOSCleared": foreSonetLOSCleared,
       "foreSonetPathLabelDetected": foreSonetPathLabelDetected,
       "foreSonetPathLabelCleared": foreSonetPathLabelCleared,
       "foreSonetLineAISDetected": foreSonetLineAISDetected,
       "foreSonetLineAISCleared": foreSonetLineAISCleared,
       "foreSonetLOFDetected": foreSonetLOFDetected,
       "foreSonetLOFCleared": foreSonetLOFCleared,
       "foreSonetLineRDIDetected": foreSonetLineRDIDetected,
       "foreSonetLineRDICleared": foreSonetLineRDICleared,
       "foreSonetPathAISDetected": foreSonetPathAISDetected,
       "foreSonetPathAISCleared": foreSonetPathAISCleared,
       "foreSonetPathLOPDetected": foreSonetPathLOPDetected,
       "foreSonetPathLOPCleared": foreSonetPathLOPCleared,
       "foreSonetPathUNEQDetected": foreSonetPathUNEQDetected,
       "foreSonetPathUNEQCleared": foreSonetPathUNEQCleared,
       "foreSonetPathRDIDetected": foreSonetPathRDIDetected,
       "foreSonetPathRDICleared": foreSonetPathRDICleared,
       "foreSonetPathPDIDetected": foreSonetPathPDIDetected,
       "foreSonetPathPDICleared": foreSonetPathPDICleared,
       "foreSonetLineBIPDetected": foreSonetLineBIPDetected,
       "foreSonetLineBIPCleared": foreSonetLineBIPCleared,
       "foreSonetVtAISDetected": foreSonetVtAISDetected,
       "foreSonetVtAISCleared": foreSonetVtAISCleared,
       "foreSonetVtLOPDetected": foreSonetVtLOPDetected,
       "foreSonetVtLOPCleared": foreSonetVtLOPCleared,
       "foreSonetVtUNEQDetected": foreSonetVtUNEQDetected,
       "foreSonetVtUNEQCleared": foreSonetVtUNEQCleared,
       "foreSonetVtVILMDetected": foreSonetVtVILMDetected,
       "foreSonetVtVILMCleared": foreSonetVtVILMCleared,
       "foreSonetVtRDIDetected": foreSonetVtRDIDetected,
       "foreSonetVtRDICleared": foreSonetVtRDICleared,
       "foreSonetVtRFIDetected": foreSonetVtRFIDetected,
       "foreSonetVtRFICleared": foreSonetVtRFICleared,
       "foreSonetMedium": foreSonetMedium,
       "foreSonetMediumConfigTable": foreSonetMediumConfigTable,
       "foreSonetMediumConfigEntry": foreSonetMediumConfigEntry,
       "foreSonetMediumConfigLoopbackMode": foreSonetMediumConfigLoopbackMode,
       "foreSonetMediumConfigTxClockSource": foreSonetMediumConfigTxClockSource,
       "foreSonetSection": foreSonetSection,
       "foreSonetSectionTotalTable": foreSonetSectionTotalTable,
       "foreSonetSectionTotalEntry": foreSonetSectionTotalEntry,
       "foreSonetSectionTotalBIPs": foreSonetSectionTotalBIPs,
       "foreSonetSectionTotalLOSs": foreSonetSectionTotalLOSs,
       "foreSonetSectionTotalLOFs": foreSonetSectionTotalLOFs,
       "foreSonetSectionDiagnosticsTable": foreSonetSectionDiagnosticsTable,
       "foreSonetSectionDiagnosticsEntry": foreSonetSectionDiagnosticsEntry,
       "foreSonetSectionDiagnosticsFraming": foreSonetSectionDiagnosticsFraming,
       "foreSonetSectionDiagnosticsB1": foreSonetSectionDiagnosticsB1,
       "foreSonetSectionDiagnosticsDisableTxScrambling": foreSonetSectionDiagnosticsDisableTxScrambling,
       "foreSonetSectionDiagnosticsDisableRxDescrambling": foreSonetSectionDiagnosticsDisableRxDescrambling,
       "foreSonetSectionDiagnosticsLOS": foreSonetSectionDiagnosticsLOS,
       "foreSonetSectionCurrentTable": foreSonetSectionCurrentTable,
       "foreSonetSectionCurrentEntry": foreSonetSectionCurrentEntry,
       "foreSonetSectionCurrentBBEs": foreSonetSectionCurrentBBEs,
       "foreSonetSectionIntervalTable": foreSonetSectionIntervalTable,
       "foreSonetSectionIntervalEntry": foreSonetSectionIntervalEntry,
       "foreSonetSectionIntervalBBEs": foreSonetSectionIntervalBBEs,
       "foreSonetSectionIntervalESR": foreSonetSectionIntervalESR,
       "foreSonetSectionIntervalSESR": foreSonetSectionIntervalSESR,
       "foreSonetSectionIntervalBBER": foreSonetSectionIntervalBBER,
       "foreSonetLine": foreSonetLine,
       "foreSonetLineConfigTable": foreSonetLineConfigTable,
       "foreSonetLineConfigEntry": foreSonetLineConfigEntry,
       "foreSonetLineBipThrSeconds": foreSonetLineBipThrSeconds,
       "foreSonetLineBipThrErrors": foreSonetLineBipThrErrors,
       "foreSonetLineBipFailEnable": foreSonetLineBipFailEnable,
       "foreSonetLineSignalDegradeBer": foreSonetLineSignalDegradeBer,
       "foreSonetLineSignalFailBer": foreSonetLineSignalFailBer,
       "foreSonetLineBerErrorModel": foreSonetLineBerErrorModel,
       "foreSonetLineBerState": foreSonetLineBerState,
       "foreSonetLineTotalTable": foreSonetLineTotalTable,
       "foreSonetLineTotalEntry": foreSonetLineTotalEntry,
       "foreSonetLineTotalBIPs": foreSonetLineTotalBIPs,
       "foreSonetLineTotalFEBEs": foreSonetLineTotalFEBEs,
       "foreSonetLineTotalAISs": foreSonetLineTotalAISs,
       "foreSonetLineTotalRDIs": foreSonetLineTotalRDIs,
       "foreSonetLineDiagnosticsTable": foreSonetLineDiagnosticsTable,
       "foreSonetLineDiagnosticsEntry": foreSonetLineDiagnosticsEntry,
       "foreSonetLineDiagnosticsLAIS": foreSonetLineDiagnosticsLAIS,
       "foreSonetLineDiagnosticsB2": foreSonetLineDiagnosticsB2,
       "foreSonetLineDiagnosticsAPS": foreSonetLineDiagnosticsAPS,
       "foreSonetLineDiagnosticsK1channel": foreSonetLineDiagnosticsK1channel,
       "foreSonetLineDiagnosticsK1request": foreSonetLineDiagnosticsK1request,
       "foreSonetLineDiagnosticsK2channel": foreSonetLineDiagnosticsK2channel,
       "foreSonetLineDiagnosticsK2Architecture": foreSonetLineDiagnosticsK2Architecture,
       "foreSonetLineDiagnosticsK2Mode": foreSonetLineDiagnosticsK2Mode,
       "foreSonetLineDiagnosticsLRDI": foreSonetLineDiagnosticsLRDI,
       "foreSonetLineDiagnosticsLREI": foreSonetLineDiagnosticsLREI,
       "foreSonetLineCurrentTable": foreSonetLineCurrentTable,
       "foreSonetLineCurrentEntry": foreSonetLineCurrentEntry,
       "foreSonetLineCurrentBBEs": foreSonetLineCurrentBBEs,
       "foreSonetLineIntervalTable": foreSonetLineIntervalTable,
       "foreSonetLineIntervalEntry": foreSonetLineIntervalEntry,
       "foreSonetLineIntervalBBEs": foreSonetLineIntervalBBEs,
       "foreSonetLineIntervalESR": foreSonetLineIntervalESR,
       "foreSonetLineIntervalSESR": foreSonetLineIntervalSESR,
       "foreSonetLineIntervalBBER": foreSonetLineIntervalBBER,
       "foreSonetPath": foreSonetPath,
       "foreSonetPathConfigTable": foreSonetPathConfigTable,
       "foreSonetPathConfigEntry": foreSonetPathConfigEntry,
       "foreSonetPathRxSignalLabel": foreSonetPathRxSignalLabel,
       "foreSonetPathTxSignalLabel": foreSonetPathTxSignalLabel,
       "foreSonetPathLoopbackMode": foreSonetPathLoopbackMode,
       "foreSonetPathTotalTable": foreSonetPathTotalTable,
       "foreSonetPathTotalEntry": foreSonetPathTotalEntry,
       "foreSonetPathTotalBIPs": foreSonetPathTotalBIPs,
       "foreSonetPathTotalLOPs": foreSonetPathTotalLOPs,
       "foreSonetPathTotalAISs": foreSonetPathTotalAISs,
       "foreSonetPathTotalRDIs": foreSonetPathTotalRDIs,
       "foreSonetPathTotalUNEQs": foreSonetPathTotalUNEQs,
       "foreSonetPathTotalPLMs": foreSonetPathTotalPLMs,
       "foreSonetPathTotalFEBEs": foreSonetPathTotalFEBEs,
       "foreSonetPathCurrentTable": foreSonetPathCurrentTable,
       "foreSonetPathCurrentEntry": foreSonetPathCurrentEntry,
       "foreSonetPathCurrentStatus": foreSonetPathCurrentStatus,
       "foreSonetPathCurrentBBEs": foreSonetPathCurrentBBEs,
       "foreSonetPathDiagnosticsTable": foreSonetPathDiagnosticsTable,
       "foreSonetPathDiagnosticsEntry": foreSonetPathDiagnosticsEntry,
       "foreSonetPathDiagnosticsC2": foreSonetPathDiagnosticsC2,
       "foreSonetPathDiagnosticsC2Value": foreSonetPathDiagnosticsC2Value,
       "foreSonetPathDiagnosticsB3": foreSonetPathDiagnosticsB3,
       "foreSonetPathDiagnosticsPREI": foreSonetPathDiagnosticsPREI,
       "foreSonetPathDiagnosticsPAIS": foreSonetPathDiagnosticsPAIS,
       "foreSonetPathDiagnosticsPERDI": foreSonetPathDiagnosticsPERDI,
       "foreSonetPathDiagnosticsERDIValue": foreSonetPathDiagnosticsERDIValue,
       "foreSonetPathDiagnosticsLOP": foreSonetPathDiagnosticsLOP,
       "foreSonetPathGroupConfigTable": foreSonetPathGroupConfigTable,
       "foreSonetPathGroupConfigEntry": foreSonetPathGroupConfigEntry,
       "foreVTGroup": foreVTGroup,
       "foreVTWidth": foreVTWidth,
       "foreSonetPathIntervalTable": foreSonetPathIntervalTable,
       "foreSonetPathIntervalEntry": foreSonetPathIntervalEntry,
       "foreSonetPathIntervalBBEs": foreSonetPathIntervalBBEs,
       "foreSonetPathIntervalESR": foreSonetPathIntervalESR,
       "foreSonetPathIntervalSESR": foreSonetPathIntervalSESR,
       "foreSonetPathIntervalBBER": foreSonetPathIntervalBBER,
       "foreSonetVT": foreSonetVT,
       "foreSonetVTConfigTable": foreSonetVTConfigTable,
       "foreSonetVTConfigEntry": foreSonetVTConfigEntry,
       "foreSonetVTLoopbackMode": foreSonetVTLoopbackMode,
       "foreSonetVTTotalTable": foreSonetVTTotalTable,
       "foreSonetVTTotalEntry": foreSonetVTTotalEntry,
       "foreSonetVTTotalBIPs": foreSonetVTTotalBIPs,
       "foreSonetVTTotalREIs": foreSonetVTTotalREIs,
       "foreSonetVTTotalLOPs": foreSonetVTTotalLOPs,
       "foreSonetVTTotalAISs": foreSonetVTTotalAISs,
       "foreSonetVTTotalRDIs": foreSonetVTTotalRDIs,
       "foreSonetVTTotalUNEQs": foreSonetVTTotalUNEQs,
       "foreSonetVTTotalPLMs": foreSonetVTTotalPLMs,
       "foreSonetVTDiagnosticsTable": foreSonetVTDiagnosticsTable,
       "foreSonetVTDiagnosticsEntry": foreSonetVTDiagnosticsEntry,
       "foreSonetVtDiagnosticsBIP": foreSonetVtDiagnosticsBIP,
       "foreSonetVtDiagnosticsRDI": foreSonetVtDiagnosticsRDI,
       "foreSonetVtDiagnosticsRFI": foreSonetVtDiagnosticsRFI,
       "foreSonetVtDiagnosticsAIS": foreSonetVtDiagnosticsAIS,
       "foreSonetVtDiagnosticsLOP": foreSonetVtDiagnosticsLOP,
       "foreSonetVtDiagnosticsLabel": foreSonetVtDiagnosticsLabel,
       "foreSonetVtDiagnosticsLabelValue": foreSonetVtDiagnosticsLabelValue,
       "foreSonetVtDiagnosticsREI": foreSonetVtDiagnosticsREI,
       "foreSonetVTCurrentTable": foreSonetVTCurrentTable,
       "foreSonetVTCurrentEntry": foreSonetVTCurrentEntry,
       "foreSonetVTCurrentBBEs": foreSonetVTCurrentBBEs,
       "foreSonetVTIntervalTable": foreSonetVTIntervalTable,
       "foreSonetVTIntervalEntry": foreSonetVTIntervalEntry,
       "foreSonetVTIntervalBBEs": foreSonetVTIntervalBBEs,
       "foreSonetVTIntervalESR": foreSonetVTIntervalESR,
       "foreSonetVTIntervalSESR": foreSonetVTIntervalSESR,
       "foreSonetVTIntervalBBER": foreSonetVTIntervalBBER,
       "foreSonetSPE": foreSonetSPE,
       "foreSonetFarEndLine": foreSonetFarEndLine,
       "foreSonetFarEndLineCurrentTable": foreSonetFarEndLineCurrentTable,
       "foreSonetFarEndLineCurrentEntry": foreSonetFarEndLineCurrentEntry,
       "foreSonetFarEndLineCurrentBBEs": foreSonetFarEndLineCurrentBBEs,
       "foreSonetFarEndLineIntervalTable": foreSonetFarEndLineIntervalTable,
       "foreSonetFarEndLineIntervalEntry": foreSonetFarEndLineIntervalEntry,
       "foreSonetFarEndLineIntervalBBEs": foreSonetFarEndLineIntervalBBEs,
       "foreSonetFarEndLineIntervalESR": foreSonetFarEndLineIntervalESR,
       "foreSonetFarEndLineIntervalSESR": foreSonetFarEndLineIntervalSESR,
       "foreSonetFarEndLineIntervalBBER": foreSonetFarEndLineIntervalBBER,
       "foreSonetFarEndPath": foreSonetFarEndPath,
       "foreSonetFarEndPathCurrentTable": foreSonetFarEndPathCurrentTable,
       "foreSonetFarEndPathCurrentEntry": foreSonetFarEndPathCurrentEntry,
       "foreSonetFarEndPathCurrentBBEs": foreSonetFarEndPathCurrentBBEs,
       "foreSonetFarEndPathIntervalTable": foreSonetFarEndPathIntervalTable,
       "foreSonetFarEndPathIntervalEntry": foreSonetFarEndPathIntervalEntry,
       "foreSonetFarEndPathIntervalBBEs": foreSonetFarEndPathIntervalBBEs,
       "foreSonetFarEndPathIntervalESR": foreSonetFarEndPathIntervalESR,
       "foreSonetFarEndPathIntervalSESR": foreSonetFarEndPathIntervalSESR,
       "foreSonetFarEndPathIntervalBBER": foreSonetFarEndPathIntervalBBER,
       "foreSonetFarEndVT": foreSonetFarEndVT,
       "foreSonetFarEndVTCurrentTable": foreSonetFarEndVTCurrentTable,
       "foreSonetFarEndVTCurrentEntry": foreSonetFarEndVTCurrentEntry,
       "foreSonetFarEndVTCurrentBBEs": foreSonetFarEndVTCurrentBBEs,
       "foreSonetFarEndVTIntervalTable": foreSonetFarEndVTIntervalTable,
       "foreSonetFarEndVTIntervalEntry": foreSonetFarEndVTIntervalEntry,
       "foreSonetFarEndVTIntervalBBEs": foreSonetFarEndVTIntervalBBEs,
       "foreSonetFarEndVTIntervalESR": foreSonetFarEndVTIntervalESR,
       "foreSonetFarEndVTIntervalSESR": foreSonetFarEndVTIntervalSESR,
       "foreSonetFarEndVTIntervalBBER": foreSonetFarEndVTIntervalBBER}
)
