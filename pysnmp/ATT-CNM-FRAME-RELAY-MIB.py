# SNMP MIB module (ATT-CNM-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:18 2024
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

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_fr_ObjectIdentity = ObjectIdentity
att_cnm_fr = _Att_cnm_fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7)
)
_AttCNMfrConfigTable_Object = MibTable
attCNMfrConfigTable = _AttCNMfrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1)
)
if mibBuilder.loadTexts:
    attCNMfrConfigTable.setStatus("mandatory")
_AttCNMfrConfigEntry_Object = MibTableRow
attCNMfrConfigEntry = _AttCNMfrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1)
)
attCNMfrConfigEntry.setIndexNames(
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMfrConfigEntry.setStatus("mandatory")
_AttCNMfrConfigIndex_Type = Integer32
_AttCNMfrConfigIndex_Object = MibTableColumn
attCNMfrConfigIndex = _AttCNMfrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 1),
    _AttCNMfrConfigIndex_Type()
)
attCNMfrConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrConfigIndex.setStatus("mandatory")
_AttCNMfrMeasMaxIntervals_Type = Integer32
_AttCNMfrMeasMaxIntervals_Object = MibTableColumn
attCNMfrMeasMaxIntervals = _AttCNMfrMeasMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 2),
    _AttCNMfrMeasMaxIntervals_Type()
)
attCNMfrMeasMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasMaxIntervals.setStatus("mandatory")
_AttCNMfrMeasIntervalLen_Type = Integer32
_AttCNMfrMeasIntervalLen_Object = MibTableColumn
attCNMfrMeasIntervalLen = _AttCNMfrMeasIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 3),
    _AttCNMfrMeasIntervalLen_Type()
)
attCNMfrMeasIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasIntervalLen.setStatus("mandatory")
_AttCNMfrPVCMeasMaxIntervals_Type = Integer32
_AttCNMfrPVCMeasMaxIntervals_Object = MibTableColumn
attCNMfrPVCMeasMaxIntervals = _AttCNMfrPVCMeasMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 4),
    _AttCNMfrPVCMeasMaxIntervals_Type()
)
attCNMfrPVCMeasMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasMaxIntervals.setStatus("mandatory")
_AttCNMfrPVCMeasIntervalLen_Type = Integer32
_AttCNMfrPVCMeasIntervalLen_Object = MibTableColumn
attCNMfrPVCMeasIntervalLen = _AttCNMfrPVCMeasIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 1, 1, 5),
    _AttCNMfrPVCMeasIntervalLen_Type()
)
attCNMfrPVCMeasIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasIntervalLen.setStatus("mandatory")
_AttCNMfrMeasTable_Object = MibTable
attCNMfrMeasTable = _AttCNMfrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2)
)
if mibBuilder.loadTexts:
    attCNMfrMeasTable.setStatus("mandatory")
_AttCNMfrMeasEntry_Object = MibTableRow
attCNMfrMeasEntry = _AttCNMfrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1)
)
attCNMfrMeasEntry.setIndexNames(
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrMeasIndex"),
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrMeasInterval"),
)
if mibBuilder.loadTexts:
    attCNMfrMeasEntry.setStatus("mandatory")
_AttCNMfrMeasIndex_Type = Integer32
_AttCNMfrMeasIndex_Object = MibTableColumn
attCNMfrMeasIndex = _AttCNMfrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 1),
    _AttCNMfrMeasIndex_Type()
)
attCNMfrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasIndex.setStatus("mandatory")
_AttCNMfrMeasInterval_Type = Integer32
_AttCNMfrMeasInterval_Object = MibTableColumn
attCNMfrMeasInterval = _AttCNMfrMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 2),
    _AttCNMfrMeasInterval_Type()
)
attCNMfrMeasInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasInterval.setStatus("mandatory")
_AttCNMfrMeasTimeStamp_Type = Integer32
_AttCNMfrMeasTimeStamp_Object = MibTableColumn
attCNMfrMeasTimeStamp = _AttCNMfrMeasTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 3),
    _AttCNMfrMeasTimeStamp_Type()
)
attCNMfrMeasTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasTimeStamp.setStatus("mandatory")


