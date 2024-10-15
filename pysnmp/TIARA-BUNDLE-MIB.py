# SNMP MIB module (TIARA-BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-BUNDLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:32 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraBundleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13)
)
tiaraBundleMib.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BundleTable_Object = MibTable
bundleTable = _BundleTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1)
)
if mibBuilder.loadTexts:
    bundleTable.setStatus("current")
_BundleTableEntry_Object = MibTableRow
bundleTableEntry = _BundleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1)
)
bundleTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    bundleTableEntry.setStatus("current")
_BundleId_Type = Integer32
_BundleId_Object = MibTableColumn
bundleId = _BundleId_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 1),
    _BundleId_Type()
)
bundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bundleId.setStatus("current")


class _BundleName_Type(DisplayString):
    """Custom type bundleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BundleName_Type.__name__ = "DisplayString"
_BundleName_Object = MibTableColumn
bundleName = _BundleName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 2),
    _BundleName_Type()
)
bundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleName.setStatus("current")


class _BundleContact_Type(DisplayString):
    """Custom type bundleContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_BundleContact_Type.__name__ = "DisplayString"
_BundleContact_Object = MibTableColumn
bundleContact = _BundleContact_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 3),
    _BundleContact_Type()
)
bundleContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleContact.setStatus("current")


class _BundleDescr_Type(DisplayString):
    """Custom type bundleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_BundleDescr_Type.__name__ = "DisplayString"
_BundleDescr_Object = MibTableColumn
bundleDescr = _BundleDescr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 4),
    _BundleDescr_Type()
)
bundleDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleDescr.setStatus("current")


class _BundleEncapsulation_Type(Integer32):
    """Custom type bundleEncapsulation based on Integer32"""
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
        *(("frameRelay", 4),
          ("hdlc", 3),
          ("noEncap", 1),
          ("ppp", 2))
    )


_BundleEncapsulation_Type.__name__ = "Integer32"
_BundleEncapsulation_Object = MibTableColumn
bundleEncapsulation = _BundleEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 5),
    _BundleEncapsulation_Type()
)
bundleEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleEncapsulation.setStatus("current")


class _BundleDropEs_Type(Integer32):
    """Custom type bundleDropEs based on Integer32"""
    defaultValue = 0


_BundleDropEs_Object = MibTableColumn
bundleDropEs = _BundleDropEs_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 6),
    _BundleDropEs_Type()
)
bundleDropEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleDropEs.setStatus("current")
if mibBuilder.loadTexts:
    bundleDropEs.setUnits("seconds")


class _BundleDropSes_Type(Integer32):
    """Custom type bundleDropSes based on Integer32"""
    defaultValue = 0


_BundleDropSes_Object = MibTableColumn
bundleDropSes = _BundleDropSes_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 7),
    _BundleDropSes_Type()
)
bundleDropSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleDropSes.setStatus("current")
if mibBuilder.loadTexts:
    bundleDropSes.setUnits("seconds")


class _BundleDropUas_Type(Integer32):
    """Custom type bundleDropUas based on Integer32"""
    defaultValue = 0


_BundleDropUas_Object = MibTableColumn
bundleDropUas = _BundleDropUas_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 8),
    _BundleDropUas_Type()
)
bundleDropUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleDropUas.setStatus("current")
if mibBuilder.loadTexts:
    bundleDropUas.setUnits("seconds")


class _BundleIpAddr_Type(IpAddress):
    """Custom type bundleIpAddr based on IpAddress"""
    defaultValue = 0


_BundleIpAddr_Object = MibTableColumn
bundleIpAddr = _BundleIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 9),
    _BundleIpAddr_Type()
)
bundleIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleIpAddr.setStatus("current")


class _BundleSubnetMask_Type(IpAddress):
    """Custom type bundleSubnetMask based on IpAddress"""
    defaultValue = 0


_BundleSubnetMask_Object = MibTableColumn
bundleSubnetMask = _BundleSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 10),
    _BundleSubnetMask_Type()
)
bundleSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleSubnetMask.setStatus("current")


class _BundleSrcForwardingAddrPrimary_Type(IpAddress):
    """Custom type bundleSrcForwardingAddrPrimary based on IpAddress"""
    defaultValue = 0


_BundleSrcForwardingAddrPrimary_Object = MibTableColumn
bundleSrcForwardingAddrPrimary = _BundleSrcForwardingAddrPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 11),
    _BundleSrcForwardingAddrPrimary_Type()
)
bundleSrcForwardingAddrPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleSrcForwardingAddrPrimary.setStatus("current")


class _BundleSrcForwardingAddrSecondary_Type(IpAddress):
    """Custom type bundleSrcForwardingAddrSecondary based on IpAddress"""
    defaultValue = 0


_BundleSrcForwardingAddrSecondary_Object = MibTableColumn
bundleSrcForwardingAddrSecondary = _BundleSrcForwardingAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 12),
    _BundleSrcForwardingAddrSecondary_Type()
)
bundleSrcForwardingAddrSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleSrcForwardingAddrSecondary.setStatus("current")


class _BundleRestoreMethod_Type(Integer32):
    """Custom type bundleRestoreMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_BundleRestoreMethod_Type.__name__ = "Integer32"
