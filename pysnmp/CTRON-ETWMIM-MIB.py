# SNMP MIB module (CTRON-ETWMIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ETWMIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:50 2024
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

(ctPModuleETWMIM,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPModuleETWMIM")

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



class _EtwDbExist_Type(Integer32):
    """Custom type etwDbExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("no-exists", 2))
    )


_EtwDbExist_Type.__name__ = "Integer32"
_EtwDbExist_Object = MibScalar
etwDbExist = _EtwDbExist_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 1),
    _EtwDbExist_Type()
)
etwDbExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwDbExist.setStatus("mandatory")


class _EtwDbEnabled_Type(Integer32):
    """Custom type etwDbEnabled based on Integer32"""
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


_EtwDbEnabled_Type.__name__ = "Integer32"
_EtwDbEnabled_Object = MibScalar
etwDbEnabled = _EtwDbEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 2),
    _EtwDbEnabled_Type()
)
etwDbEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etwDbEnabled.setStatus("mandatory")


class _EtwDbFracToggle_Type(Integer32):
    """Custom type etwDbFracToggle based on Integer32"""
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
        *(("display-new", 2),
          ("display-old", 3),
          ("restore-old", 4),
          ("update-table", 1))
    )


_EtwDbFracToggle_Type.__name__ = "Integer32"
_EtwDbFracToggle_Object = MibScalar
etwDbFracToggle = _EtwDbFracToggle_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 3),
    _EtwDbFracToggle_Type()
)
etwDbFracToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etwDbFracToggle.setStatus("mandatory")


class _EtwFWRev_Type(OctetString):
    """Custom type etwFWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EtwFWRev_Type.__name__ = "OctetString"
_EtwFWRev_Object = MibScalar
etwFWRev = _EtwFWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 4),
    _EtwFWRev_Type()
)
etwFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwFWRev.setStatus("mandatory")
_EtwHWRev_Type = Integer32
_EtwHWRev_Object = MibScalar
etwHWRev = _EtwHWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 5),
    _EtwHWRev_Type()
)
etwHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwHWRev.setStatus("mandatory")


class _EtwEpimEnabled_Type(Integer32):
    """Custom type etwEpimEnabled based on Integer32"""
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


_EtwEpimEnabled_Type.__name__ = "Integer32"
_EtwEpimEnabled_Object = MibScalar
etwEpimEnabled = _EtwEpimEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 6),
    _EtwEpimEnabled_Type()
)
etwEpimEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwEpimEnabled.setStatus("mandatory")
_EtwEpimType_Type = ObjectIdentifier
_EtwEpimType_Object = MibScalar
etwEpimType = _EtwEpimType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 7),
    _EtwEpimType_Type()
)
etwEpimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwEpimType.setStatus("mandatory")


class _EtwEpimLink_Type(Integer32):
    """Custom type etwEpimLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-established", 1),
          ("link-not-established", 2),
          ("link-unknown", 3))
    )


_EtwEpimLink_Type.__name__ = "Integer32"
_EtwEpimLink_Object = MibScalar
etwEpimLink = _EtwEpimLink_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 8),
    _EtwEpimLink_Type()
)
etwEpimLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etwEpimLink.setStatus("mandatory")
_EtwClearNvramOnBoot_Type = Integer32
_EtwClearNvramOnBoot_Object = MibScalar
etwClearNvramOnBoot = _EtwClearNvramOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 9),
    _EtwClearNvramOnBoot_Type()
)
etwClearNvramOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etwClearNvramOnBoot.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ETWMIM-MIB",
    **{"etwDbExist": etwDbExist,
       "etwDbEnabled": etwDbEnabled,
       "etwDbFracToggle": etwDbFracToggle,
       "etwFWRev": etwFWRev,
       "etwHWRev": etwHWRev,
       "etwEpimEnabled": etwEpimEnabled,
       "etwEpimType": etwEpimType,
       "etwEpimLink": etwEpimLink,
       "etwClearNvramOnBoot": etwClearNvramOnBoot}
)
