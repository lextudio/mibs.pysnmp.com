# SNMP MIB module (DOT5-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOT5-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:17 2024
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

(dot5,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "dot5")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot5Rev1_ObjectIdentity = ObjectIdentity
dot5Rev1 = _Dot5Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1)
)
_TRing_ObjectIdentity = ObjectIdentity
tRing = _TRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1)
)
_TRingMgmt_ObjectIdentity = ObjectIdentity
tRingMgmt = _TRingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1)
)
_TRingMgmtRing_ObjectIdentity = ObjectIdentity
tRingMgmtRing = _TRingMgmtRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1)
)


class _TRingMgmtRingName_Type(DisplayString):
    """Custom type tRingMgmtRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TRingMgmtRingName_Type.__name__ = "DisplayString"
_TRingMgmtRingName_Object = MibScalar
tRingMgmtRingName = _TRingMgmtRingName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 1),
    _TRingMgmtRingName_Type()
)
tRingMgmtRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtRingName.setStatus("mandatory")
_TRingMgmtStnPortCount_Type = Integer32
_TRingMgmtStnPortCount_Object = MibScalar
tRingMgmtStnPortCount = _TRingMgmtStnPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 2),
    _TRingMgmtStnPortCount_Type()
)
tRingMgmtStnPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnPortCount.setStatus("mandatory")
_TRingMgmtRingPortCount_Type = Integer32
_TRingMgmtRingPortCount_Object = MibScalar
tRingMgmtRingPortCount = _TRingMgmtRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 3),
    _TRingMgmtRingPortCount_Type()
)
tRingMgmtRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtRingPortCount.setStatus("mandatory")


class _TRingMgmtStnPortsEnable_Type(Integer32):
    """Custom type tRingMgmtStnPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_TRingMgmtStnPortsEnable_Type.__name__ = "Integer32"
_TRingMgmtStnPortsEnable_Object = MibScalar
tRingMgmtStnPortsEnable = _TRingMgmtStnPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 4),
    _TRingMgmtStnPortsEnable_Type()
)
tRingMgmtStnPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnPortsEnable.setStatus("mandatory")


class _TRingMgmtRingPortsEnable_Type(Integer32):
    """Custom type tRingMgmtRingPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_TRingMgmtRingPortsEnable_Type.__name__ = "Integer32"
_TRingMgmtRingPortsEnable_Object = MibScalar
tRingMgmtRingPortsEnable = _TRingMgmtRingPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 5),
    _TRingMgmtRingPortsEnable_Type()
)
tRingMgmtRingPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtRingPortsEnable.setStatus("mandatory")
_TRingMgmtStnPortsOn_Type = Integer32
_TRingMgmtStnPortsOn_Object = MibScalar
tRingMgmtStnPortsOn = _TRingMgmtStnPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 6),
    _TRingMgmtStnPortsOn_Type()
)
tRingMgmtStnPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnPortsOn.setStatus("mandatory")
_TRingMgmtRingPortsOn_Type = Integer32
_TRingMgmtRingPortsOn_Object = MibScalar
tRingMgmtRingPortsOn = _TRingMgmtRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 7),
    _TRingMgmtRingPortsOn_Type()
)
tRingMgmtRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtRingPortsOn.setStatus("mandatory")
_TRingMgmtStations_Type = Integer32
_TRingMgmtStations_Object = MibScalar
tRingMgmtStations = _TRingMgmtStations_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 8),
    _TRingMgmtStations_Type()
)
tRingMgmtStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStations.setStatus("mandatory")


class _TRingMgmtRingState_Type(Integer32):
    """Custom type tRingMgmtRingState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 6),
          ("closed", 2),
          ("contention", 5),
          ("lobeFail", 7),
          ("normalTokenProtocols", 3),
          ("purge", 4),
          ("ringPollFailure", 8),
          ("unknown", 1))
    )


_TRingMgmtRingState_Type.__name__ = "Integer32"
_TRingMgmtRingState_Object = MibScalar
tRingMgmtRingState = _TRingMgmtRingState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 9),
    _TRingMgmtRingState_Type()
)
tRingMgmtRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtRingState.setStatus("mandatory")
_TRingMgmtRingSpeed_Type = Integer32
_TRingMgmtRingSpeed_Object = MibScalar
tRingMgmtRingSpeed = _TRingMgmtRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 10),
    _TRingMgmtRingSpeed_Type()
)
tRingMgmtRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtRingSpeed.setStatus("mandatory")


class _TRingMgmtActiveMonitor_Type(OctetString):
    """Custom type tRingMgmtActiveMonitor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtActiveMonitor_Type.__name__ = "OctetString"
_TRingMgmtActiveMonitor_Object = MibScalar
tRingMgmtActiveMonitor = _TRingMgmtActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 11),
    _TRingMgmtActiveMonitor_Type()
)
tRingMgmtActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtActiveMonitor.setStatus("mandatory")
_TRingMgmtRingNumber_Type = Integer32
_TRingMgmtRingNumber_Object = MibScalar
tRingMgmtRingNumber = _TRingMgmtRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 12),
    _TRingMgmtRingNumber_Type()
)
tRingMgmtRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtRingNumber.setStatus("mandatory")


class _TRingMgmtBeaconRecovery_Type(Integer32):
    """Custom type tRingMgmtBeaconRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("invalid", 3))
    )


_TRingMgmtBeaconRecovery_Type.__name__ = "Integer32"
_TRingMgmtBeaconRecovery_Object = MibScalar
tRingMgmtBeaconRecovery = _TRingMgmtBeaconRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 13),
    _TRingMgmtBeaconRecovery_Type()
)
tRingMgmtBeaconRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBeaconRecovery.setStatus("mandatory")


class _TRingMgmtBcnRecRingPortRetryCount_Type(Integer32):
    """Custom type tRingMgmtBcnRecRingPortRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecRingPortRetryCount_Type.__name__ = "Integer32"
_TRingMgmtBcnRecRingPortRetryCount_Object = MibScalar
tRingMgmtBcnRecRingPortRetryCount = _TRingMgmtBcnRecRingPortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 14),
    _TRingMgmtBcnRecRingPortRetryCount_Type()
)
tRingMgmtBcnRecRingPortRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecRingPortRetryCount.setStatus("mandatory")


class _TRingMgmtBcnRecRingPortRetryDelay_Type(Integer32):
    """Custom type tRingMgmtBcnRecRingPortRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecRingPortRetryDelay_Type.__name__ = "Integer32"
_TRingMgmtBcnRecRingPortRetryDelay_Object = MibScalar
tRingMgmtBcnRecRingPortRetryDelay = _TRingMgmtBcnRecRingPortRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 15),
    _TRingMgmtBcnRecRingPortRetryDelay_Type()
)
tRingMgmtBcnRecRingPortRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecRingPortRetryDelay.setStatus("mandatory")


class _TRingMgmtBcnRecStnPortRetryCount_Type(Integer32):
    """Custom type tRingMgmtBcnRecStnPortRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecStnPortRetryCount_Type.__name__ = "Integer32"
_TRingMgmtBcnRecStnPortRetryCount_Object = MibScalar
tRingMgmtBcnRecStnPortRetryCount = _TRingMgmtBcnRecStnPortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 16),
    _TRingMgmtBcnRecStnPortRetryCount_Type()
)
tRingMgmtBcnRecStnPortRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecStnPortRetryCount.setStatus("mandatory")


class _TRingMgmtBcnRecStnPortRetryDelay_Type(Integer32):
    """Custom type tRingMgmtBcnRecStnPortRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecStnPortRetryDelay_Type.__name__ = "Integer32"
_TRingMgmtBcnRecStnPortRetryDelay_Object = MibScalar
tRingMgmtBcnRecStnPortRetryDelay = _TRingMgmtBcnRecStnPortRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 17),
    _TRingMgmtBcnRecStnPortRetryDelay_Type()
)
tRingMgmtBcnRecStnPortRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecStnPortRetryDelay.setStatus("mandatory")


class _TRingMgmtBcnRecBrdBypassRetryCount_Type(Integer32):
    """Custom type tRingMgmtBcnRecBrdBypassRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecBrdBypassRetryCount_Type.__name__ = "Integer32"
_TRingMgmtBcnRecBrdBypassRetryCount_Object = MibScalar
tRingMgmtBcnRecBrdBypassRetryCount = _TRingMgmtBcnRecBrdBypassRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 18),
    _TRingMgmtBcnRecBrdBypassRetryCount_Type()
)
tRingMgmtBcnRecBrdBypassRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecBrdBypassRetryCount.setStatus("mandatory")


class _TRingMgmtBcnRecBrdBypassRetryDelay_Type(Integer32):
    """Custom type tRingMgmtBcnRecBrdBypassRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TRingMgmtBcnRecBrdBypassRetryDelay_Type.__name__ = "Integer32"
_TRingMgmtBcnRecBrdBypassRetryDelay_Object = MibScalar
tRingMgmtBcnRecBrdBypassRetryDelay = _TRingMgmtBcnRecBrdBypassRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 19),
    _TRingMgmtBcnRecBrdBypassRetryDelay_Type()
)
tRingMgmtBcnRecBrdBypassRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecBrdBypassRetryDelay.setStatus("mandatory")


class _TRingMgmtBcnRecBrdWrapRetryCount_Type(Integer32):
    """Custom type tRingMgmtBcnRecBrdWrapRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TRingMgmtBcnRecBrdWrapRetryCount_Type.__name__ = "Integer32"
_TRingMgmtBcnRecBrdWrapRetryCount_Object = MibScalar
tRingMgmtBcnRecBrdWrapRetryCount = _TRingMgmtBcnRecBrdWrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 20),
    _TRingMgmtBcnRecBrdWrapRetryCount_Type()
)
tRingMgmtBcnRecBrdWrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecBrdWrapRetryCount.setStatus("mandatory")


class _TRingMgmtBcnRecBrdWrapRetryDelay_Type(Integer32):
    """Custom type tRingMgmtBcnRecBrdWrapRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TRingMgmtBcnRecBrdWrapRetryDelay_Type.__name__ = "Integer32"
_TRingMgmtBcnRecBrdWrapRetryDelay_Object = MibScalar
tRingMgmtBcnRecBrdWrapRetryDelay = _TRingMgmtBcnRecBrdWrapRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 21),
    _TRingMgmtBcnRecBrdWrapRetryDelay_Type()
)
tRingMgmtBcnRecBrdWrapRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtBcnRecBrdWrapRetryDelay.setStatus("mandatory")


class _TRingMgmtRingPollRecovery_Type(Integer32):
    """Custom type tRingMgmtRingPollRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("invalid", 3))
    )


_TRingMgmtRingPollRecovery_Type.__name__ = "Integer32"
_TRingMgmtRingPollRecovery_Object = MibScalar
tRingMgmtRingPollRecovery = _TRingMgmtRingPollRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 1, 22),
    _TRingMgmtRingPollRecovery_Type()
)
tRingMgmtRingPollRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtRingPollRecovery.setStatus("mandatory")
_TRingMgmtStn_ObjectIdentity = ObjectIdentity
tRingMgmtStn = _TRingMgmtStn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2)
)
_TRingMgmtStnTable_Object = MibTable
tRingMgmtStnTable = _TRingMgmtStnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tRingMgmtStnTable.setStatus("mandatory")
_TRingMgmtStnEntry_Object = MibTableRow
tRingMgmtStnEntry = _TRingMgmtStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1)
)
tRingMgmtStnEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingMgmtStnAddress"),
)
if mibBuilder.loadTexts:
    tRingMgmtStnEntry.setStatus("mandatory")


class _TRingMgmtStnAddress_Type(OctetString):
    """Custom type tRingMgmtStnAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtStnAddress_Type.__name__ = "OctetString"
_TRingMgmtStnAddress_Object = MibTableColumn
tRingMgmtStnAddress = _TRingMgmtStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1),
    _TRingMgmtStnAddress_Type()
)
tRingMgmtStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnAddress.setStatus("mandatory")


