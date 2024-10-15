# SNMP MIB module (HIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:48 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_MdmHist_ObjectIdentity = ObjectIdentity
mdmHist = _MdmHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 30)
)
_MdmNacHistCurrentTable_Object = MibTable
mdmNacHistCurrentTable = _MdmNacHistCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1)
)
if mibBuilder.loadTexts:
    mdmNacHistCurrentTable.setStatus("mandatory")
_MdmNacHistCurrentEntry_Object = MibTableRow
mdmNacHistCurrentEntry = _MdmNacHistCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1, 1)
)
mdmNacHistCurrentEntry.setIndexNames(
    (0, "HIST-MIB", "mdmNacHistCurrentIndex"),
)
if mibBuilder.loadTexts:
    mdmNacHistCurrentEntry.setStatus("mandatory")
_MdmNacHistCurrentIndex_Type = Integer32
_MdmNacHistCurrentIndex_Object = MibTableColumn
mdmNacHistCurrentIndex = _MdmNacHistCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1, 1, 1),
    _MdmNacHistCurrentIndex_Type()
)
mdmNacHistCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistCurrentIndex.setStatus("mandatory")
_MdmNacHistCurrentStartTime_Type = Integer32
_MdmNacHistCurrentStartTime_Object = MibTableColumn
mdmNacHistCurrentStartTime = _MdmNacHistCurrentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1, 1, 2),
    _MdmNacHistCurrentStartTime_Type()
)
mdmNacHistCurrentStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistCurrentStartTime.setStatus("mandatory")
_MdmNacHistCurrentMgmtBusFailures_Type = Gauge32
_MdmNacHistCurrentMgmtBusFailures_Object = MibTableColumn
mdmNacHistCurrentMgmtBusFailures = _MdmNacHistCurrentMgmtBusFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1, 1, 3),
    _MdmNacHistCurrentMgmtBusFailures_Type()
)
mdmNacHistCurrentMgmtBusFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistCurrentMgmtBusFailures.setStatus("mandatory")
_MdmNacHistCurrentWatchdogTimouts_Type = Gauge32
_MdmNacHistCurrentWatchdogTimouts_Object = MibTableColumn
mdmNacHistCurrentWatchdogTimouts = _MdmNacHistCurrentWatchdogTimouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 1, 1, 4),
    _MdmNacHistCurrentWatchdogTimouts_Type()
)
mdmNacHistCurrentWatchdogTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistCurrentWatchdogTimouts.setStatus("mandatory")
_MdmNacHistIntervalTable_Object = MibTable
mdmNacHistIntervalTable = _MdmNacHistIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2)
)
if mibBuilder.loadTexts:
    mdmNacHistIntervalTable.setStatus("mandatory")
_MdmNacHistIntervalEntry_Object = MibTableRow
mdmNacHistIntervalEntry = _MdmNacHistIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1)
)
mdmNacHistIntervalEntry.setIndexNames(
    (0, "HIST-MIB", "mdmNacHistIntervalIndex"),
    (0, "HIST-MIB", "mdmNacHistIntervalNumber"),
)
if mibBuilder.loadTexts:
    mdmNacHistIntervalEntry.setStatus("mandatory")
_MdmNacHistIntervalIndex_Type = Integer32
_MdmNacHistIntervalIndex_Object = MibTableColumn
mdmNacHistIntervalIndex = _MdmNacHistIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1, 1),
    _MdmNacHistIntervalIndex_Type()
)
mdmNacHistIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistIntervalIndex.setStatus("mandatory")


