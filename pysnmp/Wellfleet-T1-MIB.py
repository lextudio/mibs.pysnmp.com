# SNMP MIB module (Wellfleet-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:16 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfLine,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfLine")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfT1Table_Object = MibTable
wfT1Table = _WfT1Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10)
)
if mibBuilder.loadTexts:
    wfT1Table.setStatus("mandatory")
_WfT1Entry_Object = MibTableRow
wfT1Entry = _WfT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1)
)
wfT1Entry.setIndexNames(
    (0, "Wellfleet-T1-MIB", "wfT1Slot"),
    (0, "Wellfleet-T1-MIB", "wfT1Connector"),
)
if mibBuilder.loadTexts:
    wfT1Entry.setStatus("mandatory")


class _WfT1Delete_Type(Integer32):
    """Custom type wfT1Delete based on Integer32"""
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


_WfT1Delete_Type.__name__ = "Integer32"
_WfT1Delete_Object = MibTableColumn
wfT1Delete = _WfT1Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 1),
    _WfT1Delete_Type()
)
wfT1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1Delete.setStatus("mandatory")


class _WfT1Disable_Type(Integer32):
    """Custom type wfT1Disable based on Integer32"""
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


_WfT1Disable_Type.__name__ = "Integer32"
_WfT1Disable_Object = MibTableColumn
wfT1Disable = _WfT1Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 2),
    _WfT1Disable_Type()
)
wfT1Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1Disable.setStatus("mandatory")


class _WfT1State_Type(Integer32):
    """Custom type wfT1State based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfT1State_Type.__name__ = "Integer32"
_WfT1State_Object = MibTableColumn
wfT1State = _WfT1State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 3),
    _WfT1State_Type()
)
wfT1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1State.setStatus("mandatory")


class _WfT1Slot_Type(Integer32):
    """Custom type wfT1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfT1Slot_Type.__name__ = "Integer32"
_WfT1Slot_Object = MibTableColumn
wfT1Slot = _WfT1Slot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 4),
    _WfT1Slot_Type()
)
wfT1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Slot.setStatus("mandatory")


class _WfT1Connector_Type(Integer32):
    """Custom type wfT1Connector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfT1Connector_Type.__name__ = "Integer32"
_WfT1Connector_Object = MibTableColumn
wfT1Connector = _WfT1Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 5),
    _WfT1Connector_Type()
)
wfT1Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Connector.setStatus("mandatory")
_WfT1Madr_Type = OctetString
_WfT1Madr_Object = MibTableColumn
wfT1Madr = _WfT1Madr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 6),
    _WfT1Madr_Type()
)
wfT1Madr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1Madr.setStatus("mandatory")


class _WfT1FrameType_Type(Integer32):
    """Custom type wfT1FrameType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_WfT1FrameType_Type.__name__ = "Integer32"
_WfT1FrameType_Object = MibTableColumn
wfT1FrameType = _WfT1FrameType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 7),
    _WfT1FrameType_Type()
)
wfT1FrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1FrameType.setStatus("mandatory")


class _WfT1LineBuildout_Type(Integer32):
    """Custom type wfT1LineBuildout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 655),
    )


_WfT1LineBuildout_Type.__name__ = "Integer32"
_WfT1LineBuildout_Object = MibTableColumn
wfT1LineBuildout = _WfT1LineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 8),
    _WfT1LineBuildout_Type()
)
wfT1LineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1LineBuildout.setStatus("mandatory")


class _WfT1B8ZSSupport_Type(Integer32):
    """Custom type wfT1B8ZSSupport based on Integer32"""
    defaultValue = 2

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


_WfT1B8ZSSupport_Type.__name__ = "Integer32"
_WfT1B8ZSSupport_Object = MibTableColumn
wfT1B8ZSSupport = _WfT1B8ZSSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 9),
    _WfT1B8ZSSupport_Type()
)
wfT1B8ZSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1B8ZSSupport.setStatus("mandatory")


class _WfT1ClockMode_Type(Integer32):
    """Custom type wfT1ClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("manual", 4),
          ("slave", 2))
    )


