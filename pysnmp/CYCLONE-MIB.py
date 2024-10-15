# SNMP MIB module (CYCLONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYCLONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:27 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Storagemanagement_ObjectIdentity = ObjectIdentity
storagemanagement = _Storagemanagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2)
)
_Cyclone_ObjectIdentity = ObjectIdentity
cyclone = _Cyclone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 5)
)
_CycTraps_ObjectIdentity = ObjectIdentity
cycTraps = _CycTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000)
)


class _CycManagerID_Type(DisplayString):
    """Custom type cycManagerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycManagerID_Type.__name__ = "DisplayString"
_CycManagerID_Object = MibScalar
cycManagerID = _CycManagerID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9001),
    _CycManagerID_Type()
)
cycManagerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycManagerID.setStatus("mandatory")


class _CycHostAdapterID_Type(DisplayString):
    """Custom type cycHostAdapterID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycHostAdapterID_Type.__name__ = "DisplayString"
_CycHostAdapterID_Object = MibScalar
cycHostAdapterID = _CycHostAdapterID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9002),
    _CycHostAdapterID_Type()
)
cycHostAdapterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycHostAdapterID.setStatus("mandatory")
_CycHostAdapterNumber_Type = Integer32
_CycHostAdapterNumber_Object = MibScalar
cycHostAdapterNumber = _CycHostAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9003),
    _CycHostAdapterNumber_Type()
)
cycHostAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycHostAdapterNumber.setStatus("mandatory")


class _CycVendor_Type(DisplayString):
    """Custom type cycVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CycVendor_Type.__name__ = "DisplayString"
_CycVendor_Object = MibScalar
cycVendor = _CycVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9004),
    _CycVendor_Type()
)
cycVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycVendor.setStatus("mandatory")


class _CycProduct_Type(DisplayString):
    """Custom type cycProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CycProduct_Type.__name__ = "DisplayString"
_CycProduct_Object = MibScalar
cycProduct = _CycProduct_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9005),
    _CycProduct_Type()
)
cycProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycProduct.setStatus("mandatory")


class _CycControllerModel_Type(DisplayString):
    """Custom type cycControllerModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycControllerModel_Type.__name__ = "DisplayString"
_CycControllerModel_Object = MibScalar
cycControllerModel = _CycControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9006),
    _CycControllerModel_Type()
)
cycControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycControllerModel.setStatus("mandatory")
_CycBusNumber_Type = Integer32
_CycBusNumber_Object = MibScalar
cycBusNumber = _CycBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9007),
    _CycBusNumber_Type()
)
cycBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycBusNumber.setStatus("mandatory")
_CycChannelNumber_Type = Integer32
_CycChannelNumber_Object = MibScalar
cycChannelNumber = _CycChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9008),
    _CycChannelNumber_Type()
)
cycChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycChannelNumber.setStatus("mandatory")
_CycScsiTargetID_Type = Integer32
_CycScsiTargetID_Object = MibScalar
cycScsiTargetID = _CycScsiTargetID_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9009),
    _CycScsiTargetID_Type()
)
cycScsiTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycScsiTargetID.setStatus("mandatory")
_CycLun_Type = Integer32
_CycLun_Object = MibScalar
cycLun = _CycLun_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9010),
    _CycLun_Type()
)
cycLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycLun.setStatus("mandatory")


class _CycArrayName_Type(DisplayString):
    """Custom type cycArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycArrayName_Type.__name__ = "DisplayString"
_CycArrayName_Object = MibScalar
cycArrayName = _CycArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9011),
    _CycArrayName_Type()
)
cycArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycArrayName.setStatus("mandatory")
_CycMisCompares_Type = Integer32
_CycMisCompares_Object = MibScalar
cycMisCompares = _CycMisCompares_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9012),
    _CycMisCompares_Type()
)
cycMisCompares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycMisCompares.setStatus("mandatory")
_CycDriver_Type = Integer32
_CycDriver_Object = MibScalar
cycDriver = _CycDriver_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9013),
    _CycDriver_Type()
)
cycDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycDriver.setStatus("mandatory")
_CycManager_Type = Integer32
_CycManager_Object = MibScalar
cycManager = _CycManager_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9014),
    _CycManager_Type()
)
cycManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycManager.setStatus("mandatory")


