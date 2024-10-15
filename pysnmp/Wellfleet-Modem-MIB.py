# SNMP MIB module (Wellfleet-Modem-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-Modem-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:43 2024
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

(wfModemGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfModemGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfModemTable_Object = MibTable
wfModemTable = _WfModemTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1)
)
if mibBuilder.loadTexts:
    wfModemTable.setStatus("mandatory")
_WfModemEntry_Object = MibTableRow
wfModemEntry = _WfModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1)
)
wfModemEntry.setIndexNames(
    (0, "Wellfleet-Modem-MIB", "wfModemSlot"),
    (0, "Wellfleet-Modem-MIB", "wfModemConnector"),
)
if mibBuilder.loadTexts:
    wfModemEntry.setStatus("mandatory")


class _WfModemDelete_Type(Integer32):
    """Custom type wfModemDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfModemDelete_Type.__name__ = "Integer32"
_WfModemDelete_Object = MibTableColumn
wfModemDelete = _WfModemDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 1),
    _WfModemDelete_Type()
)
wfModemDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemDelete.setStatus("mandatory")
_WfModemSlot_Type = Integer32
_WfModemSlot_Object = MibTableColumn
wfModemSlot = _WfModemSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 2),
    _WfModemSlot_Type()
)
wfModemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemSlot.setStatus("mandatory")
_WfModemConnector_Type = Integer32
_WfModemConnector_Object = MibTableColumn
wfModemConnector = _WfModemConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 3),
    _WfModemConnector_Type()
)
wfModemConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemConnector.setStatus("mandatory")


class _WfModemIdSwRev_Type(DisplayString):
    """Custom type wfModemIdSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_WfModemIdSwRev_Type.__name__ = "DisplayString"
_WfModemIdSwRev_Object = MibTableColumn
wfModemIdSwRev = _WfModemIdSwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 4),
    _WfModemIdSwRev_Type()
)
wfModemIdSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIdSwRev.setStatus("mandatory")


class _WfModemIdHwRev_Type(DisplayString):
    """Custom type wfModemIdHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_WfModemIdHwRev_Type.__name__ = "DisplayString"
_WfModemIdHwRev_Object = MibTableColumn
wfModemIdHwRev = _WfModemIdHwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 5),
    _WfModemIdHwRev_Type()
)
wfModemIdHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemIdHwRev.setStatus("mandatory")


class _WfModemLineState_Type(Integer32):
    """Custom type wfModemLineState based on Integer32"""
    defaultValue = 1

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
        *(("busiedOut", 5),
          ("connected", 4),
          ("offHook", 3),
          ("onHook", 2),
          ("reset", 6),
          ("unknown", 1))
    )


_WfModemLineState_Type.__name__ = "Integer32"
_WfModemLineState_Object = MibTableColumn
wfModemLineState = _WfModemLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 6),
    _WfModemLineState_Type()
)
wfModemLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemLineState.setStatus("mandatory")


class _WfModemConnectionFailReason_Type(Integer32):
    """Custom type wfModemConnectionFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lossOfCarrier", 2),
          ("noCommonProtocol", 4),
          ("noResponseFromRemote", 6),
          ("normal", 1),
          ("protocolViolation", 7),
          ("remoteDisconnect", 5),
          ("v42NegotiationFailed", 3))
    )


_WfModemConnectionFailReason_Type.__name__ = "Integer32"
_WfModemConnectionFailReason_Object = MibTableColumn
wfModemConnectionFailReason = _WfModemConnectionFailReason_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 7),
    _WfModemConnectionFailReason_Type()
)
wfModemConnectionFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemConnectionFailReason.setStatus("mandatory")


class _WfModemCfgFactoryDefaults_Type(Integer32):
    """Custom type wfModemCfgFactoryDefaults based on Integer32"""
    defaultValue = 1

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


_WfModemCfgFactoryDefaults_Type.__name__ = "Integer32"
_WfModemCfgFactoryDefaults_Object = MibTableColumn
wfModemCfgFactoryDefaults = _WfModemCfgFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 8),
    _WfModemCfgFactoryDefaults_Type()
)
wfModemCfgFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCfgFactoryDefaults.setStatus("mandatory")
_WfModemCfgInitString_Type = DisplayString
_WfModemCfgInitString_Object = MibTableColumn
wfModemCfgInitString = _WfModemCfgInitString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 9),
    _WfModemCfgInitString_Type()
)
wfModemCfgInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCfgInitString.setStatus("mandatory")
_WfModemCfgDefaultString_Type = DisplayString
_WfModemCfgDefaultString_Object = MibTableColumn
wfModemCfgDefaultString = _WfModemCfgDefaultString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 10),
    _WfModemCfgDefaultString_Type()
)
wfModemCfgDefaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemCfgDefaultString.setStatus("mandatory")
_WfModemCfgResultCodeString_Type = DisplayString
_WfModemCfgResultCodeString_Object = MibTableColumn
wfModemCfgResultCodeString = _WfModemCfgResultCodeString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 11),
    _WfModemCfgResultCodeString_Type()
)
wfModemCfgResultCodeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemCfgResultCodeString.setStatus("mandatory")