class _MdmNacHistIntervalNumber_Type(Integer32):
    """Custom type mdmNacHistIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_MdmNacHistIntervalNumber_Type.__name__ = "Integer32"
_MdmNacHistIntervalNumber_Object = MibTableColumn
mdmNacHistIntervalNumber = _MdmNacHistIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1, 2),
    _MdmNacHistIntervalNumber_Type()
)
mdmNacHistIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistIntervalNumber.setStatus("mandatory")
_MdmNacHistIntervalStartTime_Type = Integer32
_MdmNacHistIntervalStartTime_Object = MibTableColumn
mdmNacHistIntervalStartTime = _MdmNacHistIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1, 3),
    _MdmNacHistIntervalStartTime_Type()
)
mdmNacHistIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistIntervalStartTime.setStatus("mandatory")
_MdmNacHistIntervalMgmtBusFailures_Type = Gauge32
_MdmNacHistIntervalMgmtBusFailures_Object = MibTableColumn
mdmNacHistIntervalMgmtBusFailures = _MdmNacHistIntervalMgmtBusFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1, 4),
    _MdmNacHistIntervalMgmtBusFailures_Type()
)
mdmNacHistIntervalMgmtBusFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistIntervalMgmtBusFailures.setStatus("mandatory")
_MdmNacHistIntervalWatchdogTimouts_Type = Gauge32
_MdmNacHistIntervalWatchdogTimouts_Object = MibTableColumn
mdmNacHistIntervalWatchdogTimouts = _MdmNacHistIntervalWatchdogTimouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 2, 1, 5),
    _MdmNacHistIntervalWatchdogTimouts_Type()
)
mdmNacHistIntervalWatchdogTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmNacHistIntervalWatchdogTimouts.setStatus("mandatory")
_MdmHistCurrentTable_Object = MibTable
mdmHistCurrentTable = _MdmHistCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3)
)
if mibBuilder.loadTexts:
    mdmHistCurrentTable.setStatus("mandatory")
_MdmHistCurrentEntry_Object = MibTableRow
mdmHistCurrentEntry = _MdmHistCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1)
)
mdmHistCurrentEntry.setIndexNames(
    (0, "HIST-MIB", "mdmHistCurrentIndex"),
)
if mibBuilder.loadTexts:
    mdmHistCurrentEntry.setStatus("mandatory")
_MdmHistCurrentIndex_Type = Integer32
_MdmHistCurrentIndex_Object = MibTableColumn
mdmHistCurrentIndex = _MdmHistCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 1),
    _MdmHistCurrentIndex_Type()
)
mdmHistCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentIndex.setStatus("mandatory")
_MdmHistCurrentStartTime_Type = Integer32
_MdmHistCurrentStartTime_Object = MibTableColumn
mdmHistCurrentStartTime = _MdmHistCurrentStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 2),
    _MdmHistCurrentStartTime_Type()
)
mdmHistCurrentStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentStartTime.setStatus("mandatory")
_MdmHistCurrentInConnectEstabs_Type = Gauge32
_MdmHistCurrentInConnectEstabs_Object = MibTableColumn
mdmHistCurrentInConnectEstabs = _MdmHistCurrentInConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 3),
    _MdmHistCurrentInConnectEstabs_Type()
)
mdmHistCurrentInConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInConnectEstabs.setStatus("mandatory")
_MdmHistCurrentInConnectFailures_Type = Gauge32
_MdmHistCurrentInConnectFailures_Object = MibTableColumn
mdmHistCurrentInConnectFailures = _MdmHistCurrentInConnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 4),
    _MdmHistCurrentInConnectFailures_Type()
)
mdmHistCurrentInConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInConnectFailures.setStatus("mandatory")
_MdmHistCurrentInConnectTerms_Type = Gauge32
_MdmHistCurrentInConnectTerms_Object = MibTableColumn
mdmHistCurrentInConnectTerms = _MdmHistCurrentInConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 5),
    _MdmHistCurrentInConnectTerms_Type()
)
mdmHistCurrentInConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInConnectTerms.setStatus("mandatory")
_MdmHistCurrentInConnectTime_Type = Gauge32
_MdmHistCurrentInConnectTime_Object = MibTableColumn
mdmHistCurrentInConnectTime = _MdmHistCurrentInConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 6),
    _MdmHistCurrentInConnectTime_Type()
)
mdmHistCurrentInConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInConnectTime.setStatus("mandatory")
_MdmHistCurrentInTotalBytesRx_Type = Gauge32
_MdmHistCurrentInTotalBytesRx_Object = MibTableColumn
mdmHistCurrentInTotalBytesRx = _MdmHistCurrentInTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 7),
    _MdmHistCurrentInTotalBytesRx_Type()
)
mdmHistCurrentInTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInTotalBytesRx.setStatus("mandatory")
_MdmHistCurrentInTotalBytesTx_Type = Gauge32
_MdmHistCurrentInTotalBytesTx_Object = MibTableColumn
mdmHistCurrentInTotalBytesTx = _MdmHistCurrentInTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 8),
    _MdmHistCurrentInTotalBytesTx_Type()
)
mdmHistCurrentInTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentInTotalBytesTx.setStatus("mandatory")
_MdmHistCurrentOutConnectEstabs_Type = Gauge32
_MdmHistCurrentOutConnectEstabs_Object = MibTableColumn
mdmHistCurrentOutConnectEstabs = _MdmHistCurrentOutConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 9),
    _MdmHistCurrentOutConnectEstabs_Type()
)
mdmHistCurrentOutConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutConnectEstabs.setStatus("mandatory")
_MdmHistCurrentOutConnectFailures_Type = Gauge32
_MdmHistCurrentOutConnectFailures_Object = MibTableColumn
mdmHistCurrentOutConnectFailures = _MdmHistCurrentOutConnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 10),
    _MdmHistCurrentOutConnectFailures_Type()
)
mdmHistCurrentOutConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutConnectFailures.setStatus("mandatory")
_MdmHistCurrentOutConnectTerms_Type = Gauge32
_MdmHistCurrentOutConnectTerms_Object = MibTableColumn
mdmHistCurrentOutConnectTerms = _MdmHistCurrentOutConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 11),
    _MdmHistCurrentOutConnectTerms_Type()
)
mdmHistCurrentOutConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutConnectTerms.setStatus("mandatory")
_MdmHistCurrentOutConnectTime_Type = Gauge32
_MdmHistCurrentOutConnectTime_Object = MibTableColumn
mdmHistCurrentOutConnectTime = _MdmHistCurrentOutConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 12),
    _MdmHistCurrentOutConnectTime_Type()
)
mdmHistCurrentOutConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutConnectTime.setStatus("mandatory")
_MdmHistCurrentOutTotalBytesRx_Type = Gauge32
_MdmHistCurrentOutTotalBytesRx_Object = MibTableColumn
mdmHistCurrentOutTotalBytesRx = _MdmHistCurrentOutTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 13),
    _MdmHistCurrentOutTotalBytesRx_Type()
)
mdmHistCurrentOutTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutTotalBytesRx.setStatus("mandatory")
_MdmHistCurrentOutTotalBytesTx_Type = Gauge32
_MdmHistCurrentOutTotalBytesTx_Object = MibTableColumn
mdmHistCurrentOutTotalBytesTx = _MdmHistCurrentOutTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 14),
    _MdmHistCurrentOutTotalBytesTx_Type()
)
mdmHistCurrentOutTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentOutTotalBytesTx.setStatus("mandatory")
_MdmHistCurrentBlers_Type = Gauge32
_MdmHistCurrentBlers_Object = MibTableColumn
mdmHistCurrentBlers = _MdmHistCurrentBlers_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 15),
    _MdmHistCurrentBlers_Type()
)
mdmHistCurrentBlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentBlers.setStatus("mandatory")
_MdmHistCurrentFallBacks_Type = Gauge32
_MdmHistCurrentFallBacks_Object = MibTableColumn
mdmHistCurrentFallBacks = _MdmHistCurrentFallBacks_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 3, 1, 16),
    _MdmHistCurrentFallBacks_Type()
)
mdmHistCurrentFallBacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistCurrentFallBacks.setStatus("mandatory")
_MdmHistIntervalTable_Object = MibTable
mdmHistIntervalTable = _MdmHistIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4)
)
if mibBuilder.loadTexts:
    mdmHistIntervalTable.setStatus("mandatory")
_MdmHistIntervalEntry_Object = MibTableRow
mdmHistIntervalEntry = _MdmHistIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1)
)
mdmHistIntervalEntry.setIndexNames(
    (0, "HIST-MIB", "mdmHistIntervalIndex"),
    (0, "HIST-MIB", "mdmHistIntervalNumber"),
)
if mibBuilder.loadTexts:
    mdmHistIntervalEntry.setStatus("mandatory")
_MdmHistIntervalIndex_Type = Integer32
_MdmHistIntervalIndex_Object = MibTableColumn
mdmHistIntervalIndex = _MdmHistIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 1),
    _MdmHistIntervalIndex_Type()
)
mdmHistIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalIndex.setStatus("mandatory")


class _MdmHistIntervalNumber_Type(Integer32):
    """Custom type mdmHistIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_MdmHistIntervalNumber_Type.__name__ = "Integer32"
