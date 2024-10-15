# SNMP MIB module (NOKIA-IPSO-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-IPSO-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:41 2024
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

(hrFSMountPoint,
 hrPartitionIndex,
 hrPartitionLabel,
 hrPartitionSize) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrFSMountPoint",
    "hrPartitionIndex",
    "hrPartitionLabel",
    "hrPartitionSize")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ipsoSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1)
)
ipsoSystem.setRevisions(
        ("1999-10-20 00:00",
         "1900-01-11 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_IpsoProducts_ObjectIdentity = ObjectIdentity
ipsoProducts = _IpsoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21)
)
_IpsoChassisSerialNumber_Type = DisplayString
_IpsoChassisSerialNumber_Object = MibScalar
ipsoChassisSerialNumber = _IpsoChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 1),
    _IpsoChassisSerialNumber_Type()
)
ipsoChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoChassisSerialNumber.setStatus("current")
_IpsoChassisMBType_Type = DisplayString
_IpsoChassisMBType_Object = MibScalar
ipsoChassisMBType = _IpsoChassisMBType_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 2),
    _IpsoChassisMBType_Type()
)
ipsoChassisMBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoChassisMBType.setStatus("current")
_IpsoChassisMBRevNumber_Type = DisplayString
_IpsoChassisMBRevNumber_Object = MibScalar
ipsoChassisMBRevNumber = _IpsoChassisMBRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 3),
    _IpsoChassisMBRevNumber_Type()
)
ipsoChassisMBRevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoChassisMBRevNumber.setStatus("current")
_IpsoChassisMBSerialNumber_Type = DisplayString
_IpsoChassisMBSerialNumber_Object = MibScalar
ipsoChassisMBSerialNumber = _IpsoChassisMBSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 4),
    _IpsoChassisMBSerialNumber_Type()
)
ipsoChassisMBSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoChassisMBSerialNumber.setStatus("current")


class _IpsoChassisTemperature_Type(Integer32):
    """Custom type ipsoChassisTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overTemperature", 2))
    )


_IpsoChassisTemperature_Type.__name__ = "Integer32"
_IpsoChassisTemperature_Object = MibScalar
ipsoChassisTemperature = _IpsoChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 5),
    _IpsoChassisTemperature_Type()
)
ipsoChassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoChassisTemperature.setStatus("current")
_IpsoCardTable_Object = MibTable
ipsoCardTable = _IpsoCardTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipsoCardTable.setStatus("current")
_IpsoCardEntry_Object = MibTableRow
ipsoCardEntry = _IpsoCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 6, 1)
)
ipsoCardEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoCardIndex"),
)
if mibBuilder.loadTexts:
    ipsoCardEntry.setStatus("current")


class _IpsoCardIndex_Type(Integer32):
    """Custom type ipsoCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoCardIndex_Type.__name__ = "Integer32"
_IpsoCardIndex_Object = MibTableColumn
ipsoCardIndex = _IpsoCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 6, 1, 1),
    _IpsoCardIndex_Type()
)
ipsoCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoCardIndex.setStatus("current")


class _IpsoCardOperStatus_Type(Integer32):
    """Custom type ipsoCardOperStatus based on Integer32"""
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


_IpsoCardOperStatus_Type.__name__ = "Integer32"
_IpsoCardOperStatus_Object = MibTableColumn
ipsoCardOperStatus = _IpsoCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1, 6, 1, 2),
    _IpsoCardOperStatus_Type()
)
ipsoCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoCardOperStatus.setStatus("current")
_IpsoFanTable_Object = MibTable
ipsoFanTable = _IpsoFanTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipsoFanTable.setStatus("current")
_IpsoFanEntry_Object = MibTableRow
ipsoFanEntry = _IpsoFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 2, 1, 1)
)
ipsoFanEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoFanIndex"),
)
if mibBuilder.loadTexts:
    ipsoFanEntry.setStatus("current")
_IpsoFanIndex_Type = Integer32
_IpsoFanIndex_Object = MibTableColumn
ipsoFanIndex = _IpsoFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 2, 1, 1, 1),
    _IpsoFanIndex_Type()
)
ipsoFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoFanIndex.setStatus("current")


class _IpsoFanOperStatus_Type(Integer32):
    """Custom type ipsoFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_IpsoFanOperStatus_Type.__name__ = "Integer32"
_IpsoFanOperStatus_Object = MibTableColumn
ipsoFanOperStatus = _IpsoFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 2, 1, 1, 2),
    _IpsoFanOperStatus_Type()
)
ipsoFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoFanOperStatus.setStatus("current")
_IpsoPowerSupplyTable_Object = MibTable
ipsoPowerSupplyTable = _IpsoPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipsoPowerSupplyTable.setStatus("current")
_IpsoPowerSupplyEntry_Object = MibTableRow
ipsoPowerSupplyEntry = _IpsoPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3, 1, 1)
)
ipsoPowerSupplyEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ipsoPowerSupplyEntry.setStatus("current")


class _IpsoPowerSupplyIndex_Type(Integer32):
    """Custom type ipsoPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoPowerSupplyIndex_Type.__name__ = "Integer32"
