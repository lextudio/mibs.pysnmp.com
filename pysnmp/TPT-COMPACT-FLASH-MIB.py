# SNMP MIB module (TPT-COMPACT-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-COMPACT-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:54 2024
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

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_compact_flash = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14)
)
tpt_compact_flash.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MountedOrNot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mounted", 0),
          ("unmounted", 1))
    )



class OperationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-mount", 1),
          ("secure", 0))
    )



class FormattedOrNot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("formatted", 0),
          ("unformatted", 1))
    )



class PresentOrNot(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CompactFlashPresent_Type = PresentOrNot
_CompactFlashPresent_Object = MibScalar
compactFlashPresent = _CompactFlashPresent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 1),
    _CompactFlashPresent_Type()
)
compactFlashPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compactFlashPresent.setStatus("current")
_CompactFlashMounted_Type = MountedOrNot
_CompactFlashMounted_Object = MibScalar
compactFlashMounted = _CompactFlashMounted_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 2),
    _CompactFlashMounted_Type()
)
compactFlashMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compactFlashMounted.setStatus("current")
_CompactFlashFormatted_Type = FormattedOrNot
_CompactFlashFormatted_Object = MibScalar
compactFlashFormatted = _CompactFlashFormatted_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 3),
    _CompactFlashFormatted_Type()
)
compactFlashFormatted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compactFlashFormatted.setStatus("current")
_CompactFlashOperationMode_Type = OperationMode
_CompactFlashOperationMode_Object = MibScalar
compactFlashOperationMode = _CompactFlashOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 4),
    _CompactFlashOperationMode_Type()
)
compactFlashOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compactFlashOperationMode.setStatus("current")
_VendorInformation_ObjectIdentity = ObjectIdentity
vendorInformation = _VendorInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5)
)
if mibBuilder.loadTexts:
    vendorInformation.setStatus("current")


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _Model_Type(OctetString):
    """Custom type model based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Model_Type.__name__ = "OctetString"
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 2),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_Capacity_Type = Unsigned32
_Capacity_Object = MibScalar
capacity = _Capacity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 3),
    _Capacity_Type()
)
capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacity.setStatus("current")


class _Revision_Type(OctetString):
    """Custom type revision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Revision_Type.__name__ = "OctetString"
_Revision_Object = MibScalar
revision = _Revision_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 14, 5, 4),
    _Revision_Type()
)
revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revision.setStatus("current")


class _TptCompactFlashDeviceID_Type(OctetString):
    """Custom type tptCompactFlashDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptCompactFlashDeviceID_Type.__name__ = "OctetString"
_TptCompactFlashDeviceID_Object = MibScalar
tptCompactFlashDeviceID = _TptCompactFlashDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 261),
    _TptCompactFlashDeviceID_Type()
)
tptCompactFlashDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptCompactFlashDeviceID.setStatus("current")
_TptCompactFlashDeviceStatus_Type = PresentOrNot
_TptCompactFlashDeviceStatus_Object = MibScalar
tptCompactFlashDeviceStatus = _TptCompactFlashDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 262),
    _TptCompactFlashDeviceStatus_Type()
)
tptCompactFlashDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptCompactFlashDeviceStatus.setStatus("current")

# Managed Objects groups


# Notification objects

tptCFInsertedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 51)
)
tptCFInsertedNotify.setObjects(
      *(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"),
        ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
)
if mibBuilder.loadTexts:
    tptCFInsertedNotify.setStatus(
        "current"
    )

tptCFEjectedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 52)
)
tptCFEjectedNotify.setObjects(
      *(("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceID"),
        ("TPT-COMPACT-FLASH-MIB", "tptCompactFlashDeviceStatus"))
)
if mibBuilder.loadTexts:
    tptCFEjectedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-COMPACT-FLASH-MIB",
    **{"MountedOrNot": MountedOrNot,
       "OperationMode": OperationMode,
       "FormattedOrNot": FormattedOrNot,
       "PresentOrNot": PresentOrNot,
       "tpt-compact-flash": tpt_compact_flash,
       "compactFlashPresent": compactFlashPresent,
       "compactFlashMounted": compactFlashMounted,
       "compactFlashFormatted": compactFlashFormatted,
       "compactFlashOperationMode": compactFlashOperationMode,
       "vendorInformation": vendorInformation,
       "serialNumber": serialNumber,
       "model": model,
       "capacity": capacity,
       "revision": revision,
       "tptCFInsertedNotify": tptCFInsertedNotify,
       "tptCFEjectedNotify": tptCFEjectedNotify,
       "tptCompactFlashDeviceID": tptCompactFlashDeviceID,
       "tptCompactFlashDeviceStatus": tptCompactFlashDeviceStatus}
)