_MdmHistIntervalNumber_Object = MibTableColumn
mdmHistIntervalNumber = _MdmHistIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 2),
    _MdmHistIntervalNumber_Type()
)
mdmHistIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalNumber.setStatus("mandatory")
_MdmHistIntervalStartTime_Type = Integer32
_MdmHistIntervalStartTime_Object = MibTableColumn
mdmHistIntervalStartTime = _MdmHistIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 3),
    _MdmHistIntervalStartTime_Type()
)
mdmHistIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalStartTime.setStatus("mandatory")
_MdmHistIntervalInConnectEstabs_Type = Gauge32
_MdmHistIntervalInConnectEstabs_Object = MibTableColumn
mdmHistIntervalInConnectEstabs = _MdmHistIntervalInConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 4),
    _MdmHistIntervalInConnectEstabs_Type()
)
mdmHistIntervalInConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInConnectEstabs.setStatus("mandatory")
_MdmHistIntervalInConnectFailures_Type = Gauge32
_MdmHistIntervalInConnectFailures_Object = MibTableColumn
mdmHistIntervalInConnectFailures = _MdmHistIntervalInConnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 5),
    _MdmHistIntervalInConnectFailures_Type()
)
mdmHistIntervalInConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInConnectFailures.setStatus("mandatory")
_MdmHistIntervalInConnectTerms_Type = Gauge32
_MdmHistIntervalInConnectTerms_Object = MibTableColumn
mdmHistIntervalInConnectTerms = _MdmHistIntervalInConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 6),
    _MdmHistIntervalInConnectTerms_Type()
)
mdmHistIntervalInConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInConnectTerms.setStatus("mandatory")
_MdmHistIntervalInConnectTime_Type = Gauge32
_MdmHistIntervalInConnectTime_Object = MibTableColumn
mdmHistIntervalInConnectTime = _MdmHistIntervalInConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 7),
    _MdmHistIntervalInConnectTime_Type()
)
mdmHistIntervalInConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInConnectTime.setStatus("mandatory")
_MdmHistIntervalInTotalBytesRx_Type = Gauge32
_MdmHistIntervalInTotalBytesRx_Object = MibTableColumn
mdmHistIntervalInTotalBytesRx = _MdmHistIntervalInTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 8),
    _MdmHistIntervalInTotalBytesRx_Type()
)
mdmHistIntervalInTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInTotalBytesRx.setStatus("mandatory")
_MdmHistIntervalInTotalBytesTx_Type = Gauge32
_MdmHistIntervalInTotalBytesTx_Object = MibTableColumn
mdmHistIntervalInTotalBytesTx = _MdmHistIntervalInTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 9),
    _MdmHistIntervalInTotalBytesTx_Type()
)
mdmHistIntervalInTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalInTotalBytesTx.setStatus("mandatory")
_MdmHistIntervalOutConnectEstabs_Type = Gauge32
_MdmHistIntervalOutConnectEstabs_Object = MibTableColumn
mdmHistIntervalOutConnectEstabs = _MdmHistIntervalOutConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 10),
    _MdmHistIntervalOutConnectEstabs_Type()
)
mdmHistIntervalOutConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutConnectEstabs.setStatus("mandatory")
_MdmHistIntervalOutConnectFailures_Type = Gauge32
_MdmHistIntervalOutConnectFailures_Object = MibTableColumn
mdmHistIntervalOutConnectFailures = _MdmHistIntervalOutConnectFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 11),
    _MdmHistIntervalOutConnectFailures_Type()
)
mdmHistIntervalOutConnectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutConnectFailures.setStatus("mandatory")
_MdmHistIntervalOutConnectTerms_Type = Gauge32
_MdmHistIntervalOutConnectTerms_Object = MibTableColumn
mdmHistIntervalOutConnectTerms = _MdmHistIntervalOutConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 12),
    _MdmHistIntervalOutConnectTerms_Type()
)
mdmHistIntervalOutConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutConnectTerms.setStatus("mandatory")
_MdmHistIntervalOutConnectTime_Type = Gauge32
_MdmHistIntervalOutConnectTime_Object = MibTableColumn
mdmHistIntervalOutConnectTime = _MdmHistIntervalOutConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 13),
    _MdmHistIntervalOutConnectTime_Type()
)
mdmHistIntervalOutConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutConnectTime.setStatus("mandatory")
_MdmHistIntervalOutTotalBytesRx_Type = Gauge32
_MdmHistIntervalOutTotalBytesRx_Object = MibTableColumn
mdmHistIntervalOutTotalBytesRx = _MdmHistIntervalOutTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 14),
    _MdmHistIntervalOutTotalBytesRx_Type()
)
mdmHistIntervalOutTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutTotalBytesRx.setStatus("mandatory")
_MdmHistIntervalOutTotalBytesTx_Type = Gauge32
_MdmHistIntervalOutTotalBytesTx_Object = MibTableColumn
mdmHistIntervalOutTotalBytesTx = _MdmHistIntervalOutTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 15),
    _MdmHistIntervalOutTotalBytesTx_Type()
)
mdmHistIntervalOutTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalOutTotalBytesTx.setStatus("mandatory")
_MdmHistIntervalBlers_Type = Gauge32
_MdmHistIntervalBlers_Object = MibTableColumn
mdmHistIntervalBlers = _MdmHistIntervalBlers_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 16),
    _MdmHistIntervalBlers_Type()
)
mdmHistIntervalBlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalBlers.setStatus("mandatory")
_MdmHistIntervalFallBacks_Type = Gauge32
_MdmHistIntervalFallBacks_Object = MibTableColumn
mdmHistIntervalFallBacks = _MdmHistIntervalFallBacks_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 30, 4, 1, 17),
    _MdmHistIntervalFallBacks_Type()
)
mdmHistIntervalFallBacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHistIntervalFallBacks.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIST-MIB",
    **{"usr": usr,
       "nas": nas,
       "mdmHist": mdmHist,
       "mdmNacHistCurrentTable": mdmNacHistCurrentTable,
       "mdmNacHistCurrentEntry": mdmNacHistCurrentEntry,
       "mdmNacHistCurrentIndex": mdmNacHistCurrentIndex,
       "mdmNacHistCurrentStartTime": mdmNacHistCurrentStartTime,
       "mdmNacHistCurrentMgmtBusFailures": mdmNacHistCurrentMgmtBusFailures,
       "mdmNacHistCurrentWatchdogTimouts": mdmNacHistCurrentWatchdogTimouts,
       "mdmNacHistIntervalTable": mdmNacHistIntervalTable,
       "mdmNacHistIntervalEntry": mdmNacHistIntervalEntry,
       "mdmNacHistIntervalIndex": mdmNacHistIntervalIndex,
       "mdmNacHistIntervalNumber": mdmNacHistIntervalNumber,
       "mdmNacHistIntervalStartTime": mdmNacHistIntervalStartTime,
       "mdmNacHistIntervalMgmtBusFailures": mdmNacHistIntervalMgmtBusFailures,
       "mdmNacHistIntervalWatchdogTimouts": mdmNacHistIntervalWatchdogTimouts,
       "mdmHistCurrentTable": mdmHistCurrentTable,
       "mdmHistCurrentEntry": mdmHistCurrentEntry,
       "mdmHistCurrentIndex": mdmHistCurrentIndex,
       "mdmHistCurrentStartTime": mdmHistCurrentStartTime,
       "mdmHistCurrentInConnectEstabs": mdmHistCurrentInConnectEstabs,
       "mdmHistCurrentInConnectFailures": mdmHistCurrentInConnectFailures,
       "mdmHistCurrentInConnectTerms": mdmHistCurrentInConnectTerms,
       "mdmHistCurrentInConnectTime": mdmHistCurrentInConnectTime,
       "mdmHistCurrentInTotalBytesRx": mdmHistCurrentInTotalBytesRx,
       "mdmHistCurrentInTotalBytesTx": mdmHistCurrentInTotalBytesTx,
       "mdmHistCurrentOutConnectEstabs": mdmHistCurrentOutConnectEstabs,
       "mdmHistCurrentOutConnectFailures": mdmHistCurrentOutConnectFailures,
       "mdmHistCurrentOutConnectTerms": mdmHistCurrentOutConnectTerms,
       "mdmHistCurrentOutConnectTime": mdmHistCurrentOutConnectTime,
       "mdmHistCurrentOutTotalBytesRx": mdmHistCurrentOutTotalBytesRx,
       "mdmHistCurrentOutTotalBytesTx": mdmHistCurrentOutTotalBytesTx,
       "mdmHistCurrentBlers": mdmHistCurrentBlers,
       "mdmHistCurrentFallBacks": mdmHistCurrentFallBacks,
       "mdmHistIntervalTable": mdmHistIntervalTable,
       "mdmHistIntervalEntry": mdmHistIntervalEntry,
       "mdmHistIntervalIndex": mdmHistIntervalIndex,
       "mdmHistIntervalNumber": mdmHistIntervalNumber,
       "mdmHistIntervalStartTime": mdmHistIntervalStartTime,
       "mdmHistIntervalInConnectEstabs": mdmHistIntervalInConnectEstabs,
       "mdmHistIntervalInConnectFailures": mdmHistIntervalInConnectFailures,
       "mdmHistIntervalInConnectTerms": mdmHistIntervalInConnectTerms,
       "mdmHistIntervalInConnectTime": mdmHistIntervalInConnectTime,
       "mdmHistIntervalInTotalBytesRx": mdmHistIntervalInTotalBytesRx,
       "mdmHistIntervalInTotalBytesTx": mdmHistIntervalInTotalBytesTx,
       "mdmHistIntervalOutConnectEstabs": mdmHistIntervalOutConnectEstabs,
       "mdmHistIntervalOutConnectFailures": mdmHistIntervalOutConnectFailures,
       "mdmHistIntervalOutConnectTerms": mdmHistIntervalOutConnectTerms,
       "mdmHistIntervalOutConnectTime": mdmHistIntervalOutConnectTime,
       "mdmHistIntervalOutTotalBytesRx": mdmHistIntervalOutTotalBytesRx,
       "mdmHistIntervalOutTotalBytesTx": mdmHistIntervalOutTotalBytesTx,
       "mdmHistIntervalBlers": mdmHistIntervalBlers,
       "mdmHistIntervalFallBacks": mdmHistIntervalFallBacks}
)