_IpsoPowerSupplyIndex_Object = MibTableColumn
ipsoPowerSupplyIndex = _IpsoPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3, 1, 1, 1),
    _IpsoPowerSupplyIndex_Type()
)
ipsoPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPowerSupplyIndex.setStatus("current")


class _IpsoPowerSupplyOverTemperature_Type(Integer32):
    """Custom type ipsoPowerSupplyOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overTemperature", 2))
    )


_IpsoPowerSupplyOverTemperature_Type.__name__ = "Integer32"
_IpsoPowerSupplyOverTemperature_Object = MibTableColumn
ipsoPowerSupplyOverTemperature = _IpsoPowerSupplyOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3, 1, 1, 2),
    _IpsoPowerSupplyOverTemperature_Type()
)
ipsoPowerSupplyOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPowerSupplyOverTemperature.setStatus("current")


class _IpsoPowerSupplyOperStatus_Type(Integer32):
    """Custom type ipsoPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_IpsoPowerSupplyOperStatus_Type.__name__ = "Integer32"
_IpsoPowerSupplyOperStatus_Object = MibTableColumn
ipsoPowerSupplyOperStatus = _IpsoPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3, 1, 1, 3),
    _IpsoPowerSupplyOperStatus_Type()
)
ipsoPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPowerSupplyOperStatus.setStatus("current")
_IpsoConfigTable_Object = MibTable
ipsoConfigTable = _IpsoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipsoConfigTable.setStatus("current")
_IpsoConfigEntry_Object = MibTableRow
ipsoConfigEntry = _IpsoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 1, 1)
)
ipsoConfigEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigIndex"),
)
if mibBuilder.loadTexts:
    ipsoConfigEntry.setStatus("current")


class _IpsoConfigIndex_Type(Integer32):
    """Custom type ipsoConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoConfigIndex_Type.__name__ = "Integer32"
_IpsoConfigIndex_Object = MibTableColumn
ipsoConfigIndex = _IpsoConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 1, 1, 1),
    _IpsoConfigIndex_Type()
)
ipsoConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoConfigIndex.setStatus("current")
_IpsoConfigFilePath_Type = DisplayString
_IpsoConfigFilePath_Object = MibTableColumn
ipsoConfigFilePath = _IpsoConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 1, 1, 2),
    _IpsoConfigFilePath_Type()
)
ipsoConfigFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoConfigFilePath.setStatus("current")
_IpsoConfigFileDateAndTime_Type = DateAndTime
_IpsoConfigFileDateAndTime_Object = MibTableColumn
ipsoConfigFileDateAndTime = _IpsoConfigFileDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 1, 1, 3),
    _IpsoConfigFileDateAndTime_Type()
)
ipsoConfigFileDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoConfigFileDateAndTime.setStatus("current")


class _IpsoConfigLogSize_Type(Integer32):
    """Custom type ipsoConfigLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsoConfigLogSize_Type.__name__ = "Integer32"
_IpsoConfigLogSize_Object = MibScalar
ipsoConfigLogSize = _IpsoConfigLogSize_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 2),
    _IpsoConfigLogSize_Type()
)
ipsoConfigLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsoConfigLogSize.setStatus("current")
_IpsoConfigLogTable_Object = MibTable
ipsoConfigLogTable = _IpsoConfigLogTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ipsoConfigLogTable.setStatus("current")
_IpsoConfigLogEntry_Object = MibTableRow
ipsoConfigLogEntry = _IpsoConfigLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 3, 1)
)
ipsoConfigLogEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigLogIndex"),
)
if mibBuilder.loadTexts:
    ipsoConfigLogEntry.setStatus("current")


class _IpsoConfigLogIndex_Type(Integer32):
    """Custom type ipsoConfigLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpsoConfigLogIndex_Type.__name__ = "Integer32"
_IpsoConfigLogIndex_Object = MibTableColumn
ipsoConfigLogIndex = _IpsoConfigLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 3, 1, 1),
    _IpsoConfigLogIndex_Type()
)
ipsoConfigLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoConfigLogIndex.setStatus("current")
_IpsoConfigLogDescr_Type = DisplayString
_IpsoConfigLogDescr_Object = MibTableColumn
ipsoConfigLogDescr = _IpsoConfigLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4, 3, 1, 2),
    _IpsoConfigLogDescr_Type()
)
ipsoConfigLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoConfigLogDescr.setStatus("current")
_IpsoImageTable_Object = MibTable
ipsoImageTable = _IpsoImageTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipsoImageTable.setStatus("current")
_IpsoImageEntry_Object = MibTableRow
ipsoImageEntry = _IpsoImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1, 1)
)
ipsoImageEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoImageIndex"),
)
if mibBuilder.loadTexts:
    ipsoImageEntry.setStatus("current")


class _IpsoImageIndex_Type(Integer32):
    """Custom type ipsoImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoImageIndex_Type.__name__ = "Integer32"
