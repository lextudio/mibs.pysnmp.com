# SNMP MIB module (ASCEND-MIBREDHM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBREDHM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:05 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibredHealthMonitoringProfile_ObjectIdentity = ObjectIdentity
mibredHealthMonitoringProfile = _MibredHealthMonitoringProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 179)
)
_MibredHealthMonitoringProfileTable_Object = MibTable
mibredHealthMonitoringProfileTable = _MibredHealthMonitoringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1)
)
if mibBuilder.loadTexts:
    mibredHealthMonitoringProfileTable.setStatus("mandatory")
_MibredHealthMonitoringProfileEntry_Object = MibTableRow
mibredHealthMonitoringProfileEntry = _MibredHealthMonitoringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1)
)
mibredHealthMonitoringProfileEntry.setIndexNames(
    (0, "ASCEND-MIBREDHM-MIB", "redHealthMonitoringProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibredHealthMonitoringProfileEntry.setStatus("mandatory")
_RedHealthMonitoringProfile_Index_o_Type = Integer32
_RedHealthMonitoringProfile_Index_o_Object = MibScalar
redHealthMonitoringProfile_Index_o = _RedHealthMonitoringProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 1),
    _RedHealthMonitoringProfile_Index_o_Type()
)
redHealthMonitoringProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_Index_o.setStatus("mandatory")


class _RedHealthMonitoringProfile_HmEnabled_Type(Integer32):
    """Custom type redHealthMonitoringProfile_HmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RedHealthMonitoringProfile_HmEnabled_Type.__name__ = "Integer32"
_RedHealthMonitoringProfile_HmEnabled_Object = MibScalar
redHealthMonitoringProfile_HmEnabled = _RedHealthMonitoringProfile_HmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 2),
    _RedHealthMonitoringProfile_HmEnabled_Type()
)
redHealthMonitoringProfile_HmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_HmEnabled.setStatus("mandatory")
_RedHealthMonitoringProfile_MaxWarningPrimary_Type = Integer32
_RedHealthMonitoringProfile_MaxWarningPrimary_Object = MibScalar
redHealthMonitoringProfile_MaxWarningPrimary = _RedHealthMonitoringProfile_MaxWarningPrimary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 3),
    _RedHealthMonitoringProfile_MaxWarningPrimary_Type()
)
redHealthMonitoringProfile_MaxWarningPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MaxWarningPrimary.setStatus("mandatory")
_RedHealthMonitoringProfile_MaxWarningSecondary_Type = Integer32
_RedHealthMonitoringProfile_MaxWarningSecondary_Object = MibScalar
redHealthMonitoringProfile_MaxWarningSecondary = _RedHealthMonitoringProfile_MaxWarningSecondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 4),
    _RedHealthMonitoringProfile_MaxWarningSecondary_Type()
)
redHealthMonitoringProfile_MaxWarningSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MaxWarningSecondary.setStatus("mandatory")
_RedHealthMonitoringProfile_MaxWarningPerMinutePrimary_Type = Integer32
_RedHealthMonitoringProfile_MaxWarningPerMinutePrimary_Object = MibScalar
redHealthMonitoringProfile_MaxWarningPerMinutePrimary = _RedHealthMonitoringProfile_MaxWarningPerMinutePrimary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 5),
    _RedHealthMonitoringProfile_MaxWarningPerMinutePrimary_Type()
)
redHealthMonitoringProfile_MaxWarningPerMinutePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MaxWarningPerMinutePrimary.setStatus("mandatory")
_RedHealthMonitoringProfile_MaxWarningPerMinuteSecondary_Type = Integer32
_RedHealthMonitoringProfile_MaxWarningPerMinuteSecondary_Object = MibScalar
redHealthMonitoringProfile_MaxWarningPerMinuteSecondary = _RedHealthMonitoringProfile_MaxWarningPerMinuteSecondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 6),
    _RedHealthMonitoringProfile_MaxWarningPerMinuteSecondary_Type()
)
redHealthMonitoringProfile_MaxWarningPerMinuteSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MaxWarningPerMinuteSecondary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryThresholdPrimary_Type = Integer32
_RedHealthMonitoringProfile_MemoryThresholdPrimary_Object = MibScalar
redHealthMonitoringProfile_MemoryThresholdPrimary = _RedHealthMonitoringProfile_MemoryThresholdPrimary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 7),
    _RedHealthMonitoringProfile_MemoryThresholdPrimary_Type()
)
redHealthMonitoringProfile_MemoryThresholdPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryThresholdPrimary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryThresholdSecondary_Type = Integer32
_RedHealthMonitoringProfile_MemoryThresholdSecondary_Object = MibScalar
redHealthMonitoringProfile_MemoryThresholdSecondary = _RedHealthMonitoringProfile_MemoryThresholdSecondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 8),
    _RedHealthMonitoringProfile_MemoryThresholdSecondary_Type()
)
redHealthMonitoringProfile_MemoryThresholdSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryThresholdSecondary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryAlertThresholdPrimary_Type = Integer32
_RedHealthMonitoringProfile_MemoryAlertThresholdPrimary_Object = MibScalar
redHealthMonitoringProfile_MemoryAlertThresholdPrimary = _RedHealthMonitoringProfile_MemoryAlertThresholdPrimary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 9),
    _RedHealthMonitoringProfile_MemoryAlertThresholdPrimary_Type()
)
redHealthMonitoringProfile_MemoryAlertThresholdPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryAlertThresholdPrimary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryAlertThresholdSecondary_Type = Integer32
_RedHealthMonitoringProfile_MemoryAlertThresholdSecondary_Object = MibScalar
redHealthMonitoringProfile_MemoryAlertThresholdSecondary = _RedHealthMonitoringProfile_MemoryAlertThresholdSecondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 10),
    _RedHealthMonitoringProfile_MemoryAlertThresholdSecondary_Type()
)
redHealthMonitoringProfile_MemoryAlertThresholdSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryAlertThresholdSecondary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryAlertTimeoutPrimary_Type = Integer32
_RedHealthMonitoringProfile_MemoryAlertTimeoutPrimary_Object = MibScalar
redHealthMonitoringProfile_MemoryAlertTimeoutPrimary = _RedHealthMonitoringProfile_MemoryAlertTimeoutPrimary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 11),
    _RedHealthMonitoringProfile_MemoryAlertTimeoutPrimary_Type()
)
redHealthMonitoringProfile_MemoryAlertTimeoutPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryAlertTimeoutPrimary.setStatus("mandatory")
_RedHealthMonitoringProfile_MemoryAlertTimeoutSecondary_Type = Integer32
_RedHealthMonitoringProfile_MemoryAlertTimeoutSecondary_Object = MibScalar
redHealthMonitoringProfile_MemoryAlertTimeoutSecondary = _RedHealthMonitoringProfile_MemoryAlertTimeoutSecondary_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 12),
    _RedHealthMonitoringProfile_MemoryAlertTimeoutSecondary_Type()
)
redHealthMonitoringProfile_MemoryAlertTimeoutSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_MemoryAlertTimeoutSecondary.setStatus("mandatory")
_RedHealthMonitoringProfile_ResetStuckPrimaryTimeout_Type = Integer32
_RedHealthMonitoringProfile_ResetStuckPrimaryTimeout_Object = MibScalar
redHealthMonitoringProfile_ResetStuckPrimaryTimeout = _RedHealthMonitoringProfile_ResetStuckPrimaryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 13),
    _RedHealthMonitoringProfile_ResetStuckPrimaryTimeout_Type()
)
redHealthMonitoringProfile_ResetStuckPrimaryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_ResetStuckPrimaryTimeout.setStatus("mandatory")


class _RedHealthMonitoringProfile_Action_o_Type(Integer32):
    """Custom type redHealthMonitoringProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RedHealthMonitoringProfile_Action_o_Type.__name__ = "Integer32"