class _AttCNMfrMeasLocalTime_Type(DisplayString):
    """Custom type attCNMfrMeasLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMfrMeasLocalTime_Type.__name__ = "DisplayString"
_AttCNMfrMeasLocalTime_Object = MibTableColumn
attCNMfrMeasLocalTime = _AttCNMfrMeasLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 4),
    _AttCNMfrMeasLocalTime_Type()
)
attCNMfrMeasLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrMeasLocalTime.setStatus("mandatory")
_AttCNMfrReceivedOctets_Type = Gauge32
_AttCNMfrReceivedOctets_Object = MibTableColumn
attCNMfrReceivedOctets = _AttCNMfrReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 5),
    _AttCNMfrReceivedOctets_Type()
)
attCNMfrReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrReceivedOctets.setStatus("mandatory")
_AttCNMfrSentOctets_Type = Gauge32
_AttCNMfrSentOctets_Object = MibTableColumn
attCNMfrSentOctets = _AttCNMfrSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 6),
    _AttCNMfrSentOctets_Type()
)
attCNMfrSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrSentOctets.setStatus("mandatory")
_AttCNMfrReceivedFrames_Type = Gauge32
_AttCNMfrReceivedFrames_Object = MibTableColumn
attCNMfrReceivedFrames = _AttCNMfrReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 7),
    _AttCNMfrReceivedFrames_Type()
)
attCNMfrReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrReceivedFrames.setStatus("mandatory")
_AttCNMfrSentFrames_Type = Gauge32
_AttCNMfrSentFrames_Object = MibTableColumn
attCNMfrSentFrames = _AttCNMfrSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 8),
    _AttCNMfrSentFrames_Type()
)
attCNMfrSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrSentFrames.setStatus("mandatory")
_AttCNMfrBadFrames_Type = Gauge32
_AttCNMfrBadFrames_Object = MibTableColumn
attCNMfrBadFrames = _AttCNMfrBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 9),
    _AttCNMfrBadFrames_Type()
)
attCNMfrBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrBadFrames.setStatus("mandatory")
_AttCNMfrReceiverOverruns_Type = Gauge32
_AttCNMfrReceiverOverruns_Object = MibTableColumn
attCNMfrReceiverOverruns = _AttCNMfrReceiverOverruns_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 2, 1, 10),
    _AttCNMfrReceiverOverruns_Type()
)
attCNMfrReceiverOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrReceiverOverruns.setStatus("mandatory")
_AttCNMfrPVCMeasTable_Object = MibTable
attCNMfrPVCMeasTable = _AttCNMfrPVCMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3)
)
if mibBuilder.loadTexts:
    attCNMfrPVCMeasTable.setStatus("mandatory")
_AttCNMfrPVCMeasEntry_Object = MibTableRow
attCNMfrPVCMeasEntry = _AttCNMfrPVCMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1)
)
attCNMfrPVCMeasEntry.setIndexNames(
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasIfIndex"),
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasIndex"),
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCMeasInterval"),
)
if mibBuilder.loadTexts:
    attCNMfrPVCMeasEntry.setStatus("mandatory")
_AttCNMfrPVCMeasIfIndex_Type = Integer32
_AttCNMfrPVCMeasIfIndex_Object = MibTableColumn
attCNMfrPVCMeasIfIndex = _AttCNMfrPVCMeasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 1),
    _AttCNMfrPVCMeasIfIndex_Type()
)
attCNMfrPVCMeasIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasIfIndex.setStatus("mandatory")
_AttCNMfrPVCMeasIndex_Type = Integer32
_AttCNMfrPVCMeasIndex_Object = MibTableColumn
attCNMfrPVCMeasIndex = _AttCNMfrPVCMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 2),
    _AttCNMfrPVCMeasIndex_Type()
)
attCNMfrPVCMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasIndex.setStatus("mandatory")
_AttCNMfrPVCMeasInterval_Type = Integer32
_AttCNMfrPVCMeasInterval_Object = MibTableColumn
attCNMfrPVCMeasInterval = _AttCNMfrPVCMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 3),
    _AttCNMfrPVCMeasInterval_Type()
)
attCNMfrPVCMeasInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasInterval.setStatus("mandatory")
_AttCNMfrPVCMeasTimeStamp_Type = Integer32
_AttCNMfrPVCMeasTimeStamp_Object = MibTableColumn
attCNMfrPVCMeasTimeStamp = _AttCNMfrPVCMeasTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 4),
    _AttCNMfrPVCMeasTimeStamp_Type()
)
attCNMfrPVCMeasTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasTimeStamp.setStatus("mandatory")


class _AttCNMfrPVCMeasLocalTime_Type(DisplayString):
    """Custom type attCNMfrPVCMeasLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMfrPVCMeasLocalTime_Type.__name__ = "DisplayString"
_AttCNMfrPVCMeasLocalTime_Object = MibTableColumn
attCNMfrPVCMeasLocalTime = _AttCNMfrPVCMeasLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 5),
    _AttCNMfrPVCMeasLocalTime_Type()
)
attCNMfrPVCMeasLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCMeasLocalTime.setStatus("mandatory")
_AttCNMfrCongestionAtIngress_Type = Gauge32
_AttCNMfrCongestionAtIngress_Object = MibTableColumn
attCNMfrCongestionAtIngress = _AttCNMfrCongestionAtIngress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 6),
    _AttCNMfrCongestionAtIngress_Type()
)
attCNMfrCongestionAtIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrCongestionAtIngress.setStatus("mandatory")
_AttCNMfrCongestionAtEgress_Type = Gauge32
_AttCNMfrCongestionAtEgress_Object = MibTableColumn
attCNMfrCongestionAtEgress = _AttCNMfrCongestionAtEgress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 3, 1, 7),
    _AttCNMfrCongestionAtEgress_Type()
)
attCNMfrCongestionAtEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrCongestionAtEgress.setStatus("mandatory")
_AttCNMfrPVCStatusTable_Object = MibTable
attCNMfrPVCStatusTable = _AttCNMfrPVCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4)
)
if mibBuilder.loadTexts:
    attCNMfrPVCStatusTable.setStatus("mandatory")
