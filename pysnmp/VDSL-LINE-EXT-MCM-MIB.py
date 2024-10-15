# SNMP MIB module (VDSL-LINE-EXT-MCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VDSL-LINE-EXT-MCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:04 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(vdslLineConfProfileName,) = mibBuilder.importSymbols(
    "VDSL-LINE-MIB",
    "vdslLineConfProfileName")


# MODULE-IDENTITY

vdslExtMCMMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229)
)
vdslExtMCMMIB.setRevisions(
        ("2005-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VdslLineExtMCMMib_ObjectIdentity = ObjectIdentity
vdslLineExtMCMMib = _VdslLineExtMCMMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229, 1)
)
_VdslLineExtMCMMibObjects_ObjectIdentity = ObjectIdentity
vdslLineExtMCMMibObjects = _VdslLineExtMCMMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1)
)
_VdslLineMCMConfProfileTable_Object = MibTable
vdslLineMCMConfProfileTable = _VdslLineMCMConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTable.setStatus("current")
_VdslLineMCMConfProfileEntry_Object = MibTableRow
vdslLineMCMConfProfileEntry = _VdslLineMCMConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 1, 1)
)
vdslLineMCMConfProfileEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileEntry.setStatus("current")


class _VdslLineMCMConfProfileTxWindowLength_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxWindowLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VdslLineMCMConfProfileTxWindowLength_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxWindowLength_Object = MibTableColumn
vdslLineMCMConfProfileTxWindowLength = _VdslLineMCMConfProfileTxWindowLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 1, 1, 1),
    _VdslLineMCMConfProfileTxWindowLength_Type()
)
vdslLineMCMConfProfileTxWindowLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxWindowLength.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxWindowLength.setUnits("samples")
_VdslLineMCMConfProfileRowStatus_Type = RowStatus
_VdslLineMCMConfProfileRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileRowStatus = _VdslLineMCMConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 1, 1, 2),
    _VdslLineMCMConfProfileRowStatus_Type()
)
vdslLineMCMConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRowStatus.setStatus("current")
_VdslLineMCMConfProfileTxBandTable_Object = MibTable
vdslLineMCMConfProfileTxBandTable = _VdslLineMCMConfProfileTxBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandTable.setStatus("current")
_VdslLineMCMConfProfileTxBandEntry_Object = MibTableRow
vdslLineMCMConfProfileTxBandEntry = _VdslLineMCMConfProfileTxBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2, 1)
)
vdslLineMCMConfProfileTxBandEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxBandNumber"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandEntry.setStatus("current")


class _VdslLineMCMConfProfileTxBandNumber_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxBandNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileTxBandNumber_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxBandNumber_Object = MibTableColumn
vdslLineMCMConfProfileTxBandNumber = _VdslLineMCMConfProfileTxBandNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2, 1, 1),
    _VdslLineMCMConfProfileTxBandNumber_Type()
)
vdslLineMCMConfProfileTxBandNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandNumber.setStatus("current")


class _VdslLineMCMConfProfileTxBandStart_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxBandStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileTxBandStart_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxBandStart_Object = MibTableColumn
vdslLineMCMConfProfileTxBandStart = _VdslLineMCMConfProfileTxBandStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2, 1, 2),
    _VdslLineMCMConfProfileTxBandStart_Type()
)
vdslLineMCMConfProfileTxBandStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandStart.setStatus("current")


class _VdslLineMCMConfProfileTxBandStop_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxBandStop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileTxBandStop_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxBandStop_Object = MibTableColumn
vdslLineMCMConfProfileTxBandStop = _VdslLineMCMConfProfileTxBandStop_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2, 1, 3),
    _VdslLineMCMConfProfileTxBandStop_Type()
)
vdslLineMCMConfProfileTxBandStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandStop.setStatus("current")
_VdslLineMCMConfProfileTxBandRowStatus_Type = RowStatus
_VdslLineMCMConfProfileTxBandRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileTxBandRowStatus = _VdslLineMCMConfProfileTxBandRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 2, 1, 4),
    _VdslLineMCMConfProfileTxBandRowStatus_Type()
)
vdslLineMCMConfProfileTxBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxBandRowStatus.setStatus("current")
_VdslLineMCMConfProfileRxBandTable_Object = MibTable
vdslLineMCMConfProfileRxBandTable = _VdslLineMCMConfProfileRxBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandTable.setStatus("current")
_VdslLineMCMConfProfileRxBandEntry_Object = MibTableRow
vdslLineMCMConfProfileRxBandEntry = _VdslLineMCMConfProfileRxBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3, 1)
)
vdslLineMCMConfProfileRxBandEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileRxBandNumber"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandEntry.setStatus("current")


