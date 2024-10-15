# SNMP MIB module (Wellfleet-E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:10 2024
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

_WfE1Table_Object = MibTable
wfE1Table = _WfE1Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11)
)
if mibBuilder.loadTexts:
    wfE1Table.setStatus("mandatory")
_WfE1Entry_Object = MibTableRow
wfE1Entry = _WfE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1)
)
wfE1Entry.setIndexNames(
    (0, "Wellfleet-E1-MIB", "wfE1Slot"),
    (0, "Wellfleet-E1-MIB", "wfE1Connector"),
)
if mibBuilder.loadTexts:
    wfE1Entry.setStatus("mandatory")


class _WfE1Delete_Type(Integer32):
    """Custom type wfE1Delete based on Integer32"""
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


_WfE1Delete_Type.__name__ = "Integer32"
_WfE1Delete_Object = MibTableColumn
wfE1Delete = _WfE1Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 1),
    _WfE1Delete_Type()
)
wfE1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1Delete.setStatus("mandatory")


class _WfE1Disable_Type(Integer32):
    """Custom type wfE1Disable based on Integer32"""
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


_WfE1Disable_Type.__name__ = "Integer32"
_WfE1Disable_Object = MibTableColumn
wfE1Disable = _WfE1Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 2),
    _WfE1Disable_Type()
)
wfE1Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1Disable.setStatus("mandatory")


class _WfE1State_Type(Integer32):
    """Custom type wfE1State based on Integer32"""
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


_WfE1State_Type.__name__ = "Integer32"
_WfE1State_Object = MibTableColumn
wfE1State = _WfE1State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 3),
    _WfE1State_Type()
)
wfE1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1State.setStatus("mandatory")


class _WfE1Slot_Type(Integer32):
    """Custom type wfE1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfE1Slot_Type.__name__ = "Integer32"
_WfE1Slot_Object = MibTableColumn
wfE1Slot = _WfE1Slot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 4),
    _WfE1Slot_Type()
)
wfE1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Slot.setStatus("mandatory")


class _WfE1Connector_Type(Integer32):
    """Custom type wfE1Connector based on Integer32"""
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


_WfE1Connector_Type.__name__ = "Integer32"
_WfE1Connector_Object = MibTableColumn
wfE1Connector = _WfE1Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 5),
    _WfE1Connector_Type()
)
wfE1Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Connector.setStatus("mandatory")
_WfE1Madr_Type = OctetString
_WfE1Madr_Object = MibTableColumn
wfE1Madr = _WfE1Madr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 6),
    _WfE1Madr_Type()
)
wfE1Madr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1Madr.setStatus("mandatory")


class _WfE1HDB3Support_Type(Integer32):
    """Custom type wfE1HDB3Support based on Integer32"""
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


_WfE1HDB3Support_Type.__name__ = "Integer32"
_WfE1HDB3Support_Object = MibTableColumn
wfE1HDB3Support = _WfE1HDB3Support_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 7),
    _WfE1HDB3Support_Type()
)
wfE1HDB3Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1HDB3Support.setStatus("mandatory")


class _WfE1ClockMode_Type(Integer32):
    """Custom type wfE1ClockMode based on Integer32"""
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


_WfE1ClockMode_Type.__name__ = "Integer32"
_WfE1ClockMode_Object = MibTableColumn
wfE1ClockMode = _WfE1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 8),
    _WfE1ClockMode_Type()
)
wfE1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1ClockMode.setStatus("mandatory")
_WfE1MiniDacs_Type = DisplayString
_WfE1MiniDacs_Object = MibTableColumn
wfE1MiniDacs = _WfE1MiniDacs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 9),
    _WfE1MiniDacs_Type()
)
wfE1MiniDacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1MiniDacs.setStatus("mandatory")
_WfE1BipolarVios_Type = Counter32
_WfE1BipolarVios_Object = MibTableColumn
wfE1BipolarVios = _WfE1BipolarVios_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 10),
    _WfE1BipolarVios_Type()
)
wfE1BipolarVios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1BipolarVios.setStatus("mandatory")
_WfE1FrameErrs_Type = Counter32
_WfE1FrameErrs_Object = MibTableColumn
wfE1FrameErrs = _WfE1FrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 11),
    _WfE1FrameErrs_Type()
)
wfE1FrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1FrameErrs.setStatus("mandatory")
_WfE1RcvRemAlms_Type = Counter32
_WfE1RcvRemAlms_Object = MibTableColumn
wfE1RcvRemAlms = _WfE1RcvRemAlms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 12),
    _WfE1RcvRemAlms_Type()
)
wfE1RcvRemAlms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvRemAlms.setStatus("mandatory")
_WfE1RcvMfmAlms_Type = Counter32
_WfE1RcvMfmAlms_Object = MibTableColumn
wfE1RcvMfmAlms = _WfE1RcvMfmAlms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 13),
    _WfE1RcvMfmAlms_Type()
)
wfE1RcvMfmAlms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvMfmAlms.setStatus("mandatory")
_WfE1MfsErrs_Type = Counter32
_WfE1MfsErrs_Object = MibTableColumn
wfE1MfsErrs = _WfE1MfsErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 14),
    _WfE1MfsErrs_Type()
)
wfE1MfsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1MfsErrs.setStatus("mandatory")
_WfE1SyncLoss_Type = Counter32
_WfE1SyncLoss_Object = MibTableColumn
wfE1SyncLoss = _WfE1SyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 15),
    _WfE1SyncLoss_Type()
)
wfE1SyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1SyncLoss.setStatus("mandatory")
_WfE1RcvSig1s_Type = Counter32
_WfE1RcvSig1s_Object = MibTableColumn
wfE1RcvSig1s = _WfE1RcvSig1s_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 16),
    _WfE1RcvSig1s_Type()
)
wfE1RcvSig1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvSig1s.setStatus("mandatory")
_WfE1RcvUnfrm1s_Type = Counter32
_WfE1RcvUnfrm1s_Object = MibTableColumn
wfE1RcvUnfrm1s = _WfE1RcvUnfrm1s_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 17),
    _WfE1RcvUnfrm1s_Type()
)
wfE1RcvUnfrm1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1RcvUnfrm1s.setStatus("mandatory")


class _WfE1LineType_Type(Integer32):
    """Custom type wfE1LineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e1crc4", 2))
    )