_IpsoImageIndex_Object = MibTableColumn
ipsoImageIndex = _IpsoImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1, 1, 1),
    _IpsoImageIndex_Type()
)
ipsoImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoImageIndex.setStatus("current")
_IpsoImageVersionNumber_Type = DisplayString
_IpsoImageVersionNumber_Object = MibTableColumn
ipsoImageVersionNumber = _IpsoImageVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1, 1, 2),
    _IpsoImageVersionNumber_Type()
)
ipsoImageVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoImageVersionNumber.setStatus("current")
_IpsoImageSerialNumber_Type = DisplayString
_IpsoImageSerialNumber_Object = MibTableColumn
ipsoImageSerialNumber = _IpsoImageSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1, 1, 3),
    _IpsoImageSerialNumber_Type()
)
ipsoImageSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoImageSerialNumber.setStatus("current")
_IpsoImageTimeOfLoad_Type = DateAndTime
_IpsoImageTimeOfLoad_Object = MibTableColumn
ipsoImageTimeOfLoad = _IpsoImageTimeOfLoad_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5, 1, 1, 4),
    _IpsoImageTimeOfLoad_Type()
)
ipsoImageTimeOfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoImageTimeOfLoad.setStatus("current")


class _IpsoSIMMTotal_Type(Integer32):
    """Custom type ipsoSIMMTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoSIMMTotal_Type.__name__ = "Integer32"
_IpsoSIMMTotal_Object = MibScalar
ipsoSIMMTotal = _IpsoSIMMTotal_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 6, 1),
    _IpsoSIMMTotal_Type()
)
ipsoSIMMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoSIMMTotal.setStatus("current")
_IpsoProcessorUtilization_Type = Gauge32
_IpsoProcessorUtilization_Object = MibScalar
ipsoProcessorUtilization = _IpsoProcessorUtilization_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 1),
    _IpsoProcessorUtilization_Type()
)
ipsoProcessorUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessorUtilization.setStatus("current")
_IpsoProcessTable_Object = MibTable
ipsoProcessTable = _IpsoProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipsoProcessTable.setStatus("current")
_IpsoProcessEntry_Object = MibTableRow
ipsoProcessEntry = _IpsoProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1)
)
ipsoProcessEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessID"),
)
if mibBuilder.loadTexts:
    ipsoProcessEntry.setStatus("current")


class _IpsoProcessID_Type(Integer32):
    """Custom type ipsoProcessID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoProcessID_Type.__name__ = "Integer32"
_IpsoProcessID_Object = MibTableColumn
ipsoProcessID = _IpsoProcessID_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1, 1),
    _IpsoProcessID_Type()
)
ipsoProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessID.setStatus("current")


class _IpsoProcessParentID_Type(Integer32):
    """Custom type ipsoProcessParentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoProcessParentID_Type.__name__ = "Integer32"
_IpsoProcessParentID_Object = MibTableColumn
ipsoProcessParentID = _IpsoProcessParentID_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1, 2),
    _IpsoProcessParentID_Type()
)
ipsoProcessParentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessParentID.setStatus("current")
_IpsoProcessOwner_Type = DisplayString
_IpsoProcessOwner_Object = MibTableColumn
ipsoProcessOwner = _IpsoProcessOwner_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1, 3),
    _IpsoProcessOwner_Type()
)
ipsoProcessOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessOwner.setStatus("current")


class _IpsoProcessMemory_Type(Integer32):
    """Custom type ipsoProcessMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoProcessMemory_Type.__name__ = "Integer32"
_IpsoProcessMemory_Object = MibTableColumn
ipsoProcessMemory = _IpsoProcessMemory_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1, 4),
    _IpsoProcessMemory_Type()
)
ipsoProcessMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessMemory.setStatus("current")


class _IpsoProcessPercentCPU_Type(Integer32):
    """Custom type ipsoProcessPercentCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpsoProcessPercentCPU_Type.__name__ = "Integer32"
_IpsoProcessPercentCPU_Object = MibTableColumn
ipsoProcessPercentCPU = _IpsoProcessPercentCPU_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7, 2, 1, 5),
    _IpsoProcessPercentCPU_Type()
)
ipsoProcessPercentCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProcessPercentCPU.setStatus("current")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1)
)


class _IpsoTotalDiskMirrorSets_Type(Integer32):
    """Custom type ipsoTotalDiskMirrorSets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoTotalDiskMirrorSets_Type.__name__ = "Integer32"
_IpsoTotalDiskMirrorSets_Object = MibScalar
ipsoTotalDiskMirrorSets = _IpsoTotalDiskMirrorSets_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 1),
    _IpsoTotalDiskMirrorSets_Type()
)
ipsoTotalDiskMirrorSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoTotalDiskMirrorSets.setStatus("current")
_IpsoDiskMirrorSetTable_Object = MibTable
ipsoDiskMirrorSetTable = _IpsoDiskMirrorSetTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetTable.setStatus("current")
_IpsoDiskMirrorSetEntry_Object = MibTableRow
ipsoDiskMirrorSetEntry = _IpsoDiskMirrorSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2, 1)
)
ipsoDiskMirrorSetEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetIndex"),
)
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetEntry.setStatus("current")