class _VdslLineMCMConfProfileRxBandNumber_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileRxBandNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileRxBandNumber_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileRxBandNumber_Object = MibTableColumn
vdslLineMCMConfProfileRxBandNumber = _VdslLineMCMConfProfileRxBandNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3, 1, 1),
    _VdslLineMCMConfProfileRxBandNumber_Type()
)
vdslLineMCMConfProfileRxBandNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandNumber.setStatus("current")


class _VdslLineMCMConfProfileRxBandStart_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileRxBandStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileRxBandStart_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileRxBandStart_Object = MibTableColumn
vdslLineMCMConfProfileRxBandStart = _VdslLineMCMConfProfileRxBandStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3, 1, 2),
    _VdslLineMCMConfProfileRxBandStart_Type()
)
vdslLineMCMConfProfileRxBandStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandStart.setStatus("current")


class _VdslLineMCMConfProfileRxBandStop_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileRxBandStop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileRxBandStop_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileRxBandStop_Object = MibTableColumn
vdslLineMCMConfProfileRxBandStop = _VdslLineMCMConfProfileRxBandStop_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3, 1, 3),
    _VdslLineMCMConfProfileRxBandStop_Type()
)
vdslLineMCMConfProfileRxBandStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandStop.setStatus("current")
_VdslLineMCMConfProfileRxBandRowStatus_Type = RowStatus
_VdslLineMCMConfProfileRxBandRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileRxBandRowStatus = _VdslLineMCMConfProfileRxBandRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 3, 1, 4),
    _VdslLineMCMConfProfileRxBandRowStatus_Type()
)
vdslLineMCMConfProfileRxBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileRxBandRowStatus.setStatus("current")
_VdslLineMCMConfProfileTxPSDTable_Object = MibTable
vdslLineMCMConfProfileTxPSDTable = _VdslLineMCMConfProfileTxPSDTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDTable.setStatus("current")
_VdslLineMCMConfProfileTxPSDEntry_Object = MibTableRow
vdslLineMCMConfProfileTxPSDEntry = _VdslLineMCMConfProfileTxPSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4, 1)
)
vdslLineMCMConfProfileTxPSDEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxPSDNumber"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDEntry.setStatus("current")


class _VdslLineMCMConfProfileTxPSDNumber_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxPSDNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileTxPSDNumber_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxPSDNumber_Object = MibTableColumn
vdslLineMCMConfProfileTxPSDNumber = _VdslLineMCMConfProfileTxPSDNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4, 1, 1),
    _VdslLineMCMConfProfileTxPSDNumber_Type()
)
vdslLineMCMConfProfileTxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDNumber.setStatus("current")