_WfT1ClockMode_Type.__name__ = "Integer32"
_WfT1ClockMode_Object = MibTableColumn
wfT1ClockMode = _WfT1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 10),
    _WfT1ClockMode_Type()
)
wfT1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1ClockMode.setStatus("mandatory")
_WfT1MiniDacs_Type = DisplayString
_WfT1MiniDacs_Object = MibTableColumn
wfT1MiniDacs = _WfT1MiniDacs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 11),
    _WfT1MiniDacs_Type()
)
wfT1MiniDacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfT1MiniDacs.setStatus("mandatory")
_WfT1BipolarVios_Type = Counter32
_WfT1BipolarVios_Object = MibTableColumn
wfT1BipolarVios = _WfT1BipolarVios_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 12),
    _WfT1BipolarVios_Type()
)
wfT1BipolarVios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1BipolarVios.setStatus("mandatory")
_WfT1FrameBitErrs_Type = Counter32
_WfT1FrameBitErrs_Object = MibTableColumn
wfT1FrameBitErrs = _WfT1FrameBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 13),
    _WfT1FrameBitErrs_Type()
)
wfT1FrameBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1FrameBitErrs.setStatus("mandatory")
_WfT1OutOfFrameErrs_Type = Counter32
_WfT1OutOfFrameErrs_Object = MibTableColumn
wfT1OutOfFrameErrs = _WfT1OutOfFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 14),
    _WfT1OutOfFrameErrs_Type()
)
wfT1OutOfFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1OutOfFrameErrs.setStatus("mandatory")
_WfT1SuperFrameErrs_Type = Counter32
_WfT1SuperFrameErrs_Object = MibTableColumn
wfT1SuperFrameErrs = _WfT1SuperFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 15),
    _WfT1SuperFrameErrs_Type()
)
wfT1SuperFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1SuperFrameErrs.setStatus("mandatory")
_WfT1RcvYelAlarms_Type = Counter32
_WfT1RcvYelAlarms_Object = MibTableColumn
wfT1RcvYelAlarms = _WfT1RcvYelAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 16),
    _WfT1RcvYelAlarms_Type()
)
wfT1RcvYelAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvYelAlarms.setStatus("mandatory")
_WfT1RcvCarrierLoss_Type = Counter32
_WfT1RcvCarrierLoss_Object = MibTableColumn
wfT1RcvCarrierLoss = _WfT1RcvCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 17),
    _WfT1RcvCarrierLoss_Type()
)
wfT1RcvCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvCarrierLoss.setStatus("mandatory")
_WfT1RcvRedAlarms_Type = Counter32
_WfT1RcvRedAlarms_Object = MibTableColumn
wfT1RcvRedAlarms = _WfT1RcvRedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 10, 1, 18),
    _WfT1RcvRedAlarms_Type()
)
wfT1RcvRedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfT1RcvRedAlarms.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-T1-MIB",
    **{"wfT1Table": wfT1Table,
       "wfT1Entry": wfT1Entry,
       "wfT1Delete": wfT1Delete,
       "wfT1Disable": wfT1Disable,
       "wfT1State": wfT1State,
       "wfT1Slot": wfT1Slot,
       "wfT1Connector": wfT1Connector,
       "wfT1Madr": wfT1Madr,
       "wfT1FrameType": wfT1FrameType,
       "wfT1LineBuildout": wfT1LineBuildout,
       "wfT1B8ZSSupport": wfT1B8ZSSupport,
       "wfT1ClockMode": wfT1ClockMode,
       "wfT1MiniDacs": wfT1MiniDacs,
       "wfT1BipolarVios": wfT1BipolarVios,
       "wfT1FrameBitErrs": wfT1FrameBitErrs,
       "wfT1OutOfFrameErrs": wfT1OutOfFrameErrs,
       "wfT1SuperFrameErrs": wfT1SuperFrameErrs,
       "wfT1RcvYelAlarms": wfT1RcvYelAlarms,
       "wfT1RcvCarrierLoss": wfT1RcvCarrierLoss,
       "wfT1RcvRedAlarms": wfT1RcvRedAlarms}
)