class _IpsoDiskMirrorSetIndex_Type(Integer32):
    """Custom type ipsoDiskMirrorSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoDiskMirrorSetIndex_Type.__name__ = "Integer32"
_IpsoDiskMirrorSetIndex_Object = MibTableColumn
ipsoDiskMirrorSetIndex = _IpsoDiskMirrorSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2, 1, 1),
    _IpsoDiskMirrorSetIndex_Type()
)
ipsoDiskMirrorSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetIndex.setStatus("current")
_IpsoDiskMirrorSetSourceDriveIndex_Type = Integer32
_IpsoDiskMirrorSetSourceDriveIndex_Object = MibTableColumn
ipsoDiskMirrorSetSourceDriveIndex = _IpsoDiskMirrorSetSourceDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2, 1, 2),
    _IpsoDiskMirrorSetSourceDriveIndex_Type()
)
ipsoDiskMirrorSetSourceDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetSourceDriveIndex.setStatus("current")
_IpsoDiskMirrorSetDestinationDriveIndex_Type = Integer32
_IpsoDiskMirrorSetDestinationDriveIndex_Object = MibTableColumn
ipsoDiskMirrorSetDestinationDriveIndex = _IpsoDiskMirrorSetDestinationDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2, 1, 3),
    _IpsoDiskMirrorSetDestinationDriveIndex_Type()
)
ipsoDiskMirrorSetDestinationDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetDestinationDriveIndex.setStatus("current")
_IpsoDiskMirrorSetSyncPercent_Type = DisplayString
_IpsoDiskMirrorSetSyncPercent_Object = MibTableColumn
ipsoDiskMirrorSetSyncPercent = _IpsoDiskMirrorSetSyncPercent_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9, 2, 1, 4),
    _IpsoDiskMirrorSetSyncPercent_Type()
)
ipsoDiskMirrorSetSyncPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskMirrorSetSyncPercent.setStatus("current")
_IpsoAssetChassisSerialNumber_Type = DisplayString
_IpsoAssetChassisSerialNumber_Object = MibScalar
ipsoAssetChassisSerialNumber = _IpsoAssetChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 1),
    _IpsoAssetChassisSerialNumber_Type()
)
ipsoAssetChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoAssetChassisSerialNumber.setStatus("current")
_IpsoCPUModel_Type = DisplayString
_IpsoCPUModel_Object = MibScalar
ipsoCPUModel = _IpsoCPUModel_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 2),
    _IpsoCPUModel_Type()
)
ipsoCPUModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoCPUModel.setStatus("current")
_IpsoCPUMfr_Type = DisplayString
_IpsoCPUMfr_Object = MibScalar
ipsoCPUMfr = _IpsoCPUMfr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 3),
    _IpsoCPUMfr_Type()
)
ipsoCPUMfr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoCPUMfr.setStatus("current")
_IpsoCPUFreq_Type = Integer32
_IpsoCPUFreq_Object = MibScalar
ipsoCPUFreq = _IpsoCPUFreq_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 4),
    _IpsoCPUFreq_Type()
)
ipsoCPUFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoCPUFreq.setStatus("current")
_IpsoKernMaxMem_Type = Integer32
_IpsoKernMaxMem_Object = MibScalar
ipsoKernMaxMem = _IpsoKernMaxMem_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 5),
    _IpsoKernMaxMem_Type()
)
ipsoKernMaxMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoKernMaxMem.setStatus("current")
_IpsoMotherBoardSerNum_Type = DisplayString
_IpsoMotherBoardSerNum_Object = MibScalar
ipsoMotherBoardSerNum = _IpsoMotherBoardSerNum_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 6),
    _IpsoMotherBoardSerNum_Type()
)
ipsoMotherBoardSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoMotherBoardSerNum.setStatus("current")
_IpsoMotherBoardRev_Type = DisplayString
_IpsoMotherBoardRev_Object = MibScalar
ipsoMotherBoardRev = _IpsoMotherBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 7),
    _IpsoMotherBoardRev_Type()
)
ipsoMotherBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoMotherBoardRev.setStatus("current")
_IpsoMotherBoardModel_Type = DisplayString
_IpsoMotherBoardModel_Object = MibScalar
ipsoMotherBoardModel = _IpsoMotherBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 8),
    _IpsoMotherBoardModel_Type()
)
ipsoMotherBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoMotherBoardModel.setStatus("current")
_IpsoOSRelease_Type = DisplayString
_IpsoOSRelease_Object = MibScalar
ipsoOSRelease = _IpsoOSRelease_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 9),
    _IpsoOSRelease_Type()
)
ipsoOSRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoOSRelease.setStatus("current")
_IpsoOSVersion_Type = DisplayString
_IpsoOSVersion_Object = MibScalar
ipsoOSVersion = _IpsoOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 10),
    _IpsoOSVersion_Type()
)
ipsoOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoOSVersion.setStatus("current")
_IpsoProductModel_Type = DisplayString
_IpsoProductModel_Object = MibScalar
ipsoProductModel = _IpsoProductModel_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 11),
    _IpsoProductModel_Type()
)
ipsoProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoProductModel.setStatus("current")
_IpsoAssetTable_Object = MibTable
ipsoAssetTable = _IpsoAssetTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12)
)
if mibBuilder.loadTexts:
    ipsoAssetTable.setStatus("current")
_IpsoAssetEntry_Object = MibTableRow
ipsoAssetEntry = _IpsoAssetEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1)
)
ipsoAssetEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgIndex"),
)
if mibBuilder.loadTexts:
    ipsoAssetEntry.setStatus("current")
_IpsoPkgIndex_Type = Integer32
_IpsoPkgIndex_Object = MibTableColumn
ipsoPkgIndex = _IpsoPkgIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1, 1),
    _IpsoPkgIndex_Type()
)
ipsoPkgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPkgIndex.setStatus("current")
_IpsoPkgName_Type = DisplayString
_IpsoPkgName_Object = MibTableColumn
ipsoPkgName = _IpsoPkgName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1, 2),
    _IpsoPkgName_Type()
)
ipsoPkgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPkgName.setStatus("current")
_IpsoPkgMajorVersion_Type = DisplayString
_IpsoPkgMajorVersion_Object = MibTableColumn
ipsoPkgMajorVersion = _IpsoPkgMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1, 3),
    _IpsoPkgMajorVersion_Type()
)
ipsoPkgMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPkgMajorVersion.setStatus("current")
_IpsoPkgMinorVersion_Type = DisplayString
_IpsoPkgMinorVersion_Object = MibTableColumn
ipsoPkgMinorVersion = _IpsoPkgMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1, 4),
    _IpsoPkgMinorVersion_Type()
)
ipsoPkgMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPkgMinorVersion.setStatus("current")
_IpsoPkgLicense_Type = DisplayString
_IpsoPkgLicense_Object = MibTableColumn
ipsoPkgLicense = _IpsoPkgLicense_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 12, 1, 5),
    _IpsoPkgLicense_Type()
)
ipsoPkgLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoPkgLicense.setStatus("current")
_IpsoDiskDriveTable_Object = MibTable
ipsoDiskDriveTable = _IpsoDiskDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13)
)
if mibBuilder.loadTexts:
    ipsoDiskDriveTable.setStatus("current")
_IpsoDiskDriveEntry_Object = MibTableRow
ipsoDiskDriveEntry = _IpsoDiskDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1)
)
ipsoDiskDriveEntry.setIndexNames(
    (0, "NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveIndex"),
)
if mibBuilder.loadTexts:
    ipsoDiskDriveEntry.setStatus("current")


class _IpsoDiskDriveIndex_Type(Integer32):
    """Custom type ipsoDiskDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoDiskDriveIndex_Type.__name__ = "Integer32"