class _VdslLineMCMConfProfileTxPSDTone_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileTxPSDTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileTxPSDTone_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileTxPSDTone_Object = MibTableColumn
vdslLineMCMConfProfileTxPSDTone = _VdslLineMCMConfProfileTxPSDTone_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4, 1, 2),
    _VdslLineMCMConfProfileTxPSDTone_Type()
)
vdslLineMCMConfProfileTxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDTone.setStatus("current")
_VdslLineMCMConfProfileTxPSDPSD_Type = Unsigned32
_VdslLineMCMConfProfileTxPSDPSD_Object = MibTableColumn
vdslLineMCMConfProfileTxPSDPSD = _VdslLineMCMConfProfileTxPSDPSD_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4, 1, 3),
    _VdslLineMCMConfProfileTxPSDPSD_Type()
)
vdslLineMCMConfProfileTxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDPSD.setUnits("0.5dBm/Hz")
_VdslLineMCMConfProfileTxPSDRowStatus_Type = RowStatus
_VdslLineMCMConfProfileTxPSDRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileTxPSDRowStatus = _VdslLineMCMConfProfileTxPSDRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 4, 1, 4),
    _VdslLineMCMConfProfileTxPSDRowStatus_Type()
)
vdslLineMCMConfProfileTxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileTxPSDRowStatus.setStatus("current")
_VdslLineMCMConfProfileMaxTxPSDTable_Object = MibTable
vdslLineMCMConfProfileMaxTxPSDTable = _VdslLineMCMConfProfileMaxTxPSDTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDTable.setStatus("current")
_VdslLineMCMConfProfileMaxTxPSDEntry_Object = MibTableRow
vdslLineMCMConfProfileMaxTxPSDEntry = _VdslLineMCMConfProfileMaxTxPSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5, 1)
)
vdslLineMCMConfProfileMaxTxPSDEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxTxPSDNumber"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDEntry.setStatus("current")


class _VdslLineMCMConfProfileMaxTxPSDNumber_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileMaxTxPSDNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileMaxTxPSDNumber_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileMaxTxPSDNumber_Object = MibTableColumn
vdslLineMCMConfProfileMaxTxPSDNumber = _VdslLineMCMConfProfileMaxTxPSDNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5, 1, 1),
    _VdslLineMCMConfProfileMaxTxPSDNumber_Type()
)
vdslLineMCMConfProfileMaxTxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDNumber.setStatus("current")


class _VdslLineMCMConfProfileMaxTxPSDTone_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileMaxTxPSDTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileMaxTxPSDTone_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileMaxTxPSDTone_Object = MibTableColumn
vdslLineMCMConfProfileMaxTxPSDTone = _VdslLineMCMConfProfileMaxTxPSDTone_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5, 1, 2),
    _VdslLineMCMConfProfileMaxTxPSDTone_Type()
)
vdslLineMCMConfProfileMaxTxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDTone.setStatus("current")
_VdslLineMCMConfProfileMaxTxPSDPSD_Type = Unsigned32
_VdslLineMCMConfProfileMaxTxPSDPSD_Object = MibTableColumn
vdslLineMCMConfProfileMaxTxPSDPSD = _VdslLineMCMConfProfileMaxTxPSDPSD_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5, 1, 3),
    _VdslLineMCMConfProfileMaxTxPSDPSD_Type()
)
vdslLineMCMConfProfileMaxTxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDPSD.setUnits("0.5dBm/Hz")
_VdslLineMCMConfProfileMaxTxPSDRowStatus_Type = RowStatus
_VdslLineMCMConfProfileMaxTxPSDRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileMaxTxPSDRowStatus = _VdslLineMCMConfProfileMaxTxPSDRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 5, 1, 4),
    _VdslLineMCMConfProfileMaxTxPSDRowStatus_Type()
)
vdslLineMCMConfProfileMaxTxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxTxPSDRowStatus.setStatus("current")
_VdslLineMCMConfProfileMaxRxPSDTable_Object = MibTable
vdslLineMCMConfProfileMaxRxPSDTable = _VdslLineMCMConfProfileMaxRxPSDTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6)
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDTable.setStatus("current")
_VdslLineMCMConfProfileMaxRxPSDEntry_Object = MibTableRow
vdslLineMCMConfProfileMaxRxPSDEntry = _VdslLineMCMConfProfileMaxRxPSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6, 1)
)
vdslLineMCMConfProfileMaxRxPSDEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxRxPSDNumber"),
)
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDEntry.setStatus("current")


class _VdslLineMCMConfProfileMaxRxPSDNumber_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileMaxRxPSDNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileMaxRxPSDNumber_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileMaxRxPSDNumber_Object = MibTableColumn
vdslLineMCMConfProfileMaxRxPSDNumber = _VdslLineMCMConfProfileMaxRxPSDNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6, 1, 1),
    _VdslLineMCMConfProfileMaxRxPSDNumber_Type()
)
vdslLineMCMConfProfileMaxRxPSDNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDNumber.setStatus("current")