class _TRingMgmtStnName_Type(DisplayString):
    """Custom type tRingMgmtStnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TRingMgmtStnName_Type.__name__ = "DisplayString"
_TRingMgmtStnName_Object = MibTableColumn
tRingMgmtStnName = _TRingMgmtStnName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2),
    _TRingMgmtStnName_Type()
)
tRingMgmtStnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnName.setStatus("mandatory")
_TRingMgmtStnBoard_Type = Integer32
_TRingMgmtStnBoard_Object = MibTableColumn
tRingMgmtStnBoard = _TRingMgmtStnBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 3),
    _TRingMgmtStnBoard_Type()
)
tRingMgmtStnBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnBoard.setStatus("mandatory")
_TRingMgmtStnPort_Type = Integer32
_TRingMgmtStnPort_Object = MibTableColumn
tRingMgmtStnPort = _TRingMgmtStnPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 4),
    _TRingMgmtStnPort_Type()
)
tRingMgmtStnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnPort.setStatus("mandatory")


class _TRingMgmtStnUNA_Type(OctetString):
    """Custom type tRingMgmtStnUNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtStnUNA_Type.__name__ = "OctetString"
_TRingMgmtStnUNA_Object = MibTableColumn
tRingMgmtStnUNA = _TRingMgmtStnUNA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 5),
    _TRingMgmtStnUNA_Type()
)
tRingMgmtStnUNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnUNA.setStatus("mandatory")


class _TRingMgmtStnDNA_Type(OctetString):
    """Custom type tRingMgmtStnDNA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtStnDNA_Type.__name__ = "OctetString"
_TRingMgmtStnDNA_Object = MibTableColumn
tRingMgmtStnDNA = _TRingMgmtStnDNA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 6),
    _TRingMgmtStnDNA_Type()
)
tRingMgmtStnDNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtStnDNA.setStatus("mandatory")


class _TRingMgmtStnPhysLocation_Type(OctetString):
    """Custom type tRingMgmtStnPhysLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TRingMgmtStnPhysLocation_Type.__name__ = "OctetString"
_TRingMgmtStnPhysLocation_Object = MibTableColumn
tRingMgmtStnPhysLocation = _TRingMgmtStnPhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 7),
    _TRingMgmtStnPhysLocation_Type()
)
tRingMgmtStnPhysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnPhysLocation.setStatus("mandatory")


class _TRingMgmtStnFuncClasses_Type(OctetString):
    """Custom type tRingMgmtStnFuncClasses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TRingMgmtStnFuncClasses_Type.__name__ = "OctetString"
_TRingMgmtStnFuncClasses_Object = MibTableColumn
tRingMgmtStnFuncClasses = _TRingMgmtStnFuncClasses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 8),
    _TRingMgmtStnFuncClasses_Type()
)
tRingMgmtStnFuncClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnFuncClasses.setStatus("mandatory")


class _TRingMgmtStnPriority_Type(Integer32):
    """Custom type tRingMgmtStnPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_TRingMgmtStnPriority_Type.__name__ = "Integer32"
_TRingMgmtStnPriority_Object = MibTableColumn
tRingMgmtStnPriority = _TRingMgmtStnPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 9),
    _TRingMgmtStnPriority_Type()
)
tRingMgmtStnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnPriority.setStatus("mandatory")


class _TRingMgmtStnRemoveStn_Type(Integer32):
    """Custom type tRingMgmtStnRemoveStn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRemove", 1),
          ("remove", 2))
    )


_TRingMgmtStnRemoveStn_Type.__name__ = "Integer32"
_TRingMgmtStnRemoveStn_Object = MibTableColumn
tRingMgmtStnRemoveStn = _TRingMgmtStnRemoveStn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 2, 1, 1, 10),
    _TRingMgmtStnRemoveStn_Type()
)
tRingMgmtStnRemoveStn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtStnRemoveStn.setStatus("mandatory")
_TRingMgmtHost_ObjectIdentity = ObjectIdentity
tRingMgmtHost = _TRingMgmtHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3)
)


class _TRingMgmtHostCommands_Type(Integer32):
    """Custom type tRingMgmtHostCommands based on Integer32"""
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
        *(("close", 5),
          ("hwReset", 2),
          ("nop", 1),
          ("open", 4),
          ("swReset", 3))
    )


_TRingMgmtHostCommands_Type.__name__ = "Integer32"
_TRingMgmtHostCommands_Object = MibScalar
tRingMgmtHostCommands = _TRingMgmtHostCommands_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 1),
    _TRingMgmtHostCommands_Type()
)
tRingMgmtHostCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtHostCommands.setStatus("mandatory")


class _TRingMgmtHostOpenStatus_Type(Integer32):
    """Custom type tRingMgmtHostOpenStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMACAddress", 8),
          ("insertionTimeout", 5),
          ("lobeTestFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_TRingMgmtHostOpenStatus_Type.__name__ = "Integer32"
_TRingMgmtHostOpenStatus_Object = MibScalar
tRingMgmtHostOpenStatus = _TRingMgmtHostOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 2),
    _TRingMgmtHostOpenStatus_Type()
)
tRingMgmtHostOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtHostOpenStatus.setStatus("mandatory")
_TRingMgmtHostErrorStatus_Type = Integer32
_TRingMgmtHostErrorStatus_Object = MibScalar
tRingMgmtHostErrorStatus = _TRingMgmtHostErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 3),
    _TRingMgmtHostErrorStatus_Type()
)
tRingMgmtHostErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtHostErrorStatus.setStatus("mandatory")


class _TRingMgmtHostAMContention_Type(Integer32):
    """Custom type tRingMgmtHostAMContention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("contentionAllowed", 2),
          ("noContentionAllowed", 1))
    )


_TRingMgmtHostAMContention_Type.__name__ = "Integer32"
_TRingMgmtHostAMContention_Object = MibScalar
tRingMgmtHostAMContention = _TRingMgmtHostAMContention_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 4),
    _TRingMgmtHostAMContention_Type()
)
tRingMgmtHostAMContention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtHostAMContention.setStatus("mandatory")
_TRingMgmtHostTErrorReport_Type = Integer32
_TRingMgmtHostTErrorReport_Object = MibScalar
tRingMgmtHostTErrorReport = _TRingMgmtHostTErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 5),
    _TRingMgmtHostTErrorReport_Type()
)
tRingMgmtHostTErrorReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtHostTErrorReport.setStatus("mandatory")


class _TRingMgmtHostLocalAdminMac_Type(OctetString):
    """Custom type tRingMgmtHostLocalAdminMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtHostLocalAdminMac_Type.__name__ = "OctetString"
_TRingMgmtHostLocalAdminMac_Object = MibScalar
tRingMgmtHostLocalAdminMac = _TRingMgmtHostLocalAdminMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 3, 6),
    _TRingMgmtHostLocalAdminMac_Type()
)
tRingMgmtHostLocalAdminMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtHostLocalAdminMac.setStatus("deprecated")
_TRingMgmtSecurity_ObjectIdentity = ObjectIdentity
tRingMgmtSecurity = _TRingMgmtSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4)
)


class _TRingMgmtSecurityAdminState_Type(Integer32):
    """Custom type tRingMgmtSecurityAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableWithAlarm", 2),
          ("enableWithRemoveAndAlarm", 3))
    )


_TRingMgmtSecurityAdminState_Type.__name__ = "Integer32"
_TRingMgmtSecurityAdminState_Object = MibScalar
tRingMgmtSecurityAdminState = _TRingMgmtSecurityAdminState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 1),
    _TRingMgmtSecurityAdminState_Type()
)
tRingMgmtSecurityAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtSecurityAdminState.setStatus("mandatory")


class _TRingMgmtSecurityAddressAdd_Type(OctetString):
    """Custom type tRingMgmtSecurityAddressAdd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtSecurityAddressAdd_Type.__name__ = "OctetString"
_TRingMgmtSecurityAddressAdd_Object = MibScalar
tRingMgmtSecurityAddressAdd = _TRingMgmtSecurityAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 2),
    _TRingMgmtSecurityAddressAdd_Type()
)
tRingMgmtSecurityAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtSecurityAddressAdd.setStatus("mandatory")


class _TRingMgmtSecurityAddressRemove_Type(OctetString):
    """Custom type tRingMgmtSecurityAddressRemove based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtSecurityAddressRemove_Type.__name__ = "OctetString"
_TRingMgmtSecurityAddressRemove_Object = MibScalar
tRingMgmtSecurityAddressRemove = _TRingMgmtSecurityAddressRemove_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 3),
    _TRingMgmtSecurityAddressRemove_Type()
)
tRingMgmtSecurityAddressRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingMgmtSecurityAddressRemove.setStatus("mandatory")
_TRingMgmtSecurityStnCount_Type = Integer32
_TRingMgmtSecurityStnCount_Object = MibScalar
tRingMgmtSecurityStnCount = _TRingMgmtSecurityStnCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 4),
    _TRingMgmtSecurityStnCount_Type()
)
tRingMgmtSecurityStnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtSecurityStnCount.setStatus("mandatory")
_TRingMgmtSecurityTable_Object = MibTable
tRingMgmtSecurityTable = _TRingMgmtSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tRingMgmtSecurityTable.setStatus("mandatory")
_TRingMgmtSecurityEntry_Object = MibTableRow
tRingMgmtSecurityEntry = _TRingMgmtSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 5, 1)
)
tRingMgmtSecurityEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingMgmtSecurityIfIndex"),
    (0, "DOT5-LOG-MIB", "tRingMgmtSecurityStnAddress"),
)
if mibBuilder.loadTexts:
    tRingMgmtSecurityEntry.setStatus("mandatory")
_TRingMgmtSecurityIfIndex_Type = Integer32
_TRingMgmtSecurityIfIndex_Object = MibTableColumn
tRingMgmtSecurityIfIndex = _TRingMgmtSecurityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 5, 1, 1),
    _TRingMgmtSecurityIfIndex_Type()
)
tRingMgmtSecurityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtSecurityIfIndex.setStatus("mandatory")


class _TRingMgmtSecurityStnAddress_Type(OctetString):
    """Custom type tRingMgmtSecurityStnAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingMgmtSecurityStnAddress_Type.__name__ = "OctetString"