_IpsoDiskDriveIndex_Object = MibTableColumn
ipsoDiskDriveIndex = _IpsoDiskDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1, 1),
    _IpsoDiskDriveIndex_Type()
)
ipsoDiskDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskDriveIndex.setStatus("current")


class _IpsoSysDiskDriveIndex_Type(Integer32):
    """Custom type ipsoSysDiskDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsoSysDiskDriveIndex_Type.__name__ = "Integer32"
_IpsoSysDiskDriveIndex_Object = MibScalar
ipsoSysDiskDriveIndex = _IpsoSysDiskDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1, 2),
    _IpsoSysDiskDriveIndex_Type()
)
ipsoSysDiskDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoSysDiskDriveIndex.setStatus("current")
_IpsoDiskDriveModel_Type = DisplayString
_IpsoDiskDriveModel_Object = MibTableColumn
ipsoDiskDriveModel = _IpsoDiskDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1, 3),
    _IpsoDiskDriveModel_Type()
)
ipsoDiskDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskDriveModel.setStatus("current")
_IpsoDiskDriveCapacity_Type = DisplayString
_IpsoDiskDriveCapacity_Object = MibTableColumn
ipsoDiskDriveCapacity = _IpsoDiskDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1, 4),
    _IpsoDiskDriveCapacity_Type()
)
ipsoDiskDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskDriveCapacity.setStatus("current")
_IpsoDiskDriveLocation_Type = DisplayString
_IpsoDiskDriveLocation_Object = MibTableColumn
ipsoDiskDriveLocation = _IpsoDiskDriveLocation_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10, 13, 1, 5),
    _IpsoDiskDriveLocation_Type()
)
ipsoDiskDriveLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDiskDriveLocation.setStatus("current")
_IpsoFeatureName_Type = DisplayString
_IpsoFeatureName_Object = MibScalar
ipsoFeatureName = _IpsoFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 11, 1),
    _IpsoFeatureName_Type()
)
ipsoFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoFeatureName.setStatus("current")
_IpsoDaysToExpire_Type = Integer32
_IpsoDaysToExpire_Object = MibScalar
ipsoDaysToExpire = _IpsoDaysToExpire_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 11, 2),
    _IpsoDaysToExpire_Type()
)
ipsoDaysToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsoDaysToExpire.setStatus("current")

# Managed Objects groups

ipsoChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 1)
)
ipsoChassisGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoChassisSerialNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoChassisMBType"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoChassisMBRevNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoChassisMBSerialNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoChassisTemperature"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoCardIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoCardOperStatus"))
)
if mibBuilder.loadTexts:
    ipsoChassisGroup.setStatus("current")

ipsoFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 2)
)
ipsoFanGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoFanIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoFanOperStatus"))
)
if mibBuilder.loadTexts:
    ipsoFanGroup.setStatus("current")

ipsoPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 3)
)
ipsoPowerSupplyGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoPowerSupplyIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPowerSupplyOverTemperature"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPowerSupplyOperStatus"))
)
if mibBuilder.loadTexts:
    ipsoPowerSupplyGroup.setStatus("current")

ipsoConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 4)
)
ipsoConfigGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigFilePath"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigFileDateAndTime"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigLogSize"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigLogIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigLogDescr"))
)
if mibBuilder.loadTexts:
    ipsoConfigGroup.setStatus("current")

ipsoImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 5)
)
ipsoImageGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoImageIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoImageVersionNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoImageSerialNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoImageTimeOfLoad"))
)
if mibBuilder.loadTexts:
    ipsoImageGroup.setStatus("current")

ipsoStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 6)
)
ipsoStorageGroup.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoSIMMTotal")
)
if mibBuilder.loadTexts:
    ipsoStorageGroup.setStatus("current")

ipsoProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 7)
)
ipsoProcessGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessorUtilization"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessID"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessParentID"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessOwner"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessMemory"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProcessPercentCPU"))
)
if mibBuilder.loadTexts:
    ipsoProcessGroup.setStatus("current")

ipsoDiskMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 9)
)
ipsoDiskMirrorGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoTotalDiskMirrorSets"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMirrorSetIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMirrorSetSourceDrive"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMirrorSetDestinationDrive"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMirrorSetSyncPercent"))
)
if mibBuilder.loadTexts:
    ipsoDiskMirrorGroup.setStatus("current")

ipsoAssetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 10)
)
ipsoAssetGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoAssetChassisSerialNumber"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoCPUModel"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoCPUMfr"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoCPUFreq"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoKernMaxMem"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMotherBoardSerNum"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMotherBoardRev"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoMotherBoardModel"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoOSRelease"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoOSVersion"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoProductModel"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgName"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgMajorVersion"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgMinorVersion"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoPkgLicense"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskSysDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveModel"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveCapacity"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveLocation"))
)
if mibBuilder.loadTexts:
    ipsoAssetGroup.setStatus("current")

ipsoLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 11)
)
ipsoLicenseGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsofeaturename"),
        ("NOKIA-IPSO-SYSTEM-MIB", "noofdaystoexpire"))
)
if mibBuilder.loadTexts:
    ipsoLicenseGroup.setStatus("current")


# Notification objects

systemTrapConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    systemTrapConfigurationChange.setStatus(
        "current"
    )

systemTrapConfigurationFileChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 2)
)
systemTrapConfigurationFileChange.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigFilePath")
)
if mibBuilder.loadTexts:
    systemTrapConfigurationFileChange.setStatus(
        "current"
    )

systemTrapConfigurationSaveChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 3)
)
systemTrapConfigurationSaveChange.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoConfigFilePath")
)
if mibBuilder.loadTexts:
    systemTrapConfigurationSaveChange.setStatus(
        "current"
    )

systemTrapLowDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 4)
)
systemTrapLowDiskSpace.setObjects(
      *(("HOST-RESOURCES-MIB", "hrPartitionIndex"),
        ("HOST-RESOURCES-MIB", "hrPartitionLabel"),
        ("HOST-RESOURCES-MIB", "hrPartitionSize"),
        ("HOST-RESOURCES-MIB", "hrFSMountPoint"))
)
if mibBuilder.loadTexts:
    systemTrapLowDiskSpace.setStatus(
        "current"
    )

systemTrapNoDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 5)
)
systemTrapNoDiskSpace.setObjects(
      *(("HOST-RESOURCES-MIB", "hrPartitionIndex"),
        ("HOST-RESOURCES-MIB", "hrPartitionLabel"),
        ("HOST-RESOURCES-MIB", "hrPartitionSize"),
        ("HOST-RESOURCES-MIB", "hrFSMountPoint"))
)
if mibBuilder.loadTexts:
    systemTrapNoDiskSpace.setStatus(
        "current"
    )

systemTrapDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 6)
)
systemTrapDiskFailure.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveIndex")
)
if mibBuilder.loadTexts:
    systemTrapDiskFailure.setStatus(
        "current"
    )

systemTrapDiskMirrorSetCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 7)
)
systemTrapDiskMirrorSetCreate.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetSourceDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetDestinationDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveLocation"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveLocation"))
)
if mibBuilder.loadTexts:
    systemTrapDiskMirrorSetCreate.setStatus(
        "current"
    )

systemTrapDiskMirrorSetDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 8)
)
systemTrapDiskMirrorSetDelete.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetSourceDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetDestinationDriveIndex"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveLocation"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskDriveLocation"))
)
if mibBuilder.loadTexts:
    systemTrapDiskMirrorSetDelete.setStatus(
        "current"
    )

systemTrapSnmpProcessShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 9)
)
if mibBuilder.loadTexts:
    systemTrapSnmpProcessShutdown.setStatus(
        "current"
    )

systemTrapDiskMirrorSyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 10)
)
systemTrapDiskMirrorSyncFailure.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetIndex")
)
if mibBuilder.loadTexts:
    systemTrapDiskMirrorSyncFailure.setStatus(
        "current"
    )

systemTrapDiskMirrorSyncSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 11)
)
systemTrapDiskMirrorSyncSuccess.setObjects(
    ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDiskMirrorSetIndex")
)
if mibBuilder.loadTexts:
    systemTrapDiskMirrorSyncSuccess.setStatus(
        "current"
    )

systemTrapLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8, 1, 16)
)
systemTrapLicense.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "ipsoFeatureName"),
        ("NOKIA-IPSO-SYSTEM-MIB", "ipsoDaysToExpire"))
)
if mibBuilder.loadTexts:
    systemTrapLicense.setStatus(
        "current"
    )


# Notifications groups

ipsoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 1, 21, 1, 8)
)
ipsoNotificationGroup.setObjects(
      *(("NOKIA-IPSO-SYSTEM-MIB", "systemTrapConfigurationChange"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapConfigurationFileChange"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapConfigurationSaveChange"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapLowDiskSpace"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapNoDiskSpace"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapDiskFailure"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapDiskMirrorSetCreate"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapDiskMirrorSetDelete"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapDiskMirrorSyncFailure"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapDiskMirrorSyncSuccess"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapSnmpProcessShutdown"),
        ("NOKIA-IPSO-SYSTEM-MIB", "systemTrapLicense"))
)
if mibBuilder.loadTexts:
    ipsoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-IPSO-SYSTEM-MIB",
    **{"nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "ipsoProducts": ipsoProducts,
       "ipsoSystem": ipsoSystem,
       "ipsoChassisGroup": ipsoChassisGroup,
       "ipsoChassisSerialNumber": ipsoChassisSerialNumber,
       "ipsoChassisMBType": ipsoChassisMBType,
       "ipsoChassisMBRevNumber": ipsoChassisMBRevNumber,
       "ipsoChassisMBSerialNumber": ipsoChassisMBSerialNumber,
       "ipsoChassisTemperature": ipsoChassisTemperature,
       "ipsoCardTable": ipsoCardTable,
       "ipsoCardEntry": ipsoCardEntry,
       "ipsoCardIndex": ipsoCardIndex,
       "ipsoCardOperStatus": ipsoCardOperStatus,
       "ipsoFanGroup": ipsoFanGroup,
       "ipsoFanTable": ipsoFanTable,
       "ipsoFanEntry": ipsoFanEntry,
       "ipsoFanIndex": ipsoFanIndex,
       "ipsoFanOperStatus": ipsoFanOperStatus,
       "ipsoPowerSupplyGroup": ipsoPowerSupplyGroup,
       "ipsoPowerSupplyTable": ipsoPowerSupplyTable,
       "ipsoPowerSupplyEntry": ipsoPowerSupplyEntry,
       "ipsoPowerSupplyIndex": ipsoPowerSupplyIndex,
       "ipsoPowerSupplyOverTemperature": ipsoPowerSupplyOverTemperature,
       "ipsoPowerSupplyOperStatus": ipsoPowerSupplyOperStatus,
       "ipsoConfigGroup": ipsoConfigGroup,
       "ipsoConfigTable": ipsoConfigTable,
       "ipsoConfigEntry": ipsoConfigEntry,
       "ipsoConfigIndex": ipsoConfigIndex,
       "ipsoConfigFilePath": ipsoConfigFilePath,
       "ipsoConfigFileDateAndTime": ipsoConfigFileDateAndTime,
       "ipsoConfigLogSize": ipsoConfigLogSize,
       "ipsoConfigLogTable": ipsoConfigLogTable,
       "ipsoConfigLogEntry": ipsoConfigLogEntry,
       "ipsoConfigLogIndex": ipsoConfigLogIndex,
       "ipsoConfigLogDescr": ipsoConfigLogDescr,
       "ipsoImageGroup": ipsoImageGroup,
       "ipsoImageTable": ipsoImageTable,
       "ipsoImageEntry": ipsoImageEntry,
       "ipsoImageIndex": ipsoImageIndex,
       "ipsoImageVersionNumber": ipsoImageVersionNumber,
       "ipsoImageSerialNumber": ipsoImageSerialNumber,
       "ipsoImageTimeOfLoad": ipsoImageTimeOfLoad,
       "ipsoStorageGroup": ipsoStorageGroup,
       "ipsoSIMMTotal": ipsoSIMMTotal,
       "ipsoProcessGroup": ipsoProcessGroup,
       "ipsoProcessorUtilization": ipsoProcessorUtilization,
       "ipsoProcessTable": ipsoProcessTable,
       "ipsoProcessEntry": ipsoProcessEntry,
       "ipsoProcessID": ipsoProcessID,
       "ipsoProcessParentID": ipsoProcessParentID,
       "ipsoProcessOwner": ipsoProcessOwner,
       "ipsoProcessMemory": ipsoProcessMemory,
       "ipsoProcessPercentCPU": ipsoProcessPercentCPU,
       "ipsoNotificationGroup": ipsoNotificationGroup,
       "systemTraps": systemTraps,
       "systemTrapConfigurationChange": systemTrapConfigurationChange,
       "systemTrapConfigurationFileChange": systemTrapConfigurationFileChange,
       "systemTrapConfigurationSaveChange": systemTrapConfigurationSaveChange,
       "systemTrapLowDiskSpace": systemTrapLowDiskSpace,
       "systemTrapNoDiskSpace": systemTrapNoDiskSpace,
       "systemTrapDiskFailure": systemTrapDiskFailure,
       "systemTrapDiskMirrorSetCreate": systemTrapDiskMirrorSetCreate,
       "systemTrapDiskMirrorSetDelete": systemTrapDiskMirrorSetDelete,
       "systemTrapSnmpProcessShutdown": systemTrapSnmpProcessShutdown,
       "systemTrapDiskMirrorSyncFailure": systemTrapDiskMirrorSyncFailure,
       "systemTrapDiskMirrorSyncSuccess": systemTrapDiskMirrorSyncSuccess,
       "systemTrapLicense": systemTrapLicense,
       "ipsoDiskMirrorGroup": ipsoDiskMirrorGroup,
       "ipsoTotalDiskMirrorSets": ipsoTotalDiskMirrorSets,
       "ipsoDiskMirrorSetTable": ipsoDiskMirrorSetTable,
       "ipsoDiskMirrorSetEntry": ipsoDiskMirrorSetEntry,
       "ipsoDiskMirrorSetIndex": ipsoDiskMirrorSetIndex,
       "ipsoDiskMirrorSetSourceDriveIndex": ipsoDiskMirrorSetSourceDriveIndex,
       "ipsoDiskMirrorSetDestinationDriveIndex": ipsoDiskMirrorSetDestinationDriveIndex,
       "ipsoDiskMirrorSetSyncPercent": ipsoDiskMirrorSetSyncPercent,
       "ipsoAssetGroup": ipsoAssetGroup,
       "ipsoAssetChassisSerialNumber": ipsoAssetChassisSerialNumber,
       "ipsoCPUModel": ipsoCPUModel,
       "ipsoCPUMfr": ipsoCPUMfr,
       "ipsoCPUFreq": ipsoCPUFreq,
       "ipsoKernMaxMem": ipsoKernMaxMem,
       "ipsoMotherBoardSerNum": ipsoMotherBoardSerNum,
       "ipsoMotherBoardRev": ipsoMotherBoardRev,
       "ipsoMotherBoardModel": ipsoMotherBoardModel,
       "ipsoOSRelease": ipsoOSRelease,
       "ipsoOSVersion": ipsoOSVersion,
       "ipsoProductModel": ipsoProductModel,
       "ipsoAssetTable": ipsoAssetTable,
       "ipsoAssetEntry": ipsoAssetEntry,
       "ipsoPkgIndex": ipsoPkgIndex,
       "ipsoPkgName": ipsoPkgName,
       "ipsoPkgMajorVersion": ipsoPkgMajorVersion,
       "ipsoPkgMinorVersion": ipsoPkgMinorVersion,
       "ipsoPkgLicense": ipsoPkgLicense,
       "ipsoDiskDriveTable": ipsoDiskDriveTable,
       "ipsoDiskDriveEntry": ipsoDiskDriveEntry,
       "ipsoDiskDriveIndex": ipsoDiskDriveIndex,
       "ipsoSysDiskDriveIndex": ipsoSysDiskDriveIndex,
       "ipsoDiskDriveModel": ipsoDiskDriveModel,
       "ipsoDiskDriveCapacity": ipsoDiskDriveCapacity,
       "ipsoDiskDriveLocation": ipsoDiskDriveLocation,
       "ipsoLicenseGroup": ipsoLicenseGroup,
       "ipsoFeatureName": ipsoFeatureName,
       "ipsoDaysToExpire": ipsoDaysToExpire}
)