class _VdslLineMCMConfProfileMaxRxPSDTone_Type(Unsigned32):
    """Custom type vdslLineMCMConfProfileMaxRxPSDTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VdslLineMCMConfProfileMaxRxPSDTone_Type.__name__ = "Unsigned32"
_VdslLineMCMConfProfileMaxRxPSDTone_Object = MibTableColumn
vdslLineMCMConfProfileMaxRxPSDTone = _VdslLineMCMConfProfileMaxRxPSDTone_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6, 1, 2),
    _VdslLineMCMConfProfileMaxRxPSDTone_Type()
)
vdslLineMCMConfProfileMaxRxPSDTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDTone.setStatus("current")
_VdslLineMCMConfProfileMaxRxPSDPSD_Type = Unsigned32
_VdslLineMCMConfProfileMaxRxPSDPSD_Object = MibTableColumn
vdslLineMCMConfProfileMaxRxPSDPSD = _VdslLineMCMConfProfileMaxRxPSDPSD_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6, 1, 3),
    _VdslLineMCMConfProfileMaxRxPSDPSD_Type()
)
vdslLineMCMConfProfileMaxRxPSDPSD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDPSD.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDPSD.setUnits("0.5dBm/Hz")
_VdslLineMCMConfProfileMaxRxPSDRowStatus_Type = RowStatus
_VdslLineMCMConfProfileMaxRxPSDRowStatus_Object = MibTableColumn
vdslLineMCMConfProfileMaxRxPSDRowStatus = _VdslLineMCMConfProfileMaxRxPSDRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 1, 6, 1, 4),
    _VdslLineMCMConfProfileMaxRxPSDRowStatus_Type()
)
vdslLineMCMConfProfileMaxRxPSDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineMCMConfProfileMaxRxPSDRowStatus.setStatus("current")
_VdslLineExtMCMConformance_ObjectIdentity = ObjectIdentity
vdslLineExtMCMConformance = _VdslLineExtMCMConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 2)
)
_VdslLineExtMCMGroups_ObjectIdentity = ObjectIdentity
vdslLineExtMCMGroups = _VdslLineExtMCMGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 2, 1)
)
_VdslLineExtMCMCompliances_ObjectIdentity = ObjectIdentity
vdslLineExtMCMCompliances = _VdslLineExtMCMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 2, 2)
)

# Managed Objects groups

vdslLineExtMCMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 2, 1, 1)
)
vdslLineExtMCMGroup.setObjects(
      *(("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxWindowLength"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileRowStatus"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxBandStart"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxBandStop"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxBandRowStatus"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileRxBandStart"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileRxBandStop"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileRxBandRowStatus"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxPSDTone"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxPSDPSD"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileTxPSDRowStatus"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxTxPSDTone"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxTxPSDPSD"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxTxPSDRowStatus"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxRxPSDTone"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxRxPSDPSD"),
        ("VDSL-LINE-EXT-MCM-MIB", "vdslLineMCMConfProfileMaxRxPSDRowStatus"))
)
if mibBuilder.loadTexts:
    vdslLineExtMCMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vdslLineExtMCMMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 229, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vdslLineExtMCMMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VDSL-LINE-EXT-MCM-MIB",
    **{"vdslExtMCMMIB": vdslExtMCMMIB,
       "vdslLineExtMCMMib": vdslLineExtMCMMib,
       "vdslLineExtMCMMibObjects": vdslLineExtMCMMibObjects,
       "vdslLineMCMConfProfileTable": vdslLineMCMConfProfileTable,
       "vdslLineMCMConfProfileEntry": vdslLineMCMConfProfileEntry,
       "vdslLineMCMConfProfileTxWindowLength": vdslLineMCMConfProfileTxWindowLength,
       "vdslLineMCMConfProfileRowStatus": vdslLineMCMConfProfileRowStatus,
       "vdslLineMCMConfProfileTxBandTable": vdslLineMCMConfProfileTxBandTable,
       "vdslLineMCMConfProfileTxBandEntry": vdslLineMCMConfProfileTxBandEntry,
       "vdslLineMCMConfProfileTxBandNumber": vdslLineMCMConfProfileTxBandNumber,
       "vdslLineMCMConfProfileTxBandStart": vdslLineMCMConfProfileTxBandStart,
       "vdslLineMCMConfProfileTxBandStop": vdslLineMCMConfProfileTxBandStop,
       "vdslLineMCMConfProfileTxBandRowStatus": vdslLineMCMConfProfileTxBandRowStatus,
       "vdslLineMCMConfProfileRxBandTable": vdslLineMCMConfProfileRxBandTable,
       "vdslLineMCMConfProfileRxBandEntry": vdslLineMCMConfProfileRxBandEntry,
       "vdslLineMCMConfProfileRxBandNumber": vdslLineMCMConfProfileRxBandNumber,
       "vdslLineMCMConfProfileRxBandStart": vdslLineMCMConfProfileRxBandStart,
       "vdslLineMCMConfProfileRxBandStop": vdslLineMCMConfProfileRxBandStop,
       "vdslLineMCMConfProfileRxBandRowStatus": vdslLineMCMConfProfileRxBandRowStatus,
       "vdslLineMCMConfProfileTxPSDTable": vdslLineMCMConfProfileTxPSDTable,
       "vdslLineMCMConfProfileTxPSDEntry": vdslLineMCMConfProfileTxPSDEntry,
       "vdslLineMCMConfProfileTxPSDNumber": vdslLineMCMConfProfileTxPSDNumber,
       "vdslLineMCMConfProfileTxPSDTone": vdslLineMCMConfProfileTxPSDTone,
       "vdslLineMCMConfProfileTxPSDPSD": vdslLineMCMConfProfileTxPSDPSD,
       "vdslLineMCMConfProfileTxPSDRowStatus": vdslLineMCMConfProfileTxPSDRowStatus,
       "vdslLineMCMConfProfileMaxTxPSDTable": vdslLineMCMConfProfileMaxTxPSDTable,
       "vdslLineMCMConfProfileMaxTxPSDEntry": vdslLineMCMConfProfileMaxTxPSDEntry,
       "vdslLineMCMConfProfileMaxTxPSDNumber": vdslLineMCMConfProfileMaxTxPSDNumber,
       "vdslLineMCMConfProfileMaxTxPSDTone": vdslLineMCMConfProfileMaxTxPSDTone,
       "vdslLineMCMConfProfileMaxTxPSDPSD": vdslLineMCMConfProfileMaxTxPSDPSD,
       "vdslLineMCMConfProfileMaxTxPSDRowStatus": vdslLineMCMConfProfileMaxTxPSDRowStatus,
       "vdslLineMCMConfProfileMaxRxPSDTable": vdslLineMCMConfProfileMaxRxPSDTable,
       "vdslLineMCMConfProfileMaxRxPSDEntry": vdslLineMCMConfProfileMaxRxPSDEntry,
       "vdslLineMCMConfProfileMaxRxPSDNumber": vdslLineMCMConfProfileMaxRxPSDNumber,
       "vdslLineMCMConfProfileMaxRxPSDTone": vdslLineMCMConfProfileMaxRxPSDTone,
       "vdslLineMCMConfProfileMaxRxPSDPSD": vdslLineMCMConfProfileMaxRxPSDPSD,
       "vdslLineMCMConfProfileMaxRxPSDRowStatus": vdslLineMCMConfProfileMaxRxPSDRowStatus,
       "vdslLineExtMCMConformance": vdslLineExtMCMConformance,
       "vdslLineExtMCMGroups": vdslLineExtMCMGroups,
       "vdslLineExtMCMGroup": vdslLineExtMCMGroup,
       "vdslLineExtMCMCompliances": vdslLineExtMCMCompliances,
       "vdslLineExtMCMMibCompliance": vdslLineExtMCMMibCompliance}
)