_TRingMgmtSecurityStnAddress_Object = MibTableColumn
tRingMgmtSecurityStnAddress = _TRingMgmtSecurityStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 1, 4, 5, 1, 2),
    _TRingMgmtSecurityStnAddress_Type()
)
tRingMgmtSecurityStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingMgmtSecurityStnAddress.setStatus("mandatory")
_TRingStats_ObjectIdentity = ObjectIdentity
tRingStats = _TRingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2)
)
_TRingStatsRing_ObjectIdentity = ObjectIdentity
tRingStatsRing = _TRingStatsRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1)
)
_TRingStatsRingErrs_ObjectIdentity = ObjectIdentity
tRingStatsRingErrs = _TRingStatsRingErrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1)
)
_TRingStatsRingFrames_Type = Counter32
_TRingStatsRingFrames_Object = MibScalar
tRingStatsRingFrames = _TRingStatsRingFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 1),
    _TRingStatsRingFrames_Type()
)
tRingStatsRingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFrames.setStatus("mandatory")
_TRingStatsRingKBytes_Type = Counter32
_TRingStatsRingKBytes_Object = MibScalar
tRingStatsRingKBytes = _TRingStatsRingKBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 2),
    _TRingStatsRingKBytes_Type()
)
tRingStatsRingKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingKBytes.setStatus("mandatory")
_TRingStatsRingLineErrors_Type = Counter32
_TRingStatsRingLineErrors_Object = MibScalar
tRingStatsRingLineErrors = _TRingStatsRingLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 3),
    _TRingStatsRingLineErrors_Type()
)
tRingStatsRingLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingLineErrors.setStatus("mandatory")
_TRingStatsRingBurstErrors_Type = Counter32
_TRingStatsRingBurstErrors_Object = MibScalar
tRingStatsRingBurstErrors = _TRingStatsRingBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 4),
    _TRingStatsRingBurstErrors_Type()
)
tRingStatsRingBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingBurstErrors.setStatus("mandatory")
_TRingStatsRingACErrors_Type = Counter32
_TRingStatsRingACErrors_Object = MibScalar
tRingStatsRingACErrors = _TRingStatsRingACErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 5),
    _TRingStatsRingACErrors_Type()
)
tRingStatsRingACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingACErrors.setStatus("mandatory")
_TRingStatsRingAbortSequences_Type = Counter32
_TRingStatsRingAbortSequences_Object = MibScalar
tRingStatsRingAbortSequences = _TRingStatsRingAbortSequences_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 6),
    _TRingStatsRingAbortSequences_Type()
)
tRingStatsRingAbortSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingAbortSequences.setStatus("mandatory")
_TRingStatsRingInternalErrors_Type = Counter32
_TRingStatsRingInternalErrors_Object = MibScalar
tRingStatsRingInternalErrors = _TRingStatsRingInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 7),
    _TRingStatsRingInternalErrors_Type()
)
tRingStatsRingInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingInternalErrors.setStatus("mandatory")
_TRingStatsRingLostFrames_Type = Counter32
_TRingStatsRingLostFrames_Object = MibScalar
tRingStatsRingLostFrames = _TRingStatsRingLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 8),
    _TRingStatsRingLostFrames_Type()
)
tRingStatsRingLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingLostFrames.setStatus("mandatory")
_TRingStatsRingCongestErrors_Type = Counter32
_TRingStatsRingCongestErrors_Object = MibScalar
tRingStatsRingCongestErrors = _TRingStatsRingCongestErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 9),
    _TRingStatsRingCongestErrors_Type()
)
tRingStatsRingCongestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingCongestErrors.setStatus("mandatory")
_TRingStatsRingFCErrors_Type = Counter32
_TRingStatsRingFCErrors_Object = MibScalar
tRingStatsRingFCErrors = _TRingStatsRingFCErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 10),
    _TRingStatsRingFCErrors_Type()
)
tRingStatsRingFCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFCErrors.setStatus("mandatory")
_TRingStatsRingTokenErrors_Type = Counter32
_TRingStatsRingTokenErrors_Object = MibScalar
tRingStatsRingTokenErrors = _TRingStatsRingTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 11),
    _TRingStatsRingTokenErrors_Type()
)
tRingStatsRingTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingTokenErrors.setStatus("mandatory")
_TRingStatsRingFreqErrors_Type = Counter32
_TRingStatsRingFreqErrors_Object = MibScalar
tRingStatsRingFreqErrors = _TRingStatsRingFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 12),
    _TRingStatsRingFreqErrors_Type()
)
tRingStatsRingFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFreqErrors.setStatus("mandatory")
_TRingStatsRingTotalErrors_Type = Counter32
_TRingStatsRingTotalErrors_Object = MibScalar
tRingStatsRingTotalErrors = _TRingStatsRingTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 13),
    _TRingStatsRingTotalErrors_Type()
)
tRingStatsRingTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingTotalErrors.setStatus("mandatory")
_TRingStatsRingAMChanges_Type = Counter32
_TRingStatsRingAMChanges_Object = MibScalar
tRingStatsRingAMChanges = _TRingStatsRingAMChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 14),
    _TRingStatsRingAMChanges_Type()
)
tRingStatsRingAMChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingAMChanges.setStatus("mandatory")
_TRingStatsRingRingPurges_Type = Counter32
_TRingStatsRingRingPurges_Object = MibScalar
tRingStatsRingRingPurges = _TRingStatsRingRingPurges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 15),
    _TRingStatsRingRingPurges_Type()
)
tRingStatsRingRingPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingRingPurges.setStatus("mandatory")
_TRingStatsRingBeaconEvents_Type = Counter32
_TRingStatsRingBeaconEvents_Object = MibScalar
tRingStatsRingBeaconEvents = _TRingStatsRingBeaconEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 16),
    _TRingStatsRingBeaconEvents_Type()
)
tRingStatsRingBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingBeaconEvents.setStatus("mandatory")
_TRingStatsRingLongestBeacon_Type = TimeTicks
_TRingStatsRingLongestBeacon_Object = MibScalar
tRingStatsRingLongestBeacon = _TRingStatsRingLongestBeacon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 17),
    _TRingStatsRingLongestBeacon_Type()
)
tRingStatsRingLongestBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingLongestBeacon.setStatus("mandatory")
_TRingStatsRingLastBeacon_Type = TimeTicks
_TRingStatsRingLastBeacon_Object = MibScalar
tRingStatsRingLastBeacon = _TRingStatsRingLastBeacon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 18),
    _TRingStatsRingLastBeacon_Type()
)
tRingStatsRingLastBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingLastBeacon.setStatus("mandatory")


class _TRingStatsRingLastBeaconType_Type(Integer32):
    """Custom type tRingStatsRingLastBeaconType based on Integer32"""
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
        *(("noBeaconFramesDetected", 5),
          ("recoveryModeSet", 1),
          ("signalLossError", 2),
          ("streamingSignalClaimToken", 4),
          ("streamingSignalNotClaimToken", 3))
    )


_TRingStatsRingLastBeaconType_Type.__name__ = "Integer32"
_TRingStatsRingLastBeaconType_Object = MibScalar
tRingStatsRingLastBeaconType = _TRingStatsRingLastBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 19),
    _TRingStatsRingLastBeaconType_Type()
)
tRingStatsRingLastBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingLastBeaconType.setStatus("mandatory")
_TRingStatsRingPollFailureNoRecovery_Type = Counter32
_TRingStatsRingPollFailureNoRecovery_Object = MibScalar
tRingStatsRingPollFailureNoRecovery = _TRingStatsRingPollFailureNoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 20),
    _TRingStatsRingPollFailureNoRecovery_Type()
)
tRingStatsRingPollFailureNoRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingPollFailureNoRecovery.setStatus("mandatory")
_TRingStatsRingPollFailureNNIFrameCount_Type = Counter32
_TRingStatsRingPollFailureNNIFrameCount_Object = MibScalar
tRingStatsRingPollFailureNNIFrameCount = _TRingStatsRingPollFailureNNIFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 21),
    _TRingStatsRingPollFailureNNIFrameCount_Type()
)
tRingStatsRingPollFailureNNIFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingPollFailureNNIFrameCount.setStatus("mandatory")


class _TRingStatsRingPollFailureNNIFrameAddress_Type(OctetString):
    """Custom type tRingStatsRingPollFailureNNIFrameAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingStatsRingPollFailureNNIFrameAddress_Type.__name__ = "OctetString"
_TRingStatsRingPollFailureNNIFrameAddress_Object = MibScalar
tRingStatsRingPollFailureNNIFrameAddress = _TRingStatsRingPollFailureNNIFrameAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 22),
    _TRingStatsRingPollFailureNNIFrameAddress_Type()
)
tRingStatsRingPollFailureNNIFrameAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingPollFailureNNIFrameAddress.setStatus("mandatory")
_TRingStatsRingPollFailureLastNNIFrameTime_Type = Counter32
_TRingStatsRingPollFailureLastNNIFrameTime_Object = MibScalar
tRingStatsRingPollFailureLastNNIFrameTime = _TRingStatsRingPollFailureLastNNIFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 23),
    _TRingStatsRingPollFailureLastNNIFrameTime_Type()
)
tRingStatsRingPollFailureLastNNIFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingPollFailureLastNNIFrameTime.setStatus("mandatory")


class _TRingStatsRingPollFailureLastDNAAddress_Type(OctetString):
    """Custom type tRingStatsRingPollFailureLastDNAAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingStatsRingPollFailureLastDNAAddress_Type.__name__ = "OctetString"
_TRingStatsRingPollFailureLastDNAAddress_Object = MibScalar
tRingStatsRingPollFailureLastDNAAddress = _TRingStatsRingPollFailureLastDNAAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 1, 24),
    _TRingStatsRingPollFailureLastDNAAddress_Type()
)
tRingStatsRingPollFailureLastDNAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingPollFailureLastDNAAddress.setStatus("mandatory")
_TRingStatsRingProtos_ObjectIdentity = ObjectIdentity
tRingStatsRingProtos = _TRingStatsRingProtos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2)
)
_TRingStatsRingProtocolSnaFrames_Type = Counter32
_TRingStatsRingProtocolSnaFrames_Object = MibScalar
tRingStatsRingProtocolSnaFrames = _TRingStatsRingProtocolSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 1),
    _TRingStatsRingProtocolSnaFrames_Type()
)
tRingStatsRingProtocolSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolSnaFrames.setStatus("mandatory")
_TRingStatsRingProtocolXnsFrames_Type = Counter32
_TRingStatsRingProtocolXnsFrames_Object = MibScalar
tRingStatsRingProtocolXnsFrames = _TRingStatsRingProtocolXnsFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 2),
    _TRingStatsRingProtocolXnsFrames_Type()
)
tRingStatsRingProtocolXnsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolXnsFrames.setStatus("mandatory")
_TRingStatsRingProtocolTcpIpFrames_Type = Counter32
_TRingStatsRingProtocolTcpIpFrames_Object = MibScalar
tRingStatsRingProtocolTcpIpFrames = _TRingStatsRingProtocolTcpIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 3),
    _TRingStatsRingProtocolTcpIpFrames_Type()
)
tRingStatsRingProtocolTcpIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolTcpIpFrames.setStatus("mandatory")
_TRingStatsRingProtocolBanyanFrames_Type = Counter32
_TRingStatsRingProtocolBanyanFrames_Object = MibScalar
tRingStatsRingProtocolBanyanFrames = _TRingStatsRingProtocolBanyanFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 4),
    _TRingStatsRingProtocolBanyanFrames_Type()
)
tRingStatsRingProtocolBanyanFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolBanyanFrames.setStatus("mandatory")
_TRingStatsRingProtocolIpxFrames_Type = Counter32
_TRingStatsRingProtocolIpxFrames_Object = MibScalar
tRingStatsRingProtocolIpxFrames = _TRingStatsRingProtocolIpxFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 5),
    _TRingStatsRingProtocolIpxFrames_Type()
)
tRingStatsRingProtocolIpxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolIpxFrames.setStatus("mandatory")
_TRingStatsRingProtocolNetbiosFrames_Type = Counter32
_TRingStatsRingProtocolNetbiosFrames_Object = MibScalar
tRingStatsRingProtocolNetbiosFrames = _TRingStatsRingProtocolNetbiosFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 6),
    _TRingStatsRingProtocolNetbiosFrames_Type()
)
tRingStatsRingProtocolNetbiosFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolNetbiosFrames.setStatus("mandatory")
_TRingStatsRingProtocolLanNetMgrFrames_Type = Counter32
_TRingStatsRingProtocolLanNetMgrFrames_Object = MibScalar
tRingStatsRingProtocolLanNetMgrFrames = _TRingStatsRingProtocolLanNetMgrFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 7),
    _TRingStatsRingProtocolLanNetMgrFrames_Type()
)
tRingStatsRingProtocolLanNetMgrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolLanNetMgrFrames.setStatus("mandatory")
_TRingStatsRingProtocolOtherFrames_Type = Counter32
_TRingStatsRingProtocolOtherFrames_Object = MibScalar
tRingStatsRingProtocolOtherFrames = _TRingStatsRingProtocolOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 2, 8),
    _TRingStatsRingProtocolOtherFrames_Type()
)
tRingStatsRingProtocolOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingProtocolOtherFrames.setStatus("mandatory")
_TRingStatsRingSizes_ObjectIdentity = ObjectIdentity
tRingStatsRingSizes = _TRingStatsRingSizes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3)
)
_TRingStatsRingFramesizeUpTo63Bytes_Type = Counter32
_TRingStatsRingFramesizeUpTo63Bytes_Object = MibScalar
tRingStatsRingFramesizeUpTo63Bytes = _TRingStatsRingFramesizeUpTo63Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 1),
    _TRingStatsRingFramesizeUpTo63Bytes_Type()
)
tRingStatsRingFramesizeUpTo63Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesizeUpTo63Bytes.setStatus("mandatory")
_TRingStatsRingFramesize64To127Bytes_Type = Counter32
_TRingStatsRingFramesize64To127Bytes_Object = MibScalar
tRingStatsRingFramesize64To127Bytes = _TRingStatsRingFramesize64To127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 2),
    _TRingStatsRingFramesize64To127Bytes_Type()
)
tRingStatsRingFramesize64To127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize64To127Bytes.setStatus("mandatory")
_TRingStatsRingFramesize128To255Bytes_Type = Counter32
_TRingStatsRingFramesize128To255Bytes_Object = MibScalar
tRingStatsRingFramesize128To255Bytes = _TRingStatsRingFramesize128To255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 3),
    _TRingStatsRingFramesize128To255Bytes_Type()
)
tRingStatsRingFramesize128To255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize128To255Bytes.setStatus("mandatory")
_TRingStatsRingFramesize256To511Bytes_Type = Counter32
_TRingStatsRingFramesize256To511Bytes_Object = MibScalar
tRingStatsRingFramesize256To511Bytes = _TRingStatsRingFramesize256To511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 4),
    _TRingStatsRingFramesize256To511Bytes_Type()
)
tRingStatsRingFramesize256To511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize256To511Bytes.setStatus("mandatory")
_TRingStatsRingFramesize512To1023Bytes_Type = Counter32
_TRingStatsRingFramesize512To1023Bytes_Object = MibScalar
tRingStatsRingFramesize512To1023Bytes = _TRingStatsRingFramesize512To1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 5),
    _TRingStatsRingFramesize512To1023Bytes_Type()
)
tRingStatsRingFramesize512To1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize512To1023Bytes.setStatus("mandatory")
_TRingStatsRingFramesize1024To2047Bytes_Type = Counter32
_TRingStatsRingFramesize1024To2047Bytes_Object = MibScalar
tRingStatsRingFramesize1024To2047Bytes = _TRingStatsRingFramesize1024To2047Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 6),
    _TRingStatsRingFramesize1024To2047Bytes_Type()
)
tRingStatsRingFramesize1024To2047Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize1024To2047Bytes.setStatus("mandatory")
_TRingStatsRingFramesize2048To4095Bytes_Type = Counter32
_TRingStatsRingFramesize2048To4095Bytes_Object = MibScalar
tRingStatsRingFramesize2048To4095Bytes = _TRingStatsRingFramesize2048To4095Bytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 7),
    _TRingStatsRingFramesize2048To4095Bytes_Type()
)
tRingStatsRingFramesize2048To4095Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize2048To4095Bytes.setStatus("mandatory")
_TRingStatsRingFramesize4096AndUpBytes_Type = Counter32
_TRingStatsRingFramesize4096AndUpBytes_Object = MibScalar
tRingStatsRingFramesize4096AndUpBytes = _TRingStatsRingFramesize4096AndUpBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 1, 3, 8),
    _TRingStatsRingFramesize4096AndUpBytes_Type()
)
tRingStatsRingFramesize4096AndUpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsRingFramesize4096AndUpBytes.setStatus("mandatory")
_TRingStatsStn_ObjectIdentity = ObjectIdentity
tRingStatsStn = _TRingStatsStn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2)
)
_TRingStatsStnTable_Object = MibTable
tRingStatsStnTable = _TRingStatsStnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tRingStatsStnTable.setStatus("mandatory")
_TRingStatsStnEntry_Object = MibTableRow
tRingStatsStnEntry = _TRingStatsStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1)
)
tRingStatsStnEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingStatsStnAddress"),
)
if mibBuilder.loadTexts:
    tRingStatsStnEntry.setStatus("mandatory")


