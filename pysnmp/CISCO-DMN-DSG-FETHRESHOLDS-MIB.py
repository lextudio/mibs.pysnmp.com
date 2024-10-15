# SNMP MIB module (CISCO-DMN-DSG-FETHRESHOLDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-FETHRESHOLDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:24 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGFeThresholds = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9)
)
ciscoDSGFeThresholds.setRevisions(
        ("2010-08-30 11:00",
         "2010-04-26 05:00",
         "2010-03-22 05:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MutingThresholdsTable_Object = MibTable
mutingThresholdsTable = _MutingThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mutingThresholdsTable.setStatus("current")
_MutingThresholdsEntry_Object = MibTableRow
mutingThresholdsEntry = _MutingThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1)
)
mutingThresholdsEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FETHRESHOLDS-MIB", "mutingThreshholdsInstance"),
)
if mibBuilder.loadTexts:
    mutingThresholdsEntry.setStatus("current")


class _MutingThreshholdsInstance_Type(Integer32):
    """Custom type mutingThreshholdsInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MutingThreshholdsInstance_Type.__name__ = "Integer32"
_MutingThreshholdsInstance_Object = MibTableColumn
mutingThreshholdsInstance = _MutingThreshholdsInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 1),
    _MutingThreshholdsInstance_Type()
)
mutingThreshholdsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mutingThreshholdsInstance.setStatus("current")


class _MutThreshRestoreDefaults_Type(Integer32):
    """Custom type mutThreshRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_MutThreshRestoreDefaults_Type.__name__ = "Integer32"
_MutThreshRestoreDefaults_Object = MibTableColumn
mutThreshRestoreDefaults = _MutThreshRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 2),
    _MutThreshRestoreDefaults_Type()
)
mutThreshRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshRestoreDefaults.setStatus("current")


class _MutThreshControl_Type(Integer32):
    """Custom type mutThreshControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MutThreshControl_Type.__name__ = "Integer32"
_MutThreshControl_Object = MibTableColumn
mutThreshControl = _MutThreshControl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 3),
    _MutThreshControl_Type()
)
mutThreshControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshControl.setStatus("current")


class _MutThreshDVBSTransportMute_Type(Integer32):
    """Custom type mutThreshDVBSTransportMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBSTransportMute_Type.__name__ = "Integer32"
_MutThreshDVBSTransportMute_Object = MibTableColumn
mutThreshDVBSTransportMute = _MutThreshDVBSTransportMute_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 4),
    _MutThreshDVBSTransportMute_Type()
)
mutThreshDVBSTransportMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBSTransportMute.setStatus("current")


class _MutThreshDVBSTransportRestore_Type(Integer32):
    """Custom type mutThreshDVBSTransportRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBSTransportRestore_Type.__name__ = "Integer32"
_MutThreshDVBSTransportRestore_Object = MibTableColumn
mutThreshDVBSTransportRestore = _MutThreshDVBSTransportRestore_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 5),
    _MutThreshDVBSTransportRestore_Type()
)
mutThreshDVBSTransportRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBSTransportRestore.setStatus("current")


class _MutThreshDVBSAudioMute_Type(Integer32):
    """Custom type mutThreshDVBSAudioMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBSAudioMute_Type.__name__ = "Integer32"
_MutThreshDVBSAudioMute_Object = MibTableColumn
mutThreshDVBSAudioMute = _MutThreshDVBSAudioMute_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 6),
    _MutThreshDVBSAudioMute_Type()
)
mutThreshDVBSAudioMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBSAudioMute.setStatus("current")


class _MutThreshDVBSAudioRestore_Type(Integer32):
    """Custom type mutThreshDVBSAudioRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBSAudioRestore_Type.__name__ = "Integer32"
_MutThreshDVBSAudioRestore_Object = MibTableColumn
mutThreshDVBSAudioRestore = _MutThreshDVBSAudioRestore_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 7),
    _MutThreshDVBSAudioRestore_Type()
)
mutThreshDVBSAudioRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBSAudioRestore.setStatus("current")


class _MutThreshDVBS2TransportMute_Type(Integer32):
    """Custom type mutThreshDVBS2TransportMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBS2TransportMute_Type.__name__ = "Integer32"
_MutThreshDVBS2TransportMute_Object = MibTableColumn
mutThreshDVBS2TransportMute = _MutThreshDVBS2TransportMute_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 8),
    _MutThreshDVBS2TransportMute_Type()
)
mutThreshDVBS2TransportMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBS2TransportMute.setStatus("current")


class _MutThreshDVBS2TransportRestore_Type(Integer32):
    """Custom type mutThreshDVBS2TransportRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBS2TransportRestore_Type.__name__ = "Integer32"
_MutThreshDVBS2TransportRestore_Object = MibTableColumn
mutThreshDVBS2TransportRestore = _MutThreshDVBS2TransportRestore_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 9),
    _MutThreshDVBS2TransportRestore_Type()
)
mutThreshDVBS2TransportRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBS2TransportRestore.setStatus("current")


class _MutThreshDVBS2AudioMute_Type(Integer32):
    """Custom type mutThreshDVBS2AudioMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBS2AudioMute_Type.__name__ = "Integer32"
_MutThreshDVBS2AudioMute_Object = MibTableColumn
mutThreshDVBS2AudioMute = _MutThreshDVBS2AudioMute_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 10),
    _MutThreshDVBS2AudioMute_Type()
)
mutThreshDVBS2AudioMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBS2AudioMute.setStatus("current")


class _MutThreshDVBS2AudioRestore_Type(Integer32):
    """Custom type mutThreshDVBS2AudioRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 200),
    )


_MutThreshDVBS2AudioRestore_Type.__name__ = "Integer32"
_MutThreshDVBS2AudioRestore_Object = MibTableColumn
mutThreshDVBS2AudioRestore = _MutThreshDVBS2AudioRestore_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 9, 1, 1, 11),
    _MutThreshDVBS2AudioRestore_Type()
)
mutThreshDVBS2AudioRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mutThreshDVBS2AudioRestore.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-FETHRESHOLDS-MIB",
    **{"ciscoDSGFeThresholds": ciscoDSGFeThresholds,
       "mutingThresholdsTable": mutingThresholdsTable,
       "mutingThresholdsEntry": mutingThresholdsEntry,
       "mutingThreshholdsInstance": mutingThreshholdsInstance,
       "mutThreshRestoreDefaults": mutThreshRestoreDefaults,
       "mutThreshControl": mutThreshControl,
       "mutThreshDVBSTransportMute": mutThreshDVBSTransportMute,
       "mutThreshDVBSTransportRestore": mutThreshDVBSTransportRestore,
       "mutThreshDVBSAudioMute": mutThreshDVBSAudioMute,
       "mutThreshDVBSAudioRestore": mutThreshDVBSAudioRestore,
       "mutThreshDVBS2TransportMute": mutThreshDVBS2TransportMute,
       "mutThreshDVBS2TransportRestore": mutThreshDVBS2TransportRestore,
       "mutThreshDVBS2AudioMute": mutThreshDVBS2AudioMute,
       "mutThreshDVBS2AudioRestore": mutThreshDVBS2AudioRestore}
)