_BundleRestoreMethod_Object = MibTableColumn
bundleRestoreMethod = _BundleRestoreMethod_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 13),
    _BundleRestoreMethod_Type()
)
bundleRestoreMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleRestoreMethod.setStatus("current")


class _BundleLinkRestoralTime_Type(Integer32):
    """Custom type bundleLinkRestoralTime based on Integer32"""
    defaultValue = 120


_BundleLinkRestoralTime_Object = MibTableColumn
bundleLinkRestoralTime = _BundleLinkRestoralTime_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 14),
    _BundleLinkRestoralTime_Type()
)
bundleLinkRestoralTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkRestoralTime.setStatus("current")
if mibBuilder.loadTexts:
    bundleLinkRestoralTime.setUnits("seconds")


class _BundleStatus_Type(Integer32):
    """Custom type bundleStatus based on Integer32"""
    defaultValue = 1

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


_BundleStatus_Type.__name__ = "Integer32"
_BundleStatus_Object = MibTableColumn
bundleStatus = _BundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 15),
    _BundleStatus_Type()
)
bundleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleStatus.setStatus("current")


class _BundleLinkRestore_Type(OctetString):
    """Custom type bundleLinkRestore based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BundleLinkRestore_Type.__name__ = "OctetString"
_BundleLinkRestore_Object = MibTableColumn
bundleLinkRestore = _BundleLinkRestore_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 16),
    _BundleLinkRestore_Type()
)
bundleLinkRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleLinkRestore.setStatus("current")
_BundleNoOfLinks_Type = Integer32
_BundleNoOfLinks_Object = MibTableColumn
bundleNoOfLinks = _BundleNoOfLinks_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 17),
    _BundleNoOfLinks_Type()
)
bundleNoOfLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleNoOfLinks.setStatus("current")
_BundleTotalBw_Type = Integer32
_BundleTotalBw_Object = MibTableColumn
bundleTotalBw = _BundleTotalBw_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 18),
    _BundleTotalBw_Type()
)
bundleTotalBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleTotalBw.setStatus("current")
if mibBuilder.loadTexts:
    bundleTotalBw.setUnits("kbps")
_BundleRowStatus_Type = RowStatus
_BundleRowStatus_Object = MibTableColumn
bundleRowStatus = _BundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 1, 1, 19),
    _BundleRowStatus_Type()
)
bundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleRowStatus.setStatus("current")
_BundleLinkTable_Object = MibTable
bundleLinkTable = _BundleLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2)
)
if mibBuilder.loadTexts:
    bundleLinkTable.setStatus("current")
_BundleLinkEntry_Object = MibTableRow
bundleLinkEntry = _BundleLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1)
)
bundleLinkEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
    (0, "TIARA-BUNDLE-MIB", "bundleLinkT1Num"),
)
if mibBuilder.loadTexts:
    bundleLinkEntry.setStatus("current")
_BundleLinkT1Num_Type = Integer32
_BundleLinkT1Num_Object = MibTableColumn
bundleLinkT1Num = _BundleLinkT1Num_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 1),
    _BundleLinkT1Num_Type()
)
bundleLinkT1Num.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bundleLinkT1Num.setStatus("current")


class _BundleLinkTimeSlots_Type(OctetString):
    """Custom type bundleLinkTimeSlots based on OctetString"""
    defaultValue = OctetString("00ffffff")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BundleLinkTimeSlots_Type.__name__ = "OctetString"
_BundleLinkTimeSlots_Object = MibTableColumn
bundleLinkTimeSlots = _BundleLinkTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 2),
    _BundleLinkTimeSlots_Type()
)
bundleLinkTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkTimeSlots.setStatus("current")


class _BundleLinkType_Type(Integer32):
    """Custom type bundleLinkType based on Integer32"""
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
        *(("ct3", 1),
          ("hssi", 3),
          ("t1", 2),
          ("t3", 4))
    )


_BundleLinkType_Type.__name__ = "Integer32"
_BundleLinkType_Object = MibTableColumn
bundleLinkType = _BundleLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 3),
    _BundleLinkType_Type()
)
bundleLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkType.setStatus("current")


class _BundleLinkSpeed_Type(Integer32):
    """Custom type bundleLinkSpeed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps56", 1),
          ("kbps64", 2))
    )