class _TRingStatsStnAddress_Type(OctetString):
    """Custom type tRingStatsStnAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingStatsStnAddress_Type.__name__ = "OctetString"
_TRingStatsStnAddress_Object = MibTableColumn
tRingStatsStnAddress = _TRingStatsStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1),
    _TRingStatsStnAddress_Type()
)
tRingStatsStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnAddress.setStatus("mandatory")
_TRingStatsStnFrames_Type = Counter32
_TRingStatsStnFrames_Object = MibTableColumn
tRingStatsStnFrames = _TRingStatsStnFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2),
    _TRingStatsStnFrames_Type()
)
tRingStatsStnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnFrames.setStatus("mandatory")
_TRingStatsStnBytes_Type = Counter32
_TRingStatsStnBytes_Object = MibTableColumn
tRingStatsStnBytes = _TRingStatsStnBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 3),
    _TRingStatsStnBytes_Type()
)
tRingStatsStnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnBytes.setStatus("mandatory")
_TRingStatsStnLineErrors_Type = Counter32
_TRingStatsStnLineErrors_Object = MibTableColumn
tRingStatsStnLineErrors = _TRingStatsStnLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 4),
    _TRingStatsStnLineErrors_Type()
)
tRingStatsStnLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnLineErrors.setStatus("mandatory")
_TRingStatsStnBurstErrors_Type = Counter32
_TRingStatsStnBurstErrors_Object = MibTableColumn
tRingStatsStnBurstErrors = _TRingStatsStnBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 5),
    _TRingStatsStnBurstErrors_Type()
)
tRingStatsStnBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnBurstErrors.setStatus("mandatory")
_TRingStatsStnACErrors_Type = Counter32
_TRingStatsStnACErrors_Object = MibTableColumn
tRingStatsStnACErrors = _TRingStatsStnACErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 6),
    _TRingStatsStnACErrors_Type()
)
tRingStatsStnACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnACErrors.setStatus("mandatory")
_TRingStatsStnAbortSequences_Type = Counter32
_TRingStatsStnAbortSequences_Object = MibTableColumn
tRingStatsStnAbortSequences = _TRingStatsStnAbortSequences_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 7),
    _TRingStatsStnAbortSequences_Type()
)
tRingStatsStnAbortSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnAbortSequences.setStatus("mandatory")
_TRingStatsStnInternalErrors_Type = Counter32
_TRingStatsStnInternalErrors_Object = MibTableColumn
tRingStatsStnInternalErrors = _TRingStatsStnInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 8),
    _TRingStatsStnInternalErrors_Type()
)
tRingStatsStnInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnInternalErrors.setStatus("mandatory")
_TRingStatsStnLostFrames_Type = Counter32
_TRingStatsStnLostFrames_Object = MibTableColumn
tRingStatsStnLostFrames = _TRingStatsStnLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 9),
    _TRingStatsStnLostFrames_Type()
)
tRingStatsStnLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnLostFrames.setStatus("mandatory")
_TRingStatsStnCongestErrors_Type = Counter32
_TRingStatsStnCongestErrors_Object = MibTableColumn
tRingStatsStnCongestErrors = _TRingStatsStnCongestErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 10),
    _TRingStatsStnCongestErrors_Type()
)
tRingStatsStnCongestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnCongestErrors.setStatus("mandatory")
_TRingStatsStnFCErrors_Type = Counter32
_TRingStatsStnFCErrors_Object = MibTableColumn
tRingStatsStnFCErrors = _TRingStatsStnFCErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 11),
    _TRingStatsStnFCErrors_Type()
)
tRingStatsStnFCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnFCErrors.setStatus("mandatory")
_TRingStatsStnTokenErrors_Type = Counter32
_TRingStatsStnTokenErrors_Object = MibTableColumn
tRingStatsStnTokenErrors = _TRingStatsStnTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 12),
    _TRingStatsStnTokenErrors_Type()
)
tRingStatsStnTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnTokenErrors.setStatus("mandatory")
_TRingStatsStnFreqErrors_Type = Counter32
_TRingStatsStnFreqErrors_Object = MibTableColumn
tRingStatsStnFreqErrors = _TRingStatsStnFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 13),
    _TRingStatsStnFreqErrors_Type()
)
tRingStatsStnFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnFreqErrors.setStatus("mandatory")
_TRingStatsStnErrors_Type = Counter32
_TRingStatsStnErrors_Object = MibTableColumn
tRingStatsStnErrors = _TRingStatsStnErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 2, 1, 1, 14),
    _TRingStatsStnErrors_Type()
)
tRingStatsStnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsStnErrors.setStatus("mandatory")
_TRingStatsReset_ObjectIdentity = ObjectIdentity
tRingStatsReset = _TRingStatsReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 3)
)


class _TRingStatsResetCounters_Type(Integer32):
    """Custom type tRingStatsResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResetCounters", 1),
          ("resetCounters", 2))
    )


_TRingStatsResetCounters_Type.__name__ = "Integer32"
_TRingStatsResetCounters_Object = MibScalar
tRingStatsResetCounters = _TRingStatsResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 3, 1),
    _TRingStatsResetCounters_Type()
)
tRingStatsResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingStatsResetCounters.setStatus("mandatory")
_TRingStatsResetTime_Type = TimeTicks
_TRingStatsResetTime_Object = MibScalar
tRingStatsResetTime = _TRingStatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 2, 3, 2),
    _TRingStatsResetTime_Type()
)
tRingStatsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingStatsResetTime.setStatus("mandatory")
_TRingAlarms_ObjectIdentity = ObjectIdentity
tRingAlarms = _TRingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3)
)
_TRingAlarmsRing_ObjectIdentity = ObjectIdentity
tRingAlarmsRing = _TRingAlarmsRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1)
)
_TRingAlarmsRingEnbl_ObjectIdentity = ObjectIdentity
tRingAlarmsRingEnbl = _TRingAlarmsRingEnbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1)
)
_TRingAlarmsRingTimebase_Type = Integer32
_TRingAlarmsRingTimebase_Object = MibScalar
tRingAlarmsRingTimebase = _TRingAlarmsRingTimebase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 1),
    _TRingAlarmsRingTimebase_Type()
)
tRingAlarmsRingTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingTimebase.setStatus("mandatory")


class _TRingAlarmsRingRingPurgesEnable_Type(Integer32):
    """Custom type tRingAlarmsRingRingPurgesEnable based on Integer32"""
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


_TRingAlarmsRingRingPurgesEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingRingPurgesEnable_Object = MibScalar
tRingAlarmsRingRingPurgesEnable = _TRingAlarmsRingRingPurgesEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 2),
    _TRingAlarmsRingRingPurgesEnable_Type()
)
tRingAlarmsRingRingPurgesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingRingPurgesEnable.setStatus("mandatory")


class _TRingAlarmsRingAMPErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsRingAMPErrsEnable based on Integer32"""
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


_TRingAlarmsRingAMPErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingAMPErrsEnable_Object = MibScalar
tRingAlarmsRingAMPErrsEnable = _TRingAlarmsRingAMPErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 3),
    _TRingAlarmsRingAMPErrsEnable_Type()
)
tRingAlarmsRingAMPErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingAMPErrsEnable.setStatus("mandatory")


class _TRingAlarmsRingTokenErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsRingTokenErrsEnable based on Integer32"""
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


_TRingAlarmsRingTokenErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingTokenErrsEnable_Object = MibScalar
tRingAlarmsRingTokenErrsEnable = _TRingAlarmsRingTokenErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 4),
    _TRingAlarmsRingTokenErrsEnable_Type()
)
tRingAlarmsRingTokenErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingTokenErrsEnable.setStatus("mandatory")


class _TRingAlarmsRingClaimTknErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsRingClaimTknErrsEnable based on Integer32"""
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


_TRingAlarmsRingClaimTknErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingClaimTknErrsEnable_Object = MibScalar
tRingAlarmsRingClaimTknErrsEnable = _TRingAlarmsRingClaimTknErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 5),
    _TRingAlarmsRingClaimTknErrsEnable_Type()
)
tRingAlarmsRingClaimTknErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingClaimTknErrsEnable.setStatus("mandatory")


class _TRingAlarmsRingLostFramesEnable_Type(Integer32):
    """Custom type tRingAlarmsRingLostFramesEnable based on Integer32"""
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


_TRingAlarmsRingLostFramesEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingLostFramesEnable_Object = MibScalar
tRingAlarmsRingLostFramesEnable = _TRingAlarmsRingLostFramesEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 6),
    _TRingAlarmsRingLostFramesEnable_Type()
)
tRingAlarmsRingLostFramesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingLostFramesEnable.setStatus("mandatory")


class _TRingAlarmsRingBeaconStateEnable_Type(Integer32):
    """Custom type tRingAlarmsRingBeaconStateEnable based on Integer32"""
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


_TRingAlarmsRingBeaconStateEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingBeaconStateEnable_Object = MibScalar
tRingAlarmsRingBeaconStateEnable = _TRingAlarmsRingBeaconStateEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 7),
    _TRingAlarmsRingBeaconStateEnable_Type()
)
tRingAlarmsRingBeaconStateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingBeaconStateEnable.setStatus("mandatory")


class _TRingAlarmsRingFrameCountEnable_Type(Integer32):
    """Custom type tRingAlarmsRingFrameCountEnable based on Integer32"""
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


_TRingAlarmsRingFrameCountEnable_Type.__name__ = "Integer32"
_TRingAlarmsRingFrameCountEnable_Object = MibScalar
tRingAlarmsRingFrameCountEnable = _TRingAlarmsRingFrameCountEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 1, 8),
    _TRingAlarmsRingFrameCountEnable_Type()
)
tRingAlarmsRingFrameCountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingFrameCountEnable.setStatus("mandatory")
_TRingAlarmsRingThrsh_ObjectIdentity = ObjectIdentity
tRingAlarmsRingThrsh = _TRingAlarmsRingThrsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2)
)
_TRingAlarmsRingRingPurgesThreshold_Type = Integer32
_TRingAlarmsRingRingPurgesThreshold_Object = MibScalar
tRingAlarmsRingRingPurgesThreshold = _TRingAlarmsRingRingPurgesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 1),
    _TRingAlarmsRingRingPurgesThreshold_Type()
)
tRingAlarmsRingRingPurgesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingRingPurgesThreshold.setStatus("mandatory")
_TRingAlarmsRingAMPErrsThreshold_Type = Integer32
_TRingAlarmsRingAMPErrsThreshold_Object = MibScalar
tRingAlarmsRingAMPErrsThreshold = _TRingAlarmsRingAMPErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 2),
    _TRingAlarmsRingAMPErrsThreshold_Type()
)
tRingAlarmsRingAMPErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingAMPErrsThreshold.setStatus("mandatory")
_TRingAlarmsRingTokenErrsThreshold_Type = Integer32
_TRingAlarmsRingTokenErrsThreshold_Object = MibScalar
tRingAlarmsRingTokenErrsThreshold = _TRingAlarmsRingTokenErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 3),
    _TRingAlarmsRingTokenErrsThreshold_Type()
)
tRingAlarmsRingTokenErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingTokenErrsThreshold.setStatus("mandatory")
_TRingAlarmsRingClaimTknThreshold_Type = Integer32
_TRingAlarmsRingClaimTknThreshold_Object = MibScalar
tRingAlarmsRingClaimTknThreshold = _TRingAlarmsRingClaimTknThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 4),
    _TRingAlarmsRingClaimTknThreshold_Type()
)
tRingAlarmsRingClaimTknThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingClaimTknThreshold.setStatus("mandatory")
_TRingAlarmsRingLostFramesThreshold_Type = Integer32
_TRingAlarmsRingLostFramesThreshold_Object = MibScalar
tRingAlarmsRingLostFramesThreshold = _TRingAlarmsRingLostFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 5),
    _TRingAlarmsRingLostFramesThreshold_Type()
)
tRingAlarmsRingLostFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingLostFramesThreshold.setStatus("mandatory")
_TRingAlarmsRingBeaconStateThreshold_Type = Integer32
_TRingAlarmsRingBeaconStateThreshold_Object = MibScalar
tRingAlarmsRingBeaconStateThreshold = _TRingAlarmsRingBeaconStateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 6),
    _TRingAlarmsRingBeaconStateThreshold_Type()
)
tRingAlarmsRingBeaconStateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingBeaconStateThreshold.setStatus("mandatory")
_TRingAlarmsRingFrameCountThreshold_Type = Integer32
_TRingAlarmsRingFrameCountThreshold_Object = MibScalar
tRingAlarmsRingFrameCountThreshold = _TRingAlarmsRingFrameCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 1, 2, 7),
    _TRingAlarmsRingFrameCountThreshold_Type()
)
tRingAlarmsRingFrameCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsRingFrameCountThreshold.setStatus("mandatory")
_TRingAlarmsStn_ObjectIdentity = ObjectIdentity
tRingAlarmsStn = _TRingAlarmsStn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2)
)
_TRingAlarmsStnEnbl_ObjectIdentity = ObjectIdentity
tRingAlarmsStnEnbl = _TRingAlarmsStnEnbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1)
)
_TRingAlarmsStnEnblTable_Object = MibTable
tRingAlarmsStnEnblTable = _TRingAlarmsStnEnblTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblTable.setStatus("mandatory")
_TRingAlarmsStnEnblEntry_Object = MibTableRow
tRingAlarmsStnEnblEntry = _TRingAlarmsStnEnblEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1)
)
tRingAlarmsStnEnblEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingAlarmsStnEnblAddress"),
)
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblEntry.setStatus("mandatory")
_TRingAlarmsStnEnblAddress_Type = OctetString
_TRingAlarmsStnEnblAddress_Object = MibTableColumn
tRingAlarmsStnEnblAddress = _TRingAlarmsStnEnblAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1),
    _TRingAlarmsStnEnblAddress_Type()
)
tRingAlarmsStnEnblAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblAddress.setStatus("mandatory")


class _TRingAlarmsStnEnblLineErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsStnEnblLineErrsEnable based on Integer32"""
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


_TRingAlarmsStnEnblLineErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsStnEnblLineErrsEnable_Object = MibTableColumn
tRingAlarmsStnEnblLineErrsEnable = _TRingAlarmsStnEnblLineErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 2),
    _TRingAlarmsStnEnblLineErrsEnable_Type()
)
tRingAlarmsStnEnblLineErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblLineErrsEnable.setStatus("mandatory")


class _TRingAlarmsStnEnblInternalErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsStnEnblInternalErrsEnable based on Integer32"""
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


_TRingAlarmsStnEnblInternalErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsStnEnblInternalErrsEnable_Object = MibTableColumn
tRingAlarmsStnEnblInternalErrsEnable = _TRingAlarmsStnEnblInternalErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 3),
    _TRingAlarmsStnEnblInternalErrsEnable_Type()
)
tRingAlarmsStnEnblInternalErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblInternalErrsEnable.setStatus("mandatory")


class _TRingAlarmsStnEnblBurstErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsStnEnblBurstErrsEnable based on Integer32"""
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


_TRingAlarmsStnEnblBurstErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsStnEnblBurstErrsEnable_Object = MibTableColumn
tRingAlarmsStnEnblBurstErrsEnable = _TRingAlarmsStnEnblBurstErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 4),
    _TRingAlarmsStnEnblBurstErrsEnable_Type()
)
tRingAlarmsStnEnblBurstErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblBurstErrsEnable.setStatus("mandatory")


class _TRingAlarmsStnEnblACErrsEnable_Type(Integer32):
    """Custom type tRingAlarmsStnEnblACErrsEnable based on Integer32"""
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


_TRingAlarmsStnEnblACErrsEnable_Type.__name__ = "Integer32"
_TRingAlarmsStnEnblACErrsEnable_Object = MibTableColumn
tRingAlarmsStnEnblACErrsEnable = _TRingAlarmsStnEnblACErrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 5),
    _TRingAlarmsStnEnblACErrsEnable_Type()
)
tRingAlarmsStnEnblACErrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblACErrsEnable.setStatus("mandatory")


class _TRingAlarmsStnEnblRcvrCongestEnable_Type(Integer32):
    """Custom type tRingAlarmsStnEnblRcvrCongestEnable based on Integer32"""
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


_TRingAlarmsStnEnblRcvrCongestEnable_Type.__name__ = "Integer32"
_TRingAlarmsStnEnblRcvrCongestEnable_Object = MibTableColumn
tRingAlarmsStnEnblRcvrCongestEnable = _TRingAlarmsStnEnblRcvrCongestEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 1, 1, 1, 6),
    _TRingAlarmsStnEnblRcvrCongestEnable_Type()
)
tRingAlarmsStnEnblRcvrCongestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnEnblRcvrCongestEnable.setStatus("mandatory")
_TRingAlarmsStnThrsh_ObjectIdentity = ObjectIdentity
tRingAlarmsStnThrsh = _TRingAlarmsStnThrsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2)
)
_TRingAlarmsStnThrshTable_Object = MibTable
tRingAlarmsStnThrshTable = _TRingAlarmsStnThrshTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshTable.setStatus("mandatory")
_TRingAlarmsStnThrshEntry_Object = MibTableRow
tRingAlarmsStnThrshEntry = _TRingAlarmsStnThrshEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1)
)
tRingAlarmsStnThrshEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingAlarmsStnThrshAddress"),
)
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshEntry.setStatus("mandatory")
_TRingAlarmsStnThrshAddress_Type = OctetString
_TRingAlarmsStnThrshAddress_Object = MibTableColumn
tRingAlarmsStnThrshAddress = _TRingAlarmsStnThrshAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 1),
    _TRingAlarmsStnThrshAddress_Type()
)
tRingAlarmsStnThrshAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshAddress.setStatus("mandatory")
_TRingAlarmsStnThrshLineErrsThreshold_Type = Integer32
_TRingAlarmsStnThrshLineErrsThreshold_Object = MibTableColumn
tRingAlarmsStnThrshLineErrsThreshold = _TRingAlarmsStnThrshLineErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 2),
    _TRingAlarmsStnThrshLineErrsThreshold_Type()
)
tRingAlarmsStnThrshLineErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshLineErrsThreshold.setStatus("mandatory")
_TRingAlarmsStnThrshInternalErrsThreshold_Type = Integer32
_TRingAlarmsStnThrshInternalErrsThreshold_Object = MibTableColumn
tRingAlarmsStnThrshInternalErrsThreshold = _TRingAlarmsStnThrshInternalErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 3),
    _TRingAlarmsStnThrshInternalErrsThreshold_Type()
)
tRingAlarmsStnThrshInternalErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshInternalErrsThreshold.setStatus("mandatory")
_TRingAlarmsStnThrshBurstErrsThreshold_Type = Integer32
_TRingAlarmsStnThrshBurstErrsThreshold_Object = MibTableColumn
tRingAlarmsStnThrshBurstErrsThreshold = _TRingAlarmsStnThrshBurstErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 4),
    _TRingAlarmsStnThrshBurstErrsThreshold_Type()
)
tRingAlarmsStnThrshBurstErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshBurstErrsThreshold.setStatus("mandatory")
_TRingAlarmsStnThrshACErrsThreshold_Type = Integer32
_TRingAlarmsStnThrshACErrsThreshold_Object = MibTableColumn
tRingAlarmsStnThrshACErrsThreshold = _TRingAlarmsStnThrshACErrsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 5),
    _TRingAlarmsStnThrshACErrsThreshold_Type()
)
tRingAlarmsStnThrshACErrsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshACErrsThreshold.setStatus("mandatory")
_TRingAlarmsStnThrshRcvrCongestThreshold_Type = Integer32
_TRingAlarmsStnThrshRcvrCongestThreshold_Object = MibTableColumn
tRingAlarmsStnThrshRcvrCongestThreshold = _TRingAlarmsStnThrshRcvrCongestThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 6),
    _TRingAlarmsStnThrshRcvrCongestThreshold_Type()
)
tRingAlarmsStnThrshRcvrCongestThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingAlarmsStnThrshRcvrCongestThreshold.setStatus("mandatory")
_TRingPortGrp_ObjectIdentity = ObjectIdentity
tRingPortGrp = _TRingPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2)
)
_TRingPortGrpTable_Object = MibTable
tRingPortGrpTable = _TRingPortGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tRingPortGrpTable.setStatus("mandatory")
_TRingPortGrpEntry_Object = MibTableRow
tRingPortGrpEntry = _TRingPortGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1)
)
tRingPortGrpEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingPortGrpId"),
)
if mibBuilder.loadTexts:
    tRingPortGrpEntry.setStatus("mandatory")