_WfE1LineType_Type.__name__ = "Integer32"
_WfE1LineType_Object = MibTableColumn
wfE1LineType = _WfE1LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 18),
    _WfE1LineType_Type()
)
wfE1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfE1LineType.setStatus("mandatory")
_WfE1CRC4Errors_Type = Counter32
_WfE1CRC4Errors_Object = MibTableColumn
wfE1CRC4Errors = _WfE1CRC4Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 11, 1, 19),
    _WfE1CRC4Errors_Type()
)
wfE1CRC4Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfE1CRC4Errors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-E1-MIB",
    **{"wfE1Table": wfE1Table,
       "wfE1Entry": wfE1Entry,
       "wfE1Delete": wfE1Delete,
       "wfE1Disable": wfE1Disable,
       "wfE1State": wfE1State,
       "wfE1Slot": wfE1Slot,
       "wfE1Connector": wfE1Connector,
       "wfE1Madr": wfE1Madr,
       "wfE1HDB3Support": wfE1HDB3Support,
       "wfE1ClockMode": wfE1ClockMode,
       "wfE1MiniDacs": wfE1MiniDacs,
       "wfE1BipolarVios": wfE1BipolarVios,
       "wfE1FrameErrs": wfE1FrameErrs,
       "wfE1RcvRemAlms": wfE1RcvRemAlms,
       "wfE1RcvMfmAlms": wfE1RcvMfmAlms,
       "wfE1MfsErrs": wfE1MfsErrs,
       "wfE1SyncLoss": wfE1SyncLoss,
       "wfE1RcvSig1s": wfE1RcvSig1s,
       "wfE1RcvUnfrm1s": wfE1RcvUnfrm1s,
       "wfE1LineType": wfE1LineType,
       "wfE1CRC4Errors": wfE1CRC4Errors}
)