_AttCNMfrPVCStatusEntry_Object = MibTableRow
attCNMfrPVCStatusEntry = _AttCNMfrPVCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1)
)
attCNMfrPVCStatusEntry.setIndexNames(
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCStatusIfIndex"),
    (0, "ATT-CNM-FRAME-RELAY-MIB", "attCNMfrPVCStatusIndex"),
)
if mibBuilder.loadTexts:
    attCNMfrPVCStatusEntry.setStatus("mandatory")
_AttCNMfrPVCStatusIfIndex_Type = Integer32
_AttCNMfrPVCStatusIfIndex_Object = MibTableColumn
attCNMfrPVCStatusIfIndex = _AttCNMfrPVCStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 1),
    _AttCNMfrPVCStatusIfIndex_Type()
)
attCNMfrPVCStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCStatusIfIndex.setStatus("mandatory")
_AttCNMfrPVCStatusIndex_Type = Integer32
_AttCNMfrPVCStatusIndex_Object = MibTableColumn
attCNMfrPVCStatusIndex = _AttCNMfrPVCStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 2),
    _AttCNMfrPVCStatusIndex_Type()
)
attCNMfrPVCStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCStatusIndex.setStatus("mandatory")


class _AttCNMfrPVCAdminStatus_Type(Integer32):
    """Custom type attCNMfrPVCAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMfrPVCAdminStatus_Type.__name__ = "Integer32"
_AttCNMfrPVCAdminStatus_Object = MibTableColumn
attCNMfrPVCAdminStatus = _AttCNMfrPVCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 3),
    _AttCNMfrPVCAdminStatus_Type()
)
attCNMfrPVCAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCAdminStatus.setStatus("mandatory")


class _AttCNMfrPVCOperStatus_Type(Integer32):
    """Custom type attCNMfrPVCOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMfrPVCOperStatus_Type.__name__ = "Integer32"
_AttCNMfrPVCOperStatus_Object = MibTableColumn
attCNMfrPVCOperStatus = _AttCNMfrPVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 7, 4, 1, 4),
    _AttCNMfrPVCOperStatus_Type()
)
attCNMfrPVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMfrPVCOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-FRAME-RELAY-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-fr": att_cnm_fr,
       "attCNMfrConfigTable": attCNMfrConfigTable,
       "attCNMfrConfigEntry": attCNMfrConfigEntry,
       "attCNMfrConfigIndex": attCNMfrConfigIndex,
       "attCNMfrMeasMaxIntervals": attCNMfrMeasMaxIntervals,
       "attCNMfrMeasIntervalLen": attCNMfrMeasIntervalLen,
       "attCNMfrPVCMeasMaxIntervals": attCNMfrPVCMeasMaxIntervals,
       "attCNMfrPVCMeasIntervalLen": attCNMfrPVCMeasIntervalLen,
       "attCNMfrMeasTable": attCNMfrMeasTable,
       "attCNMfrMeasEntry": attCNMfrMeasEntry,
       "attCNMfrMeasIndex": attCNMfrMeasIndex,
       "attCNMfrMeasInterval": attCNMfrMeasInterval,
       "attCNMfrMeasTimeStamp": attCNMfrMeasTimeStamp,
       "attCNMfrMeasLocalTime": attCNMfrMeasLocalTime,
       "attCNMfrReceivedOctets": attCNMfrReceivedOctets,
       "attCNMfrSentOctets": attCNMfrSentOctets,
       "attCNMfrReceivedFrames": attCNMfrReceivedFrames,
       "attCNMfrSentFrames": attCNMfrSentFrames,
       "attCNMfrBadFrames": attCNMfrBadFrames,
       "attCNMfrReceiverOverruns": attCNMfrReceiverOverruns,
       "attCNMfrPVCMeasTable": attCNMfrPVCMeasTable,
       "attCNMfrPVCMeasEntry": attCNMfrPVCMeasEntry,
       "attCNMfrPVCMeasIfIndex": attCNMfrPVCMeasIfIndex,
       "attCNMfrPVCMeasIndex": attCNMfrPVCMeasIndex,
       "attCNMfrPVCMeasInterval": attCNMfrPVCMeasInterval,
       "attCNMfrPVCMeasTimeStamp": attCNMfrPVCMeasTimeStamp,
       "attCNMfrPVCMeasLocalTime": attCNMfrPVCMeasLocalTime,
       "attCNMfrCongestionAtIngress": attCNMfrCongestionAtIngress,
       "attCNMfrCongestionAtEgress": attCNMfrCongestionAtEgress,
       "attCNMfrPVCStatusTable": attCNMfrPVCStatusTable,
       "attCNMfrPVCStatusEntry": attCNMfrPVCStatusEntry,
       "attCNMfrPVCStatusIfIndex": attCNMfrPVCStatusIfIndex,
       "attCNMfrPVCStatusIndex": attCNMfrPVCStatusIndex,
       "attCNMfrPVCAdminStatus": attCNMfrPVCAdminStatus,
       "attCNMfrPVCOperStatus": attCNMfrPVCOperStatus}
)