_TRingPortGrpId_Type = Integer32
_TRingPortGrpId_Object = MibTableColumn
tRingPortGrpId = _TRingPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 1),
    _TRingPortGrpId_Type()
)
tRingPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpId.setStatus("mandatory")


class _TRingPortGrpName_Type(DisplayString):
    """Custom type tRingPortGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TRingPortGrpName_Type.__name__ = "DisplayString"
_TRingPortGrpName_Object = MibTableColumn
tRingPortGrpName = _TRingPortGrpName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 2),
    _TRingPortGrpName_Type()
)
tRingPortGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpName.setStatus("mandatory")
_TRingPortGrpStnPortCount_Type = Integer32
_TRingPortGrpStnPortCount_Object = MibTableColumn
tRingPortGrpStnPortCount = _TRingPortGrpStnPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 3),
    _TRingPortGrpStnPortCount_Type()
)
tRingPortGrpStnPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpStnPortCount.setStatus("mandatory")
_TRingPortGrpRingPortCount_Type = Integer32
_TRingPortGrpRingPortCount_Object = MibTableColumn
tRingPortGrpRingPortCount = _TRingPortGrpRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 4),
    _TRingPortGrpRingPortCount_Type()
)
tRingPortGrpRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpRingPortCount.setStatus("mandatory")


class _TRingPortGrpStnPortsEnable_Type(Integer32):
    """Custom type tRingPortGrpStnPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_TRingPortGrpStnPortsEnable_Type.__name__ = "Integer32"
_TRingPortGrpStnPortsEnable_Object = MibTableColumn
tRingPortGrpStnPortsEnable = _TRingPortGrpStnPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 5),
    _TRingPortGrpStnPortsEnable_Type()
)
tRingPortGrpStnPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpStnPortsEnable.setStatus("mandatory")


class _TRingPortGrpRingPortsEnable_Type(Integer32):
    """Custom type tRingPortGrpRingPortsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("noEnable", 1))
    )


_TRingPortGrpRingPortsEnable_Type.__name__ = "Integer32"
_TRingPortGrpRingPortsEnable_Object = MibTableColumn
tRingPortGrpRingPortsEnable = _TRingPortGrpRingPortsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 6),
    _TRingPortGrpRingPortsEnable_Type()
)
tRingPortGrpRingPortsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpRingPortsEnable.setStatus("mandatory")
_TRingPortGrpStnPortsOn_Type = Integer32
_TRingPortGrpStnPortsOn_Object = MibTableColumn
tRingPortGrpStnPortsOn = _TRingPortGrpStnPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 7),
    _TRingPortGrpStnPortsOn_Type()
)
tRingPortGrpStnPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpStnPortsOn.setStatus("mandatory")
_TRingPortGrpRingPortsOn_Type = Integer32
_TRingPortGrpRingPortsOn_Object = MibTableColumn
tRingPortGrpRingPortsOn = _TRingPortGrpRingPortsOn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 8),
    _TRingPortGrpRingPortsOn_Type()
)
tRingPortGrpRingPortsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpRingPortsOn.setStatus("mandatory")


class _TRingPortGrpMode_Type(Integer32):
    """Custom type tRingPortGrpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoMode", 2),
          ("managementMode", 1))
    )


_TRingPortGrpMode_Type.__name__ = "Integer32"
_TRingPortGrpMode_Object = MibTableColumn
tRingPortGrpMode = _TRingPortGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 9),
    _TRingPortGrpMode_Type()
)
tRingPortGrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpMode.setStatus("mandatory")


class _TRingPortGrpSpeed_Type(Integer32):
    """Custom type tRingPortGrpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("fourMegaBits", 4),
          ("sixteenMegaBits", 16))
    )


_TRingPortGrpSpeed_Type.__name__ = "Integer32"
_TRingPortGrpSpeed_Object = MibTableColumn
tRingPortGrpSpeed = _TRingPortGrpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 10),
    _TRingPortGrpSpeed_Type()
)
tRingPortGrpSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpSpeed.setStatus("mandatory")


class _TRingPortGrpSpeedFault_Type(Integer32):
    """Custom type tRingPortGrpSpeedFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 2),
          ("noFaultDetected", 1))
    )


_TRingPortGrpSpeedFault_Type.__name__ = "Integer32"
_TRingPortGrpSpeedFault_Object = MibTableColumn
tRingPortGrpSpeedFault = _TRingPortGrpSpeedFault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 11),
    _TRingPortGrpSpeedFault_Type()
)
tRingPortGrpSpeedFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpSpeedFault.setStatus("mandatory")


class _TRingPortGrpSpeedFaultLocation_Type(Integer32):
    """Custom type tRingPortGrpSpeedFaultLocation based on Integer32"""
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
        *(("fnb", 2),
          ("notApplicable", 1),
          ("ringIn", 3),
          ("ringOut", 4))
    )


_TRingPortGrpSpeedFaultLocation_Type.__name__ = "Integer32"
_TRingPortGrpSpeedFaultLocation_Object = MibTableColumn
tRingPortGrpSpeedFaultLocation = _TRingPortGrpSpeedFaultLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 12),
    _TRingPortGrpSpeedFaultLocation_Type()
)
tRingPortGrpSpeedFaultLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortGrpSpeedFaultLocation.setStatus("mandatory")


class _TRingPortGrpBypassRingPortState_Type(Integer32):
    """Custom type tRingPortGrpBypassRingPortState based on Integer32"""
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
        *(("illegal", 4),
          ("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_TRingPortGrpBypassRingPortState_Type.__name__ = "Integer32"
_TRingPortGrpBypassRingPortState_Object = MibTableColumn
tRingPortGrpBypassRingPortState = _TRingPortGrpBypassRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 2, 1, 1, 13),
    _TRingPortGrpBypassRingPortState_Type()
)
tRingPortGrpBypassRingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortGrpBypassRingPortState.setStatus("mandatory")
_TRingPort_ObjectIdentity = ObjectIdentity
tRingPort = _TRingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3)
)
_TRingPortMgmt_ObjectIdentity = ObjectIdentity
tRingPortMgmt = _TRingPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1)
)
_TRingPortMgmtTable_Object = MibTable
tRingPortMgmtTable = _TRingPortMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tRingPortMgmtTable.setStatus("mandatory")
_TRingPortMgmtEntry_Object = MibTableRow
tRingPortMgmtEntry = _TRingPortMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1)
)
tRingPortMgmtEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingPortMgmtPortId"),
    (0, "DOT5-LOG-MIB", "tRingPortMgmtPortGrpId"),
)
if mibBuilder.loadTexts:
    tRingPortMgmtEntry.setStatus("mandatory")
_TRingPortMgmtPortId_Type = Integer32
_TRingPortMgmtPortId_Object = MibTableColumn
tRingPortMgmtPortId = _TRingPortMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 1),
    _TRingPortMgmtPortId_Type()
)
tRingPortMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortMgmtPortId.setStatus("mandatory")
_TRingPortMgmtPortGrpId_Type = Integer32
_TRingPortMgmtPortGrpId_Object = MibTableColumn
tRingPortMgmtPortGrpId = _TRingPortMgmtPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 2),
    _TRingPortMgmtPortGrpId_Type()
)
tRingPortMgmtPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortMgmtPortGrpId.setStatus("mandatory")


class _TRingPortMgmtPortName_Type(DisplayString):
    """Custom type tRingPortMgmtPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TRingPortMgmtPortName_Type.__name__ = "DisplayString"
_TRingPortMgmtPortName_Object = MibTableColumn
tRingPortMgmtPortName = _TRingPortMgmtPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 3),
    _TRingPortMgmtPortName_Type()
)
tRingPortMgmtPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortMgmtPortName.setStatus("mandatory")


class _TRingPortMgmtPortAdminState_Type(Integer32):
    """Custom type tRingPortMgmtPortAdminState based on Integer32"""
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


_TRingPortMgmtPortAdminState_Type.__name__ = "Integer32"
_TRingPortMgmtPortAdminState_Object = MibTableColumn
tRingPortMgmtPortAdminState = _TRingPortMgmtPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 4),
    _TRingPortMgmtPortAdminState_Type()
)
tRingPortMgmtPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortMgmtPortAdminState.setStatus("mandatory")


class _TRingPortMgmtPortOperState_Type(Integer32):
    """Custom type tRingPortMgmtPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 1),
          ("operational", 2))
    )


_TRingPortMgmtPortOperState_Type.__name__ = "Integer32"
_TRingPortMgmtPortOperState_Object = MibTableColumn
tRingPortMgmtPortOperState = _TRingPortMgmtPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 5),
    _TRingPortMgmtPortOperState_Type()
)
tRingPortMgmtPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortMgmtPortOperState.setStatus("mandatory")
_TRingPortMgmtPortType_Type = ObjectIdentifier
_TRingPortMgmtPortType_Object = MibTableColumn
tRingPortMgmtPortType = _TRingPortMgmtPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 6),
    _TRingPortMgmtPortType_Type()
)
tRingPortMgmtPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortMgmtPortType.setStatus("mandatory")


class _TRingPortMgmtSpeedFaultDetect_Type(Integer32):
    """Custom type tRingPortMgmtSpeedFaultDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 3),
          ("noFaultDetected", 2),
          ("notDetectable", 1))
    )


_TRingPortMgmtSpeedFaultDetect_Type.__name__ = "Integer32"
_TRingPortMgmtSpeedFaultDetect_Object = MibTableColumn
tRingPortMgmtSpeedFaultDetect = _TRingPortMgmtSpeedFaultDetect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 7),
    _TRingPortMgmtSpeedFaultDetect_Type()
)
tRingPortMgmtSpeedFaultDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortMgmtSpeedFaultDetect.setStatus("mandatory")


class _TRingPortMgmtRingOutEnable_Type(Integer32):
    """Custom type tRingPortMgmtRingOutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notAvailable", 1))
    )


_TRingPortMgmtRingOutEnable_Type.__name__ = "Integer32"
_TRingPortMgmtRingOutEnable_Object = MibTableColumn
tRingPortMgmtRingOutEnable = _TRingPortMgmtRingOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 1, 1, 1, 8),
    _TRingPortMgmtRingOutEnable_Type()
)
tRingPortMgmtRingOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortMgmtRingOutEnable.setStatus("mandatory")
_TRingPortStn_ObjectIdentity = ObjectIdentity
tRingPortStn = _TRingPortStn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2)
)
_TRingPortStnTable_Object = MibTable
tRingPortStnTable = _TRingPortStnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tRingPortStnTable.setStatus("mandatory")
_TRingPortStnEntry_Object = MibTableRow
tRingPortStnEntry = _TRingPortStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1)
)
tRingPortStnEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingPortStnPortId"),
    (0, "DOT5-LOG-MIB", "tRingPortStnPortGrpId"),
)
if mibBuilder.loadTexts:
    tRingPortStnEntry.setStatus("mandatory")
_TRingPortStnPortId_Type = Integer32
_TRingPortStnPortId_Object = MibTableColumn
tRingPortStnPortId = _TRingPortStnPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 1),
    _TRingPortStnPortId_Type()
)
tRingPortStnPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortStnPortId.setStatus("mandatory")
_TRingPortStnPortGrpId_Type = Integer32
_TRingPortStnPortGrpId_Object = MibTableColumn
tRingPortStnPortGrpId = _TRingPortStnPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 2),
    _TRingPortStnPortGrpId_Type()
)
tRingPortStnPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortStnPortGrpId.setStatus("mandatory")


class _TRingPortStnPortLinkState_Type(Integer32):
    """Custom type tRingPortStnPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 2),
          ("noLink", 1))
    )


_TRingPortStnPortLinkState_Type.__name__ = "Integer32"
_TRingPortStnPortLinkState_Object = MibTableColumn
tRingPortStnPortLinkState = _TRingPortStnPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 3),
    _TRingPortStnPortLinkState_Type()
)
tRingPortStnPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortStnPortLinkState.setStatus("mandatory")
_TRingPortStnPortLinkStateTime_Type = TimeTicks
_TRingPortStnPortLinkStateTime_Object = MibTableColumn
tRingPortStnPortLinkStateTime = _TRingPortStnPortLinkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 4),
    _TRingPortStnPortLinkStateTime_Type()
)
tRingPortStnPortLinkStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortStnPortLinkStateTime.setStatus("mandatory")


class _TRingPortStnPortMapEnable_Type(Integer32):
    """Custom type tRingPortStnPortMapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mappingDisabled", 2),
          ("mappingEnabled", 1))
    )