class _CycOldArrayName_Type(DisplayString):
    """Custom type cycOldArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycOldArrayName_Type.__name__ = "DisplayString"
_CycOldArrayName_Object = MibScalar
cycOldArrayName = _CycOldArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9015),
    _CycOldArrayName_Type()
)
cycOldArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycOldArrayName.setStatus("mandatory")


class _CycNewArrayName_Type(DisplayString):
    """Custom type cycNewArrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CycNewArrayName_Type.__name__ = "DisplayString"
_CycNewArrayName_Object = MibScalar
cycNewArrayName = _CycNewArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9016),
    _CycNewArrayName_Type()
)
cycNewArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycNewArrayName.setStatus("mandatory")
_CycPriority_Type = Integer32
_CycPriority_Object = MibScalar
cycPriority = _CycPriority_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9017),
    _CycPriority_Type()
)
cycPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycPriority.setStatus("mandatory")
_CycSenseInfo_Type = Integer32
_CycSenseInfo_Object = MibScalar
cycSenseInfo = _CycSenseInfo_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 9000, 9018),
    _CycSenseInfo_Type()
)
cycSenseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cycSenseInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sCSISmart1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 101)
)
if mibBuilder.loadTexts:
    sCSISmart1.setStatus(
        ""
    )

sCSISmart2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 102)
)
if mibBuilder.loadTexts:
    sCSISmart2.setStatus(
        ""
    )

sCSISmart3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 107)
)
if mibBuilder.loadTexts:
    sCSISmart3.setStatus(
        ""
    )

sCSISmart4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 108)
)
sCSISmart4.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycHostAdapterID"),
        ("CYCLONE-MIB", "cycManagerID"))
)
if mibBuilder.loadTexts:
    sCSISmart4.setStatus(
        ""
    )

sCSISmart5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 109)
)
sCSISmart5.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycHostAdapterID"),
        ("CYCLONE-MIB", "cycManagerID"))
)
if mibBuilder.loadTexts:
    sCSISmart5.setStatus(
        ""
    )

sCSISmart6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 110)
)
sCSISmart6.setObjects(
    ("CYCLONE-MIB", "cycHostAdapterNumber")
)
if mibBuilder.loadTexts:
    sCSISmart6.setStatus(
        ""
    )

sCSISmart7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 111)
)
sCSISmart7.setObjects(
    ("CYCLONE-MIB", "cycHostAdapterNumber")
)
if mibBuilder.loadTexts:
    sCSISmart7.setStatus(
        ""
    )

sCSISmart8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 112)
)
sCSISmart8.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycScsiTargetID"),
        ("CYCLONE-MIB", "cycLun"))
)
if mibBuilder.loadTexts:
    sCSISmart8.setStatus(
        ""
    )

sCSISmart9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 113)
)
sCSISmart9.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycScsiTargetID"),
        ("CYCLONE-MIB", "cycLun"),
        ("CYCLONE-MIB", "cycVendor"),
        ("CYCLONE-MIB", "cycProduct"))
)
if mibBuilder.loadTexts:
    sCSISmart9.setStatus(
        ""
    )

sCSISmart10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 114)
)
sCSISmart10.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycScsiTargetID"),
        ("CYCLONE-MIB", "cycLun"))
)
if mibBuilder.loadTexts:
    sCSISmart10.setStatus(
        ""
    )