class _WfModemCfgState_Type(Integer32):
    """Custom type wfModemCfgState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfgIdle", 1),
          ("cfgInProgress", 2),
          ("cfgResponseReturned", 3))
    )


_WfModemCfgState_Type.__name__ = "Integer32"
_WfModemCfgState_Object = MibTableColumn
wfModemCfgState = _WfModemCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 12),
    _WfModemCfgState_Type()
)
wfModemCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCfgState.setStatus("mandatory")


class _WfModemCfgCountry_Type(Integer32):
    """Custom type wfModemCfgCountry based on Integer32"""
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
        *(("germany", 4),
          ("japan", 2),
          ("northAmerica", 1),
          ("uk", 3))
    )


_WfModemCfgCountry_Type.__name__ = "Integer32"
_WfModemCfgCountry_Object = MibTableColumn
wfModemCfgCountry = _WfModemCfgCountry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 13),
    _WfModemCfgCountry_Type()
)
wfModemCfgCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemCfgCountry.setStatus("mandatory")


class _WfModemV54Lpbk_Type(Integer32):
    """Custom type wfModemV54Lpbk based on Integer32"""
    defaultValue = 1

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
        *(("localAnlgLpbk", 2),
          ("localAnlgLpbkWPattern", 6),
          ("localDigLpbk", 3),
          ("noLpbk", 1),
          ("remDigLpbk", 4),
          ("remDigLpbkWPattern", 5))
    )


_WfModemV54Lpbk_Type.__name__ = "Integer32"
_WfModemV54Lpbk_Object = MibTableColumn
wfModemV54Lpbk = _WfModemV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 14),
    _WfModemV54Lpbk_Type()
)
wfModemV54Lpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemV54Lpbk.setStatus("mandatory")


class _WfModemV54Timer_Type(Integer32):
    """Custom type wfModemV54Timer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfModemV54Timer_Type.__name__ = "Integer32"
_WfModemV54Timer_Object = MibTableColumn
wfModemV54Timer = _WfModemV54Timer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 15),
    _WfModemV54Timer_Type()
)
wfModemV54Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemV54Timer.setStatus("mandatory")
_WfModemV54Errors_Type = Counter32
_WfModemV54Errors_Object = MibTableColumn
wfModemV54Errors = _WfModemV54Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 16),
    _WfModemV54Errors_Type()
)
wfModemV54Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemV54Errors.setStatus("mandatory")


class _WfModemV54RemLpbkDetect_Type(Integer32):
    """Custom type wfModemV54RemLpbkDetect based on Integer32"""
    defaultValue = 1

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


_WfModemV54RemLpbkDetect_Type.__name__ = "Integer32"
_WfModemV54RemLpbkDetect_Object = MibTableColumn
wfModemV54RemLpbkDetect = _WfModemV54RemLpbkDetect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 17),
    _WfModemV54RemLpbkDetect_Type()
)
wfModemV54RemLpbkDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemV54RemLpbkDetect.setStatus("mandatory")
_WfModemPhoneNumber_Type = DisplayString
_WfModemPhoneNumber_Object = MibTableColumn
wfModemPhoneNumber = _WfModemPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 18),
    _WfModemPhoneNumber_Type()
)
wfModemPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemPhoneNumber.setStatus("mandatory")


class _WfModemInitState_Type(Integer32):
    """Custom type wfModemInitState based on Integer32"""
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
        *(("getInfo", 3),
          ("initComplete", 8),
          ("initialization", 5),
          ("loopback", 7),
          ("phoneNumber", 6),
          ("sccInit", 2),
          ("setDefaults", 4),
          ("startup", 1))
    )


_WfModemInitState_Type.__name__ = "Integer32"
_WfModemInitState_Object = MibTableColumn
wfModemInitState = _WfModemInitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 19),
    _WfModemInitState_Type()
)
wfModemInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfModemInitState.setStatus("mandatory")


class _WfModemUnitReset_Type(Integer32):
    """Custom type wfModemUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetUnit", 1)
    )


_WfModemUnitReset_Type.__name__ = "Integer32"
_WfModemUnitReset_Object = MibTableColumn
wfModemUnitReset = _WfModemUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 20),
    _WfModemUnitReset_Type()
)
wfModemUnitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemUnitReset.setStatus("mandatory")


class _WfModemType_Type(Integer32):
    """Custom type wfModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfModemType_Type.__name__ = "Integer32"
_WfModemType_Object = MibTableColumn
wfModemType = _WfModemType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 29, 1, 1, 21),
    _WfModemType_Type()
)
wfModemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-Modem-MIB",
    **{"wfModemTable": wfModemTable,
       "wfModemEntry": wfModemEntry,
       "wfModemDelete": wfModemDelete,
       "wfModemSlot": wfModemSlot,
       "wfModemConnector": wfModemConnector,
       "wfModemIdSwRev": wfModemIdSwRev,
       "wfModemIdHwRev": wfModemIdHwRev,
       "wfModemLineState": wfModemLineState,
       "wfModemConnectionFailReason": wfModemConnectionFailReason,
       "wfModemCfgFactoryDefaults": wfModemCfgFactoryDefaults,
       "wfModemCfgInitString": wfModemCfgInitString,
       "wfModemCfgDefaultString": wfModemCfgDefaultString,
       "wfModemCfgResultCodeString": wfModemCfgResultCodeString,
       "wfModemCfgState": wfModemCfgState,
       "wfModemCfgCountry": wfModemCfgCountry,
       "wfModemV54Lpbk": wfModemV54Lpbk,
       "wfModemV54Timer": wfModemV54Timer,
       "wfModemV54Errors": wfModemV54Errors,
       "wfModemV54RemLpbkDetect": wfModemV54RemLpbkDetect,
       "wfModemPhoneNumber": wfModemPhoneNumber,
       "wfModemInitState": wfModemInitState,
       "wfModemUnitReset": wfModemUnitReset,
       "wfModemType": wfModemType}
)
