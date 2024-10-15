# SNMP MIB module (EMC-CELERRA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMC-CELERRA
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:22 2024
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
 Opaque,
 NotificationType,
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
    "Opaque",
    "NotificationType",
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

_Emc_ObjectIdentity = ObjectIdentity
emc = _Emc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139)
)
_EmcCelerra_ObjectIdentity = ObjectIdentity
emcCelerra = _EmcCelerra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1139, 2)
)
_CelEventTable_Object = MibTable
celEventTable = _CelEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1)
)
if mibBuilder.loadTexts:
    celEventTable.setStatus("mandatory")
_CelEvent_Object = MibTableRow
celEvent = _CelEvent_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1, 1)
)
celEvent.setIndexNames(
    (0, "EMC-CELERRA", "celEventFacility"),
    (0, "EMC-CELERRA", "celEventID"),
)
if mibBuilder.loadTexts:
    celEvent.setStatus("mandatory")
_CelEventFacility_Type = Integer32
_CelEventFacility_Object = MibTableColumn
celEventFacility = _CelEventFacility_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 1),
    _CelEventFacility_Type()
)
celEventFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celEventFacility.setStatus("mandatory")
_CelEventID_Type = Integer32
_CelEventID_Object = MibTableColumn
celEventID = _CelEventID_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 2),
    _CelEventID_Type()
)
celEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celEventID.setStatus("mandatory")
_CelEventSeverity_Type = Integer32
_CelEventSeverity_Object = MibTableColumn
celEventSeverity = _CelEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 3),
    _CelEventSeverity_Type()
)
celEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celEventSeverity.setStatus("mandatory")
_CelEventDescr_Type = DisplayString
_CelEventDescr_Object = MibTableColumn
celEventDescr = _CelEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1139, 2, 1, 1, 4),
    _CelEventDescr_Type()
)
celEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    celEventDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

celReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 1)
)
celReboot.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celReboot.setStatus(
        ""
    )

celMasterCtlFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 2)
)
celMasterCtlFault.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celMasterCtlFault.setStatus(
        ""
    )

celHWFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 3)
)
celHWFailure.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celHWFailure.setStatus(
        ""
    )

celSlotStale = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 4)
)
celSlotStale.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celSlotStale.setStatus(
        ""
    )

celSlotPanicked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 5)
)
celSlotPanicked.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celSlotPanicked.setStatus(
        ""
    )

celIntfFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 6)
)
celIntfFailure.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celIntfFailure.setStatus(
        ""
    )

celAAF = NotificationType(
    (1, 3, 6, 1, 4, 1, 1139, 2, 0, 7)
)
celAAF.setObjects(
    ("EMC-CELERRA", "celEvent")
)
if mibBuilder.loadTexts:
    celAAF.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMC-CELERRA",
    **{"emc": emc,
       "emcCelerra": emcCelerra,
       "celReboot": celReboot,
       "celMasterCtlFault": celMasterCtlFault,
       "celHWFailure": celHWFailure,
       "celSlotStale": celSlotStale,
       "celSlotPanicked": celSlotPanicked,
       "celIntfFailure": celIntfFailure,
       "celAAF": celAAF,
       "celEventTable": celEventTable,
       "celEvent": celEvent,
       "celEventFacility": celEventFacility,
       "celEventID": celEventID,
       "celEventSeverity": celEventSeverity,
       "celEventDescr": celEventDescr}
)
