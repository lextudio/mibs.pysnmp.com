# SNMP MIB module (SA-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SA-MTA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:15 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

saMta = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3)
)
saMta.setRevisions(
        ("2016-11-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sa_ObjectIdentity = ObjectIdentity
sa = _Sa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429)
)
_SaVoip_ObjectIdentity = ObjectIdentity
saVoip = _SaVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78)
)
_SaMtaDevice_ObjectIdentity = ObjectIdentity
saMtaDevice = _SaMtaDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 1)
)


class _SaMtaDevOffHookWarnTOBusy_Type(Integer32):
    """Custom type saMtaDevOffHookWarnTOBusy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SaMtaDevOffHookWarnTOBusy_Type.__name__ = "Integer32"
_SaMtaDevOffHookWarnTOBusy_Object = MibScalar
saMtaDevOffHookWarnTOBusy = _SaMtaDevOffHookWarnTOBusy_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 1, 61),
    _SaMtaDevOffHookWarnTOBusy_Type()
)
saMtaDevOffHookWarnTOBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saMtaDevOffHookWarnTOBusy.setStatus("current")
_SaMtaEndPointTable_Object = MibTable
saMtaEndPointTable = _SaMtaEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2)
)
if mibBuilder.loadTexts:
    saMtaEndPointTable.setStatus("current")
_SaMtaEndPointEntry_Object = MibTableRow
saMtaEndPointEntry = _SaMtaEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2, 1)
)
saMtaEndPointEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    saMtaEndPointEntry.setStatus("current")


class _SaMtaEndPntHookFlashMinTime_Type(Integer32):
    """Custom type saMtaEndPntHookFlashMinTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 2000),
    )


_SaMtaEndPntHookFlashMinTime_Type.__name__ = "Integer32"
_SaMtaEndPntHookFlashMinTime_Object = MibTableColumn
saMtaEndPntHookFlashMinTime = _SaMtaEndPntHookFlashMinTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2, 1, 1),
    _SaMtaEndPntHookFlashMinTime_Type()
)
saMtaEndPntHookFlashMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saMtaEndPntHookFlashMinTime.setStatus("current")
if mibBuilder.loadTexts:
    saMtaEndPntHookFlashMinTime.setUnits("milliseconds")


class _SaMtaEndPntHookFlashMaxTime_Type(Integer32):
    """Custom type saMtaEndPntHookFlashMaxTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000),
    )


_SaMtaEndPntHookFlashMaxTime_Type.__name__ = "Integer32"
_SaMtaEndPntHookFlashMaxTime_Object = MibTableColumn
saMtaEndPntHookFlashMaxTime = _SaMtaEndPntHookFlashMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2, 1, 2),
    _SaMtaEndPntHookFlashMaxTime_Type()
)
saMtaEndPntHookFlashMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saMtaEndPntHookFlashMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    saMtaEndPntHookFlashMaxTime.setUnits("milliseconds")


class _SaMtaEndPntStatePhysical_Type(Integer32):
    """Custom type saMtaEndPntStatePhysical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offHook", 2),
          ("onHook", 1))
    )


_SaMtaEndPntStatePhysical_Type.__name__ = "Integer32"
_SaMtaEndPntStatePhysical_Object = MibTableColumn
saMtaEndPntStatePhysical = _SaMtaEndPntStatePhysical_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2, 1, 6),
    _SaMtaEndPntStatePhysical_Type()
)
saMtaEndPntStatePhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saMtaEndPntStatePhysical.setStatus("current")


class _SaMtaEndPntStateLogical_Type(Integer32):
    """Custom type saMtaEndPntStateLogical based on Integer32"""
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
        *(("connectedIdle", 1),
          ("disconnected", 2),
          ("inCallData", 4),
          ("inCallVoice", 3))
    )


_SaMtaEndPntStateLogical_Type.__name__ = "Integer32"
_SaMtaEndPntStateLogical_Object = MibTableColumn
saMtaEndPntStateLogical = _SaMtaEndPntStateLogical_Object(
    (1, 3, 6, 1, 4, 1, 1429, 78, 3, 2, 1, 7),
    _SaMtaEndPntStateLogical_Type()
)
saMtaEndPntStateLogical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saMtaEndPntStateLogical.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SA-MTA-MIB",
    **{"sa": sa,
       "saVoip": saVoip,
       "saMta": saMta,
       "saMtaDevice": saMtaDevice,
       "saMtaDevOffHookWarnTOBusy": saMtaDevOffHookWarnTOBusy,
       "saMtaEndPointTable": saMtaEndPointTable,
       "saMtaEndPointEntry": saMtaEndPointEntry,
       "saMtaEndPntHookFlashMinTime": saMtaEndPntHookFlashMinTime,
       "saMtaEndPntHookFlashMaxTime": saMtaEndPntHookFlashMaxTime,
       "saMtaEndPntStatePhysical": saMtaEndPntStatePhysical,
       "saMtaEndPntStateLogical": saMtaEndPntStateLogical}
)