_RedHealthMonitoringProfile_Action_o_Object = MibScalar
redHealthMonitoringProfile_Action_o = _RedHealthMonitoringProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 179, 1, 1, 14),
    _RedHealthMonitoringProfile_Action_o_Type()
)
redHealthMonitoringProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redHealthMonitoringProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBREDHM-MIB",
    **{"DisplayString": DisplayString,
       "mibredHealthMonitoringProfile": mibredHealthMonitoringProfile,
       "mibredHealthMonitoringProfileTable": mibredHealthMonitoringProfileTable,
       "mibredHealthMonitoringProfileEntry": mibredHealthMonitoringProfileEntry,
       "redHealthMonitoringProfile-Index-o": redHealthMonitoringProfile_Index_o,
       "redHealthMonitoringProfile-HmEnabled": redHealthMonitoringProfile_HmEnabled,
       "redHealthMonitoringProfile-MaxWarningPrimary": redHealthMonitoringProfile_MaxWarningPrimary,
       "redHealthMonitoringProfile-MaxWarningSecondary": redHealthMonitoringProfile_MaxWarningSecondary,
       "redHealthMonitoringProfile-MaxWarningPerMinutePrimary": redHealthMonitoringProfile_MaxWarningPerMinutePrimary,
       "redHealthMonitoringProfile-MaxWarningPerMinuteSecondary": redHealthMonitoringProfile_MaxWarningPerMinuteSecondary,
       "redHealthMonitoringProfile-MemoryThresholdPrimary": redHealthMonitoringProfile_MemoryThresholdPrimary,
       "redHealthMonitoringProfile-MemoryThresholdSecondary": redHealthMonitoringProfile_MemoryThresholdSecondary,
       "redHealthMonitoringProfile-MemoryAlertThresholdPrimary": redHealthMonitoringProfile_MemoryAlertThresholdPrimary,
       "redHealthMonitoringProfile-MemoryAlertThresholdSecondary": redHealthMonitoringProfile_MemoryAlertThresholdSecondary,
       "redHealthMonitoringProfile-MemoryAlertTimeoutPrimary": redHealthMonitoringProfile_MemoryAlertTimeoutPrimary,
       "redHealthMonitoringProfile-MemoryAlertTimeoutSecondary": redHealthMonitoringProfile_MemoryAlertTimeoutSecondary,
       "redHealthMonitoringProfile-ResetStuckPrimaryTimeout": redHealthMonitoringProfile_ResetStuckPrimaryTimeout,
       "redHealthMonitoringProfile-Action-o": redHealthMonitoringProfile_Action_o}
)
