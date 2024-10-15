# SNMP MIB module (AISYSCFGSOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFGSOFTWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:25 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiSysCfgSoftware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 1)
)
aiSysCfgSoftware.setRevisions(
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


class _AiSCSoftwareActive_Type(Integer32):
    """Custom type aiSCSoftwareActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCSoftwareActive_Type.__name__ = "Integer32"
_AiSCSoftwareActive_Object = MibScalar
aiSCSoftwareActive = _AiSCSoftwareActive_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 1),
    _AiSCSoftwareActive_Type()
)
aiSCSoftwareActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareActive.setStatus("current")


class _AiSCSoftwareUpdateName_Type(DisplayString):
    """Custom type aiSCSoftwareUpdateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCSoftwareUpdateName_Type.__name__ = "DisplayString"
_AiSCSoftwareUpdateName_Object = MibScalar
aiSCSoftwareUpdateName = _AiSCSoftwareUpdateName_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 2),
    _AiSCSoftwareUpdateName_Type()
)
aiSCSoftwareUpdateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCSoftwareUpdateName.setStatus("current")


class _AiSCSoftwareUpdateStatus_Type(Integer32):
    """Custom type aiSCSoftwareUpdateStatus based on Integer32"""
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
        *(("error", 4),
          ("inProgress", 2),
          ("ok", 3),
          ("ready", 1))
    )


_AiSCSoftwareUpdateStatus_Type.__name__ = "Integer32"
_AiSCSoftwareUpdateStatus_Object = MibScalar
aiSCSoftwareUpdateStatus = _AiSCSoftwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 3),
    _AiSCSoftwareUpdateStatus_Type()
)
aiSCSoftwareUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCSoftwareUpdateStatus.setStatus("current")
_AiSCSoftwareTable_Object = MibTable
aiSCSoftwareTable = _AiSCSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4)
)
if mibBuilder.loadTexts:
    aiSCSoftwareTable.setStatus("current")
_AiSCSoftwareEntry_Object = MibTableRow
aiSCSoftwareEntry = _AiSCSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1)
)
aiSCSoftwareEntry.setIndexNames(
    (0, "AISYSCFGSOFTWARE-MIB", "aiSCSoftwareIndex"),
)
if mibBuilder.loadTexts:
    aiSCSoftwareEntry.setStatus("current")


class _AiSCSoftwareIndex_Type(Integer32):
    """Custom type aiSCSoftwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCSoftwareIndex_Type.__name__ = "Integer32"
_AiSCSoftwareIndex_Object = MibTableColumn
aiSCSoftwareIndex = _AiSCSoftwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 1),
    _AiSCSoftwareIndex_Type()
)
aiSCSoftwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareIndex.setStatus("current")


class _AiSCSoftwareName_Type(DisplayString):
    """Custom type aiSCSoftwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCSoftwareName_Type.__name__ = "DisplayString"
_AiSCSoftwareName_Object = MibTableColumn
aiSCSoftwareName = _AiSCSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 2),
    _AiSCSoftwareName_Type()
)
aiSCSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareName.setStatus("current")


class _AiSCSoftwareDescr_Type(DisplayString):
    """Custom type aiSCSoftwareDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCSoftwareDescr_Type.__name__ = "DisplayString"
_AiSCSoftwareDescr_Object = MibTableColumn
aiSCSoftwareDescr = _AiSCSoftwareDescr_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 3),
    _AiSCSoftwareDescr_Type()
)
aiSCSoftwareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareDescr.setStatus("current")


class _AiSCSoftwareType_Type(Integer32):
    """Custom type aiSCSoftwareType based on Integer32"""
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
        *(("bootloader", 1),
          ("firmware", 2),
          ("module", 3),
          ("other", 4))
    )


_AiSCSoftwareType_Type.__name__ = "Integer32"
_AiSCSoftwareType_Object = MibTableColumn
aiSCSoftwareType = _AiSCSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 4),
    _AiSCSoftwareType_Type()
)
aiSCSoftwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareType.setStatus("current")


class _AiSCSoftwareVersion_Type(DisplayString):
    """Custom type aiSCSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AiSCSoftwareVersion_Type.__name__ = "DisplayString"
_AiSCSoftwareVersion_Object = MibTableColumn
aiSCSoftwareVersion = _AiSCSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 5),
    _AiSCSoftwareVersion_Type()
)
aiSCSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareVersion.setStatus("current")
_AiSCSoftwareCreationTime_Type = DateAndTime
_AiSCSoftwareCreationTime_Object = MibTableColumn
aiSCSoftwareCreationTime = _AiSCSoftwareCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 1, 4, 1, 6),
    _AiSCSoftwareCreationTime_Type()
)
aiSCSoftwareCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCSoftwareCreationTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFGSOFTWARE-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgSoftware": aiSysCfgSoftware,
       "aiSCSoftwareActive": aiSCSoftwareActive,
       "aiSCSoftwareUpdateName": aiSCSoftwareUpdateName,
       "aiSCSoftwareUpdateStatus": aiSCSoftwareUpdateStatus,
       "aiSCSoftwareTable": aiSCSoftwareTable,
       "aiSCSoftwareEntry": aiSCSoftwareEntry,
       "aiSCSoftwareIndex": aiSCSoftwareIndex,
       "aiSCSoftwareName": aiSCSoftwareName,
       "aiSCSoftwareDescr": aiSCSoftwareDescr,
       "aiSCSoftwareType": aiSCSoftwareType,
       "aiSCSoftwareVersion": aiSCSoftwareVersion,
       "aiSCSoftwareCreationTime": aiSCSoftwareCreationTime}
)
