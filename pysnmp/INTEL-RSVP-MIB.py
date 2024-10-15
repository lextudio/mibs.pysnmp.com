# SNMP MIB module (INTEL-RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-RSVP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:58 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rsvp_ObjectIdentity = ObjectIdentity
rsvp = _Rsvp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 33)
)
_Conf_ObjectIdentity = ObjectIdentity
conf = _Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1)
)
_ConfIfTable_Object = MibTable
confIfTable = _ConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1)
)
if mibBuilder.loadTexts:
    confIfTable.setStatus("mandatory")
_ConfIfEntry_Object = MibTableRow
confIfEntry = _ConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1)
)
confIfEntry.setIndexNames(
    (0, "INTEL-RSVP-MIB", "confIfIndex"),
)
if mibBuilder.loadTexts:
    confIfEntry.setStatus("mandatory")
_ConfIfIndex_Type = Integer32
_ConfIfIndex_Object = MibTableColumn
confIfIndex = _ConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 1),
    _ConfIfIndex_Type()
)
confIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confIfIndex.setStatus("mandatory")


class _ConfIfCreateObj_Type(OctetString):
    """Custom type confIfCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ConfIfCreateObj_Type.__name__ = "OctetString"
_ConfIfCreateObj_Object = MibTableColumn
confIfCreateObj = _ConfIfCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 2),
    _ConfIfCreateObj_Type()
)
confIfCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfCreateObj.setStatus("mandatory")


class _ConfIfDeleteObj_Type(Integer32):
    """Custom type confIfDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_ConfIfDeleteObj_Type.__name__ = "Integer32"
_ConfIfDeleteObj_Object = MibTableColumn
confIfDeleteObj = _ConfIfDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 3),
    _ConfIfDeleteObj_Type()
)
confIfDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfDeleteObj.setStatus("mandatory")


class _ConfIfUdpEncap_Type(Integer32):
    """Custom type confIfUdpEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfIfUdpEncap_Type.__name__ = "Integer32"
_ConfIfUdpEncap_Object = MibTableColumn
confIfUdpEncap = _ConfIfUdpEncap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 4),
    _ConfIfUdpEncap_Type()
)
confIfUdpEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfUdpEncap.setStatus("mandatory")
_ConfIfRsvpTotalBw_Type = Integer32
_ConfIfRsvpTotalBw_Object = MibTableColumn
confIfRsvpTotalBw = _ConfIfRsvpTotalBw_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 5),
    _ConfIfRsvpTotalBw_Type()
)
confIfRsvpTotalBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRsvpTotalBw.setStatus("mandatory")
_ConfIfMaxBwPerFlow_Type = Integer32
_ConfIfMaxBwPerFlow_Object = MibTableColumn
confIfMaxBwPerFlow = _ConfIfMaxBwPerFlow_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 1, 1, 6),
    _ConfIfMaxBwPerFlow_Type()
)
confIfMaxBwPerFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfMaxBwPerFlow.setStatus("mandatory")


class _ConfRsvpEnabled_Type(Integer32):
    """Custom type confRsvpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfRsvpEnabled_Type.__name__ = "Integer32"
_ConfRsvpEnabled_Object = MibScalar
confRsvpEnabled = _ConfRsvpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 2),
    _ConfRsvpEnabled_Type()
)
confRsvpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRsvpEnabled.setStatus("mandatory")
_ConfRefreshTimer_Type = Integer32
_ConfRefreshTimer_Object = MibScalar
confRefreshTimer = _ConfRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 3),
    _ConfRefreshTimer_Type()
)
confRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confRefreshTimer.setStatus("mandatory")
_ConfCleanupFactor_Type = Integer32
_ConfCleanupFactor_Object = MibScalar
confCleanupFactor = _ConfCleanupFactor_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 33, 1, 4),
    _ConfCleanupFactor_Type()
)
confCleanupFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confCleanupFactor.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-RSVP-MIB",
    **{"rsvp": rsvp,
       "conf": conf,
       "confIfTable": confIfTable,
       "confIfEntry": confIfEntry,
       "confIfIndex": confIfIndex,
       "confIfCreateObj": confIfCreateObj,
       "confIfDeleteObj": confIfDeleteObj,
       "confIfUdpEncap": confIfUdpEncap,
       "confIfRsvpTotalBw": confIfRsvpTotalBw,
       "confIfMaxBwPerFlow": confIfMaxBwPerFlow,
       "confRsvpEnabled": confRsvpEnabled,
       "confRefreshTimer": confRefreshTimer,
       "confCleanupFactor": confCleanupFactor}
)
