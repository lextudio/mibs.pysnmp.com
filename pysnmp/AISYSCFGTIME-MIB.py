# SNMP MIB module (AISYSCFGTIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFGTIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:26 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSysCfgTime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 2)
)
aiSysCfgTime.setRevisions(
        ("2001-04-30 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSysCfg_ObjectIdentity = ObjectIdentity
aiSysCfg = _AiSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32)
)


class _AiSCTimeZone_Type(DisplayString):
    """Custom type aiSCTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 6),
    )


_AiSCTimeZone_Type.__name__ = "DisplayString"
_AiSCTimeZone_Object = MibScalar
aiSCTimeZone = _AiSCTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 1),
    _AiSCTimeZone_Type()
)
aiSCTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTimeZone.setStatus("current")
_AiSCDaylightSavingEnabled_Type = TruthValue
_AiSCDaylightSavingEnabled_Object = MibScalar
aiSCDaylightSavingEnabled = _AiSCDaylightSavingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 2),
    _AiSCDaylightSavingEnabled_Type()
)
aiSCDaylightSavingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCDaylightSavingEnabled.setStatus("current")


class _AiSCDaylightSavingStatus_Type(Integer32):
    """Custom type aiSCDaylightSavingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("inactive", 3))
    )


_AiSCDaylightSavingStatus_Type.__name__ = "Integer32"
_AiSCDaylightSavingStatus_Object = MibScalar
aiSCDaylightSavingStatus = _AiSCDaylightSavingStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 3),
    _AiSCDaylightSavingStatus_Type()
)
aiSCDaylightSavingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCDaylightSavingStatus.setStatus("current")
_AiSCTimeSntpEnabled_Type = TruthValue
_AiSCTimeSntpEnabled_Object = MibScalar
aiSCTimeSntpEnabled = _AiSCTimeSntpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 4),
    _AiSCTimeSntpEnabled_Type()
)
aiSCTimeSntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTimeSntpEnabled.setStatus("current")


class _AiSCTimeSntpPollInterval_Type(Integer32):
    """Custom type aiSCTimeSntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AiSCTimeSntpPollInterval_Type.__name__ = "Integer32"
_AiSCTimeSntpPollInterval_Object = MibScalar
aiSCTimeSntpPollInterval = _AiSCTimeSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 5),
    _AiSCTimeSntpPollInterval_Type()
)
aiSCTimeSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTimeSntpPollInterval.setStatus("current")
_AiSCTimeNtpServerTable_Object = MibTable
aiSCTimeNtpServerTable = _AiSCTimeNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 6)
)
if mibBuilder.loadTexts:
    aiSCTimeNtpServerTable.setStatus("current")
_AiSCTimeNtpServerEntry_Object = MibTableRow
aiSCTimeNtpServerEntry = _AiSCTimeNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1)
)
aiSCTimeNtpServerEntry.setIndexNames(
    (0, "AISYSCFGTIME-MIB", "aiSCTimeNtpServerIndex"),
)
if mibBuilder.loadTexts:
    aiSCTimeNtpServerEntry.setStatus("current")


class _AiSCTimeNtpServerIndex_Type(Integer32):
    """Custom type aiSCTimeNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCTimeNtpServerIndex_Type.__name__ = "Integer32"
_AiSCTimeNtpServerIndex_Object = MibTableColumn
aiSCTimeNtpServerIndex = _AiSCTimeNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1, 1),
    _AiSCTimeNtpServerIndex_Type()
)
aiSCTimeNtpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTimeNtpServerIndex.setStatus("current")
_AiSCTimeNtpServerAddress_Type = IpAddress
_AiSCTimeNtpServerAddress_Object = MibTableColumn
aiSCTimeNtpServerAddress = _AiSCTimeNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 2, 6, 1, 2),
    _AiSCTimeNtpServerAddress_Type()
)
aiSCTimeNtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTimeNtpServerAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFGTIME-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgTime": aiSysCfgTime,
       "aiSCTimeZone": aiSCTimeZone,
       "aiSCDaylightSavingEnabled": aiSCDaylightSavingEnabled,
       "aiSCDaylightSavingStatus": aiSCDaylightSavingStatus,
       "aiSCTimeSntpEnabled": aiSCTimeSntpEnabled,
       "aiSCTimeSntpPollInterval": aiSCTimeSntpPollInterval,
       "aiSCTimeNtpServerTable": aiSCTimeNtpServerTable,
       "aiSCTimeNtpServerEntry": aiSCTimeNtpServerEntry,
       "aiSCTimeNtpServerIndex": aiSCTimeNtpServerIndex,
       "aiSCTimeNtpServerAddress": aiSCTimeNtpServerAddress}
)