sCSISmart11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 115)
)
sCSISmart11.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycScsiTargetID"),
        ("CYCLONE-MIB", "cycLun"),
        ("CYCLONE-MIB", "cycVendor"),
        ("CYCLONE-MIB", "cycProduct"))
)
if mibBuilder.loadTexts:
    sCSISmart11.setStatus(
        ""
    )

sCSISmart12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 116)
)
sCSISmart12.setObjects(
      *(("CYCLONE-MIB", "cycHostAdapterNumber"),
        ("CYCLONE-MIB", "cycScsiTargetID"),
        ("CYCLONE-MIB", "cycLun"),
        ("CYCLONE-MIB", "cycVendor"),
        ("CYCLONE-MIB", "cycProduct"),
        ("CYCLONE-MIB", "cycSenseInfo"))
)
if mibBuilder.loadTexts:
    sCSISmart12.setStatus(
        ""
    )

sCSISmart13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 117)
)
if mibBuilder.loadTexts:
    sCSISmart13.setStatus(
        ""
    )

sCSISmart14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 118)
)
if mibBuilder.loadTexts:
    sCSISmart14.setStatus(
        ""
    )

sCSISmart15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 119)
)
if mibBuilder.loadTexts:
    sCSISmart15.setStatus(
        ""
    )

sCSISmart16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 120)
)
if mibBuilder.loadTexts:
    sCSISmart16.setStatus(
        ""
    )

sCSISmart17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 121)
)
if mibBuilder.loadTexts:
    sCSISmart17.setStatus(
        ""
    )

sCSISmart18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 122)
)
if mibBuilder.loadTexts:
    sCSISmart18.setStatus(
        ""
    )

sCSISmart19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 123)
)
if mibBuilder.loadTexts:
    sCSISmart19.setStatus(
        ""
    )

sCSISmart20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 124)
)
if mibBuilder.loadTexts:
    sCSISmart20.setStatus(
        ""
    )

sCSISmart21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 5, 0, 125)
)
if mibBuilder.loadTexts:
    sCSISmart21.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLONE-MIB",
    **{"adaptec": adaptec,
       "storagemanagement": storagemanagement,
       "cyclone": cyclone,
       "sCSISmart1": sCSISmart1,
       "sCSISmart2": sCSISmart2,
       "sCSISmart3": sCSISmart3,
       "sCSISmart4": sCSISmart4,
       "sCSISmart5": sCSISmart5,
       "sCSISmart6": sCSISmart6,
       "sCSISmart7": sCSISmart7,
       "sCSISmart8": sCSISmart8,
       "sCSISmart9": sCSISmart9,
       "sCSISmart10": sCSISmart10,
       "sCSISmart11": sCSISmart11,
       "sCSISmart12": sCSISmart12,
       "sCSISmart13": sCSISmart13,
       "sCSISmart14": sCSISmart14,
       "sCSISmart15": sCSISmart15,
       "sCSISmart16": sCSISmart16,
       "sCSISmart17": sCSISmart17,
       "sCSISmart18": sCSISmart18,
       "sCSISmart19": sCSISmart19,
       "sCSISmart20": sCSISmart20,
       "sCSISmart21": sCSISmart21,
       "cycTraps": cycTraps,
       "cycManagerID": cycManagerID,
       "cycHostAdapterID": cycHostAdapterID,
       "cycHostAdapterNumber": cycHostAdapterNumber,
       "cycVendor": cycVendor,
       "cycProduct": cycProduct,
       "cycControllerModel": cycControllerModel,
       "cycBusNumber": cycBusNumber,
       "cycChannelNumber": cycChannelNumber,
       "cycScsiTargetID": cycScsiTargetID,
       "cycLun": cycLun,
       "cycArrayName": cycArrayName,
       "cycMisCompares": cycMisCompares,
       "cycDriver": cycDriver,
       "cycManager": cycManager,
       "cycOldArrayName": cycOldArrayName,
       "cycNewArrayName": cycNewArrayName,
       "cycPriority": cycPriority,
       "cycSenseInfo": cycSenseInfo}
)