_TRingPortStnPortMapEnable_Type.__name__ = "Integer32"
_TRingPortStnPortMapEnable_Object = MibTableColumn
tRingPortStnPortMapEnable = _TRingPortStnPortMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 5),
    _TRingPortStnPortMapEnable_Type()
)
tRingPortStnPortMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortStnPortMapEnable.setStatus("mandatory")


class _TRingPortStnPortMappedMacAddr_Type(OctetString):
    """Custom type tRingPortStnPortMappedMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TRingPortStnPortMappedMacAddr_Type.__name__ = "OctetString"
_TRingPortStnPortMappedMacAddr_Object = MibTableColumn
tRingPortStnPortMappedMacAddr = _TRingPortStnPortMappedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 6),
    _TRingPortStnPortMappedMacAddr_Type()
)
tRingPortStnPortMappedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortStnPortMappedMacAddr.setStatus("mandatory")


class _TRingPortStnInsertionTrapEnable_Type(Integer32):
    """Custom type tRingPortStnInsertionTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TRingPortStnInsertionTrapEnable_Type.__name__ = "Integer32"
_TRingPortStnInsertionTrapEnable_Object = MibTableColumn
tRingPortStnInsertionTrapEnable = _TRingPortStnInsertionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 2, 1, 1, 7),
    _TRingPortStnInsertionTrapEnable_Type()
)
tRingPortStnInsertionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortStnInsertionTrapEnable.setStatus("mandatory")
_TRingPortRing_ObjectIdentity = ObjectIdentity
tRingPortRing = _TRingPortRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3)
)
_TRingPortRingTable_Object = MibTable
tRingPortRingTable = _TRingPortRingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tRingPortRingTable.setStatus("mandatory")
_TRingPortRingEntry_Object = MibTableRow
tRingPortRingEntry = _TRingPortRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1)
)
tRingPortRingEntry.setIndexNames(
    (0, "DOT5-LOG-MIB", "tRingPortRingPortId"),
    (0, "DOT5-LOG-MIB", "tRingPortRingPortGrpId"),
)
if mibBuilder.loadTexts:
    tRingPortRingEntry.setStatus("mandatory")
_TRingPortRingPortId_Type = Integer32
_TRingPortRingPortId_Object = MibTableColumn
tRingPortRingPortId = _TRingPortRingPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 1),
    _TRingPortRingPortId_Type()
)
tRingPortRingPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingPortId.setStatus("mandatory")
_TRingPortRingPortGrpId_Type = Integer32
_TRingPortRingPortGrpId_Object = MibTableColumn
tRingPortRingPortGrpId = _TRingPortRingPortGrpId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 2),
    _TRingPortRingPortGrpId_Type()
)
tRingPortRingPortGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingPortGrpId.setStatus("mandatory")


class _TRingPortRingPortClass_Type(Integer32):
    """Custom type tRingPortRingPortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autowrap", 2),
          ("noAutowrap", 1),
          ("selectable", 3))
    )


_TRingPortRingPortClass_Type.__name__ = "Integer32"
_TRingPortRingPortClass_Object = MibTableColumn
tRingPortRingPortClass = _TRingPortRingPortClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 3),
    _TRingPortRingPortClass_Type()
)
tRingPortRingPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingPortClass.setStatus("mandatory")


class _TRingPortRingPortMediaSelect_Type(Integer32):
    """Custom type tRingPortRingPortMediaSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 3),
          ("noSelection", 1),
          ("stp", 2))
    )


_TRingPortRingPortMediaSelect_Type.__name__ = "Integer32"
_TRingPortRingPortMediaSelect_Object = MibTableColumn
tRingPortRingPortMediaSelect = _TRingPortRingPortMediaSelect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 4),
    _TRingPortRingPortMediaSelect_Type()
)
tRingPortRingPortMediaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortRingPortMediaSelect.setStatus("mandatory")


class _TRingPortRingFaultStatus_Type(Integer32):
    """Custom type tRingPortRingFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultDetected", 3),
          ("noFaultDetected", 2),
          ("notSupported", 1))
    )


_TRingPortRingFaultStatus_Type.__name__ = "Integer32"
_TRingPortRingFaultStatus_Object = MibTableColumn
tRingPortRingFaultStatus = _TRingPortRingFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 5),
    _TRingPortRingFaultStatus_Type()
)
tRingPortRingFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingFaultStatus.setStatus("mandatory")
_TRingPortRingFaultStateTime_Type = TimeTicks
_TRingPortRingFaultStateTime_Object = MibTableColumn
tRingPortRingFaultStateTime = _TRingPortRingFaultStateTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 6),
    _TRingPortRingFaultStateTime_Type()
)
tRingPortRingFaultStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingFaultStateTime.setStatus("mandatory")


class _TRingPortRingPhantomCurrent_Type(Integer32):
    """Custom type tRingPortRingPhantomCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activatePhantom", 2),
          ("deactivatePhantom", 3),
          ("noPhantomAvailable", 1))
    )


_TRingPortRingPhantomCurrent_Type.__name__ = "Integer32"
_TRingPortRingPhantomCurrent_Object = MibTableColumn
tRingPortRingPhantomCurrent = _TRingPortRingPhantomCurrent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 7),
    _TRingPortRingPhantomCurrent_Type()
)
tRingPortRingPhantomCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tRingPortRingPhantomCurrent.setStatus("mandatory")