_BundleLinkSpeed_Type.__name__ = "Integer32"
_BundleLinkSpeed_Object = MibTableColumn
bundleLinkSpeed = _BundleLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 4),
    _BundleLinkSpeed_Type()
)
bundleLinkSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkSpeed.setStatus("current")


class _BundleLinkInvertedData_Type(TruthValue):
    """Custom type bundleLinkInvertedData based on TruthValue"""


_BundleLinkInvertedData_Object = MibTableColumn
bundleLinkInvertedData = _BundleLinkInvertedData_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 5),
    _BundleLinkInvertedData_Type()
)
bundleLinkInvertedData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkInvertedData.setStatus("current")


class _BundleLinkPhysIfNum_Type(Integer32):
    """Custom type bundleLinkPhysIfNum based on Integer32"""
    defaultValue = 0


_BundleLinkPhysIfNum_Object = MibTableColumn
bundleLinkPhysIfNum = _BundleLinkPhysIfNum_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 6),
    _BundleLinkPhysIfNum_Type()
)
bundleLinkPhysIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkPhysIfNum.setStatus("current")
_BundleLinkDiffDelay_Type = Integer32
_BundleLinkDiffDelay_Object = MibTableColumn
bundleLinkDiffDelay = _BundleLinkDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 7),
    _BundleLinkDiffDelay_Type()
)
bundleLinkDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    bundleLinkDiffDelay.setUnits("milli-seconds")
_BundleLinkBw_Type = Integer32
_BundleLinkBw_Object = MibTableColumn
bundleLinkBw = _BundleLinkBw_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 8),
    _BundleLinkBw_Type()
)
bundleLinkBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkBw.setStatus("current")
if mibBuilder.loadTexts:
    bundleLinkBw.setUnits("kbps")


class _BundleLinkStatus_Type(Integer32):
    """Custom type bundleLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_BundleLinkStatus_Type.__name__ = "Integer32"
_BundleLinkStatus_Object = MibTableColumn
bundleLinkStatus = _BundleLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 9),
    _BundleLinkStatus_Type()
)
bundleLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkStatus.setStatus("current")
_BundleLinkRowStatus_Type = RowStatus
_BundleLinkRowStatus_Object = MibTableColumn
bundleLinkRowStatus = _BundleLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 13, 2, 1, 10),
    _BundleLinkRowStatus_Type()
)
bundleLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-BUNDLE-MIB",
    **{"tiaraBundleMib": tiaraBundleMib,
       "bundleTable": bundleTable,
       "bundleTableEntry": bundleTableEntry,
       "bundleId": bundleId,
       "bundleName": bundleName,
       "bundleContact": bundleContact,
       "bundleDescr": bundleDescr,
       "bundleEncapsulation": bundleEncapsulation,
       "bundleDropEs": bundleDropEs,
       "bundleDropSes": bundleDropSes,
       "bundleDropUas": bundleDropUas,
       "bundleIpAddr": bundleIpAddr,
       "bundleSubnetMask": bundleSubnetMask,
       "bundleSrcForwardingAddrPrimary": bundleSrcForwardingAddrPrimary,
       "bundleSrcForwardingAddrSecondary": bundleSrcForwardingAddrSecondary,
       "bundleRestoreMethod": bundleRestoreMethod,
       "bundleLinkRestoralTime": bundleLinkRestoralTime,
       "bundleStatus": bundleStatus,
       "bundleLinkRestore": bundleLinkRestore,
       "bundleNoOfLinks": bundleNoOfLinks,
       "bundleTotalBw": bundleTotalBw,
       "bundleRowStatus": bundleRowStatus,
       "bundleLinkTable": bundleLinkTable,
       "bundleLinkEntry": bundleLinkEntry,
       "bundleLinkT1Num": bundleLinkT1Num,
       "bundleLinkTimeSlots": bundleLinkTimeSlots,
       "bundleLinkType": bundleLinkType,
       "bundleLinkSpeed": bundleLinkSpeed,
       "bundleLinkInvertedData": bundleLinkInvertedData,
       "bundleLinkPhysIfNum": bundleLinkPhysIfNum,
       "bundleLinkDiffDelay": bundleLinkDiffDelay,
       "bundleLinkBw": bundleLinkBw,
       "bundleLinkStatus": bundleLinkStatus,
       "bundleLinkRowStatus": bundleLinkRowStatus}
)
