# SNMP MIB module (HUAWEI-FTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:51 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwFtp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166)
)
hwFtp.setRevisions(
        ("2014-04-21 09:00",
         "2014-08-15 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwFtpObjects_ObjectIdentity = ObjectIdentity
hwFtpObjects = _HwFtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1)
)
_HwFtpServer_ObjectIdentity = ObjectIdentity
hwFtpServer = _HwFtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1)
)


class _HwFtpServerEnable_Type(Integer32):
    """Custom type hwFtpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwFtpServerEnable_Type.__name__ = "Integer32"
_HwFtpServerEnable_Object = MibScalar
hwFtpServerEnable = _HwFtpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 1),
    _HwFtpServerEnable_Type()
)
hwFtpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpServerEnable.setStatus("current")
_HwFtpHostPermit_ObjectIdentity = ObjectIdentity
hwFtpHostPermit = _HwFtpHostPermit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2)
)
_HwFtpHostPermitTable_Object = MibTable
hwFtpHostPermitTable = _HwFtpHostPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwFtpHostPermitTable.setStatus("current")
_HwFtpHostPermitEntry_Object = MibTableRow
hwFtpHostPermitEntry = _HwFtpHostPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1)
)
hwFtpHostPermitEntry.setIndexNames(
    (0, "HUAWEI-FTP-MIB", "hwFtpHostPermitIndex"),
)
if mibBuilder.loadTexts:
    hwFtpHostPermitEntry.setStatus("current")


class _HwFtpHostPermitIndex_Type(Integer32):
    """Custom type hwFtpHostPermitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwFtpHostPermitIndex_Type.__name__ = "Integer32"
_HwFtpHostPermitIndex_Object = MibTableColumn
hwFtpHostPermitIndex = _HwFtpHostPermitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1, 1),
    _HwFtpHostPermitIndex_Type()
)
hwFtpHostPermitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpHostPermitIndex.setStatus("current")
_HwFtpHostPermitIpAddress_Type = IpAddress
_HwFtpHostPermitIpAddress_Object = MibTableColumn
hwFtpHostPermitIpAddress = _HwFtpHostPermitIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1, 2),
    _HwFtpHostPermitIpAddress_Type()
)
hwFtpHostPermitIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpHostPermitIpAddress.setStatus("current")
_HwFtpHostPermitMaskAddress_Type = IpAddress
_HwFtpHostPermitMaskAddress_Object = MibTableColumn
hwFtpHostPermitMaskAddress = _HwFtpHostPermitMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1, 3),
    _HwFtpHostPermitMaskAddress_Type()
)
hwFtpHostPermitMaskAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpHostPermitMaskAddress.setStatus("current")


class _HwFtpHostPermitInformation_Type(OctetString):
    """Custom type hwFtpHostPermitInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwFtpHostPermitInformation_Type.__name__ = "OctetString"
_HwFtpHostPermitInformation_Object = MibTableColumn
hwFtpHostPermitInformation = _HwFtpHostPermitInformation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1, 4),
    _HwFtpHostPermitInformation_Type()
)
hwFtpHostPermitInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpHostPermitInformation.setStatus("current")
_HwFtpHostPermitRowState_Type = RowStatus
_HwFtpHostPermitRowState_Object = MibTableColumn
hwFtpHostPermitRowState = _HwFtpHostPermitRowState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 2, 1, 1, 5),
    _HwFtpHostPermitRowState_Type()
)
hwFtpHostPermitRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFtpHostPermitRowState.setStatus("current")


class _HwFtpUpperThreshold_Type(Integer32):
    """Custom type hwFtpUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFtpUpperThreshold_Type.__name__ = "Integer32"
_HwFtpUpperThreshold_Object = MibScalar
hwFtpUpperThreshold = _HwFtpUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 3),
    _HwFtpUpperThreshold_Type()
)
hwFtpUpperThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFtpUpperThreshold.setStatus("current")


class _HwFtpLowerThreshold_Type(Integer32):
    """Custom type hwFtpLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFtpLowerThreshold_Type.__name__ = "Integer32"
_HwFtpLowerThreshold_Object = MibScalar
hwFtpLowerThreshold = _HwFtpLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 1, 1, 4),
    _HwFtpLowerThreshold_Type()
)
hwFtpLowerThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFtpLowerThreshold.setStatus("current")
_HwFtpNotification_ObjectIdentity = ObjectIdentity
hwFtpNotification = _HwFtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 2)
)
_HwFtpMIBConformance_ObjectIdentity = ObjectIdentity
hwFtpMIBConformance = _HwFtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 3)
)
_HwFtpMIBCompliances_ObjectIdentity = ObjectIdentity
hwFtpMIBCompliances = _HwFtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 3, 1)
)
_HwFtpMIBGroups_ObjectIdentity = ObjectIdentity
hwFtpMIBGroups = _HwFtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 3, 2)
)

# Managed Objects groups

hwFtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 3, 2, 1)
)
hwFtpServerGroup.setObjects(
    ("HUAWEI-FTP-MIB", "hwFtpServerEnable")
)
if mibBuilder.loadTexts:
    hwFtpServerGroup.setStatus("current")


# Notification objects

hwFtpNumThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 2, 1)
)
hwFtpNumThreshold.setObjects(
    ("HUAWEI-FTP-MIB", "hwFtpUpperThreshold")
)
if mibBuilder.loadTexts:
    hwFtpNumThreshold.setStatus(
        "current"
    )

hwFtpNumThresholdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 2, 2)
)
hwFtpNumThresholdResume.setObjects(
    ("HUAWEI-FTP-MIB", "hwFtpLowerThreshold")
)
if mibBuilder.loadTexts:
    hwFtpNumThresholdResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hwFtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 166, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwFtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FTP-MIB",
    **{"hwFtp": hwFtp,
       "hwFtpObjects": hwFtpObjects,
       "hwFtpServer": hwFtpServer,
       "hwFtpServerEnable": hwFtpServerEnable,
       "hwFtpHostPermit": hwFtpHostPermit,
       "hwFtpHostPermitTable": hwFtpHostPermitTable,
       "hwFtpHostPermitEntry": hwFtpHostPermitEntry,
       "hwFtpHostPermitIndex": hwFtpHostPermitIndex,
       "hwFtpHostPermitIpAddress": hwFtpHostPermitIpAddress,
       "hwFtpHostPermitMaskAddress": hwFtpHostPermitMaskAddress,
       "hwFtpHostPermitInformation": hwFtpHostPermitInformation,
       "hwFtpHostPermitRowState": hwFtpHostPermitRowState,
       "hwFtpUpperThreshold": hwFtpUpperThreshold,
       "hwFtpLowerThreshold": hwFtpLowerThreshold,
       "hwFtpNotification": hwFtpNotification,
       "hwFtpNumThreshold": hwFtpNumThreshold,
       "hwFtpNumThresholdResume": hwFtpNumThresholdResume,
       "hwFtpMIBConformance": hwFtpMIBConformance,
       "hwFtpMIBCompliances": hwFtpMIBCompliances,
       "hwFtpMIBCompliance": hwFtpMIBCompliance,
       "hwFtpMIBGroups": hwFtpMIBGroups,
       "hwFtpServerGroup": hwFtpServerGroup}
)