class _TRingPortRingPortType_Type(Integer32):
    """Custom type tRingPortRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringIn", 1),
          ("ringOut", 2))
    )


_TRingPortRingPortType_Type.__name__ = "Integer32"
_TRingPortRingPortType_Object = MibTableColumn
tRingPortRingPortType = _TRingPortRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 3, 3, 1, 1, 8),
    _TRingPortRingPortType_Type()
)
tRingPortRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingPortRingPortType.setStatus("mandatory")
_TRingIf_ObjectIdentity = ObjectIdentity
tRingIf = _TRingIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 4)
)
_TRingIfIndex_Type = Integer32
_TRingIfIndex_Object = MibScalar
tRingIfIndex = _TRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1, 1, 4, 1),
    _TRingIfIndex_Type()
)
tRingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRingIfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOT5-LOG-MIB",
    **{"dot5Rev1": dot5Rev1,
       "tRing": tRing,
       "tRingMgmt": tRingMgmt,
       "tRingMgmtRing": tRingMgmtRing,
       "tRingMgmtRingName": tRingMgmtRingName,
       "tRingMgmtStnPortCount": tRingMgmtStnPortCount,
       "tRingMgmtRingPortCount": tRingMgmtRingPortCount,
       "tRingMgmtStnPortsEnable": tRingMgmtStnPortsEnable,
       "tRingMgmtRingPortsEnable": tRingMgmtRingPortsEnable,
       "tRingMgmtStnPortsOn": tRingMgmtStnPortsOn,
       "tRingMgmtRingPortsOn": tRingMgmtRingPortsOn,
       "tRingMgmtStations": tRingMgmtStations,
       "tRingMgmtRingState": tRingMgmtRingState,
       "tRingMgmtRingSpeed": tRingMgmtRingSpeed,
       "tRingMgmtActiveMonitor": tRingMgmtActiveMonitor,
       "tRingMgmtRingNumber": tRingMgmtRingNumber,
       "tRingMgmtBeaconRecovery": tRingMgmtBeaconRecovery,
       "tRingMgmtBcnRecRingPortRetryCount": tRingMgmtBcnRecRingPortRetryCount,
       "tRingMgmtBcnRecRingPortRetryDelay": tRingMgmtBcnRecRingPortRetryDelay,
       "tRingMgmtBcnRecStnPortRetryCount": tRingMgmtBcnRecStnPortRetryCount,
       "tRingMgmtBcnRecStnPortRetryDelay": tRingMgmtBcnRecStnPortRetryDelay,
       "tRingMgmtBcnRecBrdBypassRetryCount": tRingMgmtBcnRecBrdBypassRetryCount,
       "tRingMgmtBcnRecBrdBypassRetryDelay": tRingMgmtBcnRecBrdBypassRetryDelay,
       "tRingMgmtBcnRecBrdWrapRetryCount": tRingMgmtBcnRecBrdWrapRetryCount,
       "tRingMgmtBcnRecBrdWrapRetryDelay": tRingMgmtBcnRecBrdWrapRetryDelay,
       "tRingMgmtRingPollRecovery": tRingMgmtRingPollRecovery,
       "tRingMgmtStn": tRingMgmtStn,
       "tRingMgmtStnTable": tRingMgmtStnTable,
       "tRingMgmtStnEntry": tRingMgmtStnEntry,
       "tRingMgmtStnAddress": tRingMgmtStnAddress,
       "tRingMgmtStnName": tRingMgmtStnName,
       "tRingMgmtStnBoard": tRingMgmtStnBoard,
       "tRingMgmtStnPort": tRingMgmtStnPort,
       "tRingMgmtStnUNA": tRingMgmtStnUNA,
       "tRingMgmtStnDNA": tRingMgmtStnDNA,
       "tRingMgmtStnPhysLocation": tRingMgmtStnPhysLocation,
       "tRingMgmtStnFuncClasses": tRingMgmtStnFuncClasses,
       "tRingMgmtStnPriority": tRingMgmtStnPriority,
       "tRingMgmtStnRemoveStn": tRingMgmtStnRemoveStn,
       "tRingMgmtHost": tRingMgmtHost,
       "tRingMgmtHostCommands": tRingMgmtHostCommands,
       "tRingMgmtHostOpenStatus": tRingMgmtHostOpenStatus,
       "tRingMgmtHostErrorStatus": tRingMgmtHostErrorStatus,
       "tRingMgmtHostAMContention": tRingMgmtHostAMContention,
       "tRingMgmtHostTErrorReport": tRingMgmtHostTErrorReport,
       "tRingMgmtHostLocalAdminMac": tRingMgmtHostLocalAdminMac,
       "tRingMgmtSecurity": tRingMgmtSecurity,
       "tRingMgmtSecurityAdminState": tRingMgmtSecurityAdminState,
       "tRingMgmtSecurityAddressAdd": tRingMgmtSecurityAddressAdd,
       "tRingMgmtSecurityAddressRemove": tRingMgmtSecurityAddressRemove,
       "tRingMgmtSecurityStnCount": tRingMgmtSecurityStnCount,
       "tRingMgmtSecurityTable": tRingMgmtSecurityTable,
       "tRingMgmtSecurityEntry": tRingMgmtSecurityEntry,
       "tRingMgmtSecurityIfIndex": tRingMgmtSecurityIfIndex,
       "tRingMgmtSecurityStnAddress": tRingMgmtSecurityStnAddress,
       "tRingStats": tRingStats,
       "tRingStatsRing": tRingStatsRing,
       "tRingStatsRingErrs": tRingStatsRingErrs,
       "tRingStatsRingFrames": tRingStatsRingFrames,
       "tRingStatsRingKBytes": tRingStatsRingKBytes,
       "tRingStatsRingLineErrors": tRingStatsRingLineErrors,
       "tRingStatsRingBurstErrors": tRingStatsRingBurstErrors,
       "tRingStatsRingACErrors": tRingStatsRingACErrors,
       "tRingStatsRingAbortSequences": tRingStatsRingAbortSequences,
       "tRingStatsRingInternalErrors": tRingStatsRingInternalErrors,
       "tRingStatsRingLostFrames": tRingStatsRingLostFrames,
       "tRingStatsRingCongestErrors": tRingStatsRingCongestErrors,
       "tRingStatsRingFCErrors": tRingStatsRingFCErrors,
       "tRingStatsRingTokenErrors": tRingStatsRingTokenErrors,
       "tRingStatsRingFreqErrors": tRingStatsRingFreqErrors,
       "tRingStatsRingTotalErrors": tRingStatsRingTotalErrors,
       "tRingStatsRingAMChanges": tRingStatsRingAMChanges,
       "tRingStatsRingRingPurges": tRingStatsRingRingPurges,
       "tRingStatsRingBeaconEvents": tRingStatsRingBeaconEvents,
       "tRingStatsRingLongestBeacon": tRingStatsRingLongestBeacon,
       "tRingStatsRingLastBeacon": tRingStatsRingLastBeacon,
       "tRingStatsRingLastBeaconType": tRingStatsRingLastBeaconType,
       "tRingStatsRingPollFailureNoRecovery": tRingStatsRingPollFailureNoRecovery,
       "tRingStatsRingPollFailureNNIFrameCount": tRingStatsRingPollFailureNNIFrameCount,
       "tRingStatsRingPollFailureNNIFrameAddress": tRingStatsRingPollFailureNNIFrameAddress,
       "tRingStatsRingPollFailureLastNNIFrameTime": tRingStatsRingPollFailureLastNNIFrameTime,
       "tRingStatsRingPollFailureLastDNAAddress": tRingStatsRingPollFailureLastDNAAddress,
       "tRingStatsRingProtos": tRingStatsRingProtos,
       "tRingStatsRingProtocolSnaFrames": tRingStatsRingProtocolSnaFrames,
       "tRingStatsRingProtocolXnsFrames": tRingStatsRingProtocolXnsFrames,
       "tRingStatsRingProtocolTcpIpFrames": tRingStatsRingProtocolTcpIpFrames,
       "tRingStatsRingProtocolBanyanFrames": tRingStatsRingProtocolBanyanFrames,
       "tRingStatsRingProtocolIpxFrames": tRingStatsRingProtocolIpxFrames,
       "tRingStatsRingProtocolNetbiosFrames": tRingStatsRingProtocolNetbiosFrames,
       "tRingStatsRingProtocolLanNetMgrFrames": tRingStatsRingProtocolLanNetMgrFrames,
       "tRingStatsRingProtocolOtherFrames": tRingStatsRingProtocolOtherFrames,
       "tRingStatsRingSizes": tRingStatsRingSizes,
       "tRingStatsRingFramesizeUpTo63Bytes": tRingStatsRingFramesizeUpTo63Bytes,
       "tRingStatsRingFramesize64To127Bytes": tRingStatsRingFramesize64To127Bytes,
       "tRingStatsRingFramesize128To255Bytes": tRingStatsRingFramesize128To255Bytes,
       "tRingStatsRingFramesize256To511Bytes": tRingStatsRingFramesize256To511Bytes,
       "tRingStatsRingFramesize512To1023Bytes": tRingStatsRingFramesize512To1023Bytes,
       "tRingStatsRingFramesize1024To2047Bytes": tRingStatsRingFramesize1024To2047Bytes,
       "tRingStatsRingFramesize2048To4095Bytes": tRingStatsRingFramesize2048To4095Bytes,
       "tRingStatsRingFramesize4096AndUpBytes": tRingStatsRingFramesize4096AndUpBytes,
       "tRingStatsStn": tRingStatsStn,
       "tRingStatsStnTable": tRingStatsStnTable,
       "tRingStatsStnEntry": tRingStatsStnEntry,
       "tRingStatsStnAddress": tRingStatsStnAddress,
       "tRingStatsStnFrames": tRingStatsStnFrames,
       "tRingStatsStnBytes": tRingStatsStnBytes,
       "tRingStatsStnLineErrors": tRingStatsStnLineErrors,
       "tRingStatsStnBurstErrors": tRingStatsStnBurstErrors,
       "tRingStatsStnACErrors": tRingStatsStnACErrors,
       "tRingStatsStnAbortSequences": tRingStatsStnAbortSequences,
       "tRingStatsStnInternalErrors": tRingStatsStnInternalErrors,
       "tRingStatsStnLostFrames": tRingStatsStnLostFrames,
       "tRingStatsStnCongestErrors": tRingStatsStnCongestErrors,
       "tRingStatsStnFCErrors": tRingStatsStnFCErrors,
       "tRingStatsStnTokenErrors": tRingStatsStnTokenErrors,
       "tRingStatsStnFreqErrors": tRingStatsStnFreqErrors,
       "tRingStatsStnErrors": tRingStatsStnErrors,
       "tRingStatsReset": tRingStatsReset,
       "tRingStatsResetCounters": tRingStatsResetCounters,
       "tRingStatsResetTime": tRingStatsResetTime,
       "tRingAlarms": tRingAlarms,
       "tRingAlarmsRing": tRingAlarmsRing,
       "tRingAlarmsRingEnbl": tRingAlarmsRingEnbl,
       "tRingAlarmsRingTimebase": tRingAlarmsRingTimebase,
       "tRingAlarmsRingRingPurgesEnable": tRingAlarmsRingRingPurgesEnable,
       "tRingAlarmsRingAMPErrsEnable": tRingAlarmsRingAMPErrsEnable,
       "tRingAlarmsRingTokenErrsEnable": tRingAlarmsRingTokenErrsEnable,
       "tRingAlarmsRingClaimTknErrsEnable": tRingAlarmsRingClaimTknErrsEnable,
       "tRingAlarmsRingLostFramesEnable": tRingAlarmsRingLostFramesEnable,
       "tRingAlarmsRingBeaconStateEnable": tRingAlarmsRingBeaconStateEnable,
       "tRingAlarmsRingFrameCountEnable": tRingAlarmsRingFrameCountEnable,
       "tRingAlarmsRingThrsh": tRingAlarmsRingThrsh,
       "tRingAlarmsRingRingPurgesThreshold": tRingAlarmsRingRingPurgesThreshold,
       "tRingAlarmsRingAMPErrsThreshold": tRingAlarmsRingAMPErrsThreshold,
       "tRingAlarmsRingTokenErrsThreshold": tRingAlarmsRingTokenErrsThreshold,
       "tRingAlarmsRingClaimTknThreshold": tRingAlarmsRingClaimTknThreshold,
       "tRingAlarmsRingLostFramesThreshold": tRingAlarmsRingLostFramesThreshold,
       "tRingAlarmsRingBeaconStateThreshold": tRingAlarmsRingBeaconStateThreshold,
       "tRingAlarmsRingFrameCountThreshold": tRingAlarmsRingFrameCountThreshold,
       "tRingAlarmsStn": tRingAlarmsStn,
       "tRingAlarmsStnEnbl": tRingAlarmsStnEnbl,
       "tRingAlarmsStnEnblTable": tRingAlarmsStnEnblTable,
       "tRingAlarmsStnEnblEntry": tRingAlarmsStnEnblEntry,
       "tRingAlarmsStnEnblAddress": tRingAlarmsStnEnblAddress,
       "tRingAlarmsStnEnblLineErrsEnable": tRingAlarmsStnEnblLineErrsEnable,
       "tRingAlarmsStnEnblInternalErrsEnable": tRingAlarmsStnEnblInternalErrsEnable,
       "tRingAlarmsStnEnblBurstErrsEnable": tRingAlarmsStnEnblBurstErrsEnable,
       "tRingAlarmsStnEnblACErrsEnable": tRingAlarmsStnEnblACErrsEnable,
       "tRingAlarmsStnEnblRcvrCongestEnable": tRingAlarmsStnEnblRcvrCongestEnable,
       "tRingAlarmsStnThrsh": tRingAlarmsStnThrsh,
       "tRingAlarmsStnThrshTable": tRingAlarmsStnThrshTable,
       "tRingAlarmsStnThrshEntry": tRingAlarmsStnThrshEntry,
       "tRingAlarmsStnThrshAddress": tRingAlarmsStnThrshAddress,
       "tRingAlarmsStnThrshLineErrsThreshold": tRingAlarmsStnThrshLineErrsThreshold,
       "tRingAlarmsStnThrshInternalErrsThreshold": tRingAlarmsStnThrshInternalErrsThreshold,
       "tRingAlarmsStnThrshBurstErrsThreshold": tRingAlarmsStnThrshBurstErrsThreshold,
       "tRingAlarmsStnThrshACErrsThreshold": tRingAlarmsStnThrshACErrsThreshold,
       "tRingAlarmsStnThrshRcvrCongestThreshold": tRingAlarmsStnThrshRcvrCongestThreshold,
       "tRingPortGrp": tRingPortGrp,
       "tRingPortGrpTable": tRingPortGrpTable,
       "tRingPortGrpEntry": tRingPortGrpEntry,
       "tRingPortGrpId": tRingPortGrpId,
       "tRingPortGrpName": tRingPortGrpName,
       "tRingPortGrpStnPortCount": tRingPortGrpStnPortCount,
       "tRingPortGrpRingPortCount": tRingPortGrpRingPortCount,
       "tRingPortGrpStnPortsEnable": tRingPortGrpStnPortsEnable,
       "tRingPortGrpRingPortsEnable": tRingPortGrpRingPortsEnable,
       "tRingPortGrpStnPortsOn": tRingPortGrpStnPortsOn,
       "tRingPortGrpRingPortsOn": tRingPortGrpRingPortsOn,
       "tRingPortGrpMode": tRingPortGrpMode,
       "tRingPortGrpSpeed": tRingPortGrpSpeed,
       "tRingPortGrpSpeedFault": tRingPortGrpSpeedFault,
       "tRingPortGrpSpeedFaultLocation": tRingPortGrpSpeedFaultLocation,
       "tRingPortGrpBypassRingPortState": tRingPortGrpBypassRingPortState,
       "tRingPort": tRingPort,
       "tRingPortMgmt": tRingPortMgmt,
       "tRingPortMgmtTable": tRingPortMgmtTable,
       "tRingPortMgmtEntry": tRingPortMgmtEntry,
       "tRingPortMgmtPortId": tRingPortMgmtPortId,
       "tRingPortMgmtPortGrpId": tRingPortMgmtPortGrpId,
       "tRingPortMgmtPortName": tRingPortMgmtPortName,
       "tRingPortMgmtPortAdminState": tRingPortMgmtPortAdminState,
       "tRingPortMgmtPortOperState": tRingPortMgmtPortOperState,
       "tRingPortMgmtPortType": tRingPortMgmtPortType,
       "tRingPortMgmtSpeedFaultDetect": tRingPortMgmtSpeedFaultDetect,
       "tRingPortMgmtRingOutEnable": tRingPortMgmtRingOutEnable,
       "tRingPortStn": tRingPortStn,
       "tRingPortStnTable": tRingPortStnTable,
       "tRingPortStnEntry": tRingPortStnEntry,
       "tRingPortStnPortId": tRingPortStnPortId,
       "tRingPortStnPortGrpId": tRingPortStnPortGrpId,
       "tRingPortStnPortLinkState": tRingPortStnPortLinkState,
       "tRingPortStnPortLinkStateTime": tRingPortStnPortLinkStateTime,
       "tRingPortStnPortMapEnable": tRingPortStnPortMapEnable,
       "tRingPortStnPortMappedMacAddr": tRingPortStnPortMappedMacAddr,
       "tRingPortStnInsertionTrapEnable": tRingPortStnInsertionTrapEnable,
       "tRingPortRing": tRingPortRing,
       "tRingPortRingTable": tRingPortRingTable,
       "tRingPortRingEntry": tRingPortRingEntry,
       "tRingPortRingPortId": tRingPortRingPortId,
       "tRingPortRingPortGrpId": tRingPortRingPortGrpId,
       "tRingPortRingPortClass": tRingPortRingPortClass,
       "tRingPortRingPortMediaSelect": tRingPortRingPortMediaSelect,
       "tRingPortRingFaultStatus": tRingPortRingFaultStatus,
       "tRingPortRingFaultStateTime": tRingPortRingFaultStateTime,
       "tRingPortRingPhantomCurrent": tRingPortRingPhantomCurrent,
       "tRingPortRingPortType": tRingPortRingPortType,
       "tRingIf": tRingIf,
       "tRingIfIndex": tRingIfIndex}
)
